 # Business Automation - Competitive Insights 

![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/451557/b9fb42fc-4aa1-4010-b850-5c8f20e3e05a)

## The Problem

The sales department of ABC Motors Corp, an automotive large player, when preparing sales proposals, they were spending a lot of time understanding the features of competing products and comparing them with their own products. Sales teams were spending excessive time manually researching competitor products and comparing them with their own. This process was:

- Time-consuming competitive research: sales teams spend excessive time manually gathering competitor insights, delaying decision-making and reducing productivity.

- Inefficient product positioning: Lack of structured competitor comparison leads to weak sales pitches, making it harder to highlight unique selling points effectively.

- Data overload & irrelevant information: traditional search methods yield excessive or low-quality data, making it difficult to extract meaningful competitor insights.

- Delayed response to market changes: Without real-time competitive intelligence, businesses struggle to adapt pricing, features, and strategies based on evolving market trends.

### Lack of automation in sales intelligence 
Manual processes for feature extraction, web search, and competitor analysis lead to inconsistent data and missed sales opportunities.

## Objective
To address these challenges, ABC Motors Corp aims to implement an AI-enabled Competitive Intelligence System that automates market research and competitor analysis. ABC Motor Corp, needs an automated competitive analysis system to help their sales teams quickly identify and position their products against competitors. Traditionally, gathering competitor insights required extensive manual research, making it inefficient and prone to outdated information.
Therefore, the goal of this use case is to create an AI enabled system that support the customer's competitive analysis and market research. This system will:

* Extract products from the company’s product catalog.
* Identify and extract key features of each product.
* Search for competitor products based on key attributes.
* Generate a structured competitive comparison table with price, features, and differentiators.
* Perform SWOT Analysis (Strengths, Weaknesses, Opportunities, and Threats) to provide deeper strategic insights.

By automating these tasks, the company aims to accelerate sales processes, improve data accuracy, and enable sales teams to make informed decisions faster.

## Business Value

* Reduction in manual competitor research time.
* Automated, real-time updates on market competition.
* Improved sales pitch effectiveness

## Architecture

To streamline the competitive analysis process, we have designed a Multi-Agent AI Automation System that autonomously extracts and analyzes product data. This system leverages a collaborative multi-agent approach, ensuring efficiency, accuracy, and real-time insights for sales and strategy teams. The architecture consists of specialized AI agents working together to perform key functions:
  * To extract products from the product catalog
  * Extract features of the product from the product catalog,
  * Searches for competitor products
  * Generates a structured competitive comparison table
  * Strength Weakness Opportunity & Threat (SWOT) Analysis

This system leverages 2 AI agents and an Orchestrate agent that collaborate seamlessly to automate competitive research, enhance sales pitch effectiveness, and reduce manual effort.

<img width="979" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/451557/952b54c4-28a4-4ef6-82b4-ef08991d9297">


The use case leverages wxO skills to get product specific data (name, features) from the product catalogue followed by two specialized agents developed within the watsonx.ai's Agent Lab, all of which are integrated into watsonx Orchestrate. Through the watsonx Orchestrate chat assistant, these agents & skills communicate seamlessly to provide comprehensive insights and facilitate informed decision-making. 
  * **Product Search wxO skills** : These skills are designed to search for a specified product and retrieve its details and features in a structured format from the product catalog. It ensures clarity and organization by presenting key product information systematically, making it easy to understand and use.
  * **Link Search Agent** : This agent is expert in finding URLs or links for similar products that share matching features, ensuring users can explore alternatives efficiently.
  * **Comparison Agent** : This agent is designed to compare competitor products using these links, extract key insights, and return a SWOT analysis of all products. The findings should be presented in a well-structured table format, making it easy to understand and compare the information briefly.

## Detailed Instructions

You can find step-by-step instructions here :

[Step-by-step hands-on guide](https://github.ibm.com/skol/agentic-ai-client-bootcamp/blob/main/usecases/business-automation/hands-on-lab-buisness-automation.md)

It shows how you can implement the use case using watsonx.ai and watsonx Orchestrate. 
