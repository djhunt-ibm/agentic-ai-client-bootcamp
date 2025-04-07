You can check out the code and deploy it on IBM Cloud Code Engine or any Python application hosting platform to get the API up and running.  


### Setup to run in local and Deployment

1. **Clone the Repository**  

2. **Create and Activate a Virtual Environment**  
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Server**  
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

Once the server is running, update the API link in `assets/WxO File Upload API.json`. Use this OpenAPI specification Go to Skill STudio to create a custom skill in Orchestrate and publish it.  

### Using the Skill  
- Find your skill in the Orchestrate **Skill Catalog** and add it to your personal skills.  
- Connect the app using dummy login credentials: `testuser/testuser`.  
- Execute the skill to upload a file to Cloud Object Storage (COS).  

### Supported File Formats  
The uploaded file will be stored in a COS bucket with a randomized name. Currently, the supported file formats are:  
`zip`, `png`, `jpg/jpeg`, `pdf`, `docx`, `pptx`, `xlsx`, `csv`, and `txt`.  

Referred from: https://github.ibm.com/madhu/acceleratorsX-assets.git
