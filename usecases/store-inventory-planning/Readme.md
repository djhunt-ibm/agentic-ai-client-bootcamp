
# Store Inventory Planning Assistant – Client Lab

[![IBM Cloud](https://img.shields.io/badge/Platform-IBM%20Cloud-blue)](https://cloud.ibm.com/)
[![Built with watsonx](https://img.shields.io/badge/Built%20with-IBM%20watsonx-ff69b4)](https://www.ibm.com/watsonx)
[![Retail Use Case](https://img.shields.io/badge/Use%20Case-Retail%20Planning-brightgreen)]()

Welcome! In this lab, you’ll explore how AI agents built on **IBM watsonx** can help store managers solve real-world inventory planning problems. You’ll interact with a pre-built multi-agent system — **no coding required**.



## Table of Contents

1. [Use Case Overview](#use-case-overview)
2. [Meet the Agents](#meet-the-agents)
3. [Try It Yourself](#try-it-yourself)
4. [Wrap Up](#wrap-up)


## Use Case Overview

Imagine you're a store manager preparing for the weekend. You need to:

* Check what products are running low in stock
* Understand if local events might drive demand
* Find the best supplier
* Place restock orders instantly


You’ll interact with four smart agents, coordinated by a **Manager Agent**, that handle inventory, demand insights, supplier selection, and order placement.



## Meet the Agents

| Agent               | What It Does                                     |
| --------------------| ------------------------------------------------ |
| **Inventory Agent** | Finds items that are low in stock                |
| **Insight Agent**   | Suggests what to stock up based on trends/events |
| **Supplier Agent**  | Recommends suppliers for your inventory          |
| **Email Agent**     | Sends supplier orders based on your instructions |



## Try It Yourself

Talk to the system like you would to a teammate. The Manager Agent decides who should respond.

### Inventory Agent

Ask:

* “What items are running low in my inventory?”
* “Am I low on bananas?”

Expected: A table showing product names, stock levels, and reorder thresholds.



### Insight Agent

Ask:

* “Do I need to stock up for this weekend?”
* “Is there anything happening that I should prepare for?”

Expected: Insights using event data (like local football games) and past product turnover.



### Supplier Agent

Ask:

* “Who can supply frozen pizza and beer?”
* “List suppliers for chocolate.”

Expected: A comparison of suppliers by unit cost, delivery time, and rating.



### Email Agent

Say:

* “Order 30 pepperoni pizzas from PizzaHouse.”
* “Place order of 60 beers to Brewery Inc.”

Expected: Confirmation that the email has been sent with order details.



## Wrap Up

In this lab, you’ve explored a complete AI solution powered by **watsonx.ai** and **watsonx Orchestrate** — no technical setup or code required.

### What You Saw:

✅ AI that understands retail inventory language
✅ Coordinated agent system for business workflows
✅ Real automation you can extend across your operations

---

🎯 **Ask your facilitator** if you want to dive deeper or tailor this to your own business use case!
