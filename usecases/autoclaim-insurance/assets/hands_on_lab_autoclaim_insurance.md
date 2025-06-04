#  Automate Insurance Claim Processing with Agentic AI

## Table of Contents

- [Autoclaims Insurance: Automate Insurance with Watsonx Orchestrate and Agentic AI](#autoclaims-insurance-automate-insurance-with-watsonx-orchestrate-and-agentic-ai)
  - [Table of Contents](#table-of-contents)
  - [Use case description](#use-case-description)
  - [Architecture](#architecture)
  - [WxO Implementation](#wxo-implementation)
    - [Pre-requisites](#pre-requisites)
    - [Watsonx Orchestrate Deployment](#watsonx-orchestrate-deployment)

## Use case description

With the help of Agentic AI powered by watsonx Orchestrate, you will build an intelligent, agent-driven system that streamlines the entire claims process. This solution not only assists customers in effortlessly filing their claims but also empowers insurers to process them more efficiently, reducing manual effort and turnaround time.
Customers can simply answer a few guided questions and initiate a claim using minimal information. From there, the agentic system intelligently handles the end-to-end filing process—including document generation, data extraction, and claim verification—ensuring speed, accuracy, and ease of use. Additionally, customers can quickly check the status of their claims at any time, improving transparency and enhancing their overall experience.
On the insurer's side, submitted claims can be seamlessly fetched, and the agentic system automatically cross-verifies claim details against the customer’s policy documents. It extracts key information and validates it against predefined business rules and regulatory guidelines. Based on this analysis, the system generates intelligent, structured suggestions on whether a claim should be approved or rejected—significantly reducing manual effort and the risk of errors. The final decision, however, remains with the insurer, supported by a clear and concise summary of all relevant details.

## Architecture

<img width="1000" alt="image" src="Autoclaims_Insurance_Architecture.png">

## Implementation

### Pre-requisites

- Check with your instructor to make sure **all systems** are up and running before you continue.
- Validate that you have access to the right techzone environment for this lab.
- Validate that you have access to a credentials file that you instructor will share with you before starting the labs.
- If you're an instructor running this lab, check the **Instructor's guides** to set up all environments and systems.

### Implementation

**Information Agent:**

- Click on Agent Builder.
- Click on Create Agent
- Follow the steps according the below screenshot.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/29.png">

- Now click on add tool to upload OpenAPI Specs. Click on Add Tool.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/30.png">

- Click on Import from External Tool

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/31.png">

- Upload the required OpenAPI Specs
[duckduckgo](/usecases/autoclaim-insurance/assets/open_api_specs/duckduckgo.json)

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/32.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/33.png">

- Select the API. Then, select Done.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/34.png">

- Add Behviour as to how the Agent should behave and what it should expect.
- Make sure to also Add Description of the Agent.
- Refine the Tool Description what to expect from the tools.
- Find out what to add here: [Description and Behaviour](/usecases/autoclaim-insurance/assets/description_and_behaviour/information_agent.txt)

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/35.png">

- Test the Agent flow and then Click on Deploy.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/36.png">

**Claim_Processor_Agent:**

- Login into IBM Cloud. Navigate to Resource List. Click on Watsonx Orchestrate.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/0.png">

- Welcome to Watsonx Orchestrate. Click on Build.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/1.png">

- Click on Agent Builder.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/2.png">

- Click on Create Agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/3.png">

- Follow the steps according the below screenshot.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/4.png">

- Upload "Policy.pdf"  [Claim Processor Knowledge Base](/data/Policy.pdf) to the knowledge base by clicking on Upload files.
- Add Description of Knowledge Base as to what the Knowledge Base is about.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/5.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/6.png">

- Now click on add tool to upload OpenAPI Specs. Click on Add Tool.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/7.png">

- Click on Import from External Tool

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/8.png">

- Upload the required OpenAPI Specs
[open_top_5_claims](/usecases/autoclaim-insurance/assets/open_api_specs/open_top_5_claims.json)
[claim_processor_fetch_claim](/usecases/autoclaim-insurance/assets/open_api_specs/claim_processor_fetch_claim.json)
[claim_status_update](/usecases/autoclaim-insurance/assets/open_api_specs/claim_status_update.json)

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/9.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/10.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/10_1.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/10_2.png">

- Select the API. Then, select Done.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/11.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/11_1.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/11_2.png">

- Click on Add Agent. Add from Local Instance.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/12.png">

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/13.png">

- Add information-agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/14.png">

- Add Behviour as to how the Agent should behave and what it should expect.
- Make sure to also Add Description of the Agent.
- Refine the Tool Description what to expect from the tools.
- Find out what to add here: [Description and Behaviour](/usecases/autoclaim-insurance/assets/description_and_behaviour/claim_processor_insurance_agent.txt)

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/15.png">

- Test the Agent flow and then Click on Deploy.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/16.png">


**Customer Agent:**

- Click on Agent Builder.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/17.png">

- Click on Create Agent

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/18.png">

- Follow the steps according the below screenshot.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/19.png">

- Upload "Automobile Insurance Knowledge Base.pdf" [Customer Knowledge Base](</usecases/autoclaim-insurance/assets/data/Automobile Insurance Knowledge Base.pdf>) to the knowledge base by clicking on Upload files.
- Add Description of Knowledge Base as to what the Knowledge Base is about.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/20.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/21.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/21_1.png">

- Now click on add tool to upload OpenAPI Specs. Click on Add Tool.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/22.png">

- Click on Import from External Tool

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/23.png">

- Upload the required OpenAPI Specs. Select the API. Then, select Done.
[claim_status](/usecases/autoclaim-insurance/assets/open_api_specs/claim_status.json)
[tool_create_claim](/usecases/autoclaim-insurance/assets/open_api_specs/tool_create_claim.json)

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/24.png">

API 1: 
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/25.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/26.png">

API 2: 
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/25_1.png">
<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/26_1.png">

- Add Behviour as to how the Agent should behave and what it should expect.
- Make sure to also Add Description of the Agent.
- Refine the Tool Description what to expect from the tools.
- Find out what to add here: [Description and Behaviour](/usecases/autoclaim-insurance/assets/description_and_behaviour/customer_claims_agent.txt)

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/27.png">

- Test the Agent flow and then Click on Deploy.

<img width="1000" alt="image" src="/usecases/autoclaim-insurance/assets/screenshots_hands_on_lab/28.png">

***Now, the Agents are deployed.***
***You can navigate to AI chat and select the required agent and test the flow.***
