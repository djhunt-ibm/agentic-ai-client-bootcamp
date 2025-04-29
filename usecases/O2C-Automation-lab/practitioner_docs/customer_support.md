# Customer Support Skill

1. Start by clicking on the skill studio.

<img src="./customer_support/01_skill_studio.png" alt="Skill Studio" width="800"/>

2. Click on the Create button

<img src="./customer_support/02_create_skill.png" alt="Create Skill" width="800"/>

3. Click on Import API button

<img src="./customer_support/03_import_API.png" alt="Import Skill" width="800"/>

4. Click on the Import from file button

<img src="./customer_support/04_import_from_a_file.png" alt="Import from file" width="800"/>

5. Click on upload `Drag and Drop files here or click to upload`

<img src="./customer_support/05_click_on_upload.png" alt="Upload file" width="800"/>

6. Select the `customer_support.yml` file that you downloaded from the repository.

<img src="./customer_support/06_select_customer_support.png" alt="Select customer support" width="800"/>

7. It should look like this

<img src="./customer_support/07_verify_customer_support.png" alt="Imported skill" width="800"/>

8. Then click on `Next` button

<img src="./customer_support/08_next_button.png" alt="Next button" width="800"/>

9. Choose the skill from the list and click on `Add` button

<img src="./customer_support/09_choose_the_skill.png" alt="Add skill" width="800"/>

Note: TroubleShooting: If you see an error like `Error: Failed to import skill`, 

<img src="./customer_support/error-01_skill_already_exist.png alt="Error" width="800"/>

It means a similar skill already exists. You will need to update the .yml file to a different name. Also make sure to change the `title`, `description`, as well as the description of each path in the `customer_support.yml` file.

10. Enhance the skill by clicking on the `Enhance` button

<img src="./customer_support/10_enhance_skill.png" alt="Enhance skill" width="800"/>

11. Click on `publish` button.

<img src="./customer_support/11_publish_skill.png" alt="Publish skill" width="800"/>

12. You will see that the skill is published successfully. Now let's go to `Skill catalog`.

<img src="./customer_support/12_click_on_skill_catalog.png" alt="Skill catalog" width="800"/>

13. Find the skill you just created and click on the tile

<img src="./customer_support/13_click_on_the_skill.png" alt="Click on the skill" width="800"/>

14. Click on the `Add Skill` button

<img src="./customer_support/14_add_skill.png" alt="Add skill" width="800"/>

You will see a check mark on the skill tile.

<img src="./customer_support/14.1_acknowledgement_of_skill_Added.png" alt="Skill added" width="800"/>


15. Click on `Connect to App` button

<img src="./customer_support/15_connect_to_app.png" alt="Connect to app" width="800"/>

16. Enter a dummy username and password, for this lab keep it as `test` and `test`. Click on `Connect app` button

<img src="./customer_support/16_connect_app.png" alt="Connect app" width="800"/>

<p style="color:green;">You will see a Toast message saying`connection successfull` on top right. </p>

> here we will also add pre-built skills to the app. Mainly skill related to Email by `Microsoft Outlook`.

a. search and select `Microsoft Outlook` skill tile.

<img src="./customer_support/16_a_select_microsoft_outlook.png" alt="Select Microsoft Outlook" width="800"/>

b. Select `Get All Emails` and click on `Reply to an Email` button

<img src="./customer_support/16_b_select_get_all_emails.png" alt="Get all emails" width="800"/>

`Note`: If You do not see `connected` status, on the top-right corner, click on the `triple dot` icon  > `Edit Connection` button > `Admin` or `Non-Admin` user. It will open a pop-up widow for `Microsoft Outlook` connection. Sign in with your `Microsoft` account, and connect to the app.

`creds for MS Outlook`:
```yml
username: wo-test1@ibmappcon.onmicrosoft.com
password: WatsonTestUser@123456
```

c. `Configure watsonx`, go to skill studio > apps
<img src="./customer_support/16_c_configure_watsonx.png" alt="Configure WatsonX" width="800"/>

d. Search for `watsonx` and then from the `triple dot` icon, click on `Edit` button

<img src="./customer_support/16_d_edit_watsonx.png" alt="Edit WatsonX" width="800"/>

e. Go to the conifguration tab and copy the server URL from the webpage header 
or use: 
```bash
https://us-south.watson-orchestrate.cloud.ibm.com/
```

<img src="./customer_support/16_e_server_url.png" alt="Server URL" width="800"/>

<img src="./customer_support/16_e_server_url_2.png" alt="Server URL" width="800"/>

- Then Click on `Test Connection` button. and enter a dummy `bearer token` e.g. `test`

<img src="./customer_support/16_e_test_connection.png" alt="Test connection" width="800"/>

- Click on `save` button.

f. Now, we will add some pre-built watsonx skills from Skill Catalog

<img src="./customer_support/16_f_add_watsonx_skills.png" alt="Add WatsonX skills" width="800"/>

g. Add, `Geneate a summary` and `Generate an Email`

<img src="./customer_support/16_g_add_generate_summary.png" alt="Add generate summary" width="800"/>

h. Click on `Connect App` button and a dummy bearer token e.g. `test`
<img src="./customer_support/16_h_connect_app.png" alt="Connect app" width="800"/>

17. Now let's get back to the Skill Studio from using the breadcrumbs on the top left corner. After that Click on Create > `Skill flow` button

<img src="./customer_support/17_create_skill_flow.png" alt="Create skill flow" width="800"/>

18. Click on `edit` icon

<img src="./customer_support/18_edit_icon.png" alt="Edit icon" width="800"/>

19. A side panel will open on the left. Edit the Name and Description of the skill flow. Click on `Save` button.

<img src="./customer_support/19_edit_name_description.png" alt="Edit name and description" width="800"/>

- Add A filter to the emails, that is get email via `Inbox` folder.

<img src="./customer_support/19_a_add_filter.png" alt="Add filter" width="800"/>

20. Click on the `+` icon to add a new node

<img src="./customer_support/20_add_node.png" alt="Add node" width="800"/>

21. Add `get all emails` tile.
<img src="./customer_support/21_add_get_all_emails.png" alt="Add get all emails" width="800"/>

22. Again click on the `+` icon to add a new node
<img src="./customer_support/22_add_node.png" alt="Add node" width="800"/>

23. Then select the `Get Order Details` tile and click on it. Add `716484927` as the order id.
<img src="./customer_support/23_add_get_order_details.png" alt="Add get order details" width="800"/>

24. Again click on the `+` and select the `Generate a summary` tile

In the Input add

```txt
Generate a summary for the below order details: 
```

- Then Click on the icon next to `Input` and select `Order Details` from the list.

<img src="./customer_support/24_add_generate_summary.png" alt="Add generate summary" width="800"/>

- Add Labeled Fields to create the Structured Prompt

<img src="./customer_support/24_a_add_labeled_fields.png" alt="Add labeled fields" width="800"/>

25. Again click on the `+` and select the `Generate a email` tile

<img src="./customer_support/25_add_generate_email.png" alt="Add generate email" width="800"/>

26. In the Input add

```txt
Generate an email for this summary: 
${generated_text}
```
Note: `${generated_text}` is the variable from the previous node, `generate a summary`.

<img src="./customer_support/26_add_labeled_fields.png" alt="Add labeled fields" width="800"/>

Mapping like:

<img src="./customer_support/26_a_mapping.png" alt="Mapping" width="800"/>

27. Finally to complete our skill flow, click on the `+` icon and select the `Reply to an Email` tile, in `Microsoft Outlook` skill.

<img src="./customer_support/27_add_reply_to_email.png" alt="Add reply to email" width="800"/>

a. Here the body_content will be `${generated_text}` from the previous node, `generate a email`.

<img src="./customer_support/27_a_body_content.png" alt="Body content" width="800"/>

b. Add body_content_type as `Text`

<img src="./customer_support/27_b_body_content_type.png" alt="Body content type" width="800"/>

c. Add the id from the `Get All Emails` node as `id`

<img src="./customer_support/27_c_id.png" alt="ID" width="800"/>

28. Now we are done with our flow

Click on the Actions button and click on `save and close` button.

<img src="./customer_support/28_save_and_close.png" alt="Save and close" width="800"/>

29. Now, finnaly publish the skill flow by clicking on the `Publish` button
<img src="./customer_support/29_publish_skill_flow.png" alt="Publish skill flow" width="800"/>

30. Now let's go to the `Skill Catalog` and find the skill flow we just created, inside skill flows

<img src="./customer_support/30_skill_catalog.png" alt="Skill catalog" width="800"/>

- search for the skill flow name and click on it
<img src="./customer_support/30_a_skill_flow_name.png" alt="Skill flow name" width="800"/>

31. Now let's add our skill flow to the app. Click on  the top right corner breadcrums > `Skill sets`.

<img src="./customer_support/31_skill_sets.png" alt="Skill sets" width="800"/>

32. Then we go to `Orchestrate Agent Skillset` and click it

<img src="./customer_support/32_orchestrate_agent_skillset.png" alt="Orchestrate agent skillset" width="800"/>

33. Go to connections tab and search for the flow, `Customer Support Flow` > `triple dot` icon > `connect app` button

<img src="./customer_support/33_connect_app.png" alt="Connect app" width="800"/>

34. A sidepanel will open, select team credential and click on `Connect app` button.

<img src="./customer_support/34_connect_app_2.png" alt="Connect app" width="800"/>

- Enter a dummy username and password, for this lab keep it as `test` and `test`. Click on `Connect app` button
<img src="./customer_support/34_a_connect_app.png" alt="Connect app" width="800"/>

- let's Also Add `Microsoft Outlook` app to the skillsets. Click on `Connect app` button
<img src="./customer_support/34_b_connect_app.png" alt="Connect app" width="800"/>

- Switch to the `Admin` user and click on `Connect app` button
<img src="./customer_support/34_c_connect_app.png" alt="Connect app" width="800"/>

- use the credentials mentioned above for `Microsoft Outlook` connection
```yml
username: wo-test1@ibmappcon.onmicrosoft.com
password: WatsonTestUser@123456

```

- Similarly connect to the `watsonx` app
<img src="./customer_support/34_d_connect_app.png" alt="Connect app" width="800"/>

- Click on `Connect app` button and enter a dummy bearer token e.g. `test`
<img src="./customer_support/34_e_connect_app.png" alt="Connect app" width="800"/>
35. Now, go to AI Agent Configuration

<img src="./customer_support/35_ai_agent_configuration.png" alt="AI agent configuration" width="800"/>

a. Go to `Apps and skills` > `Skill flows`

<img src="./customer_support/35_a_apps_and_skills.png" alt="Apps and skills" width="800"/>

b. search for the app `Customer Support Flow` and click on `Add to Chat` button.
<img src="./customer_support/35_b_add_to_chat.png" alt="Add to chat" width="800"/>

c. Add a routing description
```text
This is the app/flow for customer support, all queries w.r.t. to customer support should route to this Agent.
```

<img src="./customer_support/35_c_routing_description.png" alt="Routing description" width="800"/>

36. Now let's go to the AI Chat, click on breadcrumbs on the top left corner and select `Chat` from the list

<img src="./customer_support/36_ai_chat.png" alt="AI chat" width="800"/>

a. Invoke the chat with `Customer Support` and click on `Send` button

<img src="./customer_support/36_a_invoke_customer_support.png" alt="Invoke customer support" width="800"/>

b. Click on the `apply` button 

<img src="./customer_support/36_b_apply.png" alt="Apply" width="800"/>

c. The Select an email and click on `Apply` button

<img src="./customer_support/36_c_select_an_email.png" alt="Select an email" width="800"/>

d. Now select an order and click on `Apply` button

<img src="./customer_support/36_d_select_an_order.png" alt="Select an order" width="800"/>

e. Select the folder `Inbox` and message as `Updates on my order`, then click on `Apply` button

<img src="./customer_support/36_e_select_inbox.png" alt="Select inbox" width="800"/>

f. Email will be sent

<img src="./customer_support/36_f_email_sent.png" alt="Email sent" width="800"/>

g. Below you can see the email in the inbox

<img src="./customer_support/36_g_email_in_inbox.png" alt="Email in inbox" width="800"/>


`Challenge`: Try Modifying the prompt to see if you can get the email in a different format, with a different subject line, or a different body content. Try to do this by yourself and see if you can get the email in a different format.


