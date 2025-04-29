# Cash Application Skill

1. Start by clicking on the skill studio.

<img src="./cash_application/01_skill_studio.png" alt="Skill Studio" width="800"/>

2. Click on the Create button

<img src="./cash_application/02_create_skill.png" alt="Create Skill" width="800"/>

3. Click on Import API button

<img src="./cash_application/03_import_API.png" alt="Import Skill" width="800"/>

4. Click on the Import from file button


<img src="./cash_application/04_import_from_file.png" alt="Import from file" width="800"/>

5. Click on upload `Drag and Drop files here or click to upload`
 and Select the cash_application.yml file from your file system.

<img src="./cash_application/05_select_file.png" alt="Select file" width="800"/>

6. Then click on `Next` button

<img src="./cash_application/06_next.png" alt="Next" width="800"/>

7. Select all the skills and click on `Add` button

<img src="./cash_application/07_select_all.png" alt="Select all" width="800"/>

8. It will take you to the skill studio page. You will see the skill `Get Invoice Details` in the list of skills.
Click on the `Triple dot` icon on the right side of the skill and select `Enhance Skill` option.

<img src="./cash_application/08_enhance_skill.png" alt="Enhance Skill" width="800"/>

9. A window will pop up. Click on the `Publish` button.

<img src="./cash_application/09_publish.png" alt="Publish" width="800"/>

10. Repeat the same for the `Get all Remittance Details`, `Get Matching Results Rem`, `Get Remittance Details` and `Display Confirmation`  skill.

After publishing all the skills, you will see the status of all the skills as `Published` in the skill studio.

<img src="./cash_application/10_published.png" alt="Published" width="800"/>

11. Now we will go to the `Skill Catalog` page. click on the breadcrumb and select `Skill Catalog` option.
<img src="./cash_application/11_skill_catalog.png" alt="Skill Catalog" width="800"/>

12. Search for `Cash Application` in the search bar and select the `Cash Application` skill. you will see 5 skills on the `Cash Application` tile.

<img src="./cash_application/12_cash_application.png" alt="Cash Application" width="800"/>

13. A window will open up. Click on `Add Skill +` icon on all the tiles to add the skills to the skill catalog.
<img src="./cash_application/13_add_skill.png" alt="Add Skill" width="800"/>

14. After adding all the skills, Click on `Connect APP` button on the top right corner of the page.
<img src="./cash_application/14_connect_app.png" alt="Connect App" width="800"/>

15. Enter dummy auth credential, username and password, e.g. `test` Click on `Connect app` button.

<img src="./cash_application/15_connect_app.png" alt="Connect App" width="800"/>

16. Now, we will get back to the `Skill studio` page. Click on the `Skill Studio` breadcrumb and select `Skill Studio` option.

<img src="./cash_application/16_skill_studio.png" alt="Skill Studio" width="800"/>

17. Click on the `Create` button and select `Skill Flow` option.

<img src="./cash_application/17_create_skill_flow.png" alt="Create Skill Flow" width="800"/>

18. The Skill flow page will open up. Click on the `Edit` Icon as in the image below.

<img src="./cash_application/18_edit_skill_flow.png" alt="Edit Skill Flow" width="800"/>

19. Write the name of the skill flow as `Cash Application Workflow` and click on `Save` button.

<img src="./cash_application/19_cash_application_workflow.png" alt="Cash Application Workflow" width="800"/>

20. Click on the `+` icon to add a new node to the skill flow.
<img src="./cash_application/20_add_node.png" alt="Add Node" width="800"/>

21. On the right side panel, select the `Skill` option and select the `Cash Application` skill from the list of skills.

<img src="./cash_application/21_select_skill.png" alt="Select Skill" width="800"/>

22. Click on the `Get Re Remittance Details` tile.

- this will show Get All remittances details

<img src= "./cash_application/22_get_all_remmitances_details.png" alt="get invoice details" width="800">

23. Now, Similarly add another node and click on `Cash Application` > `Get Re Remittance Details` tile to get the matching results. Then in the input we need to enter a `remittance id` this will be the selection from the last step, do it like belo image

<img src="cash_application.md/23_get_select_remmitance_id.png" width="800">

24. We may not want this additional info to be shown to the user, so click on `hide from the user toggle`

<img src="cash_application/24_hide_from_user.png" width="800">

25. Now, Similarly add another node and `Cash Application` > click on `Get Invoice Details` tile to get the matching results. Then in the input we need to enter a `invoice_number` for this lab we will hardcode it to 3189, but it could be taken as an input from the User.

<img src="cash_application/25_add_invoice_details.png" width="800">

- Also click on `hide from the user toggle`.

<img src="cash_application/26_hide_user_toggle.png" width="800">

26. Similarly Add another node and `Cash Application` > click on `Get Matching results rem` skill.

27. Finally Add another node and `Cash Application` > click on `Display Confirmation` skill. 

<img src="cash_application/27_complete_flow.png" width="800">

28. Then on the top-right corner Click on `Action` > `Enhance`
A pop up will open, click on `save and close`.

<img src="cash_application/28_enhance_flow.png" width="800">

29. Then It will take you back to the `Cash Application Workflow` and click on `publish` button.

<img src="cash_application/29_publish_flow.png" width="800">

30. After publishing the Skill. click on the breadcrumb and select `Skill Catalog` option.

<img src="cash_application/30_back_to_skill_catalog.png" width="800">

31. Search for `Cash Application`. Click on `Skill flows` tile

<img src="cash_application/31_skill_flow.png" width="800">

32. Search for `Cash Application Workflow`. and Click on `Add Skill +` button

<img src="cash_application/32_add_skill_flow.png" width="800">

33. After this let's add this workflow to our skill sets and connect to `Chat` click on top-right breadcrumb > `Skill Sets`
<img src="cash_application/33_skill_sets.png" width="auto" style= "clip-path: inset(0 0 50% 0);">

34. Select the `Orchestrate Agent Skill Sets` from the list of skill sets

<img src="cash_application/34_orchestrate_agent.png" width="800">

35. Go to the `Connection` tab and Search for `Cash Application`. 
on the right side `Triple dot` icon and select `Connect APP` option.

<img src="cash_application/35_connect_app.png" width="800">

36. A Side panel will open up. Click on `Connect App` button. Enter the dummy auth credentials, username and password, e.g. `test` and click on `Connect app` button.

<img src="cash_application/36_connect_app.png" width="800">

37. Now, click on the top-left breadcrumb and select `AI Agent Configuration` option.

<img src="cash_application/37_ai_agent_configuration.png" width="800">

38. Go to `Apps and Skills` tab and click on  `Skill Flows` Tile.

<img src="cash_application/38_skill_flows.png" width="800">

39. Search for `Cash Application Workflow` and click on the `Add to chat` button.

<img src="cash_application/39_add_to_chat.png" width="800">

40. Add routing description so that Orchestrate can route the request to the correct skill flow and Click on `Add skill` button.

<img src="cash_application/40_routing_description.png" width="800">

This will take a coupe of seconds to add the skill flow to the chat.

41. Finally, let's go to the `Chat` page. Click on the top-left breadcrumb and select `Chat` option.

<img src="cash_application/41_chat.png" width="800">

42. Type `Cash Application` in the search bar and select the `Cash Application` chat.
and select the `remiitance record` line as shown below.
<img src="cash_application/42_cash_application_chat.png" width="800">
- then Click on `Apply` button.

43. You will see the Confirmation message on the chat page. Saying that the `Invoice` close successfully.
<img src="cash_application/43_invoice_close.png" width="800">

This is how you can create a cash application skill in the skill studio and connect it to the chat.

`Challenge`: Modify the workflow to see if you can see the intermediate step results in the chat. remove the `hide from user` toggle on the `Get Re Remittance Details` and `Get Invoice Details` skills. Try to do this by yourself and see if you can get the intermediate results in the chat.


