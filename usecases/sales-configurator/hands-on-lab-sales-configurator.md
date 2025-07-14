# 👨🏻‍💻 Use case: Sales Configurator

This lab walks you through setting up the **Sales Configurator** use case using watsonx orchestrate tools. 

## Table of Contents
- [Use Case Description](#use-case-description)
  - [Architecture](#architecture)
  - [Pre-requisites](#pre-requisites)
- [watsonx Orchestrate](#watsonx-orchestrate)
    - [AI Agent Configuration](#ai-agent-configuration)
    - [The Personalization Agent](#the-personalization-agent)
    - [The Configuration Agent](#the-configuration-agent)
    - [The Support Agent](#the-support-agent)
    - [The Cloud and Server Solutions Agent](#the-cloud-and-server-solutions-agent)
- [Summary](#summary)


## Use Case Description

This use case leverages AI agents to simplify the process of gathering customer requirements for cloud, server, or hybrid cloud configurations, adapting to the diverse needs of customers. The solution guides customers through targeted questions, enabling a Solutions Architect to design a tailored solution meeting their specific needs. The conversation concludes with an automated email sent to the Solutions Architect, detailing the customer's requirements and providing a unique confirmation number for the customer to track their case progress, ensuring a seamless and efficient experience for both customers and Solutions Architects.

This chat system is a multi-agent solution where each agent is specialized in handling specific parts of the process. Each agent is connected with a Large Language Model (LLM) that supports function calling, so that it can leverage one or more tools based on each tool's description. In this scenario we will build a Personalization Agent, a Configuration Agent, and a Support agent, all connected to a "routing agent" that will take requests from the end user and then select the appropriate agent for excecution before returning the answer. 

The flow of interacion we are simulating is one where a cusotmer starts the conversation to know more about IBM Cloud and Server solution, here the Personalization agent starts asking a few questions about the user such as name and job title to build their profile as well as some contact information to be able to connect with them for the possible next steps. Next, the Configuration agent starts asking questions about the cusotmer's painpoints, challenges and requirements, while adopting the question line based on the responses. Once enough information is gathered, this agent will summarize the requirements and confirm it with the user. Then the Support agent shares this summary with the Solution Architect and sets up next steps. 
<!-- There is also another agent called the Comparison agent which will take over, if the customer has questions about the IBM products advantges and/or how they compare with other solutions.--> Even though we will take you through a complete and working example, you should also consider making changes that fit your desired use case, and only take this description as a reference point that guides you along your own implementation.

### Architecture

<img width="900" alt="image" src="assets/solution_arch.png">

### Pre-requisites

- Check with your instructor to make sure **all systems** are up and running before you continue.
- If you're an instructor running this lab, check the [**Instructor's guides**](https://github.ibm.com/skol/agentic-ai-client-bootcamp-instructors/blob/main/environment-setup/readme.md) to set up all environments and systems.
<!-- - Please go the through the [environment-setup](/environment-setup) guide for steps on API key creation, project setup, and related configurations. -->

## watsonx Orchestrate

As shown in the Solution Architecture, for this lab we will build and deploy four agents on watsonx Orchestrate. To get to the watsonx Orchestrate console, go the [Resources list on the IBM Cloud homepage](https://cloud.ibm.com/resources).

<img width="900" alt="image" src="assets/ibmcloud-resources-wxo.png">

Expand the `AI / Machine Learning` section and select the resource that has `watsonx Orchestrate` in the Product column, as shown above. Next, click on the `Launch watsonx Orchestrate` button.

<img width="900" alt="image" src="assets/ibmcloud-wxo.png">

This opens the watsonx Orchestrate console.

<img width="900" alt="image" src="assets/wxo-ui.png">

Note: *When opening the console for the very first time, you may be greeted by a pop-up window offering that you create your first agent. Click on `Skip for now`.*

<img width="300" alt="image" src="assets/wxo-greeter.png">

In the console, it shows that no agents have been deployed yet. Thus, if you interact with watsonx Orchestrate at this point, not much will happen, since the system has no agents available to route any request to.

However, you can already interact with the Large Language Model (LLM) that works behind the scenes, and ask general questions, like "How are you today?" or "What is the capital of France?".

<img width="900" alt="image" src="assets/wxo-general-llm-test.png">

Go ahead and chat with watsonx Orchestrate to explore what type of answers it gives to your questions.

### AI Agent Configuration

We are now ready to build the first agent. In the watsonx Orchestrate console, click on either `Create or Deploy` or `Create new agent` (either will take you to the same place).

<img width="900" alt="image" src="assets/wxo-create-agent-1.png">

### The Personalization Agent  

In the following screen, you can select if you want to create the new agent from scratch or from a template, and give it a name and a description. To create the solution, you will need to create a number of agents and we will go through them one by one, starting with the `Personalization Agent`. Let's start by giving it a name and a description:

- Name: Personalization Agent
- Description:
```
The Personalization Agent specializes in greeting the customer in the start of the conversation and collects four specific customer details to ensure a customer can be contacted.  
```

Note that in the world of AI Agents, these descriptions are not merely used as documentation, they are also used in making decisions about selecting the right agent for the job, so what you enter into this field is important.

After you have entered the required information, click on the Create button.

<img width="700" alt="image" src="assets/wxo-create-personalizationagent-1.png">

In the next step, we can enter more information about the new agent we are building. Agents can rely on `Knowledge`, on a `Toolset` that consists of one or more `Tools` and one or more `Agents` to satisfy a request that is sent to them, and we can define all of those elements here:

- In the top middle section, you can click on the **AI Model** option to choose which LLM you want your agent to use. For this aget you can lease the `llama-3-290b-vision-instruct` model selected.

- **Profile** contains the agent description we defined earlier along with model agent settings such as `Agent Style`. We are going to select the `ReAct` style for this agent.

<img width="900" alt="image" src="assets/wxo-create-personalizationagent-2.png">

- **Knowledge** represents information that is stored in the form of "embeddings" in a so-called Vector Store. Whenever the agent answers a request, it can choose to run a search against the connected Knowledge repository (i.e. the Vector Store) to search for information that can assist in answering the request. You can either upload documents directly here, or connect the agent to an already existing repository. Note that once again, the "Description" field is key, because it will help the agent decide whether to run a search against the knowledge.

- **Toolset** contains other components that the agent can delegate certain tasks to.
    - `Tools` are functions an agent can call. It can be either an API call or an invocation of custom code. This allows to extend the agent's capabilitiy beyond what the LLM has been trained with.
    - `Agents` are other agents, either within watsonx Orchestrate or running externally, e.g., in watsonx.ai that this agent can delegate the request, or part of a request, to.

- **Behavior** is the section where you can define how and where your agent should react to requests and respond to users.

On the agent definition page, scroll all the way down to the Behavior section and copy the following text into the Instructions text field:

```
- You are a friendly and professional AI assistant which collects exactly four contact details from the user in a polite, natural, and engaging tone.

- You must always respond immediately when the user sends a greeting such as “Hi,” “Hello,” “Hey,” or “Greetings.” You should initiate the conversation by welcoming the user and prompting them to share their basic contact details. 
Example: "Hi, welcome to the IBM Cloud & Servers Solutions chat, could you please share your name and job title?"

- You must strictly adhere to gathering only the following fields: Name, Email, Job Title, and Company Name. You must not ask any other questions, attempt to infer additional details, or deviate from this structure.

- The conversation begins with a professional introduction and you request the user’s name and email in a polite manner. If the user provides only one of these details, you should ask once for the missing information but do not persist if the user does not respond.

- After collecting name and email, the agent asks for the user’s job title and company name in a single prompt. Clarification questions can be asked if the given information is deemed too broad. If the user is unsure, you may provide examples but must not attempt to press for an answer if the user refuses to answer.

- Your responses should reflect a helpful, friendly tone — feel free to use natural expressions like "Got it", or "Thanks so much" to keep things warm and engaging, but still professional.

- You must follow a strict structure, but your responses should feel warm, natural, and conversational not robotic or scripted. You should sound like a helpful human assistant.

- Once all available details are gathered, inform the user that they will be transferred to the Configuration Agent, which will assist with IT needs assessment and solution recommendations, and ask them \n\n "How can we help you today?"

- You must never request or accept any details beyond the specified four fields, must not persist in follow-ups beyond one attempt per missing field, and must not engage in conversation beyond the structured flow. The interaction is to be strictly controlled, ensuring efficiency while maintaining a professional and user-friendly tone.

- Do not share your thought process or reasoning.
```

Finally, make sure you uncheck the `Show agent` checkbox, as shown in the picture below. This switch controls whether the agent is available in the main chat window. We only want to expose the top level agent (which we haven't created yet) there.

<img width="900" alt="image" src="assets/wxo-create-personalizationagent-3.png">

Let's now test the new agent. In the Preview window, enter a question for the agent, for example
```
Hi, my name is Roshi Vojdan
```
When doing this in your own instance, you may see answers that differ from the ones shown in the screenshot above. This is due to the undeterministic nature of the AI models involved. Feel free to experiment with different types of questions to see how the agent reacts. The same equally applies to all the agents described further down.

Note that, in real production deployment, this agent can be connected to a database of profile information, to save the data that it is gathering, also if a returning customer logs in, it can automatically retrieve this information from past interations. At the end of questioning, once the personalization agent asks about what brings the customer in, it will pass it to another agent which we will implement next.

<img width="900" alt="image" src="assets/wxo-create-personalizationagent-4.png">

You can now go ahead and deploy the agent, using the `Deploy` button at the top right of the page. Then, go back to the Agents list on the Manage agents page, by clicking on the `Manage agents` link at the top left of the page. 

<img width="900" alt="image" src="assets/wxo-create-personalizationagent-5.png">

The Personalization Agent now shows a small green icon saying "Live". This indicates successful deployment of the agent.

### The Configuration Agent

This Agent asks questions about various aspects of user's business and infrastucture requirements, and summarized them to share with the solution architect. 
In the Manage agents view, click on the `Create agent` button.

<img width="800" alt="image" src="assets/wxo-create-agent-2.png">

Note: if you are not already in the Manage agents view, you can use the hamburger menu from the top left to get there: 

<img width="800" alt="image" src="assets/wxo-go-to-agentbuilder.png">

Now leave the Create from scratch option selected, enter "Configuration Agent" as the name and enter the following into the Description field:

- Name: Support Agent
- Description:
```
This agent specializes in asking questions about the customer's pain points, challenges and requirements, while adopting the question line based on the responses. Once enough information is gathered, this agent will summarize the requirements and confirm it with the user.
```
<img width="700" alt="image" src="assets/wxo-configurationagent-1.png">

Then click on `Create`.

In the following view, select the `llama-3-405b-instruct` model and the `ReAct` agent style for this agent:

<img width="700" alt="image" src="assets/wxo-configurationagent-1-2.png">

Then, scroll all the way down to the `Behavior` section, and enter the following into the `Instructions` field:

```
You are an IBM Configuration Agent specializing in IBM Cloud, IBM Z, as well as Hybrid Cloud solutions and related offerings. Your task is to engage customers, gather detailed requirements, and ask follow-up questions based on their initial queries and subsequent responses. At the end, summarize the user's requirements and ask if they want to be transferred to the Support Agent and then transfer them to the Support Agent, which will assist with setting up next steps.

* **Ask one question at a time**; do not combine multiple questions.
*  **Only ask questions based on the sources provided at the end**; do not create or infer questions.
*  **Ensure all information displayed comes exclusively from official IBM sources.**
*  **Avoid summarizing too early** and should focus on gathering as much information as possible.
*  You must ensure that you have collected **detailed and comprehensive information about the customer's requirements** before summarizing.
*  **Summarize the user's requirements only after collecting sufficient information to enable another IBM team member to follow up and provide further assistance.**

*   You must provide **clarifications, hints, and examples** when customers need help understanding a question. Your responses must be based **only on official IBM sources**—Do not use or refer to non-IBM sources under any circumstances.
*   Maintain **proper formatting** with **new lines and spacing** between questions, hints, and examples for readability.
*   You are **not allowed to**:
    *   Include technical or procedural language such as JSON, function calls, or API references in your responses.
    *   Suggesting or recommending any particular product or solution. You task is only to collect requirement from the user and summarize the user requirement without loosing any important information.
    *   Disclosing any sources, web scraping, API calls, or internal processes.

* Your responses should appear **natural and conversational**.

Conversational Depth Enhancer (for all turns):
- Each of your follow-up responses should:
    * Briefly acknowledge or paraphrase the user’s input in 1 lines to show understanding and keep the flow natural.
    * Transition into your follow-up question in a way that feels conversational and purposeful, not abrupt.
    * Avoid overly formal or technical phrasing unless you're speaking with a technical persona.
    * Maintain a tone that is friendly, focused, and human—not robotic or overly verbose.
    * Ask only one question at a time—**never combine multiple questions in a single turn.**
    
There are two personas that you may encounter in questioning:
1. Sales Director
2. Director of Compliance and IT
The persona of the customer will be given to you from previous conversations.

Never say 'Based on the search results.
Maintain a friendly, professional tone. Do not share your thought process or reasoning.
If the user Does not mention competitor companies, you should also not mention those.

The first user input will dictate what questions you ask. Make sure to switch the way you ask your questions based on the type of user (technical or non technical). 

---
## **Examples of great responses:** ##

Below is an example of how you should handle the conversation with the Sales Director (non-technical):
Example 1:

Assistant: "Now we are going to gather some workload requirements. How has your business growth impacted your ability to handle online orders?"

User: "Only during the holiday seasons is it impacted"

Assistant: "Have you experienced website slowdowns or checkout issues during high-traffic periods?"

User: "Yes we have."

Assistant: "Have you had issues with customers abandoning their carts due to slow load times or errors?"

User: "Yes we have but that really increases during the holidays."

Assistant: "Are you looking for a solution that helps process orders faster and more efficiently?"

User: "Yes that would be great!"

Assistant: "How important is it for your website to be available 24/7 without interruptions?"

User: "Very important and more so during the holidays."

Assistant: "Do you expect your traffic and order volume to continue growing at the same rate?"

User: "We expect it to grow at the same rate, yes."

Assistant: "Are you concerned about cybersecurity threads, such as data breaches and fraud?"

User: "Not at the present but when we scale, definitely."

Assistant: "Are there any specific areas where you want to improve, such as website speed, order processing, or inventory updates?"

User: "All of the above."

Assistant: "What is your typical user base count look like? In other words, per month, how many people visit your site?"

User: "We have around 2500 per month and that goes to 5000 during the holidays."


Assistant: "Let me summarize your needs:
- Your business growth has only impacted your handling of orders during the holiday season.
- It is very important to you to have your website up 24/7 without interruptions.
- You do expect your traffic and order volume to continue growing at the same rate.
- You aren't concerned about any cybersecurity threats at the present but possibly in the future when scaling
- You wish improved website speed, order processing, and inventory updates.
- You have experienced abandoned carts and it's even worse during the holiday season.
- You are interested in learning about ways to process orders faster and more efficiently.
- You typically have 2500 users per month but it spikes to 5000 during the holidays.
- Your customers have experienced website slow downs and cart errors during high traffic periods.
Does this look correct?"

User: "Yes, that’s correct."

[Only provide the next statement once the user has confirmed the summary is correct]
Assistant: "Perfect. Given these requirements, here is how IBM can address each need better…"
[Now provide *only* an explanation of how IBM's solutions solve these issues—no product names or specs unless your policy allows them. Then or only if user specifically asks, you can mention specific IBM servers.]
( do not ask any further question)

End of example 1 conversation.
---
Below is an example of how you should handle the conversation with the Director of Compliance and IT (technical):
Example 2:

Assistant: "Now we are going to get some workload requirements. What specific regulatory standards (HIPAA, HITECH, etc.) must your infrastructure comply with?"

User: "HIPAA"

Assistant: "what level of encryption would you like to use for data at rest?"

User: "I think probably AES-128"

Assistant: "What are the primary workloads (EHR systems, patient portals, medical imaging, etc.)?"

User: "Primarily user data and medical imaging."

Assistant: "Does your system need to connect to any external applications or data sources?"

User: "Yes we need the ability to have fast and secure connections to external application."

Assistant: "Are you open to using cloud-based solutions for analytics or backup storage?"

User: "Yes"

Assistant: "What’s your approach to data residency—does patient data need to remain on-prem?"

User: "The patient data needs to remain on-prem certainly. We have other data types that can be stored on cloud"

Assistant: "How many concurrent user does your system support today, and do you have any expected growth in the coming months?"

User: "We have 200 users per month and expect minimal growth in the coming months."

Assistant: "What are your uptime and latency requirements for real-time data access?"

User: "We need 99 percent availability and low latency"

Assistant:
"Let me summarize your needs:
- You must maintain your HIPAA compliance
- You will probably use AES-128 encryption
- You mostly store user data and medical imaging
- Your system requires fast and secure connections to external application
- You are open to exploring cloud based solutions for analytics and backup storage
- The patient data needs to remain On-Prem
- You have 200 user per month and expect minimal growth in the coming months
- You need a solution with 99 percent availability and low latency
Does this look correct?"

User: \\"Yes, that’s correct.\\"

[Only provide the next statement once the user has confirmed the summary is correct]
Assistant:
"Perfect. Given these requirements, here is how IBM can address each need better…"
[Now provide *only* an explanation of how IBM's solutions solve these issues—no product names or specs unless your policy allows them. Then or only if user specifically asks, you can mention specific IBM servers.]
( do not ask any further question)
End of example 2 conversation.
```
Note that in the behavior instructions, we have added details on how to guide the conversation and provided two samples of good questioning lines. In real production environment, we can connect the agent to a database of instructions, product catalogs, and more, to be able to cover a wider range of topic and provide references when needed.

Next, uncheck the Show agent checkbox, just like you did for the Dock Status agent. Before deploying this new agent, we can test its functionality by entering requests in the Preview window. For example, you can ask:

```
With a 200% sales increase and rising holiday traffic, we need high-availability servers to handle spikes, prevent downtime, and ensure a seamless shopping experience.
```
<img width="600" alt="image" src="assets/wxo-configurationagent-2.png">

You can continue the conversation and see how the agent tries to gather necessary information, and summarizes the requirements at the end for the Support Agent to pass it to the solution architect.

Each step of the way, it will try to confirm its understanding of your responses, ask questions while providing clarifications or examples where needed.

<img width="600" alt="image" src="assets/wxo-configurationagent-3.png">

<img width="600" alt="image" src="assets/wxo-configurationagent-4.png">

Once you are satisfied with the result, click on the `Deploy` button to deploy this agent, and then click on the `Manage agents` link to return to the agents overview page.

You should now see two agents listed, and both should have the "Live" indicator.

### The Support Agent  

This agent closes the conversation by informing the customer that an email has been sent to the solution architect, providing a ticket number for them to be able to follow up. 

In a real production deployment, the Support Agener would email the summary of the conversation and the requirements gathered by the Configuration Agent to the solution architect and create a ticket in the system, however, in this hands-on exercise, we will simulate that backend by assuming an email is sent and simply hardcoding the ticket number needed for the agent. 

In the Manage agents view, click on the `Create agent` button.

<img width="800" alt="image" src="assets/wxo-create-agent-2.png">

Now leave the Create from scratch option selected, enter "Support Agent" as the name and enter the following into the Description field:

- Name: Support Agent
- Description:
```
The Support Agent is designed to confirm when an email has been successfully sent to a IBM Solution Architect and setting up the next steps. It ensures seamless communication by notifying the user with a confirmation message, including the case number and expected response time. This agent plays a crucial role in closing the loop with the customer by providing clear, timely updates without adding any product recommendations.
```

<img width="600" alt="image" src="assets/wxo-create-supportagent-1.png">

Then click on `Create`.

In the following view, leave the `llama-3-2-90b-vision-instruct` model selected and the `Default` agent style for this agent:

<img width="900" alt="image" src="assets/wxo-create-supportagent-2.png">

Then, scroll all the way down to the `Behavior` section, and enter the following into the `Instructions` field:

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
5. Do not share your thought process or reasoning.
```

Uncheck the Show agent checkbox, just like you did for the Personalization and Configuration Agents.

Before deploying this new agent, we can test its functionality by entering requests in the Preview window. Since this agent is supposed to take over when the other agents have done the questioning, summarized and confirmed the requirments, we can simulate that with something like this:

```
The summary is accurate
```

<img width="800" alt="image" src="assets/wxo-supportagent-testing.png">

Once you are satisfied with the result, click on the `Deploy` button to deploy this agent, and then click on the Manage agents link to return to the agents overview page.

You should now see three agents listed, and all three should have the "Live" indicator.

### The Cloud and Server Solutions Agent

We are finally ready to create the agent that acts as the orchestrator for all other agents and is the agent the end user interacts with.

In the Manage agents view, click on the `Create agent` button one more time.

<img width="800" alt="image" src="assets/wxo-create-agent-2.png">

Like the other agents you created already, this one will be created from scratch. Enter the followings into the Description field:

- Name: Cloud & Server Solutions Agent
- Description:
```
Cloud & Server Solutions Agent is in charge of routing user requests to the proper agent working under it based on the conversation flow and the responses.
```

<img width="600" alt="image" src="assets/wxo-manageragent-1.png">

Then click on `Create`.

In the following view, leave the `llama-3-405b-instruct` model selected and the `ReAct` agent style for this agent:

<img width="900" alt="image" src="assets/wxo-manageragent-2.png">

We had mentioned above that an agent can collaborate with other agents to fulfill a certain task. You enter those collaborator agents in the `Agents` section under `Toolset` in the agent definition window.

<img width="900" alt="image" src="assets/wxo-manageragent-3.png">

Click on the `Add agent` button. Since we want to add the agents you created above as collaborators to this agent, select the `Add from local instance` option.

<img width="600" alt="image" src="assets/wxo-manageragent-4.png">

Here you see all three agents listed that you have created. We want all of them to be used by the Cloud & Server Solutions Agent, so check everyone of them and click on `Add to agent`. Note that it is possible that you will see more than the three agents covered in this lab (you may have created agents from a different lab, or created some of your own), so make sure you are selecting the right set of three.

<img width="900" alt="image" src="assets/wxo-manageragent-5.png">

You should now see all three agents listed in the Toolset section of the Cloud & Server Solutions Agent.

<img width="900" alt="image" src="assets/wxo-manageragent-6.png">

Finally, we give this agent instructions about how to use the collaborator agents we defined earlier. Enter the folllowing text in the `Instructions` field under Behavior.
```
Route the customer through the following flow, while ensuring a seamless and efficient transition between agents while maintaining context.

- First, direct them to the Personalization Agent to greet them and gather basic customer information.
- Then, transfer them to the Configuration Agent to collect relevant technical details.
- Next, after the Configuration Agent summarizes the customer needs, escalate the conversation to the Support Agent, who will draft a final support email.

Do NOT share your thought process or reasoning or the tools you are using.
```

Before we test this agent, scroll all the to the bottom and make sure the `Show agent` checkbox is actually checked! This is the agent we want to use in the main chat window and make it available to end users.

<img width="900" alt="image" src="assets/wxo-manageragent-7.png">

Let's test it. You can now test the whole flow with all agents we tested before, starting by saying hi and introducing yourself, then answering the Configurtion Agent questions and then finally getting the next steps information from the Support Agent. You may use the same or similar prompts as what you used earlier to test them individually

<img width="600" alt="image" src="assets/wxo-manageragent-8.png">

Note that the agent was "reasoning", in other words, determining how to answer this request. It decided that routing the request to the Personalization was the best option. You can expand the `Show reasoning` section in the Preview and see which steps the agent took. It should list one step, which you can expand as well.

Once you are satisfied with the answer, deploy this agent using the `Deploy` button as with the other agents before. Since we left the `Show agent` option checked, we can now go back to the home screen to see it there. Simply click on `watsonx Orchestrate` at the very top of the window.


<img width="700" alt="image" src="assets/wxo-manageragent-9.png">

Now you can enter your questions and requests in the main chat window. Note how the Cloud & Server Solutions agent is already preselected under the Agents list on the left (it is the only agent appearing in that list anyway). You can use the same questions you asked when testing the individual agents above.

<img width="900" alt="image" src="assets/wxo-chattests.png">

Congratulations! You have create a complete agentic AI solution, without writing a single line of code! 

<!-- ## watsonx.ai - Agent Lab
As shown in the Solution Architecture, we will build and deploy two of the agents for the solution on watsonx.ai:

<img width="900" alt="image" src="assets/ibmcloud-resources-wxi.png"> -->


## Summary

In this lab, we went through the use case of sloud and server solutions sales configurator at IBM, which uses an agentic solution to do requirements gathering and understanding customer needs which makes this phase much more productive for the solution architect and the initial phase smoother for the customer. We started by creating a number of agent for tasks like greeting, questiong, and setting up next steps. Finally, all of it came together in the orchestrating agent that serves as the main frontend.

After we had all configured to be used by the AI Agent chat, we can interact with the solution through the main chat interface, and the system will execute and delegate to the appropriate agent.

Note that the intention of this exercise is to provide you with a starting point. Some parts of this solution are simulated, and would have to be fully implemented for a real solution. But hopefully it triggered some ideas for you about how to leverage AI agents in your business environment.