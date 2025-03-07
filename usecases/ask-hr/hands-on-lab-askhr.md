
# AskHR - Agent setup hands on lab


1.	Login into your Watsonx account. This is Homepage of Watsonx AI.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/1c610c35-3ed2-4884-af05-378cf1a9026f)

2.  Click on “+” icon to create a project.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/092e17a5-b5c6-47fd-b667-9bda4d7a1d79)

2.a. Enter the name of your project, select storage from available storages and finally click on create. A new project will be created.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/435e66c7-ccac-4cb3-9894-3a7a9682d1b5)

3.	Click on hamburger icon on top left and select “Access (IAM)”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/ff8c1558-3dd3-4dac-a959-ec73ed1ae7bd)

4.	In next screen, select “API Keys” from menu.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/84502dbb-847e-4669-b8fb-c3537af0c5f7)

5.	Click on “Create”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/9dd51568-2e5e-4247-9855-f0b8cc8ebde5)

6.	Give your API key a name, then click on “Create”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/8dbaaf0d-701d-47e2-bb50-02ece08743ad)

7.	Copy the API key that is shown after clicking on “create”. Paste it somewhere, it’ll be used in later steps.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/08e78454-4215-4c4c-a345-eb4e47e4e96a)

8.	Switch back to the homepage. Open Agent Lab.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/3d3d326e-1ffd-4840-9dd3-f42b916df25e)

9.	In “Instructions” field, paste this prompt “You are a helpful Human Resources Assistant that uses tools to answer questions in detail. Please use website https://www.cipd.org/en/knowledge/factsheets/hr-policies-factsheet/ to give answers to user questions. When greeted, say “Hi, I am HR agent, How can I help you?”
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/89d76397-f6a4-443b-9db3-5ac5eec87dce)

10.	From “Added tools” section remove already added tools.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/f9babe58-af67-4949-84c6-59929de8d245)


11.	Then click on “Add a tool”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/f0b9951c-9f4a-4c95-bb9c-3d19fde31733)

12.	Enable “Webcrawler” tool and close this tools window.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/39278f5c-c4d8-4ccc-86e1-59387b7f9a39)

13.	Click on “Deploy”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/beb17362-bb32-4d1c-b302-49f56ffac6f7)

14. Enter Deployment name and select “Deployment Space”. If there are no deployment space you need to create one. Then click on “Deploy”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/3f6a67f3-3641-4dd8-9242-f2cf46b52304)

15.	Wait for the status to change to “Deployed” from “Initializing”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/3e11b861-3e30-4264-a830-6d5c3d894d22)

![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/3f615f68-d477-4049-a872-7f736f65bf57)

16.	Click on the name of the deployment you just deployed.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/52ede322-af38-4888-93fd-aec3b494595f)

17.	Copy and paste deployment id as shown in below image. You will need it in later step.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/0060ea89-bd3f-4480-889e-5c7a665fd622)

18.	From menu, select “Deployments”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/87bf8b8f-298a-4260-b7e4-80404eca4be5)

19.	Select “Spaces” and open the space where you deployed the agent.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/c0e46167-d1e1-473e-9d18-f5cf31cd192f)

20.	Under “manage” section, you’ll find “Space GUID”. Copy and paste it somewhere.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/9fef8f92-6ff5-4cb6-9de9-ba0a93022aea)

21.	Open the url https://multi-agent-external.1slrp41syyn5.us-south.codeengine.appdomain.cloud.
Paste “Deployment ID” and “Space ID” that you copied in previous steps. 
Click on “Generate Token”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/5077513b-9d7f-4aa5-bde9-789fa959c8ad)

22.	A token will be generated. Copy and paste it somewhere.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/0472b3f0-5a33-427c-a56e-0275fd46f2e3)

23.	Go to “Watsonx Orchestrate” homepage. 
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/dee4595e-52c6-420c-9a0c-c50bb1674c32)

24.	Click on hamburger menu on top left and select “AI agent configuration” from menu.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/301540da-a3dd-462a-9e36-3c14800a550b)

25.	Click on “Agents“
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/7e5fb891-47f2-4cd8-9b6f-0dfd829061c8)

26.	Clcik on “Add Agent +”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/f1c5aad8-7cd8-4f93-a95d-a87f4cfc33b6)

27.	Give a name to your agent. Enter the description “This HR agent is an AI-powered assistant designed to handle common HR queries efficiently. It can, provide policy information and answer frequently asked questions.”
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/9b9fc350-8456-45e1-a08a-87b030471eae)

28.	Under “Authentication type”, select “Bearer Token”, enter the generated token you copied, In “Service Instance URL” section , enter code-engine-url/chat/completions.

Click on “Connect”
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/7c0ebc9d-42a7-4682-8104-8d74d67f3dc0)



29.	Now you can see your agent in this page.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/eca781c4-1561-4705-a9b1-06c5cd1465c1)

30.	From menu, select “chat”.
![image](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/448234/2edec37b-a049-463b-84d3-6b160cf815c2)

31.	You can enter you HR queries here and see the responses.





































