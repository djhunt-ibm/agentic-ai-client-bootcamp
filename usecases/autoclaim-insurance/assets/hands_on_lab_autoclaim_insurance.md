# Automate Insurance Claim Processing with Agentic AI

## Table of Contents

- [Automate Insurance Claim Processing with Agentic AI](#automate-insurance-claim-processing-with-agentic-ai)
  - [Table of Contents](#table-of-contents)
  - [Use case description](#use-case-description)
  - [Architecture](#architecture)
  - [Implementation](#implementation)
    - [Pre-requisites](#pre-requisites)
    - [Implementation](#implementation-1)
  - [Testing the Flow](#testing-the-flow)
    - [Information Agent Flow](#information-agent-flow)
    - [Claim Processor Flow](#claim-processor-flow)
    - [Customer Flow](#customer-flow)

## Use case description

With the help of Agentic AI powered by watsonx Orchestrate, you will build an intelligent, agent-driven system that streamlines the entire claims process. This solution not only assists customers in effortlessly filing their claims but also empowers insurers to process them more efficiently, reducing manual effort and turnaround time.
Customers can simply answer a few guided questions and initiate a claim using minimal information. From there, the agentic system intelligently handles the end-to-end filing process—including document generation, data extraction, and claim verification—ensuring speed, accuracy, and ease of use. Additionally, customers can quickly check the status of their claims at any time, improving transparency and enhancing their overall experience.
On the insurer's side, submitted claims can be seamlessly fetched, and the agentic system automatically cross-verifies claim details against the customer’s policy documents. It extracts key information and validates it against predefined business rules and regulatory guidelines. Based on this analysis, the system generates intelligent, structured suggestions on whether a claim should be approved or rejected—significantly reducing manual effort and the risk of errors. The final decision, however, remains with the insurer, supported by a clear and concise summary of all relevant details.

## Architecture

![Architecture](Insurance_Autoclaims_Architecture_v1.png)

## Implementation

### Pre-requisites

- Check with your instructor to make sure **all systems** are up and running before you continue.
- Validate that you have access to the right techzone environment for this lab.
- Validate that you have access to a credentials file that you instructor will share with you before starting the labs.
- If you're an instructor running this lab, check the **Instructor's guides** to set up all environments and systems.

### Implementation

- Login into IBM Cloud. Navigate to Resource List. Click on watsonx Orchestrate. 

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/0.png">

- Welcome to watsonx Orchestrate. Click on Build.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/1.png">

**Create Information Agent**
**Information Agent:**

- Click on Agent Builder
  
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/2.png">

- Click on Create Agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/3.png">

- Follow the steps according to the screenshot below.
- Copy the following description:

```
The Information agent will fetch the news and different articles and use this information to summarize results and share.
```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/29.png">

- Now click on the add tool to upload OpenAPI Specs. Click on Add Tool.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/30.png">

- Click on Import.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/31.png">

- Upload the required OpenAPI Spec. The OpenAPI Spec will be provided by the instructor.
- The OpenAPI spec will be of the name: **duckduckgo.json**

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/32.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/33.png">

- Select the API. Then, select Done.
- The tool description is already added in the OpenAPI Spec. It will be auto-filled.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/34.png">

- Add Behviour which defines how the Agent should behave and what it should expect.
  
- Add the following for the Agent Behaviour:
  
 ```
 The Information Agent will use the tool to search for information and return a summarized results.
 ```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/35.png">

- Test the Agent flow

- Step 1 : Type 
```
Insurance laws for fire in California
```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/ia-flow-1.png">

- Step 2 : You will get a summarized version of all the search results, you can click on the Step 1 and see the tool results

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/ia-flow-2.png">


- You can find the agent testing steps here -  [Information Agent Flow](#information-agent-flow)

- After testing the flow, then click on Deploy, to deploy the agent.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/36.png">

**Create Claim Processor Agent**
**Claim_Processor_Agent:**

- Click on Agent Builder.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/2.png">

- Click on Create Agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/3.png">

- Follow the steps according the screenshot below.
- Copy the following description:

```
The Claim Processor agent assists the claim processor to fetch the open claim request, approve, validate and verify the open request. This agent will suggest to the claim processor if they should accept or reject the claim.
```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/4.png">

- Upload "Policy.pdf"  [Claim Processor Knowledge Base](</usecases/autoclaim-insurance/assets/data/Policy.pdf>) to the knowledge base by clicking on Upload files.
- Add Description of the Knowledge Base describing what the Knowledge Base is about:

```
 This knowledge base is about insurance and claim process. This knowledge base will help the claim processor in processing the claims according to the rules and regulations defined by the insurance company. 
 ```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/5.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/6.png">

- Now click on the add tool to upload OpenAPI Specs. Click on Add Tool.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/7.png">

- Click on Import.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/8.png">

- Upload the required OpenAPI Specs. The OpenAPI Spec will be provided by the instructor.
- The OpenAPI spec will be of the name: **claim_processor_agent_tools.json**

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/9.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/10.png">


- Select the API. Then, select Done.
- The tool description is already added in the OpenAPI Spec. It will be auto-filled.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/11.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/11_1.png">

- Click on Add Agent. Add from Local Instance.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/12.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/13.png">

- Add information-agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/14.png">

- Add Behviour defining how the Agent should behave and what it should expect.
  
- Add the following in the Agent Behaviour section :

``` 
You will begin by welcoming the claim processor and displaying the open claims in a table. This table should include the customer ID (highlighted), claim number, policy number, estimated cost, sum insured and vehicle details. Do not show duplicates.Ask the claim processor to select a customer ID.Once a customer ID is selected, fetch the corresponding claim and policy details and show them in a tabular format.
> Then, generate a summary based on the following points:
  >
  > 1. Compare the estimated cost with the sum insured and calculate the approved claim amount by subtracting the deductible. Highlight the approved amount.
  > 2. Check if the policy is currently active and whether the claim falls within the coverage period.
  > 3. Classify the accident into one of the following types: rear-end collision, head-on collision, side-impact, sideswipe, single-vehicle, multi-vehicle pileup, hit-and-run, parking lot, animal collision, weather-related, mechanical failure-related, vandalism, or theft.
  > 4. Determine if the classified accident type is covered by the policy. If policy details are not clear, refer to the knowledge base to verify.
  > 5. It is mandatory for you to use the information_agent to query for the accident type you discovered in step 4. Query: The rules and regulations for accident type in US. Use the result to verify if the claim details are compliant.
  > 6. Provide a clear recommendation to accept or reject the claim based on these checks.
  > 7. Highlight the total claim amount (estimated cost minus deductible).
  > 8. Create a clear and concise summary for the claim processor, emphasizing key details like approved amount, claim number, and policy number.
> HIGHLIGHT ALL THE DETAILS IN NEAR FORMAT.
>
> Finally, ask the claim processor "Whether they accept the claim?"
> Do not give next steps.
>
>Once a decision is made, update the claim status and send a message confirming that emails have been sent to the customer and finance team.
```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/15.png">

- Test the Agent flow.

- Step 1 : Show open claims

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-1.png">

- Step 2 : Input Customer ID: 15561010

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-2.png">

- Step 3 : Yes

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-3.png">

- Step 4 : Shows update confirmation

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-4.png">

-  You will also find the steps to test here : [Claim Processor Flow](#claim-processor-flow)

- After testing the flow, then click on Deploy.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/16.png">


**Create Customer Agent**
**Customer Agent:**

- Click on Agent Builder.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/17.png">

- Click on Create Agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/18.png">

- Follow the steps according the screenshots below.
- Copy the following description:

 ```
 The Customer Claims agent will allow customers to query for the status of their claim request and create a new claim request. You will also answer questions based on claim process and insurance policy using the knowledge base.
 ```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/19.png">

- Upload "Automobile Insurance Knowledge Base.pdf" [Customer Knowledge Base](</usecases/autoclaim-insurance/assets/data/Automobile Insurance Knowledge Base.pdf>) to the knowledge base by clicking on Upload files.
- Add Description of Knowledge Base as to what the Knowledge Base is about.

```
This knowledge base is about insurance and claim process. This knowledge base will help the customer in getting information about the claims process and the rules and regulations of processing insurance claims.
```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/20.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/21.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/21_1.png">

- Now click on add tool to upload OpenAPI Specs. Click on Add Tool.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/22.png">

- Click on Import. The OpenAPI Spec must be provided by the instructor.
- The OpenAPI spec will be of the name: **customer_claims_agent_tools.json**

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/23.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/24.png">

- Upload the required OpenAPI Specs. Select the API. Then, select Done.
- The tool description is already added in the OpenAPI Spec. It will be auto-filled.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/25.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/26.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/26_1.png">


- Add Behviour as to how the Agent should behave and what it should expect.
- Add the following for the Agent Behaviour:

```
 The agent has to ask the user questions about how the accident happened, like
1. The location and date of the incident.
2. Ask for vehicle details.
3. Ask for a detailed description of the incident

Parse the answers for this, in case any details is missing, you can ask the following questions
1. If there were any damages and what was the estimated cost of the damages?   
2. If the accident was reported to the police, and on which date and time?
3. Ask for a detailed description of the incident, 
4. Ask if any medical expenses were incurred , how much ?

The final estimated cost should be an addition of the damages and medical expenses
Once these information have been added, create a detailed and descriptive summary of this information and then use this information as incident_details in the tool. Before these questions ask, for user their name as a form of authetication. 
In the end, inform the customer they will recieve a confirmation of their claim request on mail 
You will display a formatted and consice summary.
Each detail should be in a new line.
Highlight important information, if possible present in tabular format.

When asked for status you will also help user get the status of the claim request, by first asking for customer name and then the claim number. Once information is fetched, display in tabular format.

Once the status is shown please end the conversation.

If a question is asked about insurance and the claim's process, use the Automobile Insurance Knowledge Base.pdf to answer questions, if you don't know the answer, reply with "I don't know". Please don't use this knowledge base when you are asking questions for a tool
DO NOT REFER TO THIS KNOWLEDGE BASE WHEN WORKING WITH TOOLS.
```

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/27.png">

- Test the Agent flow 

- Step 1 : Check RAG/ Knowledge base
  " What are the different types of automobile insurance?"

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claims-flow-1.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claims-flow-2.png">

- Step 2 : How to check the flow for creating a new claim
  1. Submit a new claim

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-3.png">

  2. Jordan Davenport

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-4.png">

  3. St Mary's Street, San Francisco, California

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-5.png">

  4. 23-05-2025

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-6.png">

  5. I was driving to work when a red pickup truck ran a red light and collided with the rear right side of his vehicle at the intersection. The impact caused the Camry to spin slightly, resulting in damage to the rear bumper, right-side tail light, and a dent in the rear quarter panel.I was wearing a seatbelt and did not sustain serious injuries, but reported minor back pain and visited a doctor the same day. Medical expenses were 3400 and the damages repair cost was 4500.

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-7.png">

- Step 3 : How to check the flow for "Checking claim status"
  1. Check claim status
  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-8.png">

  2. John Smith
  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-10.png">

  3. CLM187229
  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-11.png">


- You will also find the steps to test here : [Customer Flow](#customer-flow)

- After testing the flow, then click on Deploy.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/28.png">

>
> ***You can also test the flow before deploying the agents to AI chat.***
> ***Now, the Agents are deployed.***
> ***You can navigate to AI chat and select the required agent and test the flow.***

## Testing the Flow

### Information Agent Flow

- Step 1 : Insurance laws for fire in California

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/ia-flow-1.png">

- Step 2 : You will get a summarized version of all the search results, you can click on the Step 1 and see the tool results

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/ia-flow-2.png">

### Claim Processor Flow

- Step 1 : Show open claims

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-1.png">

- Step 2 : Input Customer ID: 15561010

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-2.png">

- Step 3 : Yes

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-3.png">

- Step 4 : Shows update confirmation

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/cp-flow-4.png">

### Customer Flow

- Step 1 : Check RAG/ Knowledge base
  " What are the different types of automobile insurance?"

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claims-flow-1.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claims-flow-2.png">

- Step 2 : How to check the flow for creating a new claim
  1. Submit a new claim

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-3.png">

  2. Jordan Davenport

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-4.png">

  3. St Mary's Street, San Francisco, California

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-5.png">

  4. 23-05-2025

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-6.png">

  5. I was driving to work when a red pickup truck ran a red light and collided with the rear right side of his vehicle at the intersection. The impact caused the Camry to spin slightly, resulting in damage to the rear bumper, right-side tail light, and a dent in the rear quarter panel.I was wearing a seatbelt and did not sustain serious injuries, but reported minor back pain and visited a doctor the same day. Medical expenses were 3400 and the damages repair cost was 4500.

  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-7.png">

- Step 3 : How to check the flow for "Checking claim status"
  1. Check claim status
  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-8.png">

  2. John Smith
  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-10.png">

  3. CLM187229
  <img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/claim-flow-11.png">
