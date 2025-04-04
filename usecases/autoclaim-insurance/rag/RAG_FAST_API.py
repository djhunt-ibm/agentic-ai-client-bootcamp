from fastapi import FastAPI, HTTPException
import pandas as pd
import copy
import os
import re
from elasticsearch import Elasticsearch, exceptions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.elasticsearch import ElasticsearchStore
from llama_index.core import SimpleDirectoryReader
from dotenv import load_dotenv
from tqdm import tqdm
import time
from elasticsearch.exceptions import ConnectionTimeout
import ssl
# import ibm_boto3
# from ibm_botocore.client import Config
import logging
from fastapi.middleware.cors import CORSMiddleware
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# pip install fastapi pandas elasticsearch langchain llama-index python-dotenv tqdm ibm-cos-sdk
#pip install -U langchain-community
#pip install uvicorn  

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to read .crt file content directly from IBM COS
# def read_crt_file_from_cos(cos_client, bucket_name, file_key):
#     try:
#         # Retrieve the file from COS
#         response = cos_client.get_object(Bucket=bucket_name, Key=file_key)
        
#         # Read the content of the file
#         crt_content = response['Body'].read().decode('utf-8')
        
#         return crt_content.strip()
    
#     except Exception as e:
#         logger.error(f"Error reading {file_key} from bucket {bucket_name}: {e}")
#         return None

# Function to establish connection to Elasticsearch
def get_connection():
    # Load environment variables for IBM COS
    # COS_ENDPOINT = os.environ["COS_ENDPOINT"]
    # COS_API_KEY_ID = os.environ["COS_API_KEY_ID"]
    # COS_INSTANCE_CRN = os.environ["COS_INSTANCE_CRN"]
    # COS_BUCKET_NAME = os.environ["COS_BUCKET_NAME"]
    # COS_FILE_KEY = os.environ["COS_FILE_KEY"]

#     # Create the IBM COS client
#     cos_client = ibm_boto3.client(
#         "s3",
#         ibm_api_key_id=COS_API_KEY_ID,
#         ibm_service_instance_id=COS_INSTANCE_CRN,
#         config=Config(signature_version="oauth"),
#         endpoint_url=COS_ENDPOINT
#     )

#     # Read .crt file content from COS
#     crt_content = read_crt_file_from_cos(cos_client, COS_BUCKET_NAME, COS_FILE_KEY)
#     logger.info('Before Certificate reading')
    # crt_content = os.environ["wxd_certificate"] # Latest comment

#     # Create SSL context for Elasticsearch connection using the .crt content
    # context = ssl.create_default_context(cadata=crt_content) # Latest comment

#     logger.info('After Certificate reading')
    # es_connection = Elasticsearch([os.environ["es_endpoint"]], ssl_context=context) # Latest comment

    # By pass the SSL auth.
    es_connection = Elasticsearch([os.environ["es_endpoint"]], verify_certs=False,http_auth=None)#ssl_context=context)

    # Check if the connection to Elasticsearch is successful
    if es_connection.ping():
        logger.info('Connection Successful')
    else:
        logger.error("Connection Failed")
    return es_connection

# Function to create and deploy the embedding model on Elasticsearch
def create_and_deploy_model(es_connection, es_model_id):
    try:
        # Delete existing model if it exists
        es_connection.ml.delete_trained_model(model_id=es_model_id, force=True)
        logger.info("Model deleted successfully, We will proceed with creating one")
    except exceptions.NotFoundError:
        logger.info("Model doesn't exist, but We will proceed with creating one")

    # Create a new model
    es_connection.ml.put_trained_model(
        model_id=es_model_id, input={"field_names": ["text_field"]}
    )

    # Wait for the model to be fully defined
    while True:
        status = es_connection.ml.get_trained_models(
            model_id=es_model_id, include="definition_status"
        )

        if status["trained_model_configs"][0]["fully_defined"]:
            logger.info("ELSER Model is downloaded and ready to be deployed.")
            break
        time.sleep(5)

    # Start model deployment
    es_connection.ml.start_trained_model_deployment(
        model_id=es_model_id, number_of_allocations=1, wait_for="starting"
    )

    # Wait for the deployment to start
    while True:
        status = es_connection.ml.get_trained_models_stats(
            model_id=es_model_id,
        )
        if status["trained_model_stats"][0]["deployment_stats"]["state"] == "started":
            logger.info("ELSER Model has been successfully deployed.")
            break
        time.sleep(2)

# Function to process documents based on chunk size and prepare the data
def process_local_docs(chunk_size, chunk_overlap, split_delimeter, index_name):
    # Load raw documents from the specified directory
    raw_documents = SimpleDirectoryReader(
        os.environ["file_path_doc"], recursive=True).load_data()

    if chunk_size==0 and chunk_overlap==0:
        text_splitter = RecursiveCharacterTextSplitter(separators=[split_delimeter])
    else:
        # Initialize text splitter with specified chunk size and overlap
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap,
        )
    # text_splitter = RecursiveCharacterTextSplitter(separators=["Page Number :"])

    actions = []
    idx = 0

    # print('Raw Docuemtns :',raw_documents)

    # Split each document into chunks
    for doc in tqdm(raw_documents):
        text = doc.text
        # text = ' '.join(text.split())
        # text = re.sub(r'\s+', ' ', text)
        text_chunks = text_splitter.split_text(text)

        idx += 1
        page_num = 0
        for chunk in text_chunks:
            new_doc = copy.deepcopy(doc)
            page_num += 1
            new_doc.text = chunk

            action = {
                "index": index_name,
                "id": new_doc.metadata['file_name'] + "_" + str(idx) + "." + str(page_num),
                "title": str(new_doc.metadata['file_name']).split(".")[0],
                "page_number": page_num,
                "source_reference": '',
                #os.environ[new_doc.metadata['file_name'].replace(" ", "-")],os.environ[str(new_doc.metadata['file_name']).split(".")[0]],
                "description": "Insurance Data",
                "body_content_field": "",
                "text": chunk
            }
            actions.append(action)
            # print("Chunk :",temp,chunk)
    
    # Convert actions list to DataFrame
    documents2 = pd.DataFrame(actions)
    return documents2

# Function to upload processed data into Elasticsearch
def upload_batch(es_connection, docs_batch, index, es_model_id):
    # Create Elasticsearch vector store
    vector_store = ElasticsearchStore(es_connection=es_connection,
                                      index_name=index,
                                      strategy=ElasticsearchStore.SparseVectorRetrievalStrategy(model_id=es_model_id))
    
    # Prepare metadata for each document chunk
    metadata = []
    for file_name, page_num, source_ref in zip(docs_batch.title.tolist(), docs_batch.page_number.tolist(), docs_batch.source_reference.tolist()):
        metadata.append({"file_name": file_name, "page_number": page_num, 'source_reference': source_ref})

    # Upload document chunks to Elasticsearch
    _ = vector_store.add_texts(texts=docs_batch.text.tolist(),
                              metadatas=metadata,
                              index_name=index,
                              request_timeout=10000,
                              ids=[str(i) for i in docs_batch.id])

# Function to upload documents to Elasticsearch in batches
def elastic_upload(es_connection, documents, batch_size, index, es_model_id):
    num_docs = len(documents)
    num_batches = (num_docs + batch_size - 1) // batch_size

    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, num_docs)
        docs_batch = documents.iloc[start_idx:end_idx]
        retry_count = 0

        # Retry logic for batch upload in case of connection timeouts
        while retry_count < 4:
            try:
                upload_batch(es_connection, docs_batch, index, es_model_id)
                logger.info(f"Uploaded batch {i+1}/{num_batches}")
                time.sleep(30)
                break
            except ConnectionTimeout as e:
                retry_count += 1
                logger.warning(f"Connection timed out for batch {i+1}/{num_batches}. Retrying... (Attempt {retry_count}/3)")
                time.sleep(15)
                if f"Model [{es_model_id}] must be deployed to use." in str(e):
                    logger.info("Model must be deployed. Trying to deploy now...")
                    logger.info("Retry uploading batch...")
                elif "inference process queue is full." in str(e):
                    logger.info("Inference process queue is full. Waiting for 30 seconds before retrying...")
                    time.sleep(30)
                else:
                    logger.error(f"Error: {e}")

    logger.info("Upload complete.")

# Function to close the Elasticsearch connection
def cleanup(es_connection):
    es_connection.close()

# FUnction to generate the final reponse using LLM.
def send_to_watsonxai(prompts, model_name="meta-llama/llama-3-1-70b-instruct",
                      decoding_method="greedy", max_new_tokens=4096, min_new_tokens=1,
                      temperature=0, repetition_penalty=1.05):
    """
    Generate responses using the Watsonx AI model based on given prompts.

    Args:
        prompts (list): List of prompt strings for generating responses.
        model_name (str): The ID of the model to use.
        decoding_method (str): Decoding method, e.g., 'greedy' or 'sampling'.
        max_new_tokens (int): Maximum tokens in the response.
        min_new_tokens (int): Minimum tokens in the response.
        temperature (float): Sampling temperature; controls creativity.
        repetition_penalty (float): Penalty for repetition in output.

    Returns:
        list: Generated responses from Watsonx AI.

    Raises:
        ValueError: If any prompt in `prompts` is empty.
        Exception: If model generation fails.
    """
    # Validate input prompts
    if not all(prompts):
        logger.error("One or more prompts are empty.")
        raise ValueError("All prompts must be non-empty strings.")

    # Prepare model parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 474,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
    }

    # Authentication credentials for Watsonx AI
    creds = {
        "url": os.environ.get("CLOUD_URL"),
        "apikey": os.environ.get("WATSONX_API_KEY"),
    }

    # Ensure that credentials are available
    if not creds["url"] or not creds["apikey"]:
        logger.error("Missing Watsonx API credentials.")
        raise EnvironmentError("Watsonx API credentials not found in environment.")

    try:
        # Initialize model with given parameters and credentials
        model = Model(
            model_id=model_name,
            params=model_params,
            credentials=creds,
            project_id=os.environ.get("WATSONX_PROJECT_ID")
        )
        logger.info(f"Initialized model {model_name} with provided parameters.")

        # Generate text responses for each prompt
        responses = []
        for prompt in prompts:
            logger.info(f"Generating response for prompt: {prompt[:30]}...")  # Logging partial prompt for brevity
            response = model.generate_text(prompt)
            responses.append(response)
            logger.info("Response generated successfully.")

        return responses

    except Exception as e:
        logger.error(f"Error generating response from Watsonx AI: {e}")
        raise

# API endpoint to upload documents
@app.post("/ingest-documents/")
async def upload_documents(index_name: str, chunk_size: int, overlap_size: int, split_delimeter: str, es_model_id: str, model_deploy: bool):
    logger.info("Starting document ingestion...")
    # Establish Elasticsearch connection
    es_connection = get_connection()
    if model_deploy:
        # Create and deploy model if required
        create_and_deploy_model(es_connection, es_model_id)
    
    # Process documents and prepare data
    docs_final = process_local_docs(chunk_size, overlap_size, split_delimeter, index_name).copy(deep=True)

    # Delete existing index if required
    if os.environ["index_update"].lower() == "false":
        if es_connection.indices.exists(index=index_name):
            es_connection.indices.delete(index=index_name)
    
    # Upload documents to Elasticsearch
    elastic_upload(es_connection, docs_final, 50, index_name, es_model_id)

    # Close Elasticsearch connection
    cleanup(es_connection)
    logger.info("Document ingestion completed.")
    return {"message": "Documents are being processed and uploaded."}

# API endpoint to search documents
@app.get("/search/")
async def search_documents(search_query: str, index_name: str, es_model_id: str, relevant_chunks: int):
    logger.info("Starting document search...")
    try:
        # Establish Elasticsearch connection
        es_connection = get_connection()
        
        # Perform search on Elasticsearch
        search_results = es_connection.search(index=index_name, body={
            "query": {
                "text_expansion": {
                    "vector.tokens": {
                        "model_id": es_model_id,
                        "model_text": search_query
                    }
                }
            },
            "sort": [
                {"_score": {"order": "desc"}}
            ]
        })
        results = []
        count =0
        file_names_and_link = []
        final_response = {}
        # Parse search results
        for hit in search_results["hits"]["hits"]:
            count+=1
            result = {
                "text": hit["_source"]["text"],
                "score": hit["_score"],
                "metadata": hit["_source"]["metadata"],
                "index": hit["_index"]
            }
            results.append(result)

            file_names_and_link.append({"file_name" : hit["_source"]["metadata"]['file_name'],"file_link": hit["_source"]["metadata"]['source_reference']})
     
            # if count==1:
            #     file_names_and_relevant_chunks.append(" \n\n"+"**File name** : "+hit["_source"]["metadata"]['file_name']+" \n\n **Chunk** : "+hit["_source"]["text"]+"\n\n\n")
            # else:
            #     file_names_and_relevant_chunks.append("\n**File name** : "+hit["_source"]["metadata"]['file_name']+" \n\n **Chunk** : "+hit["_source"]["text"]+"\n\n\n")

            #Take top chunks.
            if count==relevant_chunks:
                break
        
        # Removing duplicates
        unique_file_list = list({frozenset(item.items()): item for item in file_names_and_link}.values())

        source_list = list()

        # Iterating over the list
        for file_link in unique_file_list:
            file_link['file_name']
            file_link['file_link']
            source_list.append(f"""<a href={file_link['file_link']} target='_blank'>{file_link['file_name']}</a><br>""")

        # Close Elasticsearch connection
        cleanup(es_connection)
        logger.info("Document search completed.")

        # Prepare Prompt.
        #prompt = f"""You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior.\n You are a AI language model designed to function as a specialized Retrieval Augmented Generation (RAG) assistant. When generating responses, prioritize correctness, i.e., ensure that your response is correct given the context and user query, and that it is grounded in the context. Furthermore, make sure that the response is supported by the given document or context. When the question cannot be answered using the context or document, output the following response: \'I apologize, but I could not locate any relevant information.\' Always make sure that your response is relevant to the question. If an explanation is needed, first provide the explanation or reasoning, and then give the final answer.\nAnswer Length: comprehensive.
        #                    {search_query}: '''{result}''' 
        #                    """
#         prompt = f"""You are an expert in insurance claims and document processing. Based on the provided query and the relevant section of the insurance document, generate a clear, concise answer that directly addresses the user's question. Focus only on relevant claim-related information and limit Answer Length: comprehensive.
#         Inputs:
#         Query: {search_query}
#         Chunk: {result}
#         Instructions:
#         Identify key terms and details in the query.
#         Analyze the provided document chunk, focusing on insurance claim-related sections like coverage, policy terms, required documents, or claim processing steps.
#         Answer the query accurately and concisely, based solely on the provided information.
#         Output:
#         A concise, context-relevant response addressing the query and Answer Length: comprehensive
#         """
#         prompt = (
#     f"You are an expert in insurance claims and document processing. Based on the provided query and "
#     f"the relevant section of the insurance document, generate a clear, concise answer that directly "
#     f"addresses the user's question. Focus only on relevant claim-related information and limit Answer Length: comprehensive.\n"
#     f"Inputs:\n"
#     f"Query: {search_query}\n"
#     f"Chunk: {result}\n"
#     f"Instructions:\n"
#     f"Identify key terms and details in the query.\n"
#     f"Analyze the provided document chunk, focusing on insurance claim-related sections like coverage, "
#     f"policy terms, required documents, or claim processing steps.\n"
#     f"Answer the query accurately and concisely, based solely on the provided information.\n"
#     f"Output:\n"
#     f"A concise, context-relevant response addressing the query and Answer Length: comprehensive."
# )

        prompt = (
    f"You are an expert in insurance claims and document processing. Based on the provided query and "
    f"the relevant section of the insurance document, generate a clear, concise answer that directly "
    f"addresses the user's question. Focus only on relevant claim-related information and limit Answer Length: comprehensive."
    f"If a question is asked which is out of context, reply by saying. 'I'm happy to help you with claims related questions,"
    f"However, I am not equipped to answer general knowledge questions."
    f"Inputs:\n"
    f"Query: {search_query}"
    f"Chunk: {result}"
    f"Instructions:"
    f"Identify key terms and details in the query."
    f"Analyze the provided document chunk, focusing on insurance claim-related sections like coverage, "
    f"policy terms, required documents, or claim processing steps."
    f"Answer the query accurately and concisely, based solely on the provided information."
    f"Output:\n"
    f"A concise, context-relevant response addressing the query and Answer Length: comprehensive."
    f"If answere length is more than 1 sentence, then generate the sentences in bullet points,"
    f"The relevant_chunks which are retrieved, make it short and crisp."
)

        print("WXD Response : ",results)
        # Send the prompt, query and relevant chunk to LLM and get response.
        output = send_to_watsonxai(prompts=[prompt],model_name=os.environ["MODEL_ID"],max_new_tokens=int(os.environ["MAX_TOKENS"]))
        final_response['answer'] = output
        final_response['source'] = source_list

        return {"results": final_response}
    except Exception as ex:
        logger.error(f"Error while fetching data from Elastic DB: {ex}")
        raise HTTPException(status_code=500, detail="Error while fetching data from Elastic DB." + str(ex))

# Run the FastAPI app with Uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
