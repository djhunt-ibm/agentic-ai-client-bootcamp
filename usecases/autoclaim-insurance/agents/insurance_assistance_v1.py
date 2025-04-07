from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing_extensions import List
import json
import os
import logging
from ibm_boto3 import client
from ibm_botocore.client import Config
from crewai import Agent, Task, Crew, Process
from crewai import LLM
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from ibm_watsonx_ai.credentials import Credentials

# Load environment variables from the .env file
load_dotenv()

# FastAPI setup: Creating an instance of FastAPI for routing and handling HTTP requests
app = FastAPI()

# Logging setup: Configuring logging to capture important events during execution
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Constants for API configurations.
WATSONX_URL = os.getenv("WATSONX_URL")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_APIKEY = os.getenv("WATSONX_APIKEY")
WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID")
INDEX_NAME = os.getenv("INDEX_NAME")
RELEVANT_CHUNKS = os.getenv("RELEVANT_CHUNKS")
COS_ENDPOINT = os.getenv("COS_ENDPOINT")
COS_API_KEY_ID = os.getenv("COS_API_KEY_ID")
COS_INSTANCE_CRN = os.getenv("COS_INSTANCE_CRN")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Parameters for model inference: Setting the decoding and token limits for the AI model
PARAMETERS = {
    "decoding_method": "sample",
    "max_new_tokens": 4096,
    "temperature": 0.7,
    "top_k": 50,
    "top_p": 1,
    "repetition_penalty": 1,
}

# Initialize credentials and the model: Setting up the Watsonx model credentials and parameters
credentials = Credentials(url=WATSONX_URL, api_key=WATSONX_APIKEY)
llm = LLM(
    model=WATSONX_MODEL_ID,
    base_url=WATSONX_URL,
    project_id=WATSONX_PROJECT_ID,
    api_key=WATSONX_APIKEY,
    parameters=PARAMETERS,
    max_tokens=4096,
    temperature=0
)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create COS client
cos = client("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

# Elasticsearch connection: Function to connect to Elasticsearch
def get_connection():
    """Establishes a connection to the Elasticsearch service and verifies its availability."""
    try:
        es_connection = Elasticsearch([os.environ["es_endpoint"]], verify_certs=False)
        if es_connection.ping():
            logger.info('Connection Successful')
        else:
            logger.error("Connection Failed")
        return es_connection
    except Exception as e:
        logger.error(f"Failed to connect to Elasticsearch: {e}")
        return None

# Get/download an object
def get_object(object_name):
    try:
        response = cos.get_object(Bucket=BUCKET_NAME, Key=object_name)
        data = response['Body'].read()
        logger.info(f"Downloaded object: {object_name}")
        return data
    except Exception as e:
        logger.error(f"Failed to download: {object_name}", exc_info=True)
        raise


# Function to clean up the Elasticsearch connection
def cleanup(es_connection):
    """Closes the Elasticsearch connection."""
    if es_connection:
        es_connection.close()

# Function to parse the file data: Reads and loads the JSON data from a file
def parse_data(file_path: str):
    """Parses a JSON file and returns its content."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"Error reading the file {file_path}: {e}")
        return {}

# Function to search documents in Elasticsearch: Searches for relevant policy information based on query results
def search_documents(policy_query_result: list, index_name: str, relevant_chunks: int):
    """Searches for relevant documents in Elasticsearch based on provided queries."""
    results = []
    try:
        es_connection = get_connection()  # Getting the Elasticsearch connection
        if es_connection is None:
            raise Exception("No Elasticsearch connection available.")
        
        search_queries = []
        # Prepare queries for each question in the policy query result
        for question in policy_query_result:
            search_queries.append({})
            search_queries.append({"query": {"match": {"text": question}}})

        # Execute the search queries
        search_results = es_connection.msearch(index=index_name, body=search_queries)
        count = 0
        for response in search_results["responses"]:
            for hit in response["hits"]["hits"]:
                count += 1
                result = {
                    "question": question,
                    "text": hit["_source"]["text"]
                }
                results.append(result)
                if count == relevant_chunks:
                    break
        cleanup(es_connection)  # Clean up after the search is done
    except Exception as e:
        logger.error(f"Error during document search: {e}")
    return results

def sum_token_usage(usage_metrics_list):
    # Initialize a dictionary to store the summed values
    total_usage = {
        "total_tokens": 0,
        "prompt_tokens": 0,
        "cached_prompt_tokens": 0,
        "completion_tokens": 0,
        "successful_requests": 0
    }

    # Iterate through each UsageMetrics object and sum up the values
    for usage in usage_metrics_list:
        total_usage["total_tokens"] += getattr(usage, 'total_tokens', 0)
        total_usage["prompt_tokens"] += getattr(usage, 'prompt_tokens', 0)
        total_usage["cached_prompt_tokens"] += getattr(usage, 'cached_prompt_tokens', 0)
        total_usage["completion_tokens"] += getattr(usage, 'completion_tokens', 0)
        total_usage["successful_requests"] += getattr(usage, 'successful_requests', 0)

    return total_usage


def agent_workflow(claim_data,policy_data):
    json_data_list = list()
    claim_agent = Agent(
        role="Insurance Claim Data Extractor",
        goal="Extract and validate structured data from insurance claims.",
        backstory="Expert in analyzing insurance claims and ensuring completeness and correctness of claim details.",
        verbose=True,
        allow_delegation=True,
        tools=[],  # List of tools if any are needed
        llm=llm,  # Use the initialized language model
    )

    # Define task description for the claim
    claim_prompt = f"""
    Given the following insurance claim and policy information, extract the data in structured JSON format:
    1. Claim Number
    2. Policy Number
    3. Policy Type
    4. Claimant Name
    5. Date of Loss
    6. Loss Description
    7. Estimated Repair Cost
    8. Vehicle Details (if available)

    input : 
    Claim Data : {claim_data}
    Policy Data : {policy_data}
    """

    # Define the Task for the claim extraction
    claim_task = Task(
        description=claim_prompt,
        expected_output="JSON object containing structured insurance claim details.",
        agent=claim_agent,
    )

    claim_crew = Crew(
        agents=[claim_agent],
        tasks=[claim_task],
        verbose=True,
        process=Process.sequential,
    )

    claim_extraction_result = claim_crew.kickoff()

    json_data_list.append(claim_extraction_result.token_usage)

    # Define Policy Query Agent: Generates queries to retrieve relevant policy sections
    policy_query_agent = Agent(
        role="Insurance Policy Query Generator",
        goal="Generate queries to retrieve relevant policy sections for an auto insurance claim.",
        backstory="Specialized in understanding insurance policies and mapping claims to policy clauses.",
        verbose=True,
        allow_delegation=True,
        tools=[],  # Add tools if needed
        llm=llm,  # Use the initialized language model
    )

    # Define Task Description for policy query generation
    policy_query_prompt = f"""
    You are an assistant tasked with determining what insurance policy sections to consult for a given auto claim.

    **Instructions:**
    1. Review the claim data, including the type of loss (rear-end collision), estimated repair cost, and policy number.
    2. Identify what aspects of the policy we need:
    - Collision coverage conditions
    - Deductible application
    - Any special endorsements related to rear-end collisions or no-fault scenarios
    3. Produce 3-5 queries that can be used against a vector database of insurance policies to find relevant chunks.

    Claim Data:
    {claim_extraction_result}

    Return list of queries only.
    """

    # Create the Task for policy query generation
    policy_query_task = Task(
        description=policy_query_prompt,
        expected_output="list of queries",
        agent=policy_query_agent,
    )

    policy_query_crew = Crew(
        agents=[policy_query_agent],
        tasks=[policy_query_task],
        verbose=True,
        process=Process.sequential,
    )

    policy_query_result = policy_query_crew.kickoff()

    json_data_list.append(policy_query_result.token_usage)

    # Parsing the raw output and cleaning the queries
    raw_output = policy_query_result.raw
    policy_questions_list = [question.strip() for question in raw_output.split("\n") if question.strip()]

    # Search Documents in Elasticsearch: Retrieve relevant policy information
    q_a_list = search_documents(policy_questions_list, INDEX_NAME, RELEVANT_CHUNKS)

    # Define Policy Recommendation Agent: Evaluates policy coverage based on claim and policy data
    policy_recommendation_agent = Agent(
        role="Insurance Policy Coverage Evaluator",
        goal="Analyze policy sections and claim information to provide coverage recommendations.",
        backstory=(
            "Expert in interpreting insurance policies and assessing claims for settlement and deductible recommendations."
        ),
        verbose=True,
        allow_delegation=True,
        tools=[],  # Add relevant tools if needed
        llm=llm,  # Use the initialized language model
    )

    # Policy Recommendation Task Prompt: Prompts the agent for policy recommendations
    policy_recommendation_prompt = f"""
    Given the retrieved policy sections for this claim, determine:
    - Claim number
    - Policy number
    - Policy type
    - Claimant Name
    - Vehicle Details (if available)
    - If the collision is covered
    - The applicable deductible
    - Recommended settlement amount (e.g., cost minus deductible)
    - A concise summary of coverage determination.
    - Which policy section applies

    Claim Info:
    {claim_extraction_result}

    Policy Text:
    {q_a_list}

    Return a JSON object.
    """

    # Define the Task for policy recommendation
    policy_recommendation_task = Task(
        description=policy_recommendation_prompt,
        expected_output="JSON object containing policy recommendations.",
        agent=policy_recommendation_agent,
    )

    policy_recomm_crew = Crew(
        agents=[policy_recommendation_agent],
        tasks=[policy_recommendation_task],
        verbose=True,
        process=Process.sequential,
    )

    policy_recomm_result = policy_recomm_crew.kickoff()

    json_data_list.append(policy_recomm_result.token_usage)

    policy_recommendation = policy_recomm_result.raw

    customer_email_prompt = f""" Generate a professional and empathetic email to a customer regarding their auto insurance claim process using the following JSON details:
    The email should include the following elements:
    {policy_recommendation}
    Greeting: Address the customer by name (John Doe).
    Claim Details: Include the claim number, policy number, and vehicle details (make, model, year).
    Coverage Information: Explain that the collision is covered under the policy's collision coverage.
    Deductible and Settlement: Mention the deductible amount of $500 and the recommended settlement amount of $2000.
    Policy Section Reference: Include a reference to the applicable policy section: "PART D COVERAGE FOR DAMAGE TO YOUR AUTO, INSURING AGREEMENT - COLLISION."
    Next Steps: Outline any next steps the customer needs to take, such as providing additional documents or confirming acceptance of the settlement.
    Contact Information: Provide contact details for further assistance or inquiries.
    Professional Closing: End the email with a courteous closing (e.g., "Best regards," or "Sincerely,") and the insurance company's contact information.
    Ensure the tone is clear, concise, and supportive, making the customer feel informed and reassured about their claim process.
    provide final response in JSON format that should contain subject and email body."""

    # Define Policy Customer email Generation Agent.
    customer_email_agent = Agent(
        role="Customer email generator",
        goal="Analyze policy recommendations and generate the email.",
        backstory=(
            "Expert in customer email generation for policy recommendations."
        ),
        verbose=True,
        allow_delegation=True,
        tools=[],  # Add relevant tools if needed
        llm=llm,  # Use the initialized language model
    )

    # Define the Task for customer email generation.
    customer_email_task = Task(
        description=customer_email_prompt,
        expected_output="Customer email details",
        agent=customer_email_agent,
    )

    customer_email_crew = Crew(
        agents=[customer_email_agent],
        tasks=[customer_email_task],
        verbose=True,
        process=Process.sequential,
    )

    customer_email_result = customer_email_crew.kickoff()

    json_data_list.append(customer_email_result.token_usage)

    customer_email = customer_email_result.raw

    finanace_team_email_prompt = f"""Generate a formal and concise email to the finance department requesting review and approval for payment of an auto insurance claim using the following JSON details:
    {policy_recommendation}
    The email should include the following elements:

    Subject Line: "Request for Review and Approval of Auto Insurance Claim Payment – Claim #123456"
    Greeting: Address the finance team appropriately (e.g., "Dear Finance Team,").
    Claim Summary: Provide a brief summary including the claim number, policy number, claimant name, and vehicle details.
    Coverage Confirmation: Mention that the collision is covered under the policy’s collision coverage and reference the applicable policy section.
    Payment Details: Highlight the deductible amount of $500 and the recommended settlement amount of $2000.
    Request for Action: Clearly request the finance department to review the claim details and approve the payment processing.
    Supporting Documentation: Mention that any necessary supporting documents are attached (if applicable).
    Contact Information: Provide contact details for further clarification or queries.
    Professional Closing: End the email with a courteous closing (e.g., "Best regards," or "Sincerely,") along with the sender's name, title, and company contact information.
    Ensure the tone is professional, straightforward, and respectful, providing all necessary information for efficient processing by the finance department.
    provide final response in JSON format that should contain subject and email body."""

    # Define Policy Finance team email Generation Agent.
    finance_team_email_agent = Agent(
        role="Finance team email generator",
        goal="Analyze policy recommendations and generate the email.",
        backstory=(
            "Expert in finance email generation for policy recommendations."
        ),
        verbose=True,
        allow_delegation=True,
        tools=[],  # Add relevant tools if needed
        llm=llm,  # Use the initialized language model
    )

    # Define the Task for finance team email generation.
    finance_team_email_task = Task(
        description=finanace_team_email_prompt,
        expected_output="payment aproval email details",
        agent=finance_team_email_agent,
    )

    finance_team_email_crew = Crew(
        agents=[finance_team_email_agent],
        tasks=[finance_team_email_task],
        verbose=True,
        process=Process.sequential,
    )

    finance_team_email_result = finance_team_email_crew.kickoff()

    json_data_list.append(finance_team_email_result.token_usage)

    finance_team_email = finance_team_email_result.raw

    print("Token List :",json_data_list)

    # Call the function
    result = sum_token_usage(json_data_list)
    return policy_recommendation,customer_email,finance_team_email,result


# Pydantic model for query parameters
class FilePaths(BaseModel):
    """Pydantic model to validate and serialize the input file paths."""
    filenames: List[str]

class Persona(BaseModel):
    """Pydantic model to validate which persona"""
    persona_type:str

# API endpoint to trigger the AI process: Processes the claims and provides policy recommendations
@app.post("/process_claims")
async def process_claims(file_paths: FilePaths,persona:Persona):
    """Processes the claims using AI models and provides policy recommendations."""
    json_data_list = list()
    try:
        print("Filepaths",file_paths)
        if not file_paths:
            raise Exception("Filenames not found")
        # Load data from COS
        claim_data=""
        policy_data=""
        for file in file_paths.filenames:
            if "claim" in file:
                claim_data = get_object(file)
            if "policy" in file:
                policy_data = get_object(file)
        print("Claims Data",claim_data)
        # Define Claim Extraction Agent: Agent for extracting structured data from the claim
        policy_recommendation,customer_email,finance_team_email,result=agent_workflow(claim_data,policy_data)

        # Return the result with status and policy recommendations
        if persona.persona_type.lower()=="customer":
            return json.dumps(policy_recommendation)
        else:
            return {
                "status": "success",
                "policy_recommendation": policy_recommendation,
                "customer_email": customer_email,
                "finanace_team_email": finance_team_email,
                "agents_token_usage": result
            }

    except Exception as e:
        logger.error(f"Error processing claims: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing claims: {e}")