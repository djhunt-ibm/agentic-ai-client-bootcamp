# Retail use case

The detailed instructions for this use case are pending.

The use case assumes you have the watsonx Orchestrate ADK installed locally.

You can find the agent and tool definitions and Python code in the /src folder, together with a couple of convenience scripts that allow importing (and removing) via CLI.
Note that you have to create a .env file with some values defined before you can run the use case end to end. See the .env.sample file.

A sample prompt to test it all is
"Can you look at products in https://i.imgur.com/qfiugNJ.jpeg, identify market trends and recommendations, and create an action plan for me?"

> Notes: 
> - The first time each of the two tools is invoked, it triggers a lengthy install of all the required packages in the runtime, leading to a timeout in the prompt (it says it cannot be completed). It should work when you run it again, so simply repeat your prompt in a new chat.
> - The supervisory agent does not invoke the market_analysis_agent to get an action plan, instead it creates one itself.
