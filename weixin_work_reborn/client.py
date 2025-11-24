"""
WeChat Work API Client
Implements the core functionality for interacting with WeChat Work API.
This is the main entry point that uses the modular architecture.
"""

import logging
from typing import Dict, Any, Optional
from .config import Config
from .common import AccessTokenManager
from .user import UserManager
from .wedoc import WeDocAPI


class WeChatWorkException(Exception):
    """Base exception for WeChat Work API errors."""
    pass


class WeChatWorkClient:
    """
    WeChat Work API Client
    Provides methods to interact with the WeChat Work API using a modular architecture.
    """
    
    def __init__(self, 
                 config: Optional[Config] = None,
                 config_file: Optional[str] = None,
                 token_cache_size: int = 100,
                 token_cache_ttl: int = 7000):  # Token expires in 7200 seconds, so cache for 7000
        """
        Initialize the WeChat Work client.
        
        Args:
            config: Config object with API settings (optional)
            config_file: Path to .env file (optional)
            token_cache_size: Size of the token cache
            token_cache_ttl: Time-to-live for cached tokens in seconds
        """
        # Initialize configuration
        if config:
            self.config = config
        else:
            self.config = Config(config_file)
        
        # Initialize the access token manager
        self.token_manager = AccessTokenManager(
            base_url=self.config.base_url,
            corp_id=self.config.corp_id,
            app_secret=self.config.app_secret,
            contacts_sync_secret=self.config.contacts_sync_secret,
            doc_secret=self.config.doc_secret,
            token_cache_size=token_cache_size,
            token_cache_ttl=token_cache_ttl
        )
        
        # Initialize user manager
        self.user_manager = UserManager(
            base_url=self.config.base_url,
            access_token_manager=self.token_manager
        )

        # Initialize wedoc API (will be created when needed to avoid token issues)
        self._wedoc_api = None

        self.logger = logging.getLogger(__name__)

    @property
    def wedoc_api(self):
        """
        Lazy initialization of WeDocAPI to ensure token is fresh when needed.
        """
        if self._wedoc_api is None:
            access_token = self.token_manager.get_doc_access_token()
            self._wedoc_api = WeDocAPI(access_token=access_token)
        return self._wedoc_api
    
    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Get user information by user ID.
        
        Args:
            user_id: The user ID
            
        Returns:
            User information as a dictionary
        """
        return self.user_manager.get_user(user_id)
    
    def update_user(self, 
                   userid: str,  # Required parameter
                   name: Optional[str] = None, 
                   alias: Optional[str] = None,
                   mobile: Optional[str] = None,
                   department: Optional[list] = None,
                   order: Optional[list] = None,
                   position: Optional[str] = None,
                   gender: Optional[str] = None,
                   email: Optional[str] = None,
                   biz_mail: Optional[str] = None,
                   biz_mail_alias: Optional[Dict[str, Any]] = None,
                   telephone: Optional[str] = None,
                   is_leader_in_dept: Optional[list] = None,
                   direct_leader: Optional[list] = None,
                   avatar_mediaid: Optional[str] = None,
                   enable: Optional[int] = None,
                   extattr: Optional[Dict[str, Any]] = None,
                   external_profile: Optional[Dict[str, Any]] = None,
                   external_position: Optional[str] = None,
                   nickname: Optional[str] = None,
                   address: Optional[str] = None,
                   main_department: Optional[int] = None) -> Dict[str, Any]:
        """
        Update user information.
        
        Args:
            userid: Required. User ID. Corresponds to the account in the management console, must be unique within the enterprise. Case-insensitive, 1-64 bytes long
            name: Optional. Member name, 1-64 UTF8 characters
            alias: Optional. Alias, 1-64 UTF8 characters
            mobile: Optional. Mobile number. Must be unique within the enterprise
            department: Optional. List of department IDs the member belongs to, up to 100
            order: Optional. Sorting value within the department, defaults to 0. Effective when department is provided. Number must match department, larger number means higher priority. Valid range is [0, 2^32)
            position: Optional. Position information, 0-128 UTF8 characters
            gender: Optional. Gender. 1 for male, 2 for female
            email: Optional. Email address. 6-64 bytes and valid email format, must be unique within enterprise
            biz_mail: Optional. If the enterprise has activated Tencent Corporate Mail (Enterprise WeChat Mail), setting this creates a corporate email account. 6-63 bytes and valid corporate email format, must be unique within enterprise
            biz_mail_alias: Optional. Corporate email alias. 6-63 bytes and valid corporate email format, must be unique within enterprise, up to 5 aliases can be set. Updates are overwritten. Passing empty structure or empty array clears current corporate email aliases
            telephone: Optional. Landline. Composed of 1-32 digits, "-", "+", or "," 
            is_leader_in_dept: Optional. Department head field, count must match department, indicates whether the member is a head in the department. 0-False, 1-True
            direct_leader: Optional. Direct supervisor, can set members within the enterprise as direct supervisor, max 1 can be set
            avatar_mediaid: Optional. Member's avatar mediaid, obtained through media management API upload
            enable: Optional. Enable/disable member. 1 for enabled, 0 for disabled
            extattr: Optional. Extended attributes. Fields need to be added in WEB management first
            external_profile: Optional. Member's external attributes
            external_position: Optional. External position. If set, used as the displayed position, otherwise use position. Up to 12 Chinese characters
            nickname: Optional. Video account name (after setting, the member will display this video account externally). Must be selected from the video account bound to the enterprise WeChat, accessible in the "My Enterprise" page
            address: Optional. Address. Max 128 characters
            main_department: Optional. Main department
            
        Returns:
            API response as a dictionary
        """
        return self.user_manager.update_user(
            userid=userid,
            name=name,
            alias=alias,
            mobile=mobile,
            department=department,
            order=order,
            position=position,
            gender=gender,
            email=email,
            biz_mail=biz_mail,
            biz_mail_alias=biz_mail_alias,
            telephone=telephone,
            is_leader_in_dept=is_leader_in_dept,
            direct_leader=direct_leader,
            avatar_mediaid=avatar_mediaid,
            enable=enable,
            extattr=extattr,
            external_profile=external_profile,
            external_position=external_position,
            nickname=nickname,
            address=address,
            main_department=main_department
        )
    
    def mobile_to_userid(self, mobile: str) -> Dict[str, Any]:
        """
        Convert mobile number to user ID.
        
        Args:
            mobile: The mobile number
            
        Returns:
            API response containing user ID as a dictionary
        """
        return self.user_manager.mobile_to_userid(mobile)

    # ==================== Document Management (WeDoc) Wrappers ====================

    def new_document(
        self,
        doc_type: int,
        doc_name: str,
        spaceid: Optional[str] = None,
        fatherid: Optional[str] = None,
        admin_users: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Create a new document, spreadsheet, or smart sheet.

        Args:
            doc_type: Document type, 3: document 4: spreadsheet 10: smart sheet
            doc_name: Document name (max 255 characters, will be truncated if exceeded)
            spaceid: Space ID. If specified, `fatherid` must also be specified
            fatherid: Parent directory file ID, use spaceid when in root directory
            admin_users: List of user IDs to be document administrators

        Returns:
            API response as a dictionary with docid and URL for the new document
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "url": "URL",      # Access link for the new document
                "docid": "DOCID"   # Document ID, only returned on creation, should be saved
            }
        """
        return self.wedoc_api.new_document(
            doc_type=doc_type,
            doc_name=doc_name,
            spaceid=spaceid,
            fatherid=fatherid,
            admin_users=admin_users
        )

    def rename_document(
        self,
        new_name: str,
        docid: Optional[str] = None,
        formid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Rename an existing document, spreadsheet, smart sheet, or form.

        Args:
            new_name: New name for the document (max 255 characters, English=1, Chinese=2, truncated if exceeded)
            docid: Document docid (only one of docid or formid should be provided), only app-created docs can be modified
            formid: Form ID (only one of docid or formid should be provided), only app-created forms can be modified

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }

        Raises:
            ValueError: When both docid and formid are None
        """
        return self.wedoc_api.rename_document(
            new_name=new_name,
            docid=docid,
            formid=formid
        )

    def delete_document(
        self,
        docid: Optional[str] = None,
        formid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Delete an existing document, spreadsheet, smart sheet, or form.

        Args:
            docid: Document docid (only one of docid or formid should be provided), only app-created docs can be deleted
            formid: Form ID (only one of docid or formid should be provided), only app-created forms can be deleted

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }

        Raises:
            ValueError: When both docid and formid are None
        """
        return self.wedoc_api.delete_document(
            docid=docid,
            formid=formid
        )

    def get_document_base_info(self, docid: str) -> Dict[str, Any]:
        """
        Get basic information about a document, spreadsheet, smart sheet, or form.

        Args:
            docid: Document docid

        Returns:
            API response as a dictionary containing document details
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "doc_base_info": {
                    "docid": "DOCID",      # Document docid
                    "doc_name": "DOC_NAME",# Document name
                    "create_time": 1717071093,  # Creation time
                    "modify_time": 1717071093,  # Last modification time
                    "doc_type": 3           # 3: document 4: spreadsheet 10: smart sheet
                }
            }
        """
        return self.wedoc_api.get_document_base_info(docid=docid)

    def share_document(
        self,
        docid: Optional[str] = None,
        formid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get the sharing link for a document, spreadsheet, smart sheet, or form.

        Args:
            docid: Document ID (only one of docid or formid should be provided)
            formid: Form ID (only one of docid or formid should be provided)

        Returns:
            API response as a dictionary with the share URL
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "share_url": "URL1"        # Document sharing link
            }

        Raises:
            ValueError: When both docid and formid are None
        """
        return self.wedoc_api.share_document(
            docid=docid,
            formid=formid
        )

    def edit_document_content(
        self,
        docid: str,
        requests: list,
        version: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Batch edit document content with multiple operations.

        Note:
        1. In batch update requests, if one operation fails, all updates are ineffective.
        2. Maximum 30 batch update operations per request.

        Args:
            docid: Document ID
            requests: List of update operations, supports:
                - replace_text: Replace text content at specified location
                - insert_text: Insert text content at specified location
                - delete_content: Delete content at specified location
                - insert_image: Insert image at specified location
                - insert_page_break: Insert page break at specified location
                - insert_table: Insert table at specified location
                - insert_paragraph: Insert paragraph at specified location
                - update_text_property: Update text properties at specified location
            version: Document version to edit, obtained from get document content API.
                    Document version updates after each operation. Difference between
                    target version and latest version cannot exceed 100.

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.edit_document_content(
            docid=docid,
            requests=requests,
            version=version
        )

    def get_document_data(self, docid: str) -> Dict[str, Any]:
        """
        Get content data from a document.

        Args:
            docid: Document ID

        Returns:
            API response as a dictionary containing document content and version
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "version": 10,     # Document version
                "document": {...}  # Document content root node
            }
        """
        return self.wedoc_api.get_document_data(docid=docid)

    def edit_spreadsheet_content(self, docid: str, requests: list) -> Dict[str, Any]:
        """
        Edit spreadsheet content with multiple operations.

        Note:
        1. Operations execute sequentially until completion or one fails.
        2. Each operation is validated before execution.
        3. Maximum 5 operations per batch request.

        Args:
            docid: Document ID
            requests: List of update operations, supports:
                - add_sheet_request: Add worksheet
                - delete_sheet_request: Delete worksheet
                - update_range_request: Update cell range content
                - delete_dimension_request: Delete continuous rows/columns

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "data": {
                    "responses": [        # Results list
                        {
                            "add_sheet_response": {...},         # Add worksheet response
                            "update_range_response": {...},      # Update cell range response
                            "delete_dimension_response": {...},  # Delete rows/columns response
                            "delete_sheet_response": {...}       # Delete worksheet response
                        }
                    ]
                }
            }
        """
        return self.wedoc_api.edit_spreadsheet_content(docid=docid, requests=requests)

    def get_sheet_properties(self, docid: str) -> Dict[str, Any]:
        """
        Get sheet row/column information for spreadsheets.

        Args:
            docid: Online spreadsheet docid

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "properties": [            # Worksheet properties list
                    {
                        "sheet_id": "ABCDE",      # Worksheet ID (unique identifier)
                        "title": "XXXXXX",        # Worksheet name
                        "row_count": 100,         # Total rows
                        "column_count": 100       # Total columns
                    }
                ]
            }
        """
        return self.wedoc_api.get_sheet_properties(docid=docid)

    def get_sheet_range_data(
        self,
        docid: str,
        sheet_id: str,
        range_str: str
    ) -> Dict[str, Any]:
        """
        Get spreadsheet data for a specified range.

        Single query range limits:
        1. Row count <=1000
        2. Column count <=200
        3. Total cells <=10000

        Args:
            docid: Online spreadsheet identifier
            sheet_id: Worksheet ID (unique identifier)
            range_str: Query range in A1 notation
                      A1 notation is common for table data reference, e.g.:
                      - "A1:A1" represents single cell A1
                      - "A1:B5" from cell A1 to cell B5 region
                      - "A1:D1" 4 cells in first row: A1, B1, C1, D1
                      - "A1:A3" 3 cells in first column: A1, A2, A3
                      - "B5:A1" invalid notation, B5 is bottom-right of A1

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "data": {
                    "result": {            # Table data
                        "start_row": 1,     # Start row number (0-based)
                        "start_column": 1,  # Start column number (0-based)
                        "rows": [          # Row data
                            {
                                "values": [ # Cell data
                                    {
                                        "cell_value": {...},      # Cell data content
                                        "cell_format": {...}      # Cell style information
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        """
        return self.wedoc_api.get_sheet_range_data(
            docid=docid,
            sheet_id=sheet_id,
            range_str=range_str
        )

    def add_smartsheet(
        self,
        docid: str,
        title: Optional[str] = None,
        index: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Add a smart sheet to a table.

        This API adds a smart sheet at a specific location. The smart sheet has no views,
        records, or fields initially. Use API to add views, records, and fields to it.

        Args:
            docid: Document ID
            title: Smart sheet title
            index: Smart sheet index

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "properties": {
                    "title": "Smart Sheet",# Smart sheet title
                    "index": 3,            # Smart sheet index
                    "sheet_id": "123abc"   # Smart sheet ID, 6-digit random ID generated on creation
                }
            }
        """
        return self.wedoc_api.add_smartsheet(
            docid=docid,
            title=title,
            index=index
        )

    def delete_smartsheet(self, docid: str, sheet_id: str) -> Dict[str, Any]:
        """
        Delete a smart sheet from an online table.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID to delete

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.delete_smartsheet(
            docid=docid,
            sheet_id=sheet_id
        )

    def update_smartsheet(
        self,
        docid: str,
        sheet_id: str,
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update a smart sheet title.

        Args:
            docid: Document ID
            sheet_id: Sheet ID to update
            title: New sheet title

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.update_smartsheet(
            docid=docid,
            sheet_id=sheet_id,
            title=title
        )

    def query_smartsheet(
        self,
        docid: str,
        sheet_id: Optional[str] = None,
        need_all_type_sheet: bool = False
    ) -> Dict[str, Any]:
        """
        Query smart sheet information.

        Args:
            docid: Document ID
            sheet_id: Specific sheet ID to query
            need_all_type_sheet: Get all sheet types. True to include dashboards and info pages

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "sheet_list": [            # Smart sheet info list
                    {
                        "sheet_id": "123abc",      # Sheet ID
                        "title": "XXXX",           # Sheet name
                        "is_visible": True,        # Sheet visibility
                        "type": "smartsheet"       # Sheet type: "dashboard", "external", "smartsheet"
                    }
                ]
            }
        """
        return self.wedoc_api.query_smartsheet(
            docid=docid,
            sheet_id=sheet_id,
            need_all_type_sheet=need_all_type_sheet
        )

    def add_view(
        self,
        docid: str,
        sheet_id: str,
        view_title: str,
        view_type: str,
        property_gantt: Optional[Dict[str, Any]] = None,
        property_calendar: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Add a view to a smart sheet.

        Single table allows up to 200 views.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            view_title: View title
            view_type: View type:
                      - "VIEW_TYPE_GRID": Table view
                      - "VIEW_TYPE_KANBAN": Kanban view
                      - "VIEW_TYPE_GALLERY": Gallery view
                      - "VIEW_TYPE_GANTT": Gantt view
                      - "VIEW_TYPE_CALENDAR": Calendar view
            property_gantt: Gantt view properties, required when adding Gantt
                           - start_date_field_id: Start date field ID, only DATE_TIME field types
                           - end_date_field_id: End date field ID, only DATE_TIME field types
            property_calendar: Calendar view properties, required when adding calendar
                             - start_date_field_id: Start date field ID, only DATE_TIME field types
                             - end_date_field_id: End date field ID, only DATE_TIME field types

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "view": {
                    "view_id": "vFYZUS",   # View ID
                    "view_title": "XXX",   # View title
                    "view_type": "VIEW_TYPE_GRID"  # View type
                }
            }
        """
        return self.wedoc_api.add_view(
            docid=docid,
            sheet_id=sheet_id,
            view_title=view_title,
            view_type=view_type,
            property_gantt=property_gantt,
            property_calendar=property_calendar
        )

    def delete_views(self, docid: str, sheet_id: str, view_ids: list) -> Dict[str, Any]:
        """
        Delete views from a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            view_ids: List of view IDs to delete

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.delete_views(
            docid=docid,
            sheet_id=sheet_id,
            view_ids=view_ids
        )

    def update_view(
        self,
        docid: str,
        sheet_id: str,
        view_id: str,
        view_title: Optional[str] = None,
        property_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Update a view in a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            view_id: View ID to update
            view_title: New view title
            property_data: View sorting/filtering/grouping/coloring settings, includes:
                          - auto_sort: Auto re-sort after record changes
                          - sort_spec: Sort settings
                          - group_spec: Group settings
                          - filter_spec: Filter settings
                          - is_field_stat_enabled: Enable data statistics
                          - field_visibility: Field visibility mapping
                          - frozen_field_count: Number of frozen columns
                          - color_config: Coloring settings

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "view": {          # Updated view content
                    # View info with view_id, view_title, view_type, etc.
                }
            }
        """
        return self.wedoc_api.update_view(
            docid=docid,
            sheet_id=sheet_id,
            view_id=view_id,
            view_title=view_title,
            property_data=property_data
        )

    def query_views(
        self,
        docid: str,
        sheet_id: str,
        view_ids: Optional[list] = None,
        offset: int = 0,
        limit: int = 0
    ) -> Dict[str, Any]:
        """
        Query views in a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            view_ids: List of view IDs to query
            offset: Offset, initial value 0
            limit: Page size, when not specified or 0:
                  If total > 1000, returns 1000 views
                  If total < 1000, returns all views
                  Max value 1000

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "total": 2,                # Total matching views
                "has_more": True,          # Has more data
                "next": 1,                 # Next offset
                "views": [                 # View data list
                    {
                        "view_id": "vabcde",    # View ID
                        "view_title": "Default View",# View title
                        "view_type": "VIEW_TYPE_GRID"  # View type
                    }
                ]
            }
        """
        return self.wedoc_api.query_views(
            docid=docid,
            sheet_id=sheet_id,
            view_ids=view_ids,
            offset=offset,
            limit=limit
        )

    def add_fields(
        self,
        docid: str,
        sheet_id: str,
        fields: list
    ) -> Dict[str, Any]:
        """
        Add fields to a smart sheet.

        Single table allows up to 150 fields.

        Args:
            docid: Document ID
            sheet_id: Table ID
            fields: Field details list, each includes:
                   - field_title: Field title
                   - field_type: Field type, e.g. FIELD_TYPE_TEXT, FIELD_TYPE_NUMBER
                   - property_XXX: Field properties depending on type

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "fields": [                # Field details list
                    {
                        "field_id": "FIELDID",    # Field ID
                        "field_title": "TITLE",   # Field title
                        "field_type": "FIELD_TYPE_TEXT"  # Field type
                    }
                ]
            }
        """
        return self.wedoc_api.add_fields(
            docid=docid,
            sheet_id=sheet_id,
            fields=fields
        )

    def delete_fields(self, docid: str, sheet_id: str, field_ids: list) -> Dict[str, Any]:
        """
        Delete fields from a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Table ID
            field_ids: List of field IDs to delete

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.delete_fields(
            docid=docid,
            sheet_id=sheet_id,
            field_ids=field_ids
        )

    def update_fields(
        self,
        docid: str,
        sheet_id: str,
        fields: list
    ) -> Dict[str, Any]:
        """
        Update fields in a smart sheet.

        Note: This API can only update field name and properties, not field type.

        Args:
            docid: Document ID
            sheet_id: Table ID
            fields: Field details list, each includes:
                   - field_id: Field ID, required for update, but cannot be changed
                   - field_title: Field title to update
                   - field_type: Field type, must be original type
                   - property_XXX: Field properties depending on type

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "fields": [                # Field details list
                    {
                        "field_id": "FIELDID",    # Field ID
                        "field_title": "TITLE",   # Field title
                        "field_type": "FIELD_TYPE_TEXT"  # Field type
                    }
                ]
            }
        """
        return self.wedoc_api.update_fields(
            docid=docid,
            sheet_id=sheet_id,
            fields=fields
        )

    def query_fields(
        self,
        docid: str,
        sheet_id: str,
        view_id: Optional[str] = None,
        field_ids: Optional[list] = None,
        field_titles: Optional[list] = None,
        offset: int = 0,
        limit: int = 0
    ) -> Dict[str, Any]:
        """
        Query fields in a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Table ID
            view_id: View ID
            field_ids: List of field IDs to query
            field_titles: List of field titles to query
            offset: Offset, initial value 0
            limit: Page size, when not specified or 0:
                  If total > 1000, returns 1000 fields
                  If total < 1000, returns all fields
                  Max value 1000

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "total": 1,                # Field count
                "fields": [                # Field details list
                    {
                        "field_id": "ID1",        # Field ID
                        "field_title": "TITLE1",  # Field title
                        "field_type": "FIELD_TYPE_TEXT"  # Field type
                    }
                ]
            }
        """
        return self.wedoc_api.query_fields(
            docid=docid,
            sheet_id=sheet_id,
            view_id=view_id,
            field_ids=field_ids,
            field_titles=field_titles,
            offset=offset,
            limit=limit
        )

    def add_records(
        self,
        docid: str,
        sheet_id: str,
        records: list,
        key_type: str = "CELL_VALUE_KEY_TYPE_FIELD_TITLE"
    ) -> Dict[str, Any]:
        """
        Add records to a smart sheet.

        Single table allows up to 100000 records, 15000000 cells.
        Note: Cannot add records to creation time, last edit time, creator, and last editor fields.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            records: List of record content to add
            key_type: Cell key type in returned records, default to title
                     - "CELL_VALUE_KEY_TYPE_FIELD_TITLE": Key as field title
                     - "CELL_VALUE_KEY_TYPE_FIELD_ID": Key as field ID

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "records": [       # Successfully added records content list
                    # Record details
                ]
            }
        """
        return self.wedoc_api.add_records(
            docid=docid,
            sheet_id=sheet_id,
            records=records,
            key_type=key_type
        )

    def delete_records(
        self,
        docid: str,
        sheet_id: str,
        record_ids: list
    ) -> Dict[str, Any]:
        """
        Delete records from a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            record_ids: List of record IDs to delete

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.delete_records(
            docid=docid,
            sheet_id=sheet_id,
            record_ids=record_ids
        )

    def update_records(
        self,
        docid: str,
        sheet_id: str,
        records: list,
        key_type: str = "CELL_VALUE_KEY_TYPE_FIELD_TITLE"
    ) -> Dict[str, Any]:
        """
        Update records in a smart sheet.

        Note: Cannot update creation time, last edit time, creator, and last editor fields.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            records: List of records to update
            key_type: Cell key type in returned records
                     - "CELL_VALUE_KEY_TYPE_FIELD_TITLE": Key as field title
                     - "CELL_VALUE_KEY_TYPE_FIELD_ID": Key as field ID

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "records": [       # Successfully updated records content list
                    # Record details
                ]
            }
        """
        return self.wedoc_api.update_records(
            docid=docid,
            sheet_id=sheet_id,
            records=records,
            key_type=key_type
        )

    def query_records(
        self,
        docid: str,
        sheet_id: str,
        view_id: Optional[str] = None,
        record_ids: Optional[list] = None,
        key_type: str = "CELL_VALUE_KEY_TYPE_FIELD_TITLE",
        field_titles: Optional[list] = None,
        field_ids: Optional[list] = None,
        sort: Optional[list] = None,
        offset: int = 0,
        limit: int = 0,
        ver: Optional[int] = None,
        filter_spec: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Query records in a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Smartsheet sheet ID
            view_id: View ID
            record_ids: List of record IDs to query
            key_type: Cell key type in returned records
                     - "CELL_VALUE_KEY_TYPE_FIELD_TITLE": Key as field title
                     - "CELL_VALUE_KEY_TYPE_FIELD_ID": Key as field ID
            field_titles: Return specified columns by field titles
            field_ids: Return specified columns by field IDs
            sort: Sort returned records
            offset: Offset, initial value 0
            limit: Page size, when not specified or 0:
                  If total > 1000, returns 1000 records
                  If total < 1000, returns all records
                  Max value 1000
            ver: Version number
            filter_spec: Filter settings, cannot be used with sort

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "total": 10,       # Total matching records
                "has_more": False, # Has more data
                "next": 0,         # Next offset
                "records": [       # Query records content list
                    {
                        "record_id": "r5ud8u",      # Record ID
                        "create_time": "1715846245084", # Creation time
                        "update_time": "1715846248810", # Update time
                        "values": {},               # Record content
                        "creator_name": "NAME",     # Creator name
                        "updater_name": "NAME"      # Last editor name
                    }
                ],
                "ver": 160         # Version number
            }
        """
        return self.wedoc_api.query_records(
            docid=docid,
            sheet_id=sheet_id,
            view_id=view_id,
            record_ids=record_ids,
            key_type=key_type,
            field_titles=field_titles,
            field_ids=field_ids,
            sort=sort,
            offset=offset,
            limit=limit,
            ver=ver,
            filter_spec=filter_spec
        )

    def add_field_group(
        self,
        docid: str,
        sheet_id: str,
        name: str,
        children: list
    ) -> Dict[str, Any]:
        """
        Add a field group to a smart sheet.

        Single table allows up to 150 groups.
        Each group allows up to 150 fields. Fields can only exist in one group.

        Args:
            docid: Document ID
            sheet_id: Table ID
            name: Group name, cannot duplicate existing names
            children: Group content list, each includes:
                     - field_id: Field ID

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "field_group": {
                    "field_group_id": "FIELD_GROUP_ID", # Group ID
                    "name": "Group Name",              # Group name
                    "children": [                      # Group content list
                        {
                            "field_id": "FIELD_ID"    # Field ID
                        }
                    ]
                }
            }
        """
        return self.wedoc_api.add_field_group(
            docid=docid,
            sheet_id=sheet_id,
            name=name,
            children=children
        )

    def delete_field_groups(
        self,
        docid: str,
        sheet_id: str,
        field_group_ids: list
    ) -> Dict[str, Any]:
        """
        Delete field groups from a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Sheet ID
            field_group_ids: List of group IDs to delete

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.delete_field_groups(
            docid=docid,
            sheet_id=sheet_id,
            field_group_ids=field_group_ids
        )

    def update_field_group(
        self,
        docid: str,
        sheet_id: str,
        field_group_id: str,
        name: Optional[str] = None,
        children: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Update a field group in a smart sheet.

        Each group allows up to 150 fields. Fields can only exist in one group.

        Args:
            docid: Document ID
            sheet_id: Table ID
            field_group_id: Group ID to update
            name: New group name, cannot duplicate existing names
            children: New group content list, each includes:
                     - field_id: Field ID

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "field_group": {
                    "field_group_id": "FIELD_GROUP_ID", # Group ID
                    "name": "Group Name",              # Group name
                    "children": [                      # Group content list
                        {
                            "field_id": "FIELD_ID"    # Field ID
                        }
                    ]
                }
            }
        """
        return self.wedoc_api.update_field_group(
            docid=docid,
            sheet_id=sheet_id,
            field_group_id=field_group_id,
            name=name,
            children=children
        )

    def get_field_groups(
        self,
        docid: str,
        sheet_id: str,
        offset: int = 0,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get field groups from a smart sheet.

        Args:
            docid: Document ID
            sheet_id: Table ID
            offset: Offset, initial value 0
            limit: Page size

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "total": 1,                # Group count
                "has_more": False,         # Has more data
                "next": 0,                 # Next offset
                "field_groups": [          # Group list
                    {
                        "field_group_id": "FIELD_GROUP_ID", # Group ID
                        "name": "Group Name",              # Group name
                        "children": [                      # Group content list
                            {
                                "field_id": "FIELD_ID"    # Field ID
                            }
                        ]
                    }
                ]
            }
        """
        return self.wedoc_api.get_field_groups(
            docid=docid,
            sheet_id=sheet_id,
            offset=offset,
            limit=limit
        )

    def get_document_auth(self, docid: str) -> Dict[str, Any]:
        """
        Get document permission information.

        Args:
            docid: Document ID

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "access_rule": {   # Document access rules
                    "enable_corp_internal": true,     # Allow internal members to browse
                    "corp_internal_auth": 1,          # Internal member permission type
                    "enable_corp_external": true,     # Allow external members to browse
                    "corp_external_auth": 1,          # External member permission type
                    "corp_internal_approve_only_by_admin": true,  # Internal approval by admin only
                    "corp_external_approve_only_by_admin": true,  # External approval by admin only
                    "ban_share_external": false       # Ban sharing to external
                },
                "secure_setting": {  # Document security settings
                    "enable_readonly_copy": false,    # Allow readonly members to copy/export
                    "watermark": {   # Watermark settings
                        "margin_type": 2,             # Density: 1:sparse 2:dense
                        "show_visitor_name": false,   # Show visitor name in watermark
                        "show_text": false,           # Show text watermark
                        "text": ""                    # Watermark text
                    },
                    "enable_readonly_comment": false  # Allow readonly members to comment
                },
                "doc_member_list": [  # Document member range and permissions
                    {
                        "type": 1,                    # Member type: 1:user
                        "userid": "USERID1",          # User ID
                        "auth": 7                     # Member permission: 1:read-only 2:read-write 7:admin
                    }
                ],
                "co_auth_list": [    # Specific department access list
                    {
                        "type": 2,                    # Type: 2:department
                        "departmentid": 1,            # Department ID
                        "auth": 1                     # Permission type: 1:read-only, 2:read-write
                    }
                ]
            }
        """
        return self.wedoc_api.get_document_auth(docid=docid)

    def modify_document_join_rule(
        self,
        docid: str,
        enable_corp_internal: Optional[bool] = None,
        corp_internal_auth: Optional[int] = None,
        enable_corp_external: Optional[bool] = None,
        corp_external_auth: Optional[int] = None,
        corp_internal_approve_only_by_admin: Optional[bool] = None,
        corp_external_approve_only_by_admin: Optional[bool] = None,
        ban_share_external: Optional[bool] = None,
        update_co_auth_list: Optional[bool] = None,
        co_auth_list: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Modify document access rules.

        Args:
            docid: Document ID to operate
            enable_corp_internal: Allow internal members to browse
            corp_internal_auth: Internal member permission type 1:read-only 2:read-write
            enable_corp_external: Allow external members to browse
            corp_external_auth: External member permission type 1:read-only 2:read-write
            corp_internal_approve_only_by_admin: Internal members need admin approval
            corp_external_approve_only_by_admin: External members need admin approval
            ban_share_external: Ban sharing to external
            update_co_auth_list: Update specific department access list
            co_auth_list: Department access list to update

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.modify_document_join_rule(
            docid=docid,
            enable_corp_internal=enable_corp_internal,
            corp_internal_auth=corp_internal_auth,
            enable_corp_external=enable_corp_external,
            corp_external_auth=corp_external_auth,
            corp_internal_approve_only_by_admin=corp_internal_approve_only_by_admin,
            corp_external_approve_only_by_admin=corp_external_approve_only_by_admin,
            ban_share_external=ban_share_external,
            update_co_auth_list=update_co_auth_list,
            co_auth_list=co_auth_list
        )

    def modify_document_member(
        self,
        docid: str,
        update_file_member_list: Optional[list] = None,
        del_file_member_list: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Modify document member range and permissions.

        Args:
            docid: Document ID to operate
            update_file_member_list: Update member range list, max batch size 100
                                   Each includes: type, auth, userid/tmp_external_userid
            del_file_member_list: Delete member range list, max batch size 100
                                Each includes: type, userid/tmp_external_userid

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.modify_document_member(
            docid=docid,
            update_file_member_list=update_file_member_list,
            del_file_member_list=del_file_member_list
        )

    def modify_document_safety_setting(
        self,
        docid: str,
        enable_readonly_copy: Optional[bool] = None,
        watermark: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Modify document security settings.

        Args:
            docid: Document ID to operate
            enable_readonly_copy: Allow readonly members to copy/download
            watermark: Watermark settings, includes:
                      - margin_type: Density, 1:sparse, 2:dense
                      - show_visitor_name: Show visitor name watermark
                      - show_text: Show text watermark
                      - text: Watermark text

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.modify_document_safety_setting(
            docid=docid,
            enable_readonly_copy=enable_readonly_copy,
            watermark=watermark
        )

    def query_sheet_privilege(
        self,
        docid: str,
        type_: int,
        rule_id_list: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Query smart sheet permission details.

        Args:
            docid: Smart sheet ID
            type_: Permission rule type, 1:all members, 2:additional permissions
            rule_id_list: Rule IDs to query, required when querying additional permissions

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "rule_list": [     # Permission list
                    {
                        "rule_id": 1,               # Rule ID (when type=2)
                        "type": 1,                  # Permission rule type, 1:all members, 2:additional
                        "name": "All Members",      # Permission name, only when type=2
                        "priv_list": [             # Sheet-specific content permissions
                            {
                                "sheet_id": "q979lj",        # Sheet ID
                                "priv": 2,                  # Sheet permission: 1:all 2:edit 3:browse 4:none
                                "can_insert_record": true,  # Can insert records
                                "can_delete_record": true,  # Can delete records
                                "can_create_modify_delete_view": true,  # Can create/modify/delete views
                                "field_priv": {            # Field-specific permissions
                                    "field_range_type": 2,  # Apply to all or partial fields: 1:all 2:partial
                                    "field_rule_list": [   # Field-specific permissions
                                        {
                                            "field_id": "fsMGQS",      # Field ID
                                            "field_type": "FIELD_TYPE_TEXT",  # Field type
                                            "can_edit": false,         # Can edit
                                            "can_insert": true,        # Can insert
                                            "can_view": true           # Can view
                                        }
                                    ],
                                    "field_default_rule": {  # Default for unspecified/added fields
                                        "can_edit": false,
                                        "can_insert": false,
                                        "can_view": true
                                    }
                                },
                                "record_priv": {           # Record-specific permissions
                                    "record_range_type": 1  # Apply to records: 1:all 2:match any 3:match all
                                }
                            }
                        ]
                    }
                ]
            }
        """
        return self.wedoc_api.query_sheet_privilege(
            docid=docid,
            type_=type_,
            rule_id_list=rule_id_list
        )

    def update_sheet_privilege(
        self,
        docid: str,
        type_: int,
        rule_id: Optional[int] = None,
        name: Optional[str] = None,
        priv_list: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Update smart sheet permissions.

        Args:
            docid: Smart sheet ID
            type_: Permission rule type, 1:all members, 2:additional (only one all-members rule exists)
            rule_id: Required when type=2
            name: Permission name, only when type=2
            priv_list: Sheet-specific permissions list, each includes:
                      - sheet_id: Sheet ID
                      - priv: Sheet permission: 1:all 2:edit 3:browse 4:none
                      - can_insert_record: Can insert records
                      - can_delete_record: Can delete records
                      - can_create_modify_delete_view: Can create/modify/delete views
                      - field_priv: Field-specific permissions
                      - record_priv: Record-specific permissions
                      - clear: Clear settings and restore defaults

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.update_sheet_privilege(
            docid=docid,
            type_=type_,
            rule_id=rule_id,
            name=name,
            priv_list=priv_list
        )

    def create_rule(
        self,
        docid: str,
        name: str
    ) -> Dict[str, Any]:
        """
        Create smart sheet additional member permissions.

        Args:
            docid: Smart sheet ID
            name: Permission rule name, must be unique

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "rule_id": 1       # Member permission rule ID
            }
        """
        return self.wedoc_api.create_rule(
            docid=docid,
            name=name
        )

    def modify_rule_member(
        self,
        docid: str,
        rule_id: int,
        add_member_range: Optional[Dict[str, list]] = None,
        del_member_range: Optional[Dict[str, list]] = None
    ) -> Dict[str, Any]:
        """
        Update smart sheet additional member permissions.

        Up to 50 members can be set.

        Args:
            docid: Smart sheet ID
            rule_id: Rule ID to update
            add_member_range: Add members, includes userid_list
            del_member_range: Delete members, includes userid_list

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.modify_rule_member(
            docid=docid,
            rule_id=rule_id,
            add_member_range=add_member_range,
            del_member_range=del_member_range
        )

    def delete_rule(
        self,
        docid: str,
        rule_id_list: list
    ) -> Dict[str, Any]:
        """
        Delete smart sheet additional member permissions.

        Args:
            docid: Smart sheet ID
            rule_id_list: List of rule IDs to delete

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.delete_rule(
            docid=docid,
            rule_id_list=rule_id_list
        )

    def create_form(
        self,
        form_title: str,
        form_desc: Optional[str] = None,
        form_header: Optional[str] = None,
        form_question: Optional[Dict[str, Any]] = None,
        form_setting: Optional[Dict[str, Any]] = None,
        spaceid: Optional[str] = None,
        fatherid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a form.

        Args:
            form_title: Form title
            form_desc: Form description
            form_header: Form header background image URL
            form_question: Form question list
            form_setting: Form settings
            spaceid: Space ID
            fatherid: Parent directory file ID, use spaceid when in root

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "formid": "FORMID" # Form ID
            }
        """
        return self.wedoc_api.create_form(
            form_title=form_title,
            form_desc=form_desc,
            form_header=form_header,
            form_question=form_question,
            form_setting=form_setting,
            spaceid=spaceid,
            fatherid=fatherid
        )

    def modify_form(
        self,
        formid: str,
        oper: int,
        form_title: Optional[str] = None,
        form_desc: Optional[str] = None,
        form_header: Optional[str] = None,
        form_question: Optional[Dict[str, Any]] = None,
        form_setting: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Modify a form.

        Args:
            formid: Form ID
            oper: Operation type. 1: full modify questions; 2: full modify settings
            form_title: Form title (when oper=1)
            form_desc: Form description (when oper=1)
            form_header: Form header background image URL (when oper=1)
            form_question: Form question list (when oper=1)
            form_setting: Form settings (when oper=2)

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok"     # Error message
            }
        """
        return self.wedoc_api.modify_form(
            formid=formid,
            oper=oper,
            form_title=form_title,
            form_desc=form_desc,
            form_header=form_header,
            form_question=form_question,
            form_setting=form_setting
        )

    def get_form_info(self, formid: str) -> Dict[str, Any]:
        """
        Get form information.

        Args:
            formid: Form ID

        Returns:
            API response as a dictionary
            {
                "errcode": 0,      # Error code
                "errmsg": "ok",    # Error message
                "form_info": {     # Form information
                    "formid": "FORMID1",           # Form ID
                    "form_title": "Form Title",  # Form title
                    "form_desc": "Description",        # Form description
                    "form_header": "URL",          # Form header background image URL
                    "form_question": {            # Form question list
                        "items": [                # Question list
                            # Question details
                        ]
                    },
                    "form_setting": {             # Form settings
                        # Setting details
                    },
                    "repeated_id": [              # Form cycle IDs for answers list
                        "REPEAT_ID1"
                    ]
                }
            }
        """
        return self.wedoc_api.get_form_info(formid=formid)

    def get_form_statistic(
        self,
        repeated_id: str,
        req_type: int,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        cursor: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Form statistics query.

        Args:
            repeated_id: Form repeated_id from get_form_info response
            req_type: Request type 1: statistics only 2: submitted list 3: not submitted list
            start_time: Required for submitted list, start time (00:00:00 of the day)
            end_time: Required for submitted list, end time (23:59:59 of the day)
            limit: Batch size for pagination, max 10000
            cursor: Cursor for pagination, not required on first call

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "fill_cnt": 1,             # Filled count
                "fill_user_cnt": 1,        # Filled user count
                "unfill_user_cnt": 90,     # Not filled user count
                "submit_users": [          # Submitted users list (when req_type=2)
                    {
                        "userid": "USERID1",        # Internal member ID (not for anonymous)
                        "tmp_external_userid": "TMP_EXTERNAL_USERID1",  # External user temp ID
                        "submit_time": 1668418200,   # Submission time
                        "answer_id": 1,              # Answer ID
                        "user_name": "USER_NAME1"    # Name (not for anonymous)
                    }
                ],
                "unfill_users": [          # Not submitted users list (when req_type=3)
                    {
                        "userid": "USERID1",        # Internal member ID
                        "user_name": "USER_NAME1"    # Name
                    }
                ],
                "has_more": false,         # Has more data
                "cursor": 1                # Next cursor
            }
        """
        return self.wedoc_api.get_form_statistic(
            repeated_id=repeated_id,
            req_type=req_type,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor
        )

    def get_form_answer(
        self,
        repeated_id: str,
        answer_ids: list
    ) -> Dict[str, Any]:
        """
        Get form answers.

        Args:
            repeated_id: Form cycle ID
            answer_ids: List of answer IDs to fetch, max batch size 100

        Returns:
            API response as a dictionary
            {
                "errcode": 0,              # Error code
                "errmsg": "ok",            # Error message
                "answer": {                # Answers
                    "answer_list": [       # Answer list
                        {
                            "answer_id": 15,        # Answer ID
                            "user_name": "USER_NAME1",  # User name
                            "ctime": 1668430580,    # Creation time
                            "mtime": 1668430580,    # Modification time
                            "reply": {             # Answer details
                                "items": [         # Each question's answer
                                    {
                                        "question_id": 1,      # Question ID
                                        "text_reply": "Ndjnd", # Text answer
                                        "option_reply": [2],   # Choice answer
                                        "file_extend_reply": [ # File answer list
                                            {
                                                "name": "FILE_NAME1",  # File name
                                                "fileid": "FILEID1"   # File ID
                                            }
                                        ]
                                    }
                                ]
                            },
                            "answer_status": 1,     # Answer status 1:normal 3:removed
                            "tmp_external_userid": "TMP_EXTERNAL_USERID1"  # External user temp ID
                        }
                    ]
                }
            }
        """
        return self.wedoc_api.get_form_answer(
            repeated_id=repeated_id,
            answer_ids=answer_ids
        )