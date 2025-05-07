
# 🧑‍💼 AskHR: Automate HR tasks with Agentic AI


### Pre-requisites

- Check with your instructor to make sure **all systems** are up and running before you continue.
- Validate that you have access to the right techzone environment for this lab.
- Validate that you have access to a credentials file that you instructor will share with you before starting the labs.
- If you're an instructor running this lab, check the **Instructor's guides** to set up all environments and systems.



In this lab, you'll create three different agents. One is RAG agent, which extracts information from a document to resolve user queries, second agent is HR profile management agent, which lets user check profile, third agent is Supervisory agent, which delagate tasks to these two agents, RAG agent and HR profile management agent based on the query.


### Step by step instructions to build agents: 
1. When you launch "watsonx orchestrate", you'll be directed to this page. Click on hamburger menu of top left.

<img width="1000" alt="image" src="hands-on-lab-assets/step1.png">

2. Click on down arrow against "Build".
   Then click on "Agent Builder".
<img width="1000" alt="image" src="hands-on-lab-assets/step2.png">

3. Click on "Create agent +".
<img width="1000" alt="image" src="hands-on-lab-assets/step3.png">

#### Deploying RAG agent:
4. Select "Create from scratch", Give your agent name "RAG_agent", fill the description "This agent handles queries around employee benefits" as shown in image. Then click on "Create".
<img width="1000" alt="image" src="hands-on-lab-assets/step4.png">

5. Scroll the next screen to Knowledge section. Click on "Upload files +".
<img width="1000" alt="image" src="hands-on-lab-assets/step5.png">

6. Drag or upload the "Employee Benefits.pdf" ([Employee Benefits.pdf](/usecases/ask-hr/assets/Employee-Benefits.pdf)) here and click on "Upload".
<img width="1000" alt="image" src="hands-on-lab-assets/step6.png">  

7. Scroll more to "Behavior" section, write the instructions as shown in below image, test your agent in chat window in right, finally click on "Deploy"
<img width="1000" alt="image" src="hands-on-lab-assets/step7.png">  

8. Go back to "Manage agents".
<img width="1000" alt="image" src="hands-on-lab-assets/step8.png">

#### Deploying HR profile management agent:
9. Click on "Create agent +".
<img width="1000" alt="image" src="hands-on-lab-assets/step9.png">
10. Select "Create from scratch", give this agent a name "HR_profile_management_agent" and put the Description as shown in image.
<img width="1000" alt="image" src="hands-on-lab-assets/step11.png">

11. Click on "Add tool +".
<img width="1000" alt="image" src="hands-on-lab-assets/step12.png">

12. Select "Import".
<img width="1000" alt="image" src="hands-on-lab-assets/step13.png">

13. Drag or upload openapi-agentic.json file here and click on Next.
<img width="1000" alt="image" src="hands-on-lab-assets/step14.png">    

14. Select all the operations and click on Done.
<img width="1000" alt="image" src="hands-on-lab-assets/step15.png">

15. Scroll down to "Behavior" section, Put below in Instructions field: 

"This agent helps users in managing and checking their profile data, like update
address, update title, check profile data, show time off balance, request time off. When user asks to show profile data or check time off balance, system should first ask for the name to user then invoke the tool."

 Test your agent in chat window in right and click on deploy.
<img width="1000" alt="image" src="hands-on-lab-assets/step16.png">

16. Again go back to "Manage agents", Click on "Create agent +".
<img width="1000" alt="image" src="hands-on-lab-assets/step9.png">

#### Deploying Supervisory agent:
17. Select "Create from scratch", give this agent a name "Supervisory_agent" and put the Description :
"This agent should deligate the tasks to the respective collaboration agents. You have access to two agent, HR_profile_management_agent and RAG_agent. If query is about checking and updating profile information, checking time off balance, deligate the task to HR_profile_management_agent. For any other query deligate the task to RAG_agent."

Click on "Create".
<img width="1000" alt="image" src="hands-on-lab-assets/step17.png">

18. Scroll down to "Toolset" section and click on "Add agent +".
<img width="1000" alt="image" src="hands-on-lab-assets/step18.png">

19. Select "Add from local instance".
<img width="1000" alt="image" src="hands-on-lab-assets/step19.png">

20. Select "HR_profile_management_agent" and "RAG_agent", click on "Add to agent".
<img width="1000" alt="image" src="hands-on-lab-assets/step20.png">

21. Add the following Instructions in Behavior section:
"This agent should deligate the tasks to the respective collaboration agents. You have access to two agent, HR_profile_management_agent and RAG_agent. If query is about checking and updating profile information, checking time off balance, deligate the task to HR_profile_management_agent. For any other query deligate the task to RAG_agent."

Test your agent in chat window in right, finally click on deploy.
<img width="1000" alt="image" src="hands-on-lab-assets/step21.png">


22. Go back to "Manage agents". You should see all your agents listed here. Click on hamburger menu.
<img width="1000" alt="image" src="hands-on-lab-assets/step22.png">

23. Click on "Chat".
<img width="1000" alt="image" src="hands-on-lab-assets/step23.png">

24. Select "Supervisory_agent" in Agents.
<img width="1000" alt="image" src="hands-on-lab-assets/step24.png">

 25. Test your agent now.
<img width="1000" alt="image" src="hands-on-lab-assets/step25.png">







.





