# Order Management Skillflow
1. Navigate to IBM Cloud.

<img src="./order_management/01_1_ibm_cloud.png" alt="IBM Cloud" width="600"/>

2. Go to Hamburger menu on IBM Cloud Home Page.

<img src="./order_management/01_2_hamburger_menu.png" alt="Resources List" width="600"/>
 
2. From menu, select "Resources list".

<img src="./order_management/01_3_resource_list.png" alt="Resources List" width="600"/>

3. Under AI / Machine Learning, select watsonx Orchestrate and click on it.

<img src="./order_management/01_4_ai_ml.png" alt="AI / Machine Learning" width="600"/>

4.	Click on "Launch watsonx Orchestrate".

<img src="./order_management/02_1_wxo_launcher.png" alt="Launch watsonx Orchestrate" width="600"/>

5. This is the watsonx Orchestrate homepage. Click on the hamburger menu.

<img src="./order_management/03_2_wxo_homepage.png" alt="watsonx Orchestrate homepage" width="600"/>

6. From the menu, select "Skill Studio".

<img src="docs/order_management/04_1_skill_studio.png" alt="Skill Studio" width="600"/>
 
7. On the “Create” button click on arrow and select “Import API”.

<img src="./order_management/04_2_skill_studio_import_api.png" alt="“Create Skill Import API" width="600"/>

8. Click on “From a File”.

<img src="./order_management/05_3_import_openapi_from_a_file.png" alt="Import From a File" width="600"/>

9. Select the .yml or .json which contains openapi spec for Order Management.

<img src="./order_management/05_4_import_openapi_from_a_file.png" alt="Select OpenAPI File" width="600"/>

10. This will show the filename and click on Next

 <img src="./order_management/05_5_import_openapi_from_a_file.png" alt="Click Next" width="600"/>

11. This will show all skills present in API spec imported in step 9.

<img src="./order_management/05_6_import_openapi_from_a_file.png" alt="Add Skills" width="600"/>

11. Select all checkboxes and click on "Add".

<img src="./order_management/05_7_import_openapi_from_a_file.png" alt="Select Skills" width="600"/>

12. This will add all the skills and show the status as “Ready to publish”.

<img src="./order_management/05_8_import_openapi_from_a_file.png" alt="Ready to publish" width="600"/>

13. Once the skills are imported, click on the three dots against the 'Update address' skill. And Select 'Enhance this skill'.

<img src="./order_management/06_1_enhance_skill.png" alt="Enhance Skill" width="600"/>

14. Click on Publish. Similarly do this for all other skills

<img src="./order_management/06_2_enhance_skill.png" alt="Publish Skill" width="600"/>

15. From the Hamburger Menu click on “Skill catalog”.

<img src="./order_management/07_1_skill_catalog.png" alt="Skill Catalog" width="600"/>

16. In the search bar, search of “Order or Order Management” and Click on Order Management App.

<img src="./order_management/07_4_skill_catalog_select.png" alt="Search Order Management" width="600"/>

17. You can see all the skills present in Order Management App, Click on Add skill on each skill until all skills show “Added”.

<img src="./order_management/07_5_skill_catalog_add_skills.png" alt="Order Management App" width="600"/>

18. Click on Connect app

<img src="./order_management/07_6_skill_catalog_connect_app.png" alt="Add Skills" width="600"/>

19. Enter username and password and then click on Connect app.

<img src="./order_management/07_7_skill_catalog_connect_app_create_creds.png" alt="Connect App" width="600"/>
 
21. Then again from the Hamburger Menu Click on “Skill studio”

<img src="./order_management/08_1_skill_studio.png" alt="Skill Studio" width="600"/>

22. Click on Arrow on Create button and click on Skill Flow.

<img src="./order_management/08_2_skill_studio_create_skill_flow.png" alt="Create Skill Flow" width="600"/>


23. Click on edit icon on Untitled name.

<img src="./order_management/08_3_skill_studio_name.png" alt="Skill Flow Name" width="600"/>

24. Give the flow name and save.

<img src="./order_management/08_4_skill_studio_name_save.png" alt="Skill Flow Save Name" width="600"/>
 
25. Click on “+” icon in the flow.

<img src="./order_management/08_5_add_skills_to_skill_flow.png" alt="Add Skills to Skill Flow" width="600"/>

26. Click on “Order Management”

<img src="./order_management/08_6_add_skills_to_skill_flow.png" alt="Add Skills to Skill Flow" width="600"/>

27. Add Get All PO Details

<img src="./order_management/08_6_add_skills_to_skill_flow.png" alt="Add Get All PO Details"" width="600"/>

28. Click on next “+” icon in the flow after Get All PO Details and then Order Management.

<img src="./order_management/08_8_add_skills_to_skill_flow.png" alt="Skill Flow" width="600"/>

29. Add Get PO Details and click on get PO Details

<img src="./order_management//08_9_add_get_po_details_only.png" alt="Get PO Details" width="600"/>

30. Click on Get PO Details in the flow.

<img src="./order_management/08_10_get_po_details_only_edit.png" alt="Get PO Details" width="600"/>

30. Get PO Details takes an Input  variable “po_number”, click on this.

<img src="./order_management/08_11_get_po_details_only_edit_po_number.png" alt="Get PO Details Input" width="600"/>


31. Click on Get all PO Details

<img src="./order_management/08_11_get_po_details_only_edit_po_number_all_po.png" alt="Get All PO Details" width="600"/>

32. Select po_number from Skill Output

<img src="./order_management/08_11_get_po_details_only_edit_po_number_select.png" alt="Select PO Number" width="600"/>

33. It should look like this

<img src="./order_management/08_12_get_po_details_only_edit.png" alt="Get PO Details" width="600"/>

34. Click on next “+” icon in Skillflow.

<img src="./order_management/08_13_add_skills_to_skill_flow.png" alt="Add Skills to Skill Flow" width="600"/>

35. Add Get Quotation Details.

<img src="./order_management/08_14_add_get_quotation_details.png" alt="Get Quotation Details" width="600"/>

36. Click on Get Quotation Details

<img src="./order_management/08_15_get_quotation_details_edit.png" alt="Get Quotation Details" width="600"/>

37. This will take quotation_number as input, here we will specify a Default value. Click on Specify default value edit icon.

<img src="./order_management/08_16_get_quotation_details_edit_quotation_number.png" alt="Get Quotation Details Input" width="600"/>

38. We will keep a default number from the dummy data . Click on “+” icon again from Skillflow.

<img src="./order_management/08_16_get_quotation_details_edit_quotation_number_default.png" alt="Select Quotation Number" width="600"/>

39. Add Get Matching Results

<img src="./order_management/08_17_add_get_matching_results.png" alt="Get Matching Results" width="600"/>
 
40. Add Display Confirmation.

<img src="./order_management/08_18_add_display_confirmation.png" alt="Display Confirmation" width="600"/>

41. Hide all the information which you don’t need to show to user, click on Get all PO Details and Click on “Hide this from the user”.

<img src="./order_management/09_1_hide_information_from_user_get_all_po_details.png" alt="Hide information from the user Get all PO Details" width="600"/>


42. Click on Get PO Details and Click on “Hide this from the user”.

<img src="./order_management/09_2_hide_information_from_user_get_po_details.png" alt="Hide information from the user Get PO Details" width="600"/>

43. Click on Get Quotation Details and Click on “Hide this from the user”.

<img src="./order_management/09_3_hide_information_from_user_get_quotation_details.png" alt="Hide information from the user Get Quotation Details" width="600"/>

44. Click on Get matching Results and click on “Hide this from the user”.

<img src="./order_management/09_4_hide_information_from_user_get_matching_results.png" alt="Hide information from the user Get Matching Results" width="600"/>

45. Click on Display Confirmation and click on “Hide this from the user”.

<img src="./order_management/09_5_hide_information_from_user_display_confirmation.png" alt="Hide information from the user Display Confirmation" width="600"/>

46. Click on Actions button.

<img src="./order_management/10_1_actions.png" alt="Actions" width="600"/>

47. Click on Enhance.

<img src="./order_management/10_2_enhance.png" alt="Enhance" width="600"/>

48. Click on Save and close.

<img src="./order_management/10_3_save_and_close.png" alt="Save and Close" width="600"/>

49. Click on Publish.

<img src="./order_management/10_4_publish.png" alt="Publish" width="600"/>

50. From the Hamburger Menu click on Skill catalog.

<img src="./order_management/10_5_skill_catalog.png" alt="Skill Catalog" width="600"/>

51. In the search bar seach for “Order” and click on Skill flows

<img src="./order_management/10_6_skill_catalog_search.png" alt="Search Order Management" width="600"/>

52. Add skill Order Management Workflow.

<img src="./order_management/10_7_skill_catalog_add_order_management_workflow.png" alt="Add Order Management Workflow" width="600"/>

53. From the Hamburger Menu click on chat.

<img src="./order_management/10_8_chat.png" alt="Chat" width="600"/>

54. It will open this chat page and application can be tested here.

<img src="./order_management/10_9_chat.png" alt="Chat" width="600"/>

55. In the browser, replace ‘chat’ with ‘legacy-chat’ in URL.

<img src="./order_management/10_10_legacy_chat.png" alt="Legacy Chat" width="600"/>

56. Select Order Management Workflow in legacy chat.

<img src="./order_management/10_11_legacy_chat_select_order_management_workflow.png" alt="Select Order Management Workflow" width="600"/>

57. This will show all the PO Records, select first row.

<img src="./order_management/10_12_legacy_chat_select_first_row.png" alt="Select First Row" width="600"/>

58. Click on Apply

<img src="./order_management/10_13_legacy_chat_first_row_apply.png" alt="Apply" width="600"/>

59. This will show PO Number, click on Apply

<img src="./order_management/10_14_legacy_chat_po_number_apply.png" alt="Apply PO Number" width="600"/>

60. This will show Quotation Number, here click on Apply.

<img src="./order_management/10_15_legacy_chat_quotation_number_apply.png" alt="Apply Quotation Number" width="600"/>

## Adding AI Agents

61. Go to skill sets

<img src="./order_management/11_1_skill_sets.png" alt="Skill Sets" width="600"/>

62. From the Team skills, Select “Orchestrate Agent Skillset”.

<img src="./order_management/11_2_skill_sets_orchestrate_agent_skillset.png" alt="Orchestrate Agent Skillset" width="600"/>

63. Go to Connections tab.

<img src="./order_management/11_3_skill_sets_orchestrate_agent_skillset_connections.png" alt="Connections" width="600"/>

64. Click on Search Button

<img src="./order_management/11_4_skill_sets_orchestrate_agent_skillset_connections_search.png" alt="Search" width="600"/>

65. In the search bar type Order and Selected Order Management, click on three dos and click Connect app.

<img src="./order_management/11_5_skill_sets_orchestrate_agent_skillset_connections_search_order_management.png" alt="Order Management" width="600"/>

66. Click on Connect app button.

<img src="./order_management/11_6_skill_sets_orchestrate_agent_skillset_connections_connect_app.png" alt="Connect App" width="600"/>

67. From the Hamburger Menu, go to AI agent configuration.

<img src="./customer_support/12_1_ai_agent_configuration.png" alt="AI Agent Configuration" width="600"/>


68. Click Apps and skills.

<img src="./order_management/12_2_ai_agent_configuration_apps_skills.png" alt="Apps and Skills" width="600"/>

69. Click on Skill flows

<img src="./order_management/12_3_ai_agent_configuration_skill_flows.png" alt="Skill Flows" width="600"/>

70. It will be display all the skill flow present.

<img src="./order_management/12_4_ai_agent_configuration_skill_flows.png" alt="Skill Flows" width="600"/>

71. Search for “Order” and Add Order Management Workflow to chat.

<img src="./order_management/12_5_ai_agent_configuration_skill_flows_order_management.png" alt="Order Management Workflow" width="600"/>

72. Give a routing description and click Add skill.

<img src="./order_management/12_6_ai_agent_configuration_skill_flows_order_management_routing_description.png" alt="Routing Description" width="600"/>

73. Go to Chat

<img src="./order_management/13_1_ai_agent_configuration_skill_flows_order_management_ai_chat.png" alt="Chat" width="600"/>

74. Type Order Management in chatbot and press enter

<img src="./order_management/13_2_order_management_ai_chat.png" alt="Order Management" width="600"/>

75. Seclect first row from the output and click on Apply.

<img src="./order_management/13_3_order_management_ai_chat_select_first_row.png" alt="Select First Row" width="600"/>

76. Click on Yes to confirm PO Number.

<img src="./order_management/13_4_order_management_ai_chat_confirm_po_number.png" alt="Confirm PO Number" width="600"/>

77. Click on Yes to confirm Quotation Number.

<img src="./order_management/13_5_order_management_ai_chat_confirm_quotation_number.png" alt="Confirm Quotation Number" width="600"/>

78. Order placement confirmation will be displayed. Not down the Order ID for future reference.

<img src="./order_management/13_6_order_management_ai_chat_order_placement_confirmation.png" alt="Order Placement Confirmation" width="600"/>




