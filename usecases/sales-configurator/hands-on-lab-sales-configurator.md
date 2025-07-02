# 👨🏻‍💻 Use case: Sales Configurator

This lab walks you through setting up the **Sales Configurator** use case using watsonx orchestrate tools. 

## Table of Contents
- [Use Case Description](#use-case-description)
- [Architecture](#architecture)
- [Pre-requisites](#pre-requisites)
- [watsonx Orchestrate - Agent Builder](#watsonx-Orchestrate---Agent-Builder)
    - [AI Agent Configuration](#AI-Agent-Configuration)
    - [Personalization Agent](#Personalization-Agent)
    - [Support Agent](#Support-Agent)
- [watsonx.ai - Agent Lab](#-watsonx.ai---Agent-Lab)


## Use Case Description

The Sales Configurator use case leverages AI agents to simplify the process of gathering customer requirements for cloud, server, or hybrid cloud configurations, adapting to the diverse needs of customers. The solution guides customers through targeted questions, enabling a Solutions Architect to design a tailored solution meeting their specific needs. The conversation concludes with an automated email sent to the Solutions Architect, detailing the customer's requirements and providing a unique confirmation number for the customer to track their case progress, ensuring a seamless and efficient experience for both customers and Solutions Architects.

This chat system is a multi-agent solution where each agent is specialized in handling specific parts of the process. Each agent is connected with a Large Language Model (LLM) that supports function calling, so that it can leverage one or more tools based on each tool's description. The solution consists of: Personalization, Configuration, Comparison and Support agents. All four agents are connected to a "routing agent" that will take requests from the end user and then select the appropriate agent for excecution before returning the answer. 


The flow of interacion we are simulating is one where a cusotmer starts the conversation to know more about IBM Cloud and Server solution, here the Personalization agent starts asking a few questions about the user such as name and job title to build their profile as well as some contact information to be able to connect with them for the possible next steps. Next, the Configuration agent starts asking questions about the cusotmer's painpoints, challenges and requirements, while adopting the question line based on the responses. Once enough information is gathered, this agent will summarize the requirements and confirm it with the user. Then the Support agent shared this summary with the Solution Architect and sets up next steps. There is also another agent called the Comparison agent which will take over, if the customer has questions about the IBM products advantges and/or how they compare with other solutions. Even though we will take you through a complete and working example, you should also consider making changes that fit your desired use case, and only take this description as a reference point that guides you along your own implementation.

## 🏛 Architecture  

<img width="900" alt="image" src="assets/solution_arch.png">

## Pre-requisites

- Check with your instructor to make sure **all systems** are up and running before you continue.
- Please go the through the [environment-setup](/environment-setup) guide for steps on API key creation, project setup, and related configurations.
- If you're an instructor running this lab, check the [Instructor's guides](https://github.ibm.com/skol/agentic-ai-client-bootcamp-instructors/blob/main/environment-setup/readme.md) to set up all environments and systems.

## watsonx Orchestrate - Agent Builder

As shown in the Solution Architecture, we will build and deploy two of the agents on watsonx Orchestrate. To get to the watsonx Orchestrate console, go the [Resources list on the IBM Cloud homepage](https://cloud.ibm.com/resources).

<img width="900" alt="image" src="assets/ibmcloud-resources-wxo.png">

Expand the `AI / Machine Learning` section and select the resource that has `watsonx Orchestrate` in the Product column, as shown above. Next, click on the `Launch watsonx Orchestrate` button.

<img width="900" alt="image" src="assets/ibmcloud-wxo.png">

This opens the watsonx Orchestrate console.

<img width="900" alt="image" src="assets/wxo-ui.png">

Note: *When opening the console for the very first time, you may be greeted by a pop-up window offering that you create your first agent. Click on Skip for now.*

In the console, it shows that no agents have been deployed yet. Thus, if you interact with watsonx Orchestrate at this point, not much will happen, since the system has no agents available to route any request to.

However, you can already interact with the Large Language Model (LLM) that works behind the scenes, and ask general questions, like "How are you today?" or "What is the capital of France?". Go ahead and chat with watsonx Orchestrate to explore what type of answers it gives to your questions.

### AI Agent Configuration

We are now ready to build the first agent. In the watsonx Orchestrate console, click on either `Create or Deploy` or `Create new agent` (either will take you to the same place).

<img width="900" alt="image" src="assets/wxo-create-agent-1.png">

### Personalization Agent  

In the following screen, you can select if you want to create the new agent from scratch or from a template, and give it a name and a description. To create the solution, you will need to create a number of agents and we will go through them one by one, starting with the `Personalization Agent`. Let's start by giving it a name and a description:

- Name: Personalization Agent
- Description:
```
The Personalization Agent specializes in greeting the customer when they first start the conversation and collect four specific customer details to ensure a customer can be contacted. 
```

Note that in the world of AI Agents, these descriptions are not merely used as documentation, they are also used in making decisions about selecting the right agent for the job, so what you enter into this field is important.

After you have entered the required information, click on the Create button.

<img width="800" alt="image" src="assets/wxo-create-personalizationagent-1.png">

In the next step, we can enter more information about the new agent we are building. Agents can rely on Knowledge, on a Toolset that consists of one or more Tools and one or more Agents to satisfy a request that is sent to them, and we can define all of those elements here:

- **Profile** contains the agent description we defined earlier. You can always modify it here.

- **Knowledge** represents information that is stored in the form of "embeddings" in a so-called Vector Store. Whenever the agent answers a request, it can choose to run a search against the connected Knowledge repository (i.e. the Vector Store) to search for information that can assist in answering the request. You can either upload documents directly here, or connect the agent to an already existing repository. Note that once again, the "Description" field is key, because it will help the agent decide whether to run a search against the knowledge.

- **Toolset** contains other components that the agent can delegate certain tasks to.
    - Tools are functions an agent can call. It can be either an API call or an invocation of custom code. This allows to extend the agent's capabilitiy beyond what the LLM has been trained with.
    - Agents are other agents, either within watsonx Orchestrate or running externally, e.g., in watsonx.ai that this agent can delegate the request, or part of a request, to.

- **Behavior** is the section where you can define how and where your agent should react to requests and respond to users.

On the agent definition page, scroll all the way down to the Behavior section and copy the following text into the Instructions text field:

```
- You are a friendly and professional AI assistant which collects exactly four contact details from the user in a polite, natural, and engaging tone.

- You must always respond immediately when the user sends a greeting such as “Hi,” “Hello,” “Hey,” or “Greetings.” You should initiate the conversation by introducing yourself and prompting the user to share their basic contact details. 
Example: "Hi, welcome to the IBM Cloud & Servers Solutions chat, I am the Personalization Agent, could please share your name and job title?"

- You must strictly adhere to gathering only the following fields: Name, Email, Job Title, and Company Name. You must not ask any other questions, attempt to infer additional details, or deviate from this structure.

- The conversation begins with a professional introduction and you request the user’s name and email in a polite manner. If the user provides only one of these details, you should ask once for the missing information but do not persist if the user does not respond.

- After collecting name and email, the agent asks for the user’s job title and company name in a single prompt. Clarification questions can be asked if the given information is deemed too broad. If the user is unsure, you may provide examples but must not attempt to press for an answer if the user refuses to answer.

- Your responses should reflect a helpful, friendly tone — feel free to use natural expressions like "Got it", or "Thanks so much" to keep things warm and engaging, but still professional.

- You must follow a strict structure, but your responses should feel warm, natural, and conversational not robotic or scripted. You should sound like a helpful human assistant.

- Once all available details are gathered, informs the user that they will be transferred to the Configuration Agent, which will assist with IT needs assessment and solution recommendations, and ask them \n\n "How can we help you today?"

- You must never request or accept any details beyond the specified four fields, must not persist in follow-ups beyond one attempt per missing field, and must not engage in conversation beyond the structured flow. The interaction is to be strictly controlled, ensuring efficiency while maintaining a professional and user-friendly tone.
```

Finally, make sure you uncheck the `Show agent` checkbox, as shown in the picture below. This switch controls whether the agent is available in the main chat window. We only want to expose the top level agent (which we haven't created yet) there.

<img width="800" alt="image" src="assets/wxo-create-personalizationagent-1.png">

Let's now test the new agent. 

When doing this in your own instance, you may see answers that differ from the ones shown in the screenshot above. This is due to the undeterministic nature of the AI models involved. Feel free to experiment with different types of questions to see how the agent reacts. The same equally applies to all the agents described further down.

You can now go ahead and deploy the agent, using the `Deploy` button at the top right of the page. Then, go back to the Agents list on the Manage agents page, by clicking on the `Manage agents` link at the top left of the page. The Personalization Agent now shows a small green icon saying "Live". This indicates successful deployment of the agent.

### Support Agent  

This agent closes the conversation by informing the customer that an email has been sent to the solution architect, providing a ticket number for them to be able to follow up. 

In a real production deployment, the Support Agener would email the summary of the conversation and the requirements gathered by the Configuration Agent to the solution architect and create a ticket in the system, however, in this hands-on exercise, we will simulate that backend by assuming an email is sent and simply hardcoding the ticket number needed for the agent. 

In the Manage agents view, click on the `Create agent` button.

<img width="800" alt="image" src="assets/wxo-create-agent-2.png">

Note: if you are not already in the Manage agents view, you can use the hamburger menu from the top left to get there: 

<img width="800" alt="image" src="assets/wxo-go-to-agentbuilder.png">

Now leave the Create from scratch option selected, enter "Support Agent" as the name and enter the following into the Description field:

- Name: Support Agent
- Description:
```
The Support Agent is designed to confirm when an email has been successfully sent to a IBM Solution Architect and setting up the next steps. It ensures seamless communication by notifying the user with a confirmation message, including the case number and expected response time. This agent plays a crucial role in closing the loop with the customer by providing clear, timely updates without adding any product recommendations.
```

<img width="800" alt="image" src="assets/wxo-create-supportagent-1.png">

Then click on `Create`.

In the following view, scroll all the way down to the `Behavior` section, and enter the following into the `Instructions` field:

```
Persona:
- You are the Support Agent, responsible for informing the user that an email has been sent to IBM Solution Architects. Your primary task is to notify the customer that the email has been sent to the Solution Architect **when the user confirm that the summary is accurate**.

Instructions:
- You must **not** add any product recommendations—your role is strictly to communicate to the user that you sent the email.
- Immediately after the user confirms "Yes" to the question: "Is this summary accurate?" from the previous part of the conversation, lead with this exact text:

"An email has been sent to the Solution Architect with the requirements, who will contact you within 7-10 business days regarding your inquiry. Your ticket number is 7834537. You will also receive the summary of this conversation sent through email."


Follow-up message:
- **After informing the user that the email has been sent**, provide the **follow-up message as a separate block, and for the follow-up message use this exact wording and formatting:**
  
  Did you find this interaction helpful?\"

- **Follow these instructions for responses:**
        * If they say "NO," respond only with: "I'm sorry to hear that, someone will be getting in touch with you."
        * If they say "YES," respond only with this exact text (do not add any additional explanations or text):
  "Thank you, can we help you with anything else?"

- **Wait for the user's response before proceeding to the next section**
        * If  the user's response is "No," respond only with this exact text (do not add any additional explanations or text): "Thank you for using the IBM Sales Configurator, have a good day!"
        * If the user's response is "Yes," respond only with this exact text (do not add any additional explanations or text such as: Thank you, can we help you with anything else? ): "How can I assist you?"


Behavior Guidelines:
1. **Do not include product recommendations, suggestions, or promotional language.**   
2. Avoid technical jargon, internal processes, or references to how the email is generated.  
3. If insufficient data is provided to draft the email, politely request the user to provide the necessary customer requirements or details.
4. Use plain text for follow-up message formatting and ensure proper spacing (e.g., two empty lines) as specified, avoiding any overlap between the email and the follow-up message.
```

Uncheck the Show agent checkbox, just like you did for the Personalization Agent.

Before deploying this new agent, we can test its functionality by entering requests in the Preview window. Since this agent is supposed to take over when the other agents have done the questioning, summarized and confirmed the requirments, we can simulate that with something like this:

```
The summary is accurate
```

<img width="800" alt="image" src="assets/wxo-supportagent-testing.png">

Once you are satisfied with the result, click on the `Deploy` button to deploy this agent, and then click on the Manage agents link to return to the agents overview page.

You should now see two agents listed, and both should have the "Live" indicator.


## watsonx.ai - Agent Lab

As shown in the Solution Architecture, we will build and deploy two of the agents for the solution on watsonx.ai:

<img width="900" alt="image" src="assets/ibmcloud-resources-wxi.png">

### Configuration Agent  

### Comparison Agent  