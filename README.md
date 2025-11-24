# WeChat Work API SDK

A Python SDK for interacting with the WeChat Work API. This library provides a simple and efficient way to integrate your Python applications with WeChat Work, supporting key features like user management, authentication, and more. The SDK features a clean modular architecture with static imports.

## Features

- **Static Modular Architecture**: Separate modules for configuration, common functions (access_token), user management, and document management
- **Environment Configuration**: Support for .env files and environment variables with python-dotenv
- **Easy Access Token Management**: Automatic retrieval and caching of access tokens with TTL (Time To Live) support
- **User Management**: Get user information, update user profiles, and convert mobile numbers to user IDs
- **Document Management**: Full support for WeChat Work document operations (wedoc), including document creation, editing, sharing, and permission management
- **Comprehensive Error Handling**: Proper exception handling for API errors
- **Type Hints**: Full type annotation support for better IDE experience
- **Thread-Safe**: Safe for concurrent usage in multi-threaded applications
- **Caching**: Uses `cachetools` for efficient token caching

## Installation

Install the package using pip:

```bash
pip install weixin-work-reborn
```

## Quick Start

```python
from weixin_work_reborn import WeChatWorkClient, Config

# Initialize the client with configuration
config = Config()  # Loads from .env file or environment variables
client = WeChatWorkClient(config=config)

# Get user information
user_info = client.get_user("user_id_here")
print(user_info)

# Update user information
result = client.update_user(
    user_id="user_id_here",
    name="New Name",
    mobile="13800138000",
    email="newemail@example.com"
)
print(result)

# Convert mobile to user ID
userid_result = client.mobile_to_userid("13800138000")
print(userid_result)

# Document Management Examples

# Create a new document
doc_result = client.new_document(
    doc_type=3,  # 3 for document, 4 for spreadsheet, 10 for smart sheet
    doc_name="My New Document"
)
print(f"Created document with ID: {doc_result.get('docid')}")

# Get document information
if 'docid' in doc_result:
    doc_info = client.get_document_base_info(doc_result['docid'])
    print(f"Document info: {doc_info}")

# Rename the document
if 'docid' in doc_result:
    rename_result = client.rename_document(
        docid=doc_result['docid'],
        new_name="Renamed Document"
    )
    print(f"Rename result: {rename_result}")
```

## Configuration

### Using .env File (Recommended)

Create a `.env` file in your project root:

```bash
WEIXIN_WORK_BASE_URL=https://qyapi.weixin.qq.com/
WEIXIN_WORK_CORP_ID=your_corp_id_here
WEIXIN_WORK_APP_SECRET=your_app_secret_here
WEIXIN_WORK_CONTACTS_SYNC_SECRET=your_contacts_sync_secret_here
WEIXIN_WORK_DOC_SECRET=your_doc_secret_here
WEIXIN_WORK_AGENT_ID=your_agent_id_here
```

**Note:** WeChat Work API requires different secrets for different API endpoints:
- `WEIXIN_WORK_APP_SECRET` is used for general API operations (e.g., getting user information, mobile to userid conversion)
- `WEIXIN_WORK_CONTACTS_SYNC_SECRET` is specifically required for user management operations (e.g., update_user)
- `WEIXIN_WORK_DOC_SECRET` is used for doc related API operations (e.g., create, read, write wedoc)

Then in your code:

```python
from weixin_work_reborn import WeChatWorkClient, Config

config = Config()  # Automatically loads from .env file
client = WeChatWorkClient(config=config)
```

### Environment Variables

Alternatively, you can set environment variables:

```bash
export WEIXIN_WORK_BASE_URL="https://qyapi.weixin.qq.com/"
export WEIXIN_WORK_CORP_ID="your_corp_id_here"
export WEIXIN_WORK_APP_SECRET="your_app_secret_here"
export WEIXIN_WORK_CONTACTS_SYNC_SECRET="your_contacts_sync_secret_here"
export WEIXIN_WORK_DOC_SECRET="your_doc_secret_here"
export WEIXIN_WORK_AGENT_ID="your_agent_id_here"
```

**Note:** WeChat Work API requires different secrets for different API endpoints:
- `WEIXIN_WORK_APP_SECRET` is used for general API operations (e.g., getting user information, mobile to userid conversion)
- `WEIXIN_WORK_CONTACTS_SYNC_SECRET` is specifically required for user management operations (e.g., update_user)
- `WEIXIN_WORK_DOC_SECRET` is used for doc related API operations (e.g., create, read, write wedoc)

## API Reference

### Config

Handles configuration loading from environment variables and .env files.

#### Constructor

```python
Config(env_file=None)
```

- `env_file` (str, optional): Path to a specific .env file to load

#### Properties

- `base_url` (str): The base URL for WeChat Work API (default: "https://qyapi.weixin.qq.com/")
- `corp_id` (str): Your WeChat Work corporate ID
- `corp_secret` (str): Your application secret
- `agent_id` (str): Your application agent ID

### WeChatWorkClient

The main client class for interacting with the WeChat Work API.

#### Constructor

```python
WeChatWorkClient(config=None, config_file=None, token_cache_size=100, token_cache_ttl=7000)
```

- `config` (Config, optional): Config object with API settings
- `config_file` (str, optional): Path to .env file
- `token_cache_size` (int): Size of the token cache (default: 100)
- `token_cache_ttl` (int): Time-to-live for cached tokens in seconds (default: 7000, just under the 7200s token expiry)

#### Methods

##### get_user(user_id)

Get user information by user ID.

- `user_id` (str): The user ID to retrieve information for
- Returns: User information as a dictionary

##### update_user(userid, **kwargs)

Update user information.

- `userid` (str): Required. User ID. Corresponds to the account in the management console, must be unique within the enterprise. Case-insensitive, 1-64 bytes long
- `name` (str, optional): Member name, 1-64 UTF8 characters
- `alias` (str, optional): Alias, 1-64 UTF8 characters
- `mobile` (str, optional): Mobile number. Must be unique within the enterprise
- `department` (list, optional): List of department IDs the member belongs to, up to 100
- `order` (list, optional): Sorting value within the department, defaults to 0. Effective when department is provided. Number must match department, larger number means higher priority. Valid range is [0, 2^32)
- `position` (str, optional): Position information, 0-128 UTF8 characters
- `gender` (str, optional): Gender. 1 for male, 2 for female
- `email` (str, optional): Email address. 6-64 bytes and valid email format, must be unique within enterprise
- `biz_mail` (str, optional): If the enterprise has activated Tencent Corporate Mail (Enterprise WeChat Mail), setting this creates a corporate email account. 6-63 bytes and valid corporate email format, must be unique within enterprise
- `biz_mail_alias` (dict, optional): Corporate email alias. 6-63 bytes and valid corporate email format, must be unique within enterprise, up to 5 aliases can be set. Updates are overwritten. Passing empty structure or empty array clears current corporate email aliases
- `telephone` (str, optional): Landline. Composed of 1-32 digits, "-", "+", or ","
- `is_leader_in_dept` (list, optional): Department head field, count must match department, indicates whether the member is a head in the department. 0-False, 1-True
- `direct_leader` (list, optional): Direct supervisor, can set members within the enterprise as direct supervisor, max 1 can be set
- `avatar_mediaid` (str, optional): Member's avatar mediaid, obtained through media management API upload
- `enable` (int, optional): Enable/disable member. 1 for enabled, 0 for disabled
- `extattr` (dict, optional): Extended attributes. Fields need to be added in WEB management first
- `external_profile` (dict, optional): Member's external attributes
- `external_position` (str, optional): External position. If set, used as the displayed position, otherwise use position. Up to 12 Chinese characters
- `nickname` (str, optional): Video account name (after setting, the member will display this video account externally). Must be selected from the video account bound to the enterprise WeChat, accessible in the "My Enterprise" page
- `address` (str, optional): Address. Max 128 characters
- `main_department` (int, optional): Main department
- Returns: API response as a dictionary

##### mobile_to_userid(mobile)

Convert mobile number to user ID.

- `mobile` (str): The mobile number to convert
- Returns: API response containing user ID as a dictionary

### Document Management (WeDoc) Methods

The WeChatWorkClient now includes comprehensive document management (WeDoc) functionality.

##### new_document(doc_type, doc_name, spaceid=None, fatherid=None, admin_users=None)

Create a new document, spreadsheet, or smart sheet.

- `doc_type` (int): Document type, 3: document 4: spreadsheet 10: smart sheet
- `doc_name` (str): Document name (max 255 characters, will be truncated if exceeded)
- `spaceid` (str, optional): Space ID. If specified, `fatherid` must also be specified
- `fatherid` (str, optional): Parent directory file ID, use spaceid when in root directory
- `admin_users` (list, optional): List of user IDs to be document administrators
- Returns: API response as a dictionary with docid and URL for the new document

##### rename_document(new_name, docid=None, formid=None)

Rename an existing document, spreadsheet, smart sheet, or form.

- `new_name` (str): New name for the document (max 255 characters, English=1, Chinese=2, truncated if exceeded)
- `docid` (str, optional): Document docid (only one of docid or formid should be provided), only app-created docs can be modified
- `formid` (str, optional): Form ID (only one of docid or formid should be provided), only app-created forms can be modified
- Returns: API response as a dictionary

##### delete_document(docid=None, formid=None)

Delete an existing document, spreadsheet, smart sheet, or form.

- `docid` (str, optional): Document docid (only one of docid or formid should be provided), only app-created docs can be deleted
- `formid` (str, optional): Form ID (only one of docid or formid should be provided), only app-created forms can be deleted
- Returns: API response as a dictionary

##### get_document_base_info(docid)

Get basic information about a document, spreadsheet, smart sheet, or form.

- `docid` (str): Document docid
- Returns: API response as a dictionary containing document details (name, creation time, modification time, type)

##### share_document(docid=None, formid=None)

Get the sharing link for a document, spreadsheet, smart sheet, or form.

- `docid` (str, optional): Document ID (only one of docid or formid should be provided)
- `formid` (str, optional): Form ID (only one of docid or formid should be provided)
- Returns: API response as a dictionary with the share URL

##### edit_document_content(docid, requests, version=None)

Batch edit document content with multiple operations.

- `docid` (str): Document ID
- `requests` (list): List of update operations, supports:
  - replace_text: Replace text content at specified location
  - insert_text: Insert text content at specified location
  - delete_content: Delete content at specified location
  - insert_image: Insert image at specified location
  - insert_page_break: Insert page break at specified location
  - insert_table: Insert table at specified location
  - insert_paragraph: Insert paragraph at specified location
  - update_text_property: Update text properties at specified location
- `version` (int, optional): Document version to edit, obtained from get document content API
- Returns: API response as a dictionary

##### get_document_data(docid)

Get content data from a document.

- `docid` (str): Document ID
- Returns: API response as a dictionary containing document content and version

##### edit_spreadsheet_content(docid, requests)

Edit spreadsheet content with multiple operations.

- `docid` (str): Document ID
- `requests` (list): List of update operations, supports:
  - add_sheet_request: Add worksheet
  - delete_sheet_request: Delete worksheet
  - update_range_request: Update cell range content
  - delete_dimension_request: Delete continuous rows/columns
- Returns: API response as a dictionary

##### get_sheet_properties(docid)

Get sheet row/column information for spreadsheets.

- `docid` (str): Online spreadsheet docid
- Returns: API response as a dictionary with worksheet properties

##### get_sheet_range_data(docid, sheet_id, range_str)

Get spreadsheet data for a specified range.

- `docid` (str): Online spreadsheet identifier
- `sheet_id` (str): Worksheet ID (unique identifier)
- `range_str` (str): Query range in A1 notation
- Returns: API response as a dictionary with table data

##### add_smartsheet(docid, title=None, index=None)

Add a smart sheet to a table.

- `docid` (str): Document ID
- `title` (str, optional): Smart sheet title
- `index` (int, optional): Smart sheet index
- Returns: API response as a dictionary with sheet details

##### delete_smartsheet(docid, sheet_id)

Delete a smart sheet from an online table.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID to delete
- Returns: API response as a dictionary

##### update_smartsheet(docid, sheet_id, title=None)

Update a smart sheet title.

- `docid` (str): Document ID
- `sheet_id` (str): Sheet ID to update
- `title` (str, optional): New sheet title
- Returns: API response as a dictionary

##### query_smartsheet(docid, sheet_id=None, need_all_type_sheet=False)

Query smart sheet information.

- `docid` (str): Document ID
- `sheet_id` (str, optional): Specific sheet ID to query
- `need_all_type_sheet` (bool): Get all sheet types. True to include dashboards and info pages
- Returns: API response as a dictionary with sheet list

##### add_view(docid, sheet_id, view_title, view_type, property_gantt=None, property_calendar=None)

Add a view to a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `view_title` (str): View title
- `view_type` (str): View type: "VIEW_TYPE_GRID", "VIEW_TYPE_KANBAN", "VIEW_TYPE_GALLERY", "VIEW_TYPE_GANTT", "VIEW_TYPE_CALENDAR"
- `property_gantt` (dict, optional): Gantt view properties
- `property_calendar` (dict, optional): Calendar view properties
- Returns: API response as a dictionary with view details

##### delete_views(docid, sheet_id, view_ids)

Delete views from a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `view_ids` (list): List of view IDs to delete
- Returns: API response as a dictionary

##### update_view(docid, sheet_id, view_id, view_title=None, property_data=None)

Update a view in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `view_id` (str): View ID to update
- `view_title` (str, optional): New view title
- `property_data` (dict, optional): View settings and configurations
- Returns: API response as a dictionary

##### query_views(docid, sheet_id, view_ids=None, offset=0, limit=0)

Query views in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `view_ids` (list, optional): List of view IDs to query
- `offset` (int): Offset, initial value 0
- `limit` (int): Page size
- Returns: API response as a dictionary with view data

##### add_fields(docid, sheet_id, fields)

Add fields to a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `fields` (list): Field details list
- Returns: API response as a dictionary with field details

##### delete_fields(docid, sheet_id, field_ids)

Delete fields from a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `field_ids` (list): List of field IDs to delete
- Returns: API response as a dictionary

##### update_fields(docid, sheet_id, fields)

Update fields in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `fields` (list): Field details list
- Returns: API response as a dictionary

##### query_fields(docid, sheet_id, view_id=None, field_ids=None, field_titles=None, offset=0, limit=0)

Query fields in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `view_id` (str, optional): View ID
- `field_ids` (list, optional): List of field IDs to query
- `field_titles` (list, optional): List of field titles to query
- `offset` (int): Offset, initial value 0
- `limit` (int): Page size
- Returns: API response as a dictionary with field details

##### add_records(docid, sheet_id, records, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE")

Add records to a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `records` (list): List of record content to add
- `key_type` (str): Cell key type in returned records, default to "CELL_VALUE_KEY_TYPE_FIELD_TITLE"
- Returns: API response as a dictionary with record details

##### delete_records(docid, sheet_id, record_ids)

Delete records from a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `record_ids` (list): List of record IDs to delete
- Returns: API response as a dictionary

##### update_records(docid, sheet_id, records, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE")

Update records in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `records` (list): List of records to update
- `key_type` (str): Cell key type in returned records
- Returns: API response as a dictionary

##### query_records(docid, sheet_id, view_id=None, record_ids=None, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE", field_titles=None, field_ids=None, sort=None, offset=0, limit=0, ver=None, filter_spec=None)

Query records in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Smartsheet sheet ID
- `view_id` (str, optional): View ID
- `record_ids` (list, optional): List of record IDs to query
- `key_type` (str): Cell key type in returned records
- `field_titles` (list, optional): Return specified columns by field titles
- `field_ids` (list, optional): Return specified columns by field IDs
- `sort` (list, optional): Sort returned records
- `offset` (int): Offset, initial value 0
- `limit` (int): Page size
- `ver` (int, optional): Version number
- `filter_spec` (dict, optional): Filter settings
- Returns: API response as a dictionary with record data

##### add_field_group(docid, sheet_id, name, children)

Add a field group to a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `name` (str): Group name, cannot duplicate existing names
- `children` (list): Group content list
- Returns: API response as a dictionary

##### delete_field_groups(docid, sheet_id, field_group_ids)

Delete field groups from a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Sheet ID
- `field_group_ids` (list): List of group IDs to delete
- Returns: API response as a dictionary

##### update_field_group(docid, sheet_id, field_group_id, name=None, children=None)

Update a field group in a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `field_group_id` (str): Group ID to update
- `name` (str, optional): New group name
- `children` (list, optional): New group content list
- Returns: API response as a dictionary

##### get_field_groups(docid, sheet_id, offset=0, limit=10)

Get field groups from a smart sheet.

- `docid` (str): Document ID
- `sheet_id` (str): Table ID
- `offset` (int): Offset, initial value 0
- `limit` (int): Page size
- Returns: API response as a dictionary with group details

##### get_document_auth(docid)

Get document permission information.

- `docid` (str): Document ID
- Returns: API response as a dictionary with permission details

##### modify_document_join_rule(docid, enable_corp_internal=None, corp_internal_auth=None, enable_corp_external=None, corp_external_auth=None, corp_internal_approve_only_by_admin=None, corp_external_approve_only_by_admin=None, ban_share_external=None, update_co_auth_list=None, co_auth_list=None)

Modify document access rules.

- `docid` (str): Document ID to operate
- `enable_corp_internal` (bool, optional): Allow internal members to browse
- `corp_internal_auth` (int, optional): Internal member permission type
- `enable_corp_external` (bool, optional): Allow external members to browse
- `corp_external_auth` (int, optional): External member permission type
- `corp_internal_approve_only_by_admin` (bool, optional): Internal members need admin approval
- `corp_external_approve_only_by_admin` (bool, optional): External members need admin approval
- `ban_share_external` (bool, optional): Ban sharing to external
- `update_co_auth_list` (bool, optional): Update specific department access list
- `co_auth_list` (dict, optional): Department access list to update
- Returns: API response as a dictionary

##### modify_document_member(docid, update_file_member_list=None, del_file_member_list=None)

Modify document member range and permissions.

- `docid` (str): Document ID to operate
- `update_file_member_list` (list, optional): Update member range list
- `del_file_member_list` (list, optional): Delete member range list
- Returns: API response as a dictionary

##### modify_document_safety_setting(docid, enable_readonly_copy=None, watermark=None)

Modify document security settings.

- `docid` (str): Document ID to operate
- `enable_readonly_copy` (bool, optional): Allow readonly members to copy/download
- `watermark` (dict, optional): Watermark settings
- Returns: API response as a dictionary

##### query_sheet_privilege(docid, type_, rule_id_list=None)

Query smart sheet permission details.

- `docid` (str): Smart sheet ID
- `type_` (int): Permission rule type, 1:all members, 2:additional permissions
- `rule_id_list` (list, optional): Rule IDs to query
- Returns: API response as a dictionary with permissions

##### update_sheet_privilege(docid, type_, rule_id=None, name=None, priv_list=None)

Update smart sheet permissions.

- `docid` (str): Smart sheet ID
- `type_` (int): Permission rule type, 1:all members, 2:additional
- `rule_id` (int, optional): Required when type=2
- `name` (str, optional): Permission name
- `priv_list` (list, optional): Sheet-specific permissions list
- Returns: API response as a dictionary

##### create_rule(docid, name)

Create smart sheet additional member permissions.

- `docid` (str): Smart sheet ID
- `name` (str): Permission rule name, must be unique
- Returns: API response as a dictionary with rule ID

##### modify_rule_member(docid, rule_id, add_member_range=None, del_member_range=None)

Update smart sheet additional member permissions.

- `docid` (str): Smart sheet ID
- `rule_id` (int): Rule ID to update
- `add_member_range` (dict, optional): Add members
- `del_member_range` (dict, optional): Delete members
- Returns: API response as a dictionary

##### delete_rule(docid, rule_id_list)

Delete smart sheet additional member permissions.

- `docid` (str): Smart sheet ID
- `rule_id_list` (list): List of rule IDs to delete
- Returns: API response as a dictionary

##### create_form(form_title, form_desc=None, form_header=None, form_question=None, form_setting=None, spaceid=None, fatherid=None)

Create a form.

- `form_title` (str): Form title
- `form_desc` (str, optional): Form description
- `form_header` (str, optional): Form header background image URL
- `form_question` (dict, optional): Form question list
- `form_setting` (dict, optional): Form settings
- `spaceid` (str, optional): Space ID
- `fatherid` (str, optional): Parent directory file ID
- Returns: API response as a dictionary with form ID

##### modify_form(formid, oper, form_title=None, form_desc=None, form_header=None, form_question=None, form_setting=None)

Modify a form.

- `formid` (str): Form ID
- `oper` (int): Operation type. 1: full modify questions; 2: full modify settings
- `form_title` (str, optional): Form title (when oper=1)
- `form_desc` (str, optional): Form description (when oper=1)
- `form_header` (str, optional): Form header background image URL (when oper=1)
- `form_question` (dict, optional): Form question list (when oper=1)
- `form_setting` (dict, optional): Form settings (when oper=2)
- Returns: API response as a dictionary

##### get_form_info(formid)

Get form information.

- `formid` (str): Form ID
- Returns: API response as a dictionary with form details

##### get_form_statistic(repeated_id, req_type, start_time=None, end_time=None, limit=None, cursor=None)

Form statistics query.

- `repeated_id` (str): Form repeated_id from get_form_info response
- `req_type` (int): Request type 1: statistics only 2: submitted list 3: not submitted list
- `start_time` (int, optional): Required for submitted list, start time
- `end_time` (int, optional): Required for submitted list, end time
- `limit` (int, optional): Batch size for pagination
- `cursor` (int, optional): Cursor for pagination
- Returns: API response as a dictionary with statistics

##### get_form_answer(repeated_id, answer_ids)

Get form answers.

- `repeated_id` (str): Form cycle ID
- `answer_ids` (list): List of answer IDs to fetch
- Returns: API response as a dictionary with answers

### WeDocAPI

The WeChat Work Document API client for managing documents, spreadsheets, smart sheets, and forms.

#### Constructor

```python
WeDocAPI(access_token)
```

- `access_token` (str): The access token for WeChat Work API authentication

#### Methods

##### new_document(doc_type, doc_name, spaceid=None, fatherid=None, admin_users=None)

Create a new document, spreadsheet, or smart sheet.

- `doc_type` (int): Document type (3: document, 4: spreadsheet, 10: smart sheet)
- `doc_name` (str): Document name (max 255 characters)
- `spaceid` (str, optional): Space ID (if specified, `fatherid` must also be specified)
- `fatherid` (str, optional): Parent directory file ID, use spaceid when in root directory
- `admin_users` (List[str], optional): List of user IDs to be document administrators
- Returns: API response as a dictionary with docid and URL for the new document

##### rename_document(new_name, docid=None, formid=None)

Rename an existing document, spreadsheet, smart sheet, or form.

- `new_name` (str): New name for the document (max 255 characters)
- `docid` (str, optional): Document ID (only one of docid or formid should be provided)
- `formid` (str, optional): Form ID (only one of docid or formid should be provided)
- Returns: API response as a dictionary

##### delete_document(docid=None, formid=None)

Delete an existing document, spreadsheet, smart sheet, or form.

- `docid` (str, optional): Document ID (only one of docid or formid should be provided)
- `formid` (str, optional): Form ID (only one of docid or formid should be provided)
- Returns: API response as a dictionary

##### get_document_base_info(docid)

Get basic information about a document, spreadsheet, or smart sheet.

- `docid` (str): Document ID
- Returns: API response as a dictionary containing document details (name, creation time, modification time, type)

##### share_document(docid=None, formid=None)

Get the sharing link for a document, spreadsheet, smart sheet, or form.

- `docid` (str, optional): Document ID (only one of docid or formid should be provided)
- `formid` (str, optional): Form ID (only one of docid or formid should be provided)
- Returns: API response as a dictionary with the share URL

##### edit_document_content(docid, requests, version=None)

Batch edit document content with multiple operations.

- `docid` (str): Document ID
- `requests` (List[Dict]): List of edit operations to perform
- `version` (int, optional): Document version to edit
- Returns: API response as a dictionary

##### get_document_data(docid)

Get content data from a document.

- `docid` (str): Document ID
- Returns: API response as a dictionary containing document content and version

##### add_smartsheet(docid, title=None, index=None)

Add a new sheet to a smart sheet.

- `docid` (str): Document ID of the smart sheet
- `title` (str, optional): Title for the new sheet
- `index` (int, optional): Index position for the new sheet
- Returns: API response as a dictionary with sheet details

##### add_view(docid, sheet_id, view_title, view_type, property_gantt=None, property_calendar=None)

Add a new view to a smart sheet.

- `docid` (str): Document ID of the smart sheet
- `sheet_id` (str): Sheet ID where the view will be added
- `view_title` (str): Title for the new view
- `view_type` (str): Type of view ("VIEW_TYPE_GRID", "VIEW_TYPE_KANBAN", etc.)
- `property_gantt` (dict, optional): Properties for Gantt view
- `property_calendar` (dict, optional): Properties for calendar view
- Returns: API response as a dictionary with view details

##### add_fields(docid, sheet_id, fields)

Add new fields to a smart sheet.

- `docid` (str): Document ID of the smart sheet
- `sheet_id` (str): Sheet ID where fields will be added
- `fields` (List[Dict]): List of field definitions to add
- Returns: API response as a dictionary with field details

##### add_records(docid, sheet_id, records, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE")

Add new records to a smart sheet.

- `docid` (str): Document ID of the smart sheet
- `sheet_id` (str): Sheet ID where records will be added
- `records` (List[Dict]): List of record data to add
- `key_type` (str): Type of key used for field identification
- Returns: API response as a dictionary with record details

##### get_form_info(formid)

Get information about a form.

- `formid` (str): Form ID
- Returns: API response as a dictionary with form details

##### create_form(form_title, form_desc=None, form_header=None, form_question=None, form_setting=None, spaceid=None, fatherid=None)

Create a new form.

- `form_title` (str): Title of the form
- `form_desc` (str, optional): Description of the form
- `form_header` (str, optional): Background image URL for the form header
- `form_question` (dict, optional): Questions and settings for the form
- `form_setting` (dict, optional): Settings for the form behavior
- `spaceid` (str, optional): Space ID for the form
- `fatherid` (str, optional): Parent directory file ID
- Returns: API response as a dictionary with form ID

## Examples

More examples can be found in the `examples/` directory:

- `basic_usage.py`: Basic usage examples
- `advanced_usage.py`: Advanced usage with environment variables
- `modular_demo.py`: Demonstration of the static modular architecture
- `wedoc_examples.py`: Examples for working with WeChat Work documents (wedoc)

### Document Management Examples

Here's a quick example of how to use the WeChatWorkClient for document management:

```python
from weixin_work_reborn import WeChatWorkClient, Config

# Initialize the client with configuration
config = Config()  # Loads from .env file or environment variables
client = WeChatWorkClient(config=config)

# Create a new document
result = client.new_document(
    doc_type=3,  # 3 for document, 4 for spreadsheet, 10 for smart sheet
    doc_name="My New Document"
)
print(f"Created document with ID: {result.get('docid')}")

# Get document information
if 'docid' in result:
    doc_info = client.get_document_base_info(result['docid'])
    print(f"Document info: {doc_info}")

# Rename the document
if 'docid' in result:
    rename_result = client.rename_document(
        docid=result['docid'],
        new_name="Renamed Document"
    )
    print(f"Rename result: {rename_result}")

# Share the document
if 'docid' in result:
    share_result = client.share_document(docid=result['docid'])
    print(f"Share URL: {share_result.get('share_url')}")
```

## Development

### Setup

1. Clone the repository
2. Install dependencies with `uv` (or `pip`):
   ```bash
   # Using uv (recommended)
   uv venv
   uv pip install -e ".[dev]"
   ```

### Running Tests

```bash
python -m pytest tests/
```

### Code Formatting

```bash
black .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues, please file a bug report on the [GitHub issues page](https://github.com/liudonghua123/weixin-work/issues).

## About WeChat Work API

For more information about the WeChat Work API, visit the [official documentation](https://developer.work.weixin.qq.com/document/path/90197).