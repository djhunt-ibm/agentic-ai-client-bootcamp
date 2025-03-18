
# AskHR - Agent setup hands on lab

## Table of Contents

- [Use case: AskHR](#use-case-askHR)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Use case description](#use-case-description)
  - [Agent Lab - Creating your first agent](#agent-lab---creating-your-first-agent)
    - [Using a tool](#using-a-tool)
    - [Deploy your agent](#deploy-your-agent)
  - [watsonx Orchestrate](#watsonx-orchestrate)
    - [AI agent configuration](#ai-agent-configuration)
    - [Skill Studio](#skill-studio)

## Introduction

<img width="1000" alt="image" src="arch_diagm.png">

## Use case description

This use-case targets developing and deploying an AskHR agent leveraging IBM watsonx Orchestrate and watsonx.ai, as depicted in the provided architecture diagram. This agent will empower employees to interact with HR systems and access information efficiently through conversational AI. we have 4 skills in watsonx.orchestrate which leverages custom skills to connect to a dummy HR Application storing the employee data. Another agent in watsonx.ai can answer user queries using a grounded data source. Integrating these 5 agents, we will see how most of the routine HR operations can be brought under a single powerful Agent.

### Agent Lab - Creating your first agent

1.	Login into your watsonx account using [this](https://dataplatform.cloud.ibm.com/wx/home?context=wx). This is Homepage of watsonx AI.
   Copy the watsonx.ai URL and paste somewhere.

<img width="1000" alt="image" src="hands-on-lab-assets/image30.1.png">

1.1 For agent creation, you'll be needing a project. Click on "+" icon against "Projects" as shown in below image.
<img width="1000" alt="image" src="hands-on-lab-assets/image31.png">

1.2 Give your a project a name, select storage from available storages, then click on "Create".
<img width="1000" alt="image" src="hands-on-lab-assets/image32.png">

2.	Click on hamburger icon on top left and select “Access (IAM)”.

<img width="1000" alt="image" src="hands-on-lab-assets/image33.png">


3.	In next screen, select “API Keys” from menu.

<img width="1000" alt="image" src="hands-on-lab-assets/image34.png">

4.	Click on “Create”.

<img width="1000" alt="image" src="hands-on-lab-assets/image35.png">

5.	Give your API key a name, then click on “Create”.

<img width="1000" alt="image" src="hands-on-lab-assets/image36.png">


6.	Copy the API key that is shown after clicking on “create”. Paste it somewhere, it’ll be used in later steps.

<img width="1000" alt="image" src="hands-on-lab-assets/image37.png">


7.	Switch back to the homepage. Open Agent Lab.

<img width="1000" alt="image" src="hands-on-lab-assets/image38.png">
7.0 Click on both checkboxes, then click on "Skip tour."
<img width="1000" alt="image" src="hands-on-lab-assets/image38.0.png">
7.1 Click on "Associate service".
<img width="1000" alt="image" src="hands-on-lab-assets/image38.1.png">

7.2 Make sure "Global" and the region of your cloud account is selected in dropdown.
 <img width="1000" alt="image" src="hands-on-lab-assets/image38.3.png">

7.3  Select available watsonx.ai runtime service. (Look for the service with Type "watsonx.ai Runtime")
 <img width="1000" alt="image" src="hands-on-lab-assets/image38.4.png">

7.4 Once that's done, navigate to agent lab again (by clicking on hamburger menu in top left and then clicking on "Home", then clicking on "Agent Lab")

8.	In “Instructions” field, paste this prompt “You are a helpful Human Resources Assistant that uses tools to answer questions in detail. Please use website https://www.cipd.org/en/knowledge/factsheets/hr-policies-factsheet/ to give answers to user questions. When greeted, say “Hi, I am HR agent, How can I help you?”

<img width="1000" alt="image" src="hands-on-lab-assets/image39.png">

### Using a tool
9.	From “Added tools” section remove already added tools.

<img width="1000" alt="image" src="hands-on-lab-assets/image40.png">



10.	Then click on “Add a tool”.

<img width="1000" alt="image" src="hands-on-lab-assets/image41.png">


11.	Enable “Webcrawler” tool and close this tools window.

<img width="1000" alt="image" src="hands-on-lab-assets/image42.png">

12. Close this window.
 
<img width="1000" alt="image" src="hands-on-lab-assets/image43.png">

### Deploy your agent
12.1. For next steps, you need to create a deployment space using [this](deployment_space_creation.md) guide.)


12.2 Save your agent by clicking on Save icon, then select "Save as".
    
<img width="1000" alt="image" src="hands-on-lab-assets/image43.1.png">

12.3 Select "Agent" in Agent type, check the checkbox ""View the project after saving", then click on "save".
<img width="1000" alt="image" src="hands-on-lab-assets/image43.2.png">

12.4 Click on the agent that just got created.
<img width="1000" alt="image" src="hands-on-lab-assets/image43.3.png">

12.5 Click on "Edit".
<img width="1000" alt="image" src="hands-on-lab-assets/image43.4.png">

Your agent is saved, you  can make changes in it later if you want to experiment with it.

13.	Click on “Deploy”. (For next steps ypu'll need a deployment space. If there are no deployment space you need to create one using  [this](deployment_space_creation.md) guide.)

<img width="1000" alt="image" src="hands-on-lab-assets/image44.png">

14. Once you click on deploy, You need to create user api key.  Click on "Create"
<img width="1000" alt="image" src="hands-on-lab-assets/image44.0.1.png">

14.1 You'll be directed to another webpage. Click on "Create a key".
<img width="1000" alt="image" src="hands-on-lab-assets/image44.0.2.png">

14.2 Once key is created, navigate back to deployment page. Click on "reload".
<img width="1000" alt="image" src="hands-on-lab-assets/image44.1.png">

14.2  Enter Deployment name and select “Deployment Space”.
<img width="1000" alt="image" src="hands-on-lab-assets/image45.png">

15.	Wait for the status to change to “Deployed” from “Initializing”.

<img width="1000" alt="image" src="hands-on-lab-assets/image46.png">

<img width="1000" alt="image" src="hands-on-lab-assets/image47.png">

16.	Click on the deployment you just deployed.

<img width="1000" alt="image" src="hands-on-lab-assets/image48.png">


17.	Copy and paste deployment id as shown in below image. You will need it in later step.

<img width="1000" alt="image" src="hands-on-lab-assets/image49.png">


18.	From menu, select “Deployments”.

<img width="1000" alt="image" src="hands-on-lab-assets/image50.png">


19.	Select “Spaces” and open the space where you deployed the agent.

<img width="1000" alt="image" src="hands-on-lab-assets/image51.png">


20.	Under “manage” section, you’ll find “Space GUID”. Copy and paste it somewhere.

<img width="1000" alt="image" src="hands-on-lab-assets/image52.png">


21. For deployment, you need a Code Engine URL, which you can request from your instructor. Once you receive the deployment link, please open it.

You will reach the page shown in the image below. Follow these two steps to generate the Bearer Token:
Paste “Deployment ID” (refer step 17), “Space ID” (refer step 20), "API Key" (refer step 6) and "watsonx URL (refer step 1)". 
Click on “Generate Token”.

<img width="1000" alt="image" src="hands-on-lab-assets/image53.png">

22.	A token will be generated. Copy and paste it somewhere.

<img width="1000" alt="image" src="hands-on-lab-assets/image54.png">

## watsonx Orchestrate
22.1 Navigate to [IBM Cloud](https://cloud.ibm.com).
<img width="1000" alt="image" src="hands-on-lab-assets/image54.1.png">

22.2 From menu, select "Resources list".
<img width="1000" alt="image" src="hands-on-lab-assets/image54.2.png">
22.3 Under AI / MAchine Learning, select Watson Orchestrate and click on it.
<img width="1000" alt="image" src="hands-on-lab-assets/image54.3.png">

22.4 Click on "Launch watsonx Orchestrate". 
<img width="1000" alt="image" src="hands-on-lab-assets/image54.4.png">

23.	This is watsonx Orchestrate homepage. 
<img width="1000" alt="image" src="hands-on-lab-assets/image55.png">

### AI agent configuration

24.	Click on hamburger menu on top left and select “AI agent configuration” from menu. If you don't see  “AI agent configuration” in menu, try [this](#Common-issues-and-troubleshoot-steps)

<img width="1000" alt="image" src="hands-on-lab-assets/image56.png">

25.	Click on “Agents“

<img width="1000" alt="image" src="hands-on-lab-assets/image57.png">


26.	Click on “Add Agent +”.

<img width="1000" alt="image" src="hands-on-lab-assets/image58.png">

27.	Give a name to your agent. Enter the description: 'This HR agent is an AI-powered assistant designed to handle common HR queries efficiently. It can provide policy information and answer frequently asked questions.”

<img width="1000" alt="image" src="hands-on-lab-assets/image59.png">


28.	Under “Authentication type”, select “Bearer Token”, enter the generated token you copied, In “Service Instance URL” section , enter the  Code Engine URL recieved from instructor.

Click on “Connect”

<img width="1000" alt="image" src="hands-on-lab-assets/image60.png">


29.	Now you can see your agent in this page.

<img width="1000" alt="image" src="hands-on-lab-assets/image61.png">

30.	From menu, select “chat”.

<img width="1000" alt="image" src="hands-on-lab-assets/image62.png">

31.	You can enter you HR queries here and see the responses.

<img width="1000" alt="image" src="hands-on-lab-assets/image63.png">

### Skill Studio

32.	From the menu select "Skill Studio".

<img width="1000" alt="image" src="hands-on-lab-assets/image1.png">

33.	Click on "Create".

<img width="1000" alt="image" src="hands-on-lab-assets/image2.png">

34.	Select "Import API" from the dropdown.

<img width="1000" alt="image" src="hands-on-lab-assets/image3.png">

35.	Select "From a file".

<img width="1000" alt="image" src="hands-on-lab-assets/image4.png">


36.	Drag or Select the open specs file ([openapi.json](openapi.json)) and click on "next".

<img width="1000" alt="image" src="hands-on-lab-assets/image5.png">


37.	Select all checkboxes and click on "Add".

<img width="1000" alt="image" src="hands-on-lab-assets/image6.png">


38.	Once the skills are imported, Click on the three dots against the 'Update address' skill.

<img width="1000" alt="image" src="hands-on-lab-assets/image7.png">


39.	Select 'Enhance this skill'.

<img width="1000" alt="image" src="hands-on-lab-assets/image8.png">

40. Under "input", put "Hello! What's your name?" in name section and "What's your new address" in new_address section. Then click on "Publish".
<img width="1000" alt="image" src="hands-on-lab-assets/image8.5.png">


In a similar way,	You need to do modifications according to the below images, in all the skils by enhancing skills and then publish the skills.

To do this, first click on three dots against the skill name, then click on "Enhance this skill", then click on "Input" and refer below images for modifications:

For Request Time Off skill:
<img width="1000" alt="image" src="hands-on-lab-assets/image8.2.png">

For Get User Profile skill:
<img width="1000" alt="image" src="hands-on-lab-assets/image8.3.png">

For Update Title skill:
<img width="1000" alt="image" src="hands-on-lab-assets/image8.4.png">

For Get Time Off Balance skill:
<img width="1000" alt="image" src="hands-on-lab-assets/image8.1.png">

42.	Once all the skills are published, from menu go to "Skill sets".

<img width="1000" alt="image" src="hands-on-lab-assets/image10.png">


43.	From the dropdown, select "Orchestrate Agent Skills".

<img width="1000" alt="image" src="hands-on-lab-assets/image11.png">


44.	Click on "Connections". Your imported skills should be grouped in one app automatically. By clicking on arrow, search for that app. Click on three dots against that app and then click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image11.1.png">



45.	Select "Team credentials" and click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image11.2.png">


46.	Enter your credentials and click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image12.png">



47.	Once thats done, click on skills and then click on "Manage skills".

<img width="1000" alt="image" src="hands-on-lab-assets/image13.png">


48.	Click on app in which your skills are grouped.

<img width="1000" alt="image" src="hands-on-lab-assets/image14.png">



49.	Check if "Get Time Off Balance", "Get User Profile", "Request Time Off", "Update address" and "Update Title" skills are added. If not already added, click on "Add skill + " for all skills you want to add. 
Then click on "Connect App" on top right, if not already connected.

<img width="1000" alt="image" src="hands-on-lab-assets/image15.png">



50.	From menu, click on "AI agent configuration".

<img width="1000" alt="image" src="hands-on-lab-assets/image16.png">



51.	Select "Apps and skills" and click on the app your skills are grouped into.

<img width="1000" alt="image" src="hands-on-lab-assets/image17.png">


52.	Click on "Add to chat +" for Get Time off Balance.

<img width="1000" alt="image" src="hands-on-lab-assets/image18.png">


53.	Enter the description of this skill, "To get time off balance data" Then click on "Add skill".

<img width="1000" alt="image" src="hands-on-lab-assets/image19.png">

54.	Similarly add all the imported skills with following descriptions as follows. Get User Profile : to get complete profile data of user. Request Time Off : to request time off, apply for leaves Update Address : To update user address Update Title : To update user Title

55.	Now click on your profile icon in top right and select "settings"

<img width="1000" alt="image" src="hands-on-lab-assets/image20.png">

56.	Click on "chat", then "Switch to legacy chat", then click on "Change to legacy chat" as shown in below image.

<img width="1000" alt="image" src="hands-on-lab-assets/image21.png">


57.	From menu, select "Skill sets"

<img width="1000" alt="image" src="hands-on-lab-assets/image22.png">


58.	Select "Team Skills" in dropdown.

<img width="1000" alt="image" src="hands-on-lab-assets/image22.1.png">


59. Then click on "connections".Search for the app your skills are grouped into. Click on 3 dots and then click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image22.2.png">

59.a Select "Team Credentials", then click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image22.3.png">

59.b Enter your credentials, then click on "Connect app".

<img width="1000" alt="image" src="hands-on-lab-assets/image22.4.png">

60.	Click on "skills" and then "Manage skills".

<img width="1000" alt="image" src="hands-on-lab-assets/image23.png">


61.	Search for the app, where skills are imported, click on it.

  Then click on "add skills +" for all the skills you imported and then connect app using "Connect App" button in top right.

<img width="1000" alt="image" src="hands-on-lab-assets/image24.png">



<img width="1000" alt="image" src="hands-on-lab-assets/image26.png">

62.	Then click on profile icon, then settings , then click on chat version and switch to AI chat again.

<img width="1000" alt="image" src="hands-on-lab-assets/image27.png">

63.	From menu click on "chat".



<img width="1000" alt="image" src="hands-on-lab-assets/image28.png">

64.	Use your imported skills in chat.
<img width="1000" alt="image" src="hands-on-lab-assets/image29.png">


# Common issues and troubleshoot steps

Sometimes, when you open watsonx orchestrate homepage, the legacy chat is activated and one needs to manually activate AI Chat. Follow steps below to activate AI chat:

1. Click on profile icon in top right and click on settings.

<img width="1000" alt="image" src="hands-on-lab-assets/image64.1.png">

 2. Then click on chat version and switch to AI chat.

<img width="1000" alt="image" src="hands-on-lab-assets/image64.2.png">
End of Document
