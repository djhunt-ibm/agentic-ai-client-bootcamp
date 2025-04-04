This FastAPI-based text extraction pipeline leverages a vision model to efficiently extract text from various document types, including PDF, PPT, and DOCX formats. It provides a convenient way to quickly assess text extraction accuracy. Ongoing enhancements aim to extend support to additional file types.

The pipeline features a customizable prompt system (currently utilizing a basic prompt), allowing adjustments to optimize extraction results as required.

# .env 
es_endpoint="https://wxd_user_id:wxd_password@wxd_url:wxd_port"

file_path_doc='Folder path of the files' # ex: /data

index_update ="true" #If you want to delete existing index and create freshly then make it as false

WATSONX_PROJECT_ID="wx_ai_project_id"

WATSONX_API_KEY="wx_api_key"

CLOUD_URL="https://us-south.ml.cloud.ibm.com"

MODEL_ID="mistralai/mistral-large"

MAX_TOKENS=4096



### if you want to chunk the data based on delimeter then keep chunk size and over lap size as 0 else keep delimeter as empty string.


#### If you are new to wxd and want to find default embedding model info then please follow below instructions.
1) Log into WXD.
2) Go to Analytics --> Machine Learning --> Model Management --> Trained Models.
3) You will be able to see list of trained and deployed model list.
4) You can pick up model id based on your requirement.
