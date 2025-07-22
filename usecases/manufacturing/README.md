# 🏭 Manufacturing Operation Automation

![image](assets/manufacturing.png)

## 🤔 The Problem

XYZ Motors, a car manufacturer, spends a significant amount of time with handling equipment malfunction which slows situational awareness, widens quarantines, and drags out root-cause hunts, so every alarm costs time and yield.

## 🎯 Objective

XYZ Motors' manufacturing division faced persistent delays in resolving equipment malfunctions across their production lines. These disruptions often led to extended downtime, increased scrap, and slower recovery cycles. Key issues included:

* Manual fault diagnosis delayed resolution and reduced operational efficiency.
* Lack of contextual insights limited root-cause visibility.
* Broader quarantines occurred due to insufficient traceability and real-time data.

To address these challenges, XYZ Motors implemented an AI-powered fault management system driven by cooperating agents that streamline fault detection, analysis, and documentation.


## 📈 Business Value

* **Reduced Downtime** – Faster fault isolation and guided troubleshooting shorten repair cycles.
* **Lower Scrap and Rework** – Genealogy tracking restricts containment to only the impacted batch.
* **Knowledge Retention** – Auto-documentation preserves institutional knowledge.

---

## 🏛 Architecture

To streamline fault diagnosis and resolution across production lines, XYZ Motors has developed a **Multi-Agent AI Fault Management System** that intelligently processes machine-related incidents in real time. This system leverages a collaborative multi-agent framework powered by **Watsonx Orchestrate** and **Watsonx.ai**, allowing operational teams to respond faster, minimize downtime, and retain critical knowledge.

The architecture consists of specialized AI agents, each designed to handle specific tasks, working together to deliver an intelligent, structured, and actionable response to equipment failures.

<img width="900" alt="image" src="assets/ManufacturesUsecase.png">

This system processes user input—such as an error code or incident description—and activates agents that retrieve and analyze machine and error data, fetch real-time logs, and suggest root-cause fixes using LLMs. The collaboration between agents ensures a seamless flow of information and enables accurate and automated fault resolution.

---

### Components and Agents

#### **Master Agent**

This is the central coordinator that receives partial outputs from the specialized agents and assembles them into a unified and structured response. It ensures clarity, removes redundancy, and presents insights in an easy-to-digest format.

**Final output includes:**

* Error Description
* Machine Description
* Recent Log Highlights
* Top-5 Similar Log Incidents
* Suggested Fix from LLM

---

#### **Machine Agent** `[watsonx Orchestrate RAG]`

This agent is responsible for retrieving technical and operational details about a specific machine. It uses a CSV-based machine knowledge base and provides context such as specifications, location, and role of the machine.

---

#### **Error Agent** `[watsonx Orchestrate RAG]`

This agent focuses on decoding error codes provided by users. It queries the errors knowledge base to fetch detailed descriptions, severity levels, and possible causes for each error code.

---

#### **Log Agent**

This agent retrieves log-based insights from two external tools integrated into the system:

* **Tool-1**: Gathers the most recent log events for the specified machine
* **Tool-2**: Searches historical data to retrieve the top-5 similar log events based on pattern similarity

---

#### User Input

The system is activated by a simple query from the user. Input can be:

* An **Error Code**
* A **Machine Name** or **Incident Description**

The agents then autonomously collaborate to extract relevant data and generate a comprehensive response.

---

#### Cumulative Output

Once all agents complete their tasks, the Master Agent compiles a structured summary:

1. **Error Description** – Clarifies the nature and possible cause of the error
2. **Machine Description** – Technical overview of the involved machine
3. **Recent Log Changes** – Latest events from machine logs
4. **Top-5 Similar Logs** – Matching incidents from historical data
5. **Suggested Fix** – AI-recommended resolution using LLM-based reasoning

## 📝 Step-by-step Hands-on Lab
You can find step-by-step instructions here :

[Step-by-step hands-on guide]

## Demo Video
A video demo of the solution is below:

https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/453165/88ff3a77-0b52-4a31-9b62-f277fb071e31



