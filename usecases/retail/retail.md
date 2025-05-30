# Use case: Retail shelf analysis

## Table of contents
- [Use case: Retail shelf analysis](#use-case-retail-shelf-analysis)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Pre-requisites](#pre-requisites)
  - [watsonx Orchestrate ADK](#watsonx-orchestrate-adk)
  - [The tools](#the-tools)
    - [Image to text tool](#image-to-text-tool)
      - [Connections](#connections)
      - [Langchain](#langchain)
      - [The @tool annotation](#the-tool-annotation)
      - [Local test](#local-test)
      - [Importing the tool](#importing-the-tool)

## Introduction
This use case describes a scenario where a user can submit an image, i.e. a photograph that contains a shelf of products. Products are expected to be consumer products, that is, shoes, clothing, food, household supplies etc. The system will analyze the content of the image, i.e. identify the products shown, retrieve market trends for those products via web search, and finally develop recommendations and an action plan for how to reorganize the shelf to align with those market trends. 

The solution consists of several agents who are working together to address the problem at hand:
- The `Internet Research Agent` handles the interpretation of any images that are submitted by the user, and runs web searches to identify market trends related to the relevant products.
- The `Market Analyst Agent` will analyze market trends and develop related recommendations and create an action plan.
- The `Retail Market Agent` is the supervisory agent that interacts with the user and collaborates with other agents, i.e. the two agents listed above, to create the final answer for the user.

We will use the [IBM watsonx Orchestrate Agent Developer Kit (ADK)](https://developer.watson-orchestrate.ibm.com/) to create the solution.

### Pre-requisites
- Check with your instructor to make sure **all systems** are up and running before you continue.
- Make sure you have an instance of the watsonx Orchestrate ADK up and running, either on your own laptop or in a virtual machine provided to you by your instructor.
- If you're an instructor running this lab, check the **Instructor's guides** to set up all environments and systems.

## watsonx Orchestrate ADK
As mentioned above, we will use the ADK to develop and test the solution. The ADK consists of the following elements:
- a set of containers that run the core elements of the watsonx Orchestrate server, all orchestrated as a single set via docker-compose. 
- a container hosting the UI element, which lets you create and manage agents, as well as testing them via chat interface.
- a CLI that allows simple interactions with watsonx Orchestrate (both the locally running server as well as any SaaS instance), including importing of agents and tools, starting and stopping the server, and more.
  
We will assume here that as part of the setup, you have gained access to an environment (which could be your own laptop) that lets you access the server via browser window, as well as giving you a command line terminal in which you can enter CLI commands. Moreover, we will do the code development in an instance of VS Code. 

You can decide to which level of detail you want to explore this use case. You can take the code and the related configuraton as is and simply deploy and run them. Or, you can change some of the details and see what the impact of your change is. For example, change the prompts you are using, or switch the model to a different one. And you can tinker with the code, too! Think of the ADK environment as a developer environment in which you can develop and test before uploading the solution to a shared SaaS environment. 

> Note that the screenshots below may vary slightly, depending on which environment you are using, but the exact same functionality is offered regardless of which environment you choose.

## The tools
As part of the solution, we will create two tools:
1. a tool that utilizes a watsonx.ai vision model to create a description of the picture that was submitted by the user, and
2. a tool that can search the web.

### Image to text tool
This tool takes the URL of an image hosted on the Internet as input, and returns the description of that image. 

> Why a URL? Ideally, the user interface would allow simply attaching an image file to the interaction, and the agent would pass that image content to the tool. Such an interface is on the roadmap for watsonx Orchestrate, in the interim, we are simply using a workaround, naemly passing a URL.

The code for this tool is in [this Python file](./src/tools/generate_description_from_image.py). Feel free to open this file in your VS Code environment to follow along our explanation of the code. Rather than going through it line by line, we will point out those sections of the code that we want to take a closer look at.

The code starts with a set of import statements. To run the code, either within watsonx Orchestrate or on the command line, you need to make sure a set of packages are installed. The [requirements.txt](./src/tools/requirements.txt) file lists all of the required packages. To run it locally, you need to run `pip install -r requirements.txt` with this file. When using this code inside a tool, we can impport this file together with the code, and the server will install the listed packages into the runtime the first time the tool is called. 

Next you will find this line:
```
CONNECTION_WATSONX_AI = 'watsonxai'
```

#### Connections
watsonx Orchestrate uses a concept called "connections" to allow passing in certain runtime values, for example, API keys, separately from the code, so that they don't have to be hardcoded in the code. A `Connection` is a separately created and maintained entity that binds values to their respective keys, and the tool can resolve those values at runtime. 
Since this tool uses watsonx.ai to retrieve the image description, we need to fill some variables with required values:
- The model ID of the model we will use. It has to be a model capable of interpreting images, for example, `meta-llama/llama-3-2-90b-vision-instruct`.
- The API key of the IBM cloud account your watsonx.ai instance is running in.
- The project ID of a watsonx.ai project that is associated with a runtime. 

Further down in the code, you can see how we are resolving the value for a certain key:
```
model_id = connections.key_value(CONNECTION_WATSONX_AI)['modelid']
```

You can find more information about connections in the [watsonx Orchestrate ADK documentation](https://developer.watson-orchestrate.ibm.com/connections/build_connections).

The code in the tool was written in a way that also allows it to be called from the command line. When running it this way, it doesn't have access to `Connections` objects. You will see in the code, towards the bottom of the file, that in the main function (which is only called when running from the command line), it uses the `load_dotenv()` function to set the required environment variables.

#### Langchain
In the import section of the code, you will see the following line:
```
from langchain_ibm import ChatWatsonx
```
This indicates that we are using the [IBM watsonx extension to Langchain](https://python.langchain.com/api_reference/ibm/index.html), and specifically, its `ChatWatsonx` model. This class allows simple interactions with the watsonx.ai backend. You set it up with a set of parameters (the code below is from the `generate_description_from_image()` function:
```
    watsonx_model = ChatWatsonx(
                        model_id=model_id,
                        url="https://us-south.ml.cloud.ibm.com",
                        apikey=api_key,
                        project_id=project_id,
                        params={
                            GenParams.TEMPERATURE: 0.5,
                            GenParams.MAX_NEW_TOKENS: 1000
                        }
    )
```
The message we will send to that model object is of type `HumanMessage`, which is imported from `langchain_core.messages`. The creation of the message is located in the `contruct_message()` function:
```
    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt_text},
            {"type": "image_url",
             "image_url": {"url": f"data:image/{image_format};base64,{image_data}"}}
        ]
```
Note how the message contains both a text prompt and an image. The image is encoded in base64 format. In the code, the retrieval of the image from the passed in URL, and its encoding into base64, happens in the `encode_image_to_base64()` function:
```
def encode_image_to_base64(image_url: str) -> Optional[str]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(image_url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    image_bytes = response.content
    encoded = base64.b64encode(image_bytes).decode('utf-8')
    return encoded
```        
#### The @tool annotation
The overall flow of the tool is like this:
- invoke generate_description_from_image(), pass in image URL
  - create ChatWatsonX model instance
- use encode_image_to_base64() to retrieve image content
- use construct_message to create HumanMessage instance
- call `model.invoke()` to return description of image content

Note that the main entry point for the tool is the `generate_description_from_image()` function. This is indicated by the `@tool~ annotation that prefixes the function declaration, paired with an indication of the `Connection` that is being used:
```
@tool(
        {"app_id": CONNECTION_WATSONX_AI, "type": ConnectionType.KEY_VALUE}
)
def generate_description_from_image(image_url: str) -> str:
    """
    Takes an image URL, encodes it to base64, and generates a description using Watsonx.ai.

    Parameters:
    image_url (str): The URL of the image file.

    Returns:
    str: The generated description of the image.
    """
```

Another important element of the code extract above is the description. This description is what the agent uses to determine whether the tool is right for the task at hand. Therefore, it is critically important to include a crisp and detailed description of the functionality of the tool. There is no other place where this is described! 

#### Local test
As mentioned above, you can run this tool from the command line to test the code. Note, however, that it is expecting a file named `.env` to be available in the same folder as where you start the Python interpreter from. You will see later that the watsonx Orchestrate ADK also requires a .env file when being started. You can reuse the same file for both purposes.
```
MODEL_ID=meta-llama/llama-3-2-90b-vision-instruct
WATSONX_API_KEY=oj5BW-...... [insert your API key here]
PROJECT_ID=186ac9b7-35ec....... [insert your project ID here]
```
You call the tool from the command line like this (again, make sure you are in the right folder that has both the .py file and the .env file):
`python generate_description_from_image.py --url https://i.imgur.com/qfiugNJ.jpeg`

#### Importing the tool
The easiest way to import the tool into your ADK instance is to use the CLI. Remember that we are using the concept of a `Connection` to insert the right values for API key etc? Before we can import the tool, we need to create the Connection instance (the import will fail otherwise).
We can store the Connection details in a [YAML file named watsonxai.yaml](./src/connections/watsonxai.yaml): 
```
spec_version: v1
kind: connection
app_id: watsonxai
environments:
    draft:
        kind: kv
        type: team
```
Create the Connection instance with the CLI like this:
`orchestrate connections import -f watsonxai. yaml`

Next, we need to set the actual values for model ID, API key and project ID. Note that these values need to be added in one call, in other words, whenever you call the `set-credentials` subcommand, it will overwrite what had been defined before.
Below is a script that shows how you can use the same .env file we used earlier to set up the Connections object:
```
#!/bin/bash

# Load variables from .env
set -o allexport
source .env
set +o allexport

# Use the environment variables in a command
orchestrate connections set-credentials -a watsonxai --env draft -e "modelid=${MODEL_ID}" -e "projectid=${PROJECT_ID}" -e "apikey=${WATSONX_API_KEY}"
```
After this, you are finally ready to import the tool. On the command line, enter the following command to do so (make sure you are in the right folder when calling it):
```
orchestrate tools import -k python -f generate_description_from_image.py -r requirements.txt -a watsonxai
```
