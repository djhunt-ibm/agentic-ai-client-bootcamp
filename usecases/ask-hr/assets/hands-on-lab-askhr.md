
# AskHR - Agent setup hands on lab


1.	Login into your Watsonx account. This is Homepage of Watsonx AI.

<img width="1000" alt="image" src="hands-on-lab-assets/image30.png">


2.  Click on “+” icon to create a project.
  
<img width="1000" alt="image" src="hands-on-lab-assets/image31.png">

3. Enter the name of your project, select storage from available storages and finally click on create. A new project will be created.

<img width="1000" alt="image" src="hands-on-lab-assets/image32.png">


4.	Click on hamburger icon on top left and select “Access (IAM)”.

<img width="1000" alt="image" src="hands-on-lab-assets/image33.png">


5.	In next screen, select “API Keys” from menu.

<img width="1000" alt="image" src="hands-on-lab-assets/image34.png">

6.	Click on “Create”.

<img width="1000" alt="image" src="hands-on-lab-assets/image35.png">

7.	Give your API key a name, then click on “Create”.

<img width="1000" alt="image" src="hands-on-lab-assets/image36.png">


8.	Copy the API key that is shown after clicking on “create”. Paste it somewhere, it’ll be used in later steps.

<img width="1000" alt="image" src="hands-on-lab-assets/image37.png">


9.	Switch back to the homepage. Open Agent Lab.

<img width="1000" alt="image" src="hands-on-lab-assets/image38.png">


10.	In “Instructions” field, paste this prompt “You are a helpful Human Resources Assistant that uses tools to answer questions in detail. Please use website https://www.cipd.org/en/knowledge/factsheets/hr-policies-factsheet/ to give answers to user questions. When greeted, say “Hi, I am HR agent, How can I help you?”

<img width="1000" alt="image" src="hands-on-lab-assets/image39.png">


11.	From “Added tools” section remove already added tools.

<img width="1000" alt="image" src="hands-on-lab-assets/image40.png">



12.	Then click on “Add a tool”.

<img width="1000" alt="image" src="hands-on-lab-assets/image41.png">


13.	Enable “Webcrawler” tool and close this tools window.

<img width="1000" alt="image" src="hands-on-lab-assets/image42.png">

14. Close this window.
 
<img width="1000" alt="image" src="hands-on-lab-assets/image43.png">

15.	Click on “Deploy”.

<img width="1000" alt="image" src="hands-on-lab-assets/image44.png">

16. Enter Deployment name and select “Deployment Space”. If there are no deployment space you need to create one. Then click on “Deploy”.

<img width="1000" alt="image" src="hands-on-lab-assets/image45.png">

17.	Wait for the status to change to “Deployed” from “Initializing”.

<img width="1000" alt="image" src="hands-on-lab-assets/image46.png">

<img width="1000" alt="image" src="hands-on-lab-assets/image47.png">

18.	Click on the name of the deployment you just deployed.

<img width="1000" alt="image" src="hands-on-lab-assets/image48.png">


19.	Copy and paste deployment id as shown in below image. You will need it in later step.

<img width="1000" alt="image" src="hands-on-lab-assets/image49.png">


20.	From menu, select “Deployments”.

<img width="1000" alt="image" src="hands-on-lab-assets/image50.png">


21.	Select “Spaces” and open the space where you deployed the agent.

<img width="1000" alt="image" src="hands-on-lab-assets/image51.png">


22.	Under “manage” section, you’ll find “Space GUID”. Copy and paste it somewhere.

<img width="1000" alt="image" src="hands-on-lab-assets/image52.png">


23.	Open the url https://multi-agent-external.1slrp41syyn5.us-south.codeengine.appdomain.cloud.
Paste “Deployment ID” and “Space ID” that you copied in previous steps. 
Click on “Generate Token”.

<img width="1000" alt="image" src="hands-on-lab-assets/image53.png">

24.	A token will be generated. Copy and paste it somewhere.

<img width="1000" alt="image" src="hands-on-lab-assets/image54.png">


25.	Go to “Watsonx Orchestrate” homepage. 
<img width="1000" alt="image" src="hands-on-lab-assets/image55.png">


26.	Click on hamburger menu on top left and select “AI agent configuration” from menu.

<img width="1000" alt="image" src="hands-on-lab-assets/image56.png">

27.	Click on “Agents“

<img width="1000" alt="image" src="hands-on-lab-assets/image57.png">


28.	Clcik on “Add Agent +”.

<img width="1000" alt="image" src="hands-on-lab-assets/image58.png">

29.	Give a name to your agent. Enter the description “This HR agent is an AI-powered assistant designed to handle common HR queries efficiently. It can, provide policy information and answer frequently asked questions.”

<img width="1000" alt="image" src="hands-on-lab-assets/image59.png">


30.	Under “Authentication type”, select “Bearer Token”, enter the generated token you copied, In “Service Instance URL” section , enter code-engine-url/chat/completions.

Click on “Connect”

<img width="1000" alt="image" src="hands-on-lab-assets/image60.png">


31.	Now you can see your agent in this page.

<img width="1000" alt="image" src="hands-on-lab-assets/image61.png">

32.	From menu, select “chat”.

<img width="1000" alt="image" src="hands-on-lab-assets/image62.png">

33.	You can enter you HR queries here and see the responses.

<img width="1000" alt="image" src="hands-on-lab-assets/image63.png">

34.	From the menu select "Skill Studio".

<img width="1000" alt="image" src="hands-on-lab-assets/image1.png">

35.	Click on "Create".

<img width="1000" alt="image" src="hands-on-lab-assets/image2.png">

36.	Select "Import API" from the dropdown.

<img width="1000" alt="image" src="hands-on-lab-assets/image3.png">

37.	Select "From a file".

<img width="1000" alt="image" src="hands-on-lab-assets/image4.png">


38.	Drag or Select the open specs file and click on "next".

<img width="1000" alt="image" src="hands-on-lab-assets/image5.png">


39.	Select all checkboxes and click on "Add".

<img width="1000" alt="image" src="hands-on-lab-assets/image6.png">


40.	Once the skills are imported, click in three dots against imported "Update address" skill.

<img width="1000" alt="image" src="hands-on-lab-assets/image7.png">


41.	Select "Enhance this skill".

<img width="1000" alt="image" src="hands-on-lab-assets/image8.png">


42.	Click on "Publish".

<img width="1000" alt="image" src="hands-on-lab-assets/image9.png">



43.	Repeat last 3 steps for other imported skills as well.

44.	Once the skills are published, from menu go to "Skill sets".

<img width="1000" alt="image" src="hands-on-lab-assets/image10.png">


45.	From the dropdown, select "Orchestrate Agent Skills".

<img width="1000" alt="image" src="hands-on-lab-assets/image11.png">


46.	Click on "Connections". Your imported skills should be grouped in one app automatically. By clicking on arrow, search for that app. Click on three dots against that app and then click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image11.1.png">



47.	Select "Team credentials" and click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image11.2.png">


48.	Enter your credentials and click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image12.png">



49.	Once thats done, click on skills and then click on "Manage skills".

<img width="1000" alt="image" src="hands-on-lab-assets/image13.png">


50.	Click on app in which your skills are grouped.

<img width="1000" alt="image" src="hands-on-lab-assets/image14.png">



51.	Check if "Get Time Off Balance", "Get User Profile", "Request Time Off", "Update address" and "Update Title" skills are added. If not already added, click on "Add skill + " for all skills you want to add. 
Then click on "Connect App" on top right, if not already connected.

<img width="1000" alt="image" src="hands-on-lab-assets/image15.png">



52.	From menu, click on "AI agent configuration".

<img width="1000" alt="image" src="hands-on-lab-assets/image16.png">



53.	Select "Apps and skills" and click on the app your skills are grouped into.

<img width="1000" alt="image" src="hands-on-lab-assets/image17.png">


54.	Click on "Add to chat +" for Get Time off Balance.

<img width="1000" alt="image" src="hands-on-lab-assets/image18.png">


55.	Enter the description of this skill, "To get time off balance data" Then click on "Add skill".

<img width="1000" alt="image" src="hands-on-lab-assets/image19.png">

56.	Similarly add all the imported skills with following descriptions as follows. Get User Profile : to get complete profile data of user. Request Time Off : to request time off, apply for leaves Update Address : To update user address Update Title : To update user Title

57.	Now click on your profile icon in top right and select "settings"

<img width="1000" alt="image" src="hands-on-lab-assets/image20.png">

58.	Click on "chat", then "Switch to legacy chat", then click on "Change to legacy chat" as shown in below image.

<img width="1000" alt="image" src="hands-on-lab-assets/image21.png">


59.	From menu, select "Skill sets"

<img width="1000" alt="image" src="hands-on-lab-assets/image22.png">


60.	Select "Team Skills" in dropdown, then click on "connections".

<img width="1000" alt="image" src="hands-on-lab-assets/image22.1.png">


61.	Search for the app your skills are grouped into and connet it by clicking on 3 dots.

<img width="1000" alt="image" src="hands-on-lab-assets/image22.2.png">


62.	Click on "skills" and then "Manage skills".

<img width="1000" alt="image" src="hands-on-lab-assets/image23.png">


63.	Search for the app, where skills are imported, click on it.

  Then click on "add skills +" for all the skills you imported and then connect app using "Connect App" button in top right.

<img width="1000" alt="image" src="hands-on-lab-assets/image24.png">


64.	Then click on profile icon, then settings , then click on chat and switch to AI chat again.

<img width="1000" alt="image" src="hands-on-lab-assets/image25.png">


65.	From menu click on "chat".

<img width="1000" alt="image" src="hands-on-lab-assets/image26.png">


66.	Use your imported skills in chat.

<img width="1000" alt="image" src="hands-on-lab-assets/image27.png">



End of Document
