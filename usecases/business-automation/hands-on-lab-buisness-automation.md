# 👨🏻‍💻 Use case: Business Automation   

## Table of Contents
- [Architecture](#-architecture)
- [Use Case Description](#use-case-description)
- [Pre-requisites](#pre-requisites)
- [Agent Lab - watsonx.ai](#agent-lab---watsonxai)
  - [Link Search Agent](#link-search-agent)
    - [Setup](#setup)
    - [Configuration](#configuration)
    - [Tools](#tools)
    - [Saving and Deploying](#saving-and-deploying)
- [Deploying watsonx.ai's External-Agent on Orchestrate](#deploying-watsonxais-external-agent-on-orchestrate)
- [Orchestrate Agent](#orchestrate-agent)
  - [Comparison Agent](#comparison-agent)
  - [Product Agent](#product-agent)
- [Experience Agents in Action](#experience-agents-in-action)


## 🏛 Architecture  

<img width="900" alt="image" src="assets/Business_Automation_Architecture.png">

## Use Case Description

The sales department of ABC Motor Corp, an automotive large player, when preparing sales proposals, they were spending a lot of time understanding the features of competing products and comparing them with their own products. ABC Motor Corp, needs an automated competitive analysis system to help their sales teams quickly identify and position their products against competitors. Traditionally, gathering competitor insights required extensive manual research, making it inefficient and prone to outdated information. Therefore, the goal of this use case is to create an AI enabled system that support the customer's competitive analysis and market research.

## Pre-requisites

- Check with your instructor to make sure **all systems** are up and running before you continue.
- If you're an instructor running this lab, check the **Instructor's guides** to set up all environments and systems.

## Agent Lab - watsonx.ai

>**Note:** Before starting the Agent creation, ensure you have generated your API key of watsonx.ai instance. 

We will create one agent **Link Search Agent** in watsonx.ai's Agent Lab as part of this setup:  

From the Home page of Agent Lab, click on the Build an AI agent to automate tasks

![Home page](assets/agent_lab_home.png) 

Let's start the **Link Search Agent**. 

### Link Search Agent  
#### Setup  
1. Enter a **name** for the agent as shown in the image.
2. Add a **description** (optional).
```
Agent specialised for searching URLs on the internet.
```
![Setup](assets/setup_link_search_agent.png)  

#### Configuration    
1. Choose **LangGraph** as the framework.  
2. Select **ReAct** as the architecture. 
3. Enter the **Instructions** as shown in the image. These instructions guide your agent on what tasks it should perform. You can use below prompt for it.
```
You are a skilled assistant specialized in locating URLs for similar products with matching features. Provide a maximum of three URLs with name of the product.
```
![Configuration](assets/configuration_link_search_agent.png)  


> **Note:** The Google Search Tool is added by default to the Agent. However, if you accidentally click the delete icon, follow the Tool steps below. Otherwise, you can skip this.

#### Tools  

1. Click on the Add Tool.
![Add Tool](assets/add_tool.png)

2. Select **Google Search** as the tool to gather data.  
![Tool](assets/tool_link_search_agent.png)  

#### Saving and Deploying
1. Once the agent is created, test it on the right-hand side of the chat section, as shown in the image below.
2. Click on the **Save As** button to save your Agent
3. click on the **Deploy** button to deploy the agent.
![Link Search Agent Chat](assets/chat_link_agent.png) 
4. After clicking on the save as button select Agent (marked as 1) and Click Save ((marked as 2))
![Link Search Agent Chat](assets/saveas_link_agent.png)
5. After clicking the deployoment button make sure your Targeted deployemnt has been seleceted if not please select it.(marked as 1), click Deploy to deploy the agent (marked as 2)
![Link Search Agent Chat](assets/deployment_config.png)

Follow these steps to successfully create the Link Search Agent.  

## Deploying watsonx.ai's External-Agent on Orchestrate

To deploy your agent on Orchestrate, follow the steps below: 

1. Go to the homepage of watsonx.ai Agent Lab.
![Home page](assets/agent_lab_homepage.png)

2. Click on the hamberger menu and select **Deployments**.  
![Deployments](assets/hamberger_agent_lab.png)

3. Click on the **Spaces** tab and select the space where you deployed the agent.  
![Spaces](assets/spaces_agent_lab.png)

4. Click on the **Assets** tab and select the agent.  
![Asset tab](assets/asset_agent.png)

5. Then you will go the the main deployment page select your agent from the list.
![Deployment agent](assets/deployment_agent.png)

6. Then copy the public endpoint
![Deployment agent](assets/url_agent.png)

7. Now, go to the Orchestrate home page, click on the hamburger menu (☰), select Build, and then choose Agent Builder.
![Agent Builder](assets/agent_build_wxo.png)

8. Click on the Create Agent button.
![Create Agent](assets/create_wxo.png)

9. Select Create from scratch (as shown in image 1 below), enter your agent’s name (as shown in image 2), provide a description (as shown in image 3), and then click the Create button (as shown in image 4).
![Create from scratch](assets/create_from_scratch.png)
**Description:**
   ```
   The agent is specialized in searching for relevant URLs on the web based on the input query. It scans online sources to find useful links that can support product research, comparisons, or other business needs.
   ```
   ![Create from scratch](assets/create_from_scratch.png)   

10. After the agent is created, you will be redirected to the agent configuration page.
![Agent configuration](assets/external_agent.png)

11. Scroll down to the Toolset section, then under Agents, click on the Add Agent button.
![Add Agent](assets/add_agent.png)

12. Select the import option.
![Import option](assets/import_agent.png)

13. On the next page, ensure that External Agent is selected (as shown in image 1 below). If it’s not already selected, please choose it, then click the Next button (as shown in image 2).
![External Agent](assets/external_agent_select.png) 

14. On the next page, enter the following information:
      1. API key: Enter the watsonx.ai API key.
      2. Service instance URL: Enter the public endpoint URL of the agent that we copied in step 6.
      3. Display name: Enter the name of the agent.
      4. Description: Enter the below description.
      5. Click on the Import Agent button.

**Description:**
   ```
   This agent is skilled in locating URLs for similar products with matching features. A maximum of three URLs should be provided, each accompanied by the product name.
   ```
   ![External Agent](assets/external_agent_setup.png)

15. You can confirm that your agent has been successfully imported if it appears under the Agents section within the Toolset.
![External Agent](assets/agent_imported_success.png)

16. Once the agent is created , test it on the right-hand side of the chat section, as shown in the image below and click the deploy button to publish it.
![Link Search Agent Chat](assets/click_deploy.png) 

## Orchestrate Agent

In Orchestrate, we will create two agents, as outlined below:

1. Comparison Agent
2. Product Agent


### Comparison Agent

1. Go to the Orchestrate home page, click on the hamburger menu (☰), select Build, and then choose Agent Builder.
![Agent Builder](assets/agent_build_wxo.png)

2. Click on the Create Agent button.
![Create Agent](assets/create_wxo.png)

3. Select Create from scratch (as shown in image 1 below), enter your agent’s name (as shown in image 2), provide a description (as shown in image 3), and then click the Create button (as shown in image 4).

   For comparison Agent use the below description

   ```
   This agent is designed to compare the given data with additional information gathered from Google search results. Its task is to carefully analyze the input data, extract key insights, and identify both differences and similarities. The findings should be presented in a well-structured table format, making it easy to understand and compare the information at a glance.
   ```
   ![Create from scratch](assets/comaprison_scratch.png)

4. After the agent is created, navigate to the Agent Configuration page. Scroll down to the Behavior section, add the description shown in image as 1, and then click the Deploy button as shown in image as 2.

   For comparison Agent use the below description in Behavior Section

   ```
   You are an expert of automobile industry combining given details present in your context window. You have to use the given links to generate the comparison. Your task is to analyse and compare products on the following features strictly: Range, Pricing, Acceleration, Top Speed, Interior and Safety Features If a feature is not applicable, mark it as N/A. Additionally, perform a SWOT analysis of top products (Strengths, Weaknesses, Opportunities, and Threats) Present the comparison in 3 tables one for the comparison , second for the rating numerical rating (X/5) and a star rating (★ out of ★★★★★) for each feature  and  third for the SWOT analysis. Give heading to each table . After every table give two divider.

   Instructions:

   1. Title for Table 1: Feature Comparison
   2. Title for Table 2: Rating Comparison
   3. Make sure that the Rating Comparison table has both the numerical(X/5) and star rating(★ out of ★★★★★)
   4. The products should be the column names in all the tables.
   5. The font size of the Table Title should be 40% bigger as compared to the rest of the text.
   6. Add appropriate space between each section in the table.
   ```
   ![Behavior](assets/comparison_final.png)

### Product Agent

1. Go to the Orchestrate home page, click on the hamburger menu (☰), select Build, and then choose Agent Builder.
![Agent Builder](assets/agent_build_wxo.png)

2. Click on the Create Agent button.
![Create Agent](assets/create_wxo.png)

3. Select Create from scratch (as shown in image 1 below), enter your agent’s name (as shown in image 2), provide a description (as shown in image 3), and then click the Create button (as shown in image 4).

   For Product Agent use the below description
        
   ```
   This agent is designed to search for a specified product and retrieve its details and features using Retrieval-Augmented Generation (RAG) on the product catalog. It presents the information in a clear and structured format, ensuring systematic organization of key product data, making it easy to understand and use.
   ```
   ![Create from scratch](assets/product_scratch.png)

4. After the agent is created, navigate to the Agent Configuration page.

   **Description:**
   ```
   Your knowledge base is the document that contains all the product-related information. All queries related to the product will be addressed using this document as the primary source.
   ```
   ![Knowledge](assets/product_knowledge.png)

5. Scroll down to the Knowledge section, then in the Document section, click on the Upload file button nad upload the product catalog.
![Upload file](assets/upload_file.png)

6. Scroll down to the Toolset section, then in the Agents section click on the Add Agent button.
![Add Agent](assets/add_agent.png)

7. From the pop-up menu, select the Add from local instance option.
![Add from local instance](assets/product_add_pop_up.png)

> **Note:** : We are now adding the Link Search Agent (an external agent) and the Comparison Agent to the Product Agent, enabling it to delegate tasks to them.

8. Then, select the Comparison Agent (as shown in image 1) and the Link Search Agent [External Agent] (as shown in image 2). After selecting both, click the Add to agent button to include them (as shown in image 3).
![Delegation Agent](assets/delegation.png)

9. Once the delegated agents are added, they will appear as shown in the image below.
![Delegation Agent](assets/agent_appear_delegation.png)

10. Scroll down to the Behavior section, add the description shown in image as 1, and then click the Deploy button as shown in image as 2.

      For Product Agent use the below description in Behavior Section.

      ```
      This agent is responsible for handling product-related queries using Retrieval-Augmented Generation (RAG) on the product catalog.

      For general product queries, it retrieves structured information directly from the knowledge base.

      For queries involving URLs or web references, it delegates the task to the Link Search Agent.

      For product comparison queries, it forwards the request to the Comparison Agent.

      This delegation ensures that each query type is handled by the most suitable agent, improving accuracy and efficiency.
      ```
      ![Behavior](assets/Product_agent_deploy.png)

> **Note:** : The Product Agent is now ready to handle product-related queries, delegating tasks to the Link Search Agent and Comparison Agent as needed.

## Experience Agents in Action
Follow the steps above, then try interacting with the use case using these sample queries:

1. Product Agent

   Ask the following questions to get responses from the Product Agent:
   ```
   Q1: What are the products of ABC Motors.
   Q2: Get me the info of Velocity S1.
   ```
   ![Skill Response](assets/chat_1.png)  

2. Link Search Agent

   Use this query to retrieve competitor links:
   ```
   Provide me the links of 4 competitors of above product.
   ```
   ![Link Search Agent Response](assets/chat_2_skill.png)

3. Comparison Agent

   To compare the retrieved data, ask:
   ```
   Give me the comparison of above data.
   ```
   ![Comparison Agent Response](assets/chat_3.png)  
   ![Comparison Agent Response 2](assets/chat_4.png)

Now, explore and experience the power of Skills & Agents in action! 🚀 
