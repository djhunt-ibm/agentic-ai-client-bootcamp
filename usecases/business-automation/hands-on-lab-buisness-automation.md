# Business Automation - Step-by-Step Guide  

This guide will help you create a **Business Automation Use Case** using Agent Lab and Watsonx Orchestrate.  

## System Architecture  
Below is an overview of the system:  

![Architecture](images/architecture.png)  

## Creating Agents  
We will create three agents as part of this setup:  
1. **Product Search Agent**  
2. **Link Search Agent**  
3. **Comparison Agent**  

Let's start with the **Product Search Agent**.  

## Product Search Agent  
#### Setup  
- Enter a **name** for the agent as shown in the image.  
- Add a **description** (optional).  

![Setup](images/setup_product_search_agent.png)  

#### Configuration  
- Enter the **Instructions** as shown in the image. These instructions guide your agent on what tasks it should perform.  
- Choose **LangGraph** as the framework.  
- Select **ReAct** as the architecture.  

![Configuration](images/configuration_product_search_agent.png)  

#### Tools  
- Select **Google Search** as the tool to gather data.  

![Tool](images/tool_product_search_agent.png)  

Once the agent is created, test it on the right-hand side of the chat section, as shown in the image below.  

Click on the **Save As** button to save your agent (marked as number 1 in the image). Then, click on the **Deploy** button to deploy the agent (marked as number 2 in the image). Deployment may take 1-2 minutes.  

![Product Search Agent Chat](images/chat_product_search_agent.png)  

Follow these steps to successfully create the Product Search Agent.  

---

## Link Search Agent  
#### Setup  
- Enter a **name** for the agent as shown in the image.  
- Add a **description** (optional).  

![Setup](images/setup_link_search_agent.png)  

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

## Comparison Agent  
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

To deploy your agent on Code Engine, follow these steps to get your Space ID:

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

Follow the instructions in the Code Engine instructor guide to get the deployment link. Open that link.

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
