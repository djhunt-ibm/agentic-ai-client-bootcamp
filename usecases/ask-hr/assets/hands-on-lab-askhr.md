
# AskHR - Agent setup hands on lab


1.	Login into your Watsonx account. This is Homepage of Watsonx AI.

<img width="1000" alt="image" src="hands-on-lab-assets/image1.png">


2.  Click on “+” icon to create a project.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/3dc02304-7426-4cea-8fd6-77299198ac43">

3. Enter the name of your project, select storage from available storages and finally click on create. A new project will be created.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/05530e3f-212e-4537-98b9-05ab3b060444">


4.	Click on hamburger icon on top left and select “Access (IAM)”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/5d2e2af8-cdb1-4c1f-b00a-d4d55ccf9497">


5.	In next screen, select “API Keys” from menu.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/e49244b0-be8c-490f-97ff-92f2c21a2faf">

6.	Click on “Create”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/e2ed166c-bde2-4dca-a01d-f2c5471096b4">

7.	Give your API key a name, then click on “Create”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/cffaf1ac-7853-4ec5-a3b2-b4cd16d84689">


8.	Copy the API key that is shown after clicking on “create”. Paste it somewhere, it’ll be used in later steps.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/3d61701d-19c9-45fd-8f75-37ac267cb08f">


9.	Switch back to the homepage. Open Agent Lab.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/258da929-2784-4683-8572-c47cfffda0ae">


10.	In “Instructions” field, paste this prompt “You are a helpful Human Resources Assistant that uses tools to answer questions in detail. Please use website https://www.cipd.org/en/knowledge/factsheets/hr-policies-factsheet/ to give answers to user questions. When greeted, say “Hi, I am HR agent, How can I help you?”

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/ec4c28c4-7a9b-4a4c-bcaf-247bb44263bf">


11.	From “Added tools” section remove already added tools.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/984a6ed6-2dd0-48a6-8c13-d3e96c1489d8">



12.	Then click on “Add a tool”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/9181f1e2-f59b-4ebd-9a1e-8bbf9268880e">


13.	Enable “Webcrawler” tool and close this tools window.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/4d0dd677-bd32-42a9-8d75-a86b2c1d639c">


14.	Click on “Deploy”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/56514107-071a-474e-97fb-a1be4387b940">


15. Enter Deployment name and select “Deployment Space”. If there are no deployment space you need to create one. Then click on “Deploy”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/4ef5d3ee-4626-4c47-bce9-0c5dc0ffa8ee">


16.	Wait for the status to change to “Deployed” from “Initializing”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/2d65d715-b00a-44a4-abab-51c816247c52">


<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/6d129685-9446-4f4e-9df1-a8b8243d4c47">


17.	Click on the name of the deployment you just deployed.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/9147fd79-a431-419b-a822-ad7cfbbf3f37">


18.	Copy and paste deployment id as shown in below image. You will need it in later step.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/924e373b-a339-4712-bdd5-9ea1df405808">


19.	From menu, select “Deployments”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/2b00598c-64d4-451b-90b6-3b60f35128ce">


20.	Select “Spaces” and open the space where you deployed the agent.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/f13d25ff-34a4-4da9-933e-8afc7925a5e5">


21.	Under “manage” section, you’ll find “Space GUID”. Copy and paste it somewhere.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/2ef97b73-71b3-42e1-aa41-5026d4abf9e1">


22.	Open the url https://multi-agent-external.1slrp41syyn5.us-south.codeengine.appdomain.cloud.
Paste “Deployment ID” and “Space ID” that you copied in previous steps. 
Click on “Generate Token”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/e146759f-3c72-44e1-9b7e-6a5f1411dfc5">


23.	A token will be generated. Copy and paste it somewhere.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/bfe888ce-b292-40dc-ba61-0366323b904d">


24.	Go to “Watsonx Orchestrate” homepage. 

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/d52bd45a-a258-48f4-a3e0-08e22fa1471c">


25.	Click on hamburger menu on top left and select “AI agent configuration” from menu.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/71052104-3af3-4eb5-81e0-df24a284449e">

26.	Click on “Agents“

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/af55c0b0-6266-432c-ac61-a7ab507b4f56">


27.	Clcik on “Add Agent +”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/92bdca12-bd71-43ee-acd2-1ca9f12e025b">

28.	Give a name to your agent. Enter the description “This HR agent is an AI-powered assistant designed to handle common HR queries efficiently. It can, provide policy information and answer frequently asked questions.”

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/a6a82239-bcd6-4366-9900-9a3ee7bc5168">


29.	Under “Authentication type”, select “Bearer Token”, enter the generated token you copied, In “Service Instance URL” section , enter code-engine-url/chat/completions.

Click on “Connect”

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/d8ab4e91-6c48-4844-b7ce-101a0be49de2">


30.	Now you can see your agent in this page.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/1feaa9b4-d90f-43c6-83ca-a4756dcf6408">


31.	From menu, select “chat”.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/fa6ad4de-4273-473c-b258-4c312c1724c7">


32.	You can enter you HR queries here and see the responses.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/097b0436-9dd3-4521-a0b5-11f8a4c25d61">

33.	From the menu select "Skill Studio".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/a9419c75-acce-4606-9cbe-cdda5751a96c">

34.	Click on "Create".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/ec2aa069-e656-4c15-8384-c8df331d97f1">

35.	Select "Import API" from the dropdown.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/deb710ef-0ba8-4c28-9855-c400b83fe340">

36.	Select "From a file".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/4afc210b-ab47-4e23-a6f5-1673b2fce70a">


37.	Drag or Select the open specs file and click on "next".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/e378d080-2048-4886-b0e4-a463b26931ba">


38.	Select all checkboxes and click on "Add".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/d4bfb3db-e321-4443-aa9e-cbd54279e413">


39.	Once the skills are imported, click in three dots against imported "Update address" skill.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/fc24b459-2bdc-4018-8b9b-1a87d15d3fbd">


40.	Select "Enhance this skill".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/1db79135-58c7-43d2-aedf-bfc8d431de2d">


41.	Click on "Publish".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/93be512b-2659-498a-8b81-dd3f5db6ae34">



42.	Repeat last 3 steps for other imported skills as well.

43.	Once the skills are published, from menu go to "Skill sets".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/b9b8b7e7-2861-4f9e-be06-4709869ad210">


44.	From the dropdown, select "Orchestrate Agent Skills".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/1925835f-def2-4019-b698-443aac79b7cc">


45.	Click on "Connections". Your imported skills should be grouped in one app automatically. By clicking on arrow, search for that app. Click on three dots against that app and then click on "Connect app".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/035bb58c-1310-4c13-ba7d-8256758a66de">



46.	Select "Team credentials" and click on "Connect app".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/7223b561-0c4e-4c75-b8d1-5a1554fef72d">


47.	Enter your credentials and click on "Connect app".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/cbcf717b-0d6e-468e-92d3-bd18566d64b7">



48.	Once thats done, click on skills and then click on "Manage skills".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/ee0a4edc-ff6c-4e77-a374-20b9311b938b">


49.	Click on app in which your skills are grouped.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/2d45bee9-fbaa-4e3b-86f4-03bb54a24db1">



50.	Check if "Get Time Off Balance", "Get User Profile", "Request Time Off", "Update address" and "Update Title" skills are added. If not already added, click on "Add skill + " for all skills you want to add. 
Then click on "Connect App" on top right, if not already connected.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/5ca3ed07-adb5-4e57-bf50-913e83cdae19">



51.	From menu, click on "AI agent configuration".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/789fc782-b525-4e5d-b249-ebd77301894e">



52.	Select "Apps and skills" and click on the app your skills are grouped into.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/de01fadf-4fc1-44ad-8c32-707d260650ee">


53.	Click on "Add to chat +" for Get Time off Balance.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/90e12af0-eac2-4db3-b915-d7187be770e0">


54.	Enter the description of this skill, "To get time off balance data" Then click on "Add skill".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/853ffcc6-ea15-4e8e-9de1-88822b747c30">

55.	Similarly add all the imported skills with following descriptions as follows. Get User Profile : to get complete profile data of user. Request Time Off : to request time off, apply for leaves Update Address : To update user address Update Title : To update user Title

56.	Now click on your profile icon in top right and select "settings"

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/80fc9071-476b-44a8-97a7-2f562c3d797d">

57.	Click on "chat", then "Switch to legacy chat", then click on "Change to legacy chat" as shown in below image.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/ef1a853b-d914-40b3-a1da-546d53661fba">


58.	From menu, select "Skill sets"

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/714edcb7-a215-4b55-8eef-cb72a2cc4e19">


59.	Select "Team Skills" in dropdown, then click on "connections".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/d9b7c319-8692-485e-ae22-f124bbdc18ae">


60.	Search for the app your skills are grouped into and connet it by clicking on 3 dots.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/06c38686-ea10-4ea0-b34e-1d8506d00bb5">


61.	Click on "skills" and then "Manage skills".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/b71b1a59-41c2-4064-81000-0559bd72c027">


62.	Search for the app, where skills are imported, click on it.

  Then click on "add skills +" for all the skills you imported and then connect app using "Connect App" button in top right.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/7271f2eb-7333-4617-bd27-4de07c628046">


63.	Then click on profile icon, then settings , then click on chat and switch to AI chat again.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/75d6799c-3337-4b93-a92e-7fe9270b4c3e">


65.	From menu click on "chat".

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/ff50910d-eb13-466c-9c43-94bc1710e7f6">


66.	Use your imported skills in chat.

<img width="1000" alt="image" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/449286/d116c979-54aa-4ff9-a79f-5d4debe7ccfd">



End of Document
