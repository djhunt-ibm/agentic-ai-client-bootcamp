# Use case: Business Automation   

## Table of Contents
- [Introduction](#introduction)
- [Use Case Description](#use-case-description)
- [Adding Custom Skills](#adding-custom-skills)
- [Agent Creation](#agent-creation)
  - [Link Search Agent](#link-search-agent)
  - [Comparison Agent](#comparison-agent)
- [Getting the Space ID for Deployment on Code Engine](#getting-the-space-id-for-deployment-on-code-engine)
- [Deploying Agents on Code Engine](#deploying-agents-on-code-engine)
- [Integration with Watsonx Orchestrate](#integration-with-watsonx-orchestrate)
- [Agent Descriptions](#agent-descriptions)
- [Demo Video](#demo-video) 

## Introduction  

![Architecture](assets/architecture.png)  

## Use Case Description

The sales department of ABC Motor Corp, an automotive large player, when preparing sales proposals, they were spending a lot of time understanding the features of competing products and comparing them with their own products. ABC Motor Corp, needs an automated competitive analysis system to help their sales teams quickly identify and position their products against competitors. Traditionally, gathering competitor insights required extensive manual research, making it inefficient and prone to outdated information. Therefore, the goal of this use case is to create an AI enabled system that support the customer's competitive analysis and market research.

## Adding Custom Skill 

After your instructor has completed the **Product APP** setup, request the server URL from them. Open the [OPEN_API_SPEC File](open_api_spec.json) and replace the default server URL with the one provided.

![Server URL](assets/json_url.png)

Now, let's add this JSON file as a skill in **watsonx Orchestrate** by importing it.

Here's the corrected version with proper grammar and clarity:  

---

1. Open the **watsonx Orchestrate** home page and click on the menu icon (hamburger) as shown below.  
   ![Home Page](assets/hamburger_home_page.png)  

2. From the menu, select **Skill Studio**.  
   ![Skill Studio](assets/skill_studio.png)  

3. To import the API, click **Create** (marked as 1), then select **Import API** (marked as 2).  
   ![Skill Page](assets/skill_page_steps.png)  

4. Click the **From File** tab (marked as 1) and upload the [OPEN_API_SPEC File](open_api_spec.json) (marked as 2).  
   ![Upload Spec](assets/upload_spec.png)  

5. After uploading, confirm that the file name appears (marked as 1), then click **Next** to proceed (marked as 2).  
   ![File Upload](assets/file_uploaded.png)  

6. Accept the API by selecting the checkboxes (marked as 1), then click **Next** (marked as 2).  
   ![API Selection](assets/api_name.png)  

7. Once completed, all your skills will appear in **Skill Studio** under **Skills** but will be labeled **Ready to Publish**. You need to publish them before using them.  
   ![Skill Studio Skills](assets/skill_studio_skills.png)  

8. To publish a skill, click on the three vertical dots (marked as 1), then select **Enhance the Skill** (marked as 2).  
   ![Title Skill](assets/title_skill.png)  

9. In the **Get Product Detail by Title** skill, some configurations are needed. Click on the **Output** tab (marked as 1), then scroll down to the **Table** section. At the bottom of the table, enter the name of your variable, which will be displayed on the chat screen (marked as 2). Then, click the **Publish** button to publish your skill (marked as 3).  
   ![Title Skill Config](assets/title_skill_config.png)  

10. Once your **Get Product Detail by Title** skill is published, click on the three vertical dots (marked as 1) again and select **Enhance the Skill** to publish it.  
   ![Product Skill](assets/product_skill.png)  

11. For the **Get Product Title** skill, simply click **Publish**—no changes are required.  
   ![Product Skill Config](assets/product_skill_config.png)  

12. Once all skills are published, their status will change to **Published**.  
   ![All Published](assets/all_published.png)  

13. Now, we need to add our skills from the **Skill Catalog**. Click on the hamburger menu and select **Skill Catalog**.  
   ![Skill Catalog](assets/skill_catalog.png)  

14. In the search bar, type **Product** (marked as 1) and select **Product Information API** (marked as 2).  
   ![Search APP](assets/search_app.png)  

15. To add the skill, you first need to connect the API. Click on **Connect**.  
   ![Connect APP](assets/connect_catalog.png)  

16. Enter the API key to connect the app (use your TechZone instance API key) (marked as 1), then click **Connect App** (marked as 2).  
   ![API Connection](assets/api_catalog.png)  

17. After connecting the API, it will show as **Connected**.  
   ![API Connected](assets/app_connected.png)  

18. Now, we need to connect the app from the **Skill Set** as well. Click on the hamburger menu and select **Skill Set**.  
   ![Skill Set](assets/skill_set.png)  

19. On the **Skill Set** page, search for **Orchestrate Agent Skillset**.  
   ![Search Skill Set](assets/search_skill_set.png)  

20. In the **Connections** tab (marked as 1), search for **Product Information API** by navigating through the pages. Click on the three vertical dots and select **Connect App**.  
   ![Connect App](assets/connect_set.png)  

21. Click **Connect App** as shown below.  
   ![Connect App](assets/connect_api_button.png)  

22. Enter the API key (TechZone API key) (marked as 1) and click **Connect App** (marked as 2).  
   ![API Skill Set](assets/api_skill_set.png)  

23. Once connected, the API will display the user's email ID in the **Connected By** column.  
   ![Connected by](assets/connected_by.png)  

24. Since we have connected the app from the **Skill Set**, we now need to add the skill to the chat. Open the hamburger menu and select **AI Agent Configurations**.  
   ![AI Agent Config](assets/ai_agent_config.png)  

25. Click on **Apps and Skills** (marked as 1), then select **Product Information API** (marked as 2).  
   ![Apps and Skills](assets/apps_skill.png)  

26. Add both API-related skills to the chat as shown below.  
   ![Apps and Skills](assets/add_chat.png)  

27. First, add the **Get Product Details by Title** skill by clicking **Add to Chat**.  
   ![First Skills](assets/add_chat_1.png)  

28. Do not change the description; keep it as shown in the image below, then click **Add Skill**.  
   ![First Skills](assets/description_skill_1.png)  

29. Next, add the **Get Product Titles** skill to the chat.  
   ![Second Skills](assets/add_chat_2.png)  

30. Once both skills are connected, it will look like this:  
   ![Chat Connected](assets/chat_connect.png)  

31. From the hamburger menu, navigate to **Chat**.  
   ![Chat](assets/chat_from_skill.png)  

32. You can now interact with the skills as shown below.  
   ![Demo Skills](assets/demo_skill.png)  

Note before starting the Agent creation make sure you have generated your project Id and API key refer [api_key_project_id_setup.md](http:)

## Agent Creation  
We will create three agents as part of this setup:  
1. **Link Search Agent**  
2. **Comparison Agent**  

Let's start with the **Link Search Agent**.     

### Link Search Agent  
#### Setup  
- Enter a **name** for the agent as shown in the image.  
- Add a **description** (optional).  

![Setup](assets/setup_link_search_agent.png)  

#### Configuration  
- Enter the **Instructions** as shown in the image. These instructions guide your agent on what tasks it should perform.  
- Choose **LangGraph** as the framework.  
- Select **ReAct** as the architecture.  

![Configuration](images/configuration_link_search_agent.png)  

#### Tools  
- Select **Google Search** as the tool to gather data.  

![Tool](images/tool_link_search_agent.png)  

Once the agent is created, test it on the right-hand side of the chat section, as shown in the image below.  

Click on the **Save As** button to save your agent (marked as number 1 in the image). Then, click on the **Deploy** button to deploy the agent (marked as number 2 in the image). Deployment may take 1-2 minutes.  

![Link Search Agent Chat](images/chat_link_search_agent.png)  

Follow these steps to successfully create the Link Search Agent.  

---

### Comparison Agent  
#### Setup  
- Enter a **name** for the agent as shown in the image.  
- Add a **description** (optional).  

![Setup](images/setup_comparison_agent.png)  

#### Configuration  
- Enter the **Instructions** as shown in the image. These instructions guide your agent on what tasks it should perform.  
- Choose **LangGraph** as the framework.  
- Select **ReAct** as the architecture.  

![Configuration](images/configuration_comparison_agent.png)  

#### Tools  
- Select **Google Search** as the tool to gather data.  

![Tool](images/tool_comparison_agent.png)  

Once the agent is created, test it on the right-hand side of the chat section, as shown in the image below.  

Click on the **Save As** button to save your agent (marked as number 1 in the image). Then, click on the **Deploy** button to deploy the agent (marked as number 2 in the image). Deployment may take 1-2 minutes.  

![Comparison Agent Chat](images/chat_comparison_agent.png)  

Follow these steps to successfully create the Comparison Agent.

## Getting the Space ID for Deployment on Code Engine

To deploy your agent on Code Engine, follow the steps available in instruct lab how to deploy your agents to get your Space ID:

### Space ID

1. Go to the home page of Agent Lab. 
![Home](images/home.png)   

2. Click the hamburger menu and choose Deployment.
![Deploment Selection](images/deployment.png)  

3. On the Deployment page, find Deployment Space and click on it.
![Spaces](images/spaces.png)  

4. Click on the Manage tab and copy your Space ID.
![Manage](images/manage.png) 

### Deployment

On the Deployment Space page, select the agent. It will take you to the deployment page, where you can get the Deployment ID.

![Deployment Space](images/deployments_space.png)

![URL Deployment](images/url_deployment.png)

Repeat the same step for all the agents, as shown in the image below

## Deploying Agents on Code Engine

Please refer to the [Code Engine instructor](https://github.ibm.com/skol/agentic-ai-client-bootcamp-instructors/blob/main/environment-setup/external-agent-builder/Readme.md) guide for deployment instructions. Once you obtain the deployment link, kindly open it.

You will reach the page shown in the image below. Follow these two steps to generate the Bearer Token:

1. Enter the Deployment ID and Space ID, then click on the Generate Token button.
![Token generator](images/token_generation.png)

2. Copy the Bearer Token.
![Generated Token](images/generated_token.png)

The Space ID remains constant for all agents, but each Deployment ID has a unique Bearer Token.

Repeat these steps for all the remaining agents to get their respective Bearer Tokens.

## Integration with Watsonx Orchestrate

1. Go to the home page of Watsonx Orchestrate.
![WxO Home](images/wxo_home.png)

2. Click the hamburger menu and choose AI Agent Configuration.
![AI Agent Configuration](images/agent_config.png)

3. On the Configuration page, select Agents.
![Agents](images/agent_config_page.png)

4. On the Agents page, click the New Agent button.
![Add Agent](images/add_agent.png)

5. Enter all the details as shown in the image and select "Bearer Token" instead of "API Key."
![Bearer Token](images/bearer_token.png)

6. Click the Connect button to integrate the agents with Watsonx Orchestrate.
![Connect](images/connect.png)

Repeat these steps for all the remaining agents to integrate them in Watsonx Orchestrate.

## Agent Descriptions

1. Link Search Agent: This agent is an expert in finding URLs or links for similar products that share matching features, ensuring users can explore alternatives efficiently.

2. Comparison Agent: This agent is designed to compare the given data with additional information gathered from Google search results. Its task is to carefully analyze the input data, extract key insights, and identify both differences and similarities. The findings should be presented in a well-structured table format, making it easy to understand and compare the information at a glance.

After completing the integration, your flow will appear as shown below.

![Flow](images/flow.png)


## Demo Video

[![Demo](images/wxo_home.png)](video/Demo.mp4)
