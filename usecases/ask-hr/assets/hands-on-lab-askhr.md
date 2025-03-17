
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

1.	Login into your watsonx account. This is Homepage of watsonx AI.

<img width="1000" alt="image" src="hands-on-lab-assets/image30.png">

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

13.	Click on “Deploy”.

<img width="1000" alt="image" src="hands-on-lab-assets/image44.png">

14. Enter Deployment name and select “Deployment Space”. Then click on “Deploy”.(If there are no deployment space you need to create one using  [this](#/deployment_space_creation.md) guide.)

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


21.	Please refer to the [Code Engine instructor](https://github.ibm.com/skol/agentic-ai-client-bootcamp-instructors/blob/main/environment-setup/external-agent-builder/Readme.md) guide for deployment instructions. Once you obtain the deployment link, kindly open it.

You will reach the page shown in the image below.
Paste “Deployment ID”, “Space ID”, "API Key" and "watsonx URL" that you copied in previous steps. 
Click on “Generate Token”.

<img width="1000" alt="image" src="hands-on-lab-assets/image53.png">

22.	A token will be generated. Copy and paste it somewhere.

<img width="1000" alt="image" src="hands-on-lab-assets/image54.png">

## watsonx Orchestrate

23.	Go to “watsonx Orchestrate” homepage. 
<img width="1000" alt="image" src="hands-on-lab-assets/image55.png">

### AI agent configuration

24.	Click on hamburger menu on top left and select “AI agent configuration” from menu.

<img width="1000" alt="image" src="hands-on-lab-assets/image56.png">

25.	Click on “Agents“

<img width="1000" alt="image" src="hands-on-lab-assets/image57.png">


26.	Click on “Add Agent +”.

<img width="1000" alt="image" src="hands-on-lab-assets/image58.png">

27.	Give a name to your agent. Enter the description: 'This HR agent is an AI-powered assistant designed to handle common HR queries efficiently. It can provide policy information and answer frequently asked questions.”

<img width="1000" alt="image" src="hands-on-lab-assets/image59.png">


28.	Under “Authentication type”, select “Bearer Token”, enter the generated token you copied, In “Service Instance URL” section , enter "https://multi-agent-external.1slrp41syyn5.us-south.codeengine.appdomain.cloud/chat/completions".

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


36.	Drag or Select the open specs file and click on "next".

<img width="1000" alt="image" src="hands-on-lab-assets/image5.png">


37.	Select all checkboxes and click on "Add".

<img width="1000" alt="image" src="hands-on-lab-assets/image6.png">


38.	Once the skills are imported, Click on the three dots against the 'Update address' skill.

<img width="1000" alt="image" src="hands-on-lab-assets/image7.png">


39.	Select 'Enhance this skill'.

<img width="1000" alt="image" src="hands-on-lab-assets/image8.png">


40.	Click on 'Publish'..

<img width="1000" alt="image" src="hands-on-lab-assets/image9.png">



41.	Repeat last 3 steps for other imported skills as well.

42.	Once the skills are published, from menu go to "Skill sets".

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

End of Document
