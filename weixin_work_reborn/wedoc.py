"""
企微文档(wedoc) API 模块

该模块提供了企微文档相关的API接口功能，包括：
- 文档管理（新建、重命名、删除、获取基础信息、分享）
- 文档内容管理（编辑内容、获取数据）
- 表格内容管理（编辑表格、获取行列信息、获取表格数据）
- 智能表格内容管理（添加子表、删除子表、更新子表、查询子表、添加视图、删除视图、更新视图、查询视图、添加字段、删除字段、更新字段、查询字段、添加记录、删除记录、更新记录、查询记录、添加编组、删除编组、更新编组、获取编组）
- 文档权限管理（获取权限信息、修改查看规则、修改通知范围及权限、修改安全设置、管理智能表格内容权限）
- 收集表管理（创建收集表、编辑收集表、获取收集表信息、收集表统计信息查询、读取收集表答案）

使用前需要先获取access_token，可以通过企微的认证模块获取。
"""
import json
import requests
from typing import Dict, List, Optional, Any, Union
from urllib.parse import urljoin


class WeDocAPI:
    """
    企微文档API类，提供了企微文档的各种操作接口
    """
    
    def __init__(self, access_token: str):
        """
        初始化企微文档API
        
        Args:
            access_token: 企微应用的访问令牌
        """
        self.access_token = access_token
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin/wedoc/"
        self.doc_base_url = f"{self.base_url}document/"
        self.spreadsheet_base_url = f"{self.base_url}spreadsheet/"
        self.smartsheet_base_url = f"{self.base_url}smartsheet/"
        self.smartsheet_priv_base_url = f"{self.base_url}smartsheet/content_priv/"
        self.form_base_url = f"{self.base_url}form/"
    
    def _make_request(self, url: str, data: Dict[str, Any], method: str = "POST") -> Dict[str, Any]:
        """
        发送API请求的内部方法
        
        Args:
            url: 请求URL
            data: 请求数据
            method: 请求方法，默认为POST
            
        Returns:
            Dict: API响应数据
        """
        headers = {"Content-Type": "application/json"}
        params = {"access_token": self.access_token}
        
        if method.upper() == "GET":
            response = requests.get(url, params=params, headers=headers)
        else:
            response = requests.post(url, json=data, params=params, headers=headers)
        
        return response.json()
    
    # ==================== 文档管理相关接口 ====================
    
    def new_document(
        self,
        doc_type: int,
        doc_name: str,
        spaceid: Optional[str] = None,
        fatherid: Optional[str] = None,
        admin_users: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        新建文档
        
        该接口用于新建文档、表格及智能表格，新建收集表可前往收集表管理查看。
        
        Args:
            doc_type: 文档类型, 3:文档 4:表格 10:智能表格
            doc_name: 文档名字（注意：文件名最多填255个字符, 超过255个字符会被截断）
            spaceid: 空间spaceid。若指定`spaceid`，则`fatherid`也要同时指定
            fatherid: 父目录fileid, 在根目录时为空间spaceid
            admin_users: 文档管理员userid列表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "url": "URL",      # 新建文档的访问链接
                "docid": "DOCID"   # 新建文档的docid。docid仅在创建时返回，需要开发者妥善保存
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.base_url}create_doc"
        data = {
            "doc_type": doc_type,
            "doc_name": doc_name
        }
        
        if spaceid:
            data["spaceid"] = spaceid
        if fatherid:
            data["fatherid"] = fatherid
        if admin_users:
            data["admin_users"] = admin_users
            
        return self._make_request(url, data)
    
    def rename_document(
        self,
        new_name: str,
        docid: Optional[str] = None,
        formid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        重命名文档
        
        该接口用于对指定文档、表格、智能表格及收集表进行重命名。
        
        Args:
            new_name: 重命名后的文档名（注意：文档名最多填255个字符, 英文算1个, 汉字算2个, 超过255个字符会被截断）
            docid: 文档docid（docid、formid只能填其中一个），仅可修改应用自己创建的文档
            formid: 收集表id（docid、formid只能填其中一个），仅可修改应用自己创建的收集表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            ValueError: 当docid和formid同时为None时抛出异常
            requests.RequestException: 网络请求异常
        """
        if not docid and not formid:
            raise ValueError("docid和formid不能同时为空，必须指定其中一个")
            
        url = f"{self.base_url}rename_doc"
        data = {"new_name": new_name}
        
        if docid:
            data["docid"] = docid
        if formid:
            data["formid"] = formid
            
        return self._make_request(url, data)
    
    def delete_document(
        self,
        docid: Optional[str] = None,
        formid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        删除文档
        
        该接口用于删除指定文档、表格、智能表格及收集表。
        
        Args:
            docid: 文档docid（docid、formid只能填其中一个），仅可删除应用自己创建的文档
            formid: 收集表id（docid、formid只能填其中一个），仅可删除应用自己创建的收集表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            ValueError: 当docid和formid同时为None时抛出异常
            requests.RequestException: 网络请求异常
        """
        if not docid and not formid:
            raise ValueError("docid和formid不能同时为空，必须指定其中一个")
            
        url = f"{self.base_url}del_doc"
        data = {}
        
        if docid:
            data["docid"] = docid
        if formid:
            data["formid"] = formid
            
        return self._make_request(url, data)
    
    def get_document_base_info(self, docid: str) -> Dict[str, Any]:
        """
        获取文档基础信息
        
        该接口用于获取指定文档、表格、智能表格及收集表的基础信息。
        
        Args:
            docid: 文档docid
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "doc_base_info": {
                    "docid": "DOCID",      # 文档docid
                    "doc_name": "DOC_NAME",# 文档名字
                    "create_time": 1717071093,  # 文档创建时间
                    "modify_time": 1717071093,  # 文档最后修改时间
                    "doc_type": 3           # 3: 文档 4: 表格 10:智能表格
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.base_url}get_doc_base_info"
        data = {"docid": docid}
        
        return self._make_request(url, data)
    
    def share_document(
        self,
        docid: Optional[str] = None,
        formid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        分享文档
        
        该接口用于获取文档、表格、智能表格及收集表的分享链接。
        
        Args:
            docid: 文档id（docid、formid只能填其中一个）
            formid: 收集表id（docid、formid只能填其中一个）
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "share_url": "URL1"        # 文档分享链接
            }
            
        Raises:
            ValueError: 当docid和formid同时为None时抛出异常
            requests.RequestException: 网络请求异常
        """
        if not docid and not formid:
            raise ValueError("docid和formid不能同时为空，必须指定其中一个")
            
        url = f"{self.base_url}doc_share"
        data = {}
        
        if docid:
            data["docid"] = docid
        if formid:
            data["formid"] = formid
            
        return self._make_request(url, data)
    
    # ==================== 文档内容管理相关接口 ====================
    
    def edit_document_content(
        self,
        docid: str,
        requests: List[Dict[str, Any]],
        version: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        编辑文档内容
        
        该接口可以对一个在线文档批量执行多个更新操作。
        
        注意：
        1. 批量更新请求，若其中有一个操作报错则全部更新操作不生效。
        2. 单次批量更新操作数量 <= 30。
        
        Args:
            docid: 文档的docid
            version: 操作的文档版本, 该参数可以通过获取文档内容接口获得。操作后文档版本将更新一版。要更新的文档版本与最新文档版本相差不能超过100个。
            requests: 更新操作列表，支持以下操作类型：
                - replace_text: 替换指定位置文本内容
                - insert_text: 在指定位置插入文本内容
                - delete_content: 删除指定位置内容
                - insert_image: 在指定位置插入图片
                - insert_page_break: 在指定位置插入分页符
                - insert_table: 在指定位置插入表格
                - insert_paragraph: 在指定位置插入段落
                - update_text_property: 更新指定位置文本属性
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.doc_base_url}batch_update"
        data = {
            "docid": docid,
            "requests": requests
        }
        
        if version is not None:
            data["verison"] = version  # 注意：API文档中拼写为verison
            
        return self._make_request(url, data)
    
    def get_document_data(self, docid: str) -> Dict[str, Any]:
        """
        获取文档数据
        
        该接口用于获取文档数据
        
        Args:
            docid: 文档的docid
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "version": 10,     # 文档版本
                "document": {...}  # 文档内容根节点，详见Node结构
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.doc_base_url}get"
        data = {"docid": docid}
        
        return self._make_request(url, data)
    
    # ==================== 表格内容管理相关接口 ====================
    
    def edit_spreadsheet_content(self, docid: str, requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        编辑表格内容
        
        该接口可以对一个在线表格批量执行多个更新操作。
        
        注意：
        1. 批量更新请求中的各个操作会逐个按顺序执行，直到全部执行完成则请求返回，或者其中一个操作报错则不再继续执行后续的操作。
        2. 每一个更新操作在执行之前都会做请求校验（包括权限校验、参数校验等等），如果校验未通过则该更新操作会报错并返回，不再执行后续操作。
        3. 单次批量更新请求的操作数量 <= 5。
        
        Args:
            docid: 文档的docid
            requests: 更新操作列表，支持以下操作类型：
                - add_sheet_request: 新增工作表
                - delete_sheet_request: 删除工作表
                - update_range_request: 更新范围内单元格内容
                - delete_dimension_request: 删除表格连续的行或列
                
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "data": {
                    "responses": [        # 结果列表
                        {
                            "add_sheet_response": {...},         # 新增工作表响应结构体
                            "update_range_response": {...},      # 更新范围内单元格内容响应结构体
                            "delete_dimension_response": {...},  # 删除表格连续的行或列响应结构体
                            "delete_sheet_response": {...}       # 删除工作表响应结构体
                        }
                    ]
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.spreadsheet_base_url}batch_update"
        data = {
            "docid": docid,
            "requests": requests
        }
        
        return self._make_request(url, data)
    
    def get_sheet_properties(self, docid: str) -> Dict[str, Any]:
        """
        获取表格行列信息
        
        该接口用于获取在线表格的工作表、行数、列数等。
        
        Args:
            docid: 在线表格的docid
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "properties": [            # 工作表属性列表
                    {
                        "sheet_id": "ABCDE",      # 工作表ID，工作表的唯一标识
                        "title": "XXXXXX",        # 工作表名称
                        "row_count": 100,         # 表格的总行数
                        "column_count": 100       # 表格的总列数
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.spreadsheet_base_url}get_sheet_properties"
        data = {"docid": docid}
        
        return self._make_request(url, data)
    
    def get_sheet_range_data(
        self,
        docid: str,
        sheet_id: str,
        range_str: str
    ) -> Dict[str, Any]:
        """
        获取表格数据
        
        本接口用于获取指定范围内的在线表格信息，单次查询的范围大小需满足以下限制：
        1. 查询范围行数 <=1000
        2. 查询范围列数 <=200
        3. 范围内的总单元格数量 <=10000
        
        Args:
            docid: 在线表格唯一标识
            sheet_id: 工作表ID，工作表的唯一标识
            range_str: 查询的范围，格式遵循 A1表示法
                     A1表示法是常见的表格数据引用表示法，例如:
                     - "A1:A1" 表示一个单元格 A1
                     - "A1:B5" 从单元格 A1 到单元格 B5 的区域
                     - "A1:D1" 第一行的4个单元格，分别为 A1、B1、C1、D1
                     - "A1:A3" 第一列的3个单元格，分别为 A1、A2、A3
                     - "B5:A1" 不合法的表示，因为 B5 在 A1 的右下方
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "data": {
                    "result": {            # 表格数据，详见GridData结构
                        "start_row": 1,     # 起始行编号（从0开始计算）
                        "start_column": 1,  # 起始列编号（从0开始计算）
                        "rows": [          # 各行的数据
                            {
                                "values": [ # 各个单元格的数据内容
                                    {
                                        "cell_value": {...},      # 单元格的数据内容
                                        "cell_format": {...}      # 单元格的样式信息
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.spreadsheet_base_url}get_sheet_range_data"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "range": range_str
        }
        
        return self._make_request(url, data)
    
    # ==================== 智能表格内容管理相关接口 ====================
    
    def add_smartsheet(
        self,
        docid: str,
        title: Optional[str] = None,
        index: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        添加子表
        
        本接口用于在表格的某个位置添加一个智能表，该智能表不存在视图、记录和字段，可以使用 API 在该智能表中添加视图、记录和字段。
        
        Args:
            docid: 文档的docid
            title: 智能表标题
            index: 智能表下标
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "properties": {
                    "title": "智能表",     # 智能表标题
                    "index": 3,            # 智能表下标
                    "sheet_id": "123abc"   # 智能表 ID，创建子表时生成的 6 位随机 ID
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}add_sheet"
        data = {"docid": docid}
        
        properties = {}
        if title:
            properties["title"] = title
        if index is not None:
            properties["index"] = index
            
        if properties:
            data["properties"] = properties
            
        return self._make_request(url, data)
    
    def delete_smartsheet(self, docid: str, sheet_id: str) -> Dict[str, Any]:
        """
        删除子表
        
        本接口用于删除在线表格中的某个智能表。
        
        Args:
            docid: 文档的docid
            sheet_id: 删除的Smartsheet 子表 ID
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}delete_sheet"
        data = {
            "docid": docid,
            "sheet_id": sheet_id
        }
        
        return self._make_request(url, data)
    
    def update_smartsheet(
        self,
        docid: str,
        sheet_id: str,
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        更新子表
        
        本接口用于修改表格中某个子表的标题。
        
        Args:
            docid: 文档的docid
            sheet_id: 子表 ID
            title: 子表标题
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}update_sheet"
        data = {
            "docid": docid,
            "properties": {
                "sheet_id": sheet_id
            }
        }
        
        if title:
            data["properties"]["title"] = title
            
        return self._make_request(url, data)
    
    def query_smartsheet(
        self,
        docid: str,
        sheet_id: Optional[str] = None,
        need_all_type_sheet: bool = False
    ) -> Dict[str, Any]:
        """
        查询子表
        
        本接口用于查询一篇在线表格中全部智能表信息。
        
        Args:
            docid: 文档的docid
            sheet_id: 指定子表ID查询
            need_all_type_sheet: 获取所有类型子表。为true时可获取包含仪表盘和说明页在内的所有类型的子表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "sheet_list": [            # 智能表信息列表
                    {
                        "sheet_id": "123abc",      # 子表id
                        "title": "XXXX",           # 子表名称
                        "is_visible": True,        # 子表是否可见
                        "type": "smartsheet"       # 子表类型。"dashboard" 仪表盘。"external" 说明页，"smartsheet" 智能表
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}get_sheet"
        data = {
            "docid": docid,
            "need_all_type_sheet": need_all_type_sheet
        }
        
        if sheet_id:
            data["sheet_id"] = sheet_id
            
        return self._make_request(url, data)
    
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
        添加视图
        
        本接口用于在 Smartsheet 中的某个子表里添加一个新视图。单表最多允许有200个视图。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            view_title: 视图标题
            view_type: 视图类型，可能的值包括：
                      - "VIEW_TYPE_GRID": 表格视图
                      - "VIEW_TYPE_KANBAN": 看板视图
                      - "VIEW_TYPE_GALLERY": 画册视图
                      - "VIEW_TYPE_GANTT": 甘特视图
                      - "VIEW_TYPE_CALENDAR": 日历视图
            property_gantt: 甘特视图属性,添加甘特图时必填，包含：
                           - start_date_field_id: 时间条起点字段ID，只允许日期类型(FIELD_TYPE_DATE_TIME)的字段ID
                           - end_date_field_id: 时间条终点字段ID，只允许日期类型(FIELD_TYPE_DATE_TIME)的字段ID
            property_calendar: 日历视图属性，添加日历视图时必填，包含：
                             - start_date_field_id: 时间条起点字段ID，只允许日期类型(FIELD_TYPE_DATE_TIME)的字段ID
                             - end_date_field_id: 时间条终点字段ID，只允许日期类型(FIELD_TYPE_DATE_TIME)的字段ID
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "view": {
                    "view_id": "vFYZUS",   # 视图 ID
                    "view_title": "XXX",   # 视图标题
                    "view_type": "VIEW_TYPE_GRID"  # 视图类型
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}add_view"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "view_title": view_title,
            "view_type": view_type
        }
        
        if property_gantt:
            data["property_gantt"] = property_gantt
        if property_calendar:
            data["property_calendar"] = property_calendar
            
        return self._make_request(url, data)
    
    def delete_views(self, docid: str, sheet_id: str, view_ids: List[str]) -> Dict[str, Any]:
        """
        删除视图
        
        本接口用于在 smartsheet 中的某个子表里删除若干个视图。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            view_ids: 要删除的视图ID列表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}delete_views"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "view_ids": view_ids
        }
        
        return self._make_request(url, data)
    
    def update_view(
        self,
        docid: str,
        sheet_id: str,
        view_id: str,
        view_title: Optional[str] = None,
        property_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        更新视图
        
        本接口用于更新 Smartsheet 中的某个视图。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            view_id: 视图ID
            view_title: 视图标题
            property_data: 视图的排序/过滤/分组/填色配置，包含：
                          - auto_sort: 记录变更后自动重新排序
                          - sort_spec: 排序设置
                          - group_spec: 分组设置
                          - filter_spec: 过滤设置
                          - is_field_stat_enabled: 是否使用数据统计
                          - field_visibility: 字段可见性，类似map，key为字段ID, value为布尔值表示是否显示
                          - frozen_field_count: 冻结列数量，从首列开始
                          - color_config: 填色设置
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "view": {          # 更新成功的视图内容
                    # 视图信息，包含view_id、view_title、view_type等
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}update_view"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "view_id": view_id
        }
        
        if view_title:
            data["view_title"] = view_title
        if property_data:
            data["property"] = property_data
            
        return self._make_request(url, data)
    
    def query_views(
        self,
        docid: str,
        sheet_id: str,
        view_ids: Optional[List[str]] = None,
        offset: int = 0,
        limit: int = 0
    ) -> Dict[str, Any]:
        """
        查询视图
        
        本接口用于获取 Smartsheet 中某个子表里全部视图信息。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            view_ids: 需要查询的视图 ID 数组
            offset: 偏移量，初始值为 0
            limit: 分页大小，每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，
                  如果总数大于 1000，一次性返回 1000 个视图，当总数小于 1000 时，返回全部视图；
                  limit 最大值为 1000
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "total": 2,                # 符合筛选条件的视图总数
                "has_more": True,          # 是否还有更多项
                "next": 1,                 # 下次下一个搜索结果的偏移量
                "views": [                 # 视图数据列表
                    {
                        "view_id": "vabcde",    # 视图 ID
                        "view_title": "默认视图",# 视图标题
                        "view_type": "VIEW_TYPE_GRID"  # 视图类型
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}get_views"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "offset": offset,
            "limit": limit
        }
        
        if view_ids:
            data["view_ids"] = view_ids
            
        return self._make_request(url, data)
    
    def add_fields(
        self,
        docid: str,
        sheet_id: str,
        fields: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        添加字段
        
        本接口用于在智能表中的某个子表里添加一列或多列新字段。单表最多允许有150个字段。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            fields: 字段详情列表，每个字段包含：
                   - field_title: 字段标题
                   - field_type: 字段类型，如 FIELD_TYPE_TEXT, FIELD_TYPE_NUMBER 等
                   - property_XXX: 字段属性，根据字段类型不同而不同
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "fields": [                # 字段详情列表
                    {
                        "field_id": "FIELDID",    # 字段 ID
                        "field_title": "TITLE",   # 字段标题
                        "field_type": "FIELD_TYPE_TEXT"  # 字段类型
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}add_fields"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "fields": fields
        }
        
        return self._make_request(url, data)
    
    def delete_fields(self, docid: str, sheet_id: str, field_ids: List[str]) -> Dict[str, Any]:
        """
        删除字段
        
        本接口用于删除智能表中的某个子表里的一列或多列字段。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            field_ids: 需要删除的字段id列表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}delete_fields"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "field_ids": field_ids
        }
        
        return self._make_request(url, data)
    
    def update_fields(
        self,
        docid: str,
        sheet_id: str,
        fields: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        更新字段
        
        本接口用于更新智能中的某个子表里的一个或多个字段的标题和字段属性信息。
        注意：该接口只能更新字段名、字段属性，不能更新字段类型。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            fields: 字段详情列表，每个字段包含：
                   - field_id: 字段 ID，更新字段属性时需要填写该字段，但字段 ID 不能被更新
                   - field_title: 字段标题，需要更新为的字段标题
                   - field_type: 字段类型，必须为原属性
                   - property_XXX: 字段属性，根据字段类型不同而不同
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "fields": [                # 字段详情列表
                    {
                        "field_id": "FIELDID",    # 字段 ID
                        "field_title": "TITLE",   # 字段标题
                        "field_type": "FIELD_TYPE_TEXT"  # 字段类型
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}update_fields"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "fields": fields
        }
        
        return self._make_request(url, data)
    
    def query_fields(
        self,
        docid: str,
        sheet_id: str,
        view_id: Optional[str] = None,
        field_ids: Optional[List[str]] = None,
        field_titles: Optional[List[str]] = None,
        offset: int = 0,
        limit: int = 0
    ) -> Dict[str, Any]:
        """
        查询字段
        
        本接口用于获取智能表中某个子表下字段信息，该接口可以完成下面三种功能：
        获取全部字段信息、依据字段名获取对应字段、依据字段 ID 获取对应字段信息。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            view_id: 视图 ID
            field_ids: 由字段 ID 组成的 JSON 数组
            field_titles: 由字段标题组成的 JSON 数组
            offset: 偏移量，初始值为 0
            limit: 分页大小，每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，
                  如果总数大于 1000，一次性返回 1000 个字段，当总数小于 1000 时，返回全部字段；
                  limit 最大值为 1000
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "total": 1,                # 字段总数
                "fields": [                # 字段详情列表
                    {
                        "field_id": "ID1",        # 字段 ID
                        "field_title": "TITLE1",  # 字段标题
                        "field_type": "FIELD_TYPE_TEXT"  # 字段类型
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}get_fields"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "offset": offset,
            "limit": limit
        }
        
        if view_id:
            data["view_id"] = view_id
        if field_ids:
            data["field_ids"] = field_ids
        if field_titles:
            data["field_titles"] = field_titles
            
        return self._make_request(url, data)
    
    def add_records(
        self,
        docid: str,
        sheet_id: str,
        records: List[Dict[str, Any]],
        key_type: str = "CELL_VALUE_KEY_TYPE_FIELD_TITLE"
    ) -> Dict[str, Any]:
        """
        添加记录
        
        本接口用于在 Smartsheet 中的某个子表里添加一行或多行新记录。单表最多允许有100000行记录，15000000个单元格。
        注意：不能通过添加记录接口给创建时间、最后编辑时间、创建人和最后编辑人四种类型的字段添加记录。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            records: 需要添加的记录的具体内容组成的 JSON 数组
            key_type: 返回记录中单元格的key类型，默认用标题
                     - "CELL_VALUE_KEY_TYPE_FIELD_TITLE": key用字段标题表示
                     - "CELL_VALUE_KEY_TYPE_FIELD_ID": key用字段 ID 表示
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "records": [       # 由添加成功的记录的具体内容组成的 JSON 数组
                    # 记录详情
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}add_records"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "key_type": key_type,
            "records": records
        }
        
        return self._make_request(url, data)
    
    def delete_records(
        self,
        docid: str,
        sheet_id: str,
        record_ids: List[str]
    ) -> Dict[str, Any]:
        """
        删除记录
        
        本接口用于删除 Smartsheet 的某个子表中的一行或多行记录。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            record_ids: 要删除的记录 ID 列表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}delete_records"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "record_ids": record_ids
        }
        
        return self._make_request(url, data)
    
    def update_records(
        self,
        docid: str,
        sheet_id: str,
        records: List[Dict[str, Any]],
        key_type: str = "CELL_VALUE_KEY_TYPE_FIELD_TITLE"
    ) -> Dict[str, Any]:
        """
        更新记录
        
        本接口用于更新 Smartsheet 中的某个子表里的一行或多行记录。
        注意：不能通过更新记录接口给创建时间、最后编辑时间、创建人和最后编辑人四种类型的字段更新记录。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            records: 由需要更新的记录组成的 JSON 数组
            key_type: 返回记录中单元格的key类型
                     - "CELL_VALUE_KEY_TYPE_FIELD_TITLE": key用字段标题表示
                     - "CELL_VALUE_KEY_TYPE_FIELD_ID": key用字段 ID 表示
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "records": [       # 由更新成功的记录的具体内容组成的 JSON 数组
                    # 记录详情
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}update_records"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "key_type": key_type,
            "records": records
        }
        
        return self._make_request(url, data)
    
    def query_records(
        self,
        docid: str,
        sheet_id: str,
        view_id: Optional[str] = None,
        record_ids: Optional[List[str]] = None,
        key_type: str = "CELL_VALUE_KEY_TYPE_FIELD_TITLE",
        field_titles: Optional[List[str]] = None,
        field_ids: Optional[List[str]] = None,
        sort: Optional[List[Dict[str, Any]]] = None,
        offset: int = 0,
        limit: int = 0,
        ver: Optional[int] = None,
        filter_spec: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        查询记录
        
        本接口用于获取 Smartsheet 中某个子表下记录信息，该接口可以完成下面三种功能：
        获取全部记录信息、依据字段名和记录 ID 获取对应记录、对记录进行排序。
        
        Args:
            docid: 文档的docid
            sheet_id: Smartsheet 子表ID
            view_id: 视图 ID
            record_ids: 由记录 ID 组成的 JSON 数组
            key_type: 返回记录中单元格的key类型
                     - "CELL_VALUE_KEY_TYPE_FIELD_TITLE": key用字段标题表示
                     - "CELL_VALUE_KEY_TYPE_FIELD_ID": key用字段 ID 表示
            field_titles: 返回指定列，由字段标题组成的 JSON 数组，key_type 为 CELL_VALUE_KEY_TYPE_FIELD_TITLE 时有效
            field_ids: 返回指定列，由字段 ID 组成的 JSON 数组，key_type 为 CELL_VALUE_KEY_TYPE_FIELD_ID 时有效
            sort: 对返回记录进行排序
            offset: 偏移量，初始值为 0
            limit: 分页大小，每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，
                  如果总数大于 1000，一次性返回 1000 行记录，当总数小于 1000 时，返回全部记录；
                  limit 最大值为 1000
            ver: 版本号
            filter_spec: 过滤设置，不支持和sort一起使用
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "total": 10,       # 符合筛选条件的记录总数
                "has_more": False, # 是否还有更多项
                "next": 0,         # 下次下一个搜索结果的偏移量
                "records": [       # 由查询记录的具体内容组成的 JSON 数组
                    {
                        "record_id": "r5ud8u",      # 记录 ID
                        "create_time": "1715846245084", # 记录的创建时间
                        "update_time": "1715846248810", # 记录的更新时间
                        "values": {},               # 记录的具体内容
                        "creator_name": "NAME",     # 创建者名字
                        "updater_name": "NAME"      # 最后编辑者名字
                    }
                ],
                "ver": 160         # 版本号
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}get_records"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "key_type": key_type,
            "offset": offset,
            "limit": limit
        }
        
        if view_id:
            data["view_id"] = view_id
        if record_ids:
            data["record_ids"] = record_ids
        if field_titles:
            data["field_titles"] = field_titles
        if field_ids:
            data["field_ids"] = field_ids
        if sort:
            data["sort"] = sort
        if ver is not None:
            data["ver"] = ver
        if filter_spec:
            data["filter_spec"] = filter_spec
            
        return self._make_request(url, data)
    
    def add_field_group(
        self,
        docid: str,
        sheet_id: str,
        name: str,
        children: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """
        添加编组
        
        本接口用于在智能表中的某个子表里添加编组。单表最多允许有150个编组。
        每个编组最多允许有150个字段。字段只能同时存在于一个编组。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            name: 编组名称，不能和已有名称重复
            children: 编组内容列表，每个项包含：
                     - field_id: 字段id
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "field_group": {
                    "field_group_id": "FIELD_GROUP_ID", # 编组id
                    "name": "编组名称",                 # 编组名称
                    "children": [                      # 编组内容列表
                        {
                            "field_id": "FIELD_ID"    # 字段id
                        }
                    ]
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}add_field_group"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "name": name,
            "children": children
        }
        
        return self._make_request(url, data)
    
    def delete_field_groups(
        self,
        docid: str,
        sheet_id: str,
        field_group_ids: List[str]
    ) -> Dict[str, Any]:
        """
        删除编组
        
        本接口用于删除智能表的某个子表中的一个或多个编组。
        
        Args:
            docid: 文档的docid
            sheet_id: 子表ID
            field_group_ids: 要删除的编组 ID 列表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}delete_field_groups"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "field_group_ids": field_group_ids
        }
        
        return self._make_request(url, data)
    
    def update_field_group(
        self,
        docid: str,
        sheet_id: str,
        field_group_id: str,
        name: Optional[str] = None,
        children: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        更新编组
        
        本接口用于在智能表中的某个子表里更新已有编组。每个编组最多允许有150个字段。
        字段只能同时存在于一个编组。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            field_group_id: 编组id
            name: 编组名称，不能和已有名称重复
            children: 编组内容列表，每个项包含：
                     - field_id: 字段id
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "field_group": {
                    "field_group_id": "FIELD_GROUP_ID", # 编组id
                    "name": "编组名称",                 # 编组名称
                    "children": [                      # 编组内容列表
                        {
                            "field_id": "FIELD_ID"    # 字段id
                        }
                    ]
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}update_field_group"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "field_group_id": field_group_id
        }
        
        if name is not None:
            data["name"] = name
        if children is not None:
            data["children"] = children
            
        return self._make_request(url, data)
    
    def get_field_groups(
        self,
        docid: str,
        sheet_id: str,
        offset: int = 0,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        获取编组
        
        本接口用于在智能表中的某个子表里获取已有的编组。
        
        Args:
            docid: 文档的docid
            sheet_id: 表格ID
            offset: 偏移量，初始值为 0
            limit: 分页大小，每页返回多少条数据
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "total": 1,                # 编组数量
                "has_more": False,         # 是否还有更多数据
                "next": 0,                 # 下一偏移位置
                "field_groups": [          # 编组列表
                    {
                        "field_group_id": "FIELD_GROUP_ID", # 编组id
                        "name": "编组名称",                 # 编组名称
                        "children": [                      # 编组内容列表
                            {
                                "field_id": "FIELD_ID"    # 字段id
                            }
                        ]
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_base_url}get_field_groups"
        data = {
            "docid": docid,
            "sheet_id": sheet_id,
            "offset": offset,
            "limit": limit
        }
        
        return self._make_request(url, data)
    
    # ==================== 文档权限管理相关接口 ====================
    
    def get_document_auth(self, docid: str) -> Dict[str, Any]:
        """
        获取文档权限信息
        
        该接口用于获取文档、表格、智能表格的查看规则、文档通知范围及权限、安全设置信息
        
        Args:
            docid: 文档id
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "access_rule": {   # 文档的查看规则
                    "enable_corp_internal": true,     # 是否允许企业内成员浏览文档
                    "corp_internal_auth": 1,          # 企业内成员主动查看文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写）
                    "enable_corp_external": true,     # 是否允许企业外成员浏览文档
                    "corp_external_auth": 1,          # 企业外成员主动查看文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写）
                    "corp_internal_approve_only_by_admin": true,  # 企业内成员浏览文档是否必须由管理员审批
                    "corp_external_approve_only_by_admin": true,  # 企业外成员浏览文档是否必须由管理员审批
                    "ban_share_external": false       # 是否禁止文档分享到企业外
                },
                "secure_setting": {  # 文档安全设置
                    "enable_readonly_copy": false,    # 仅浏览权限的成员是否允许导出、复制、打印
                    "watermark": {   # 文档水印设置
                        "margin_type": 2,             # 水印密度 1:稀疏 2:紧密
                        "show_visitor_name": false,   # 是否展示访问者名字
                        "show_text": false,           # 是否展示水印文字
                        "text": ""                    # 水印文字
                    },
                    "enable_readonly_comment": false  # 是否允许只读成员评论
                },
                "doc_member_list": [  # 文档通知范围及权限列表
                    {
                        "type": 1,                    # 文档通知范围成员种类 1:user
                        "userid": "USERID1",          # 企业成员的userid
                        "auth": 7                     # 该文档通知范围成员的权限 1:只读 2:读写（目前仅智能表可设置为读写） 7:管理员
                    }
                ],
                "co_auth_list": [    # 文档查看权限特定部门列表
                    {
                        "type": 2,                    # 特定部门列表 2:部门
                        "departmentid": 1,            # 特定部门id
                        "auth": 1                     # 权限类型 1:只读,2:读写（目前仅智能表可设置为读写）
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.base_url}doc_get_auth"
        data = {"docid": docid}
        
        return self._make_request(url, data)
    
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
        co_auth_list: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        修改文档查看规则
        
        该接口用于修改文档、表格、智能表格查看规则。
        
        Args:
            docid: 操作的docid
            enable_corp_internal: 是否允许企业内成员浏览文档, 有值则覆盖
            corp_internal_auth: 企业内成员主动查看文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写）, 有值则覆盖
            enable_corp_external: 是否允许企业外成员浏览文档, 有值则覆盖
            corp_external_auth: 企业外成员主浏览文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写）, 有值则覆盖
            corp_internal_approve_only_by_admin: 企业内成员加入文档是否必须由管理员审批
            corp_external_approve_only_by_admin: 企业外成员加入文档是否必须由管理员审批
            ban_share_external: 是否禁止文档分享到企业外, 有值则覆盖
            update_co_auth_list: 是否更新文档查看权限的特定部门, true时更新特定部门列表
            co_auth_list: 需要更新文档查看权限特定部门时, 覆盖之前部门, 特别的: 列表为空则清空
                         每个项包含：departmentid, auth, type
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.base_url}mod_doc_join_rule"
        data = {"docid": docid}
        
        if enable_corp_internal is not None:
            data["enable_corp_internal"] = enable_corp_internal
        if corp_internal_auth is not None:
            data["corp_internal_auth"] = corp_internal_auth
        if enable_corp_external is not None:
            data["enable_corp_external"] = enable_corp_external
        if corp_external_auth is not None:
            data["corp_external_auth"] = corp_external_auth
        if corp_internal_approve_only_by_admin is not None:
            data["corp_internal_approve_only_by_admin"] = corp_internal_approve_only_by_admin
        if corp_external_approve_only_by_admin is not None:
            data["corp_external_approve_only_by_admin"] = corp_external_approve_only_by_admin
        if ban_share_external is not None:
            data["ban_share_external"] = ban_share_external
        if update_co_auth_list is not None:
            data["update_co_auth_list"] = update_co_auth_list
        if co_auth_list is not None:
            data["co_auth_list"] = co_auth_list
            
        return self._make_request(url, data)
    
    def modify_document_member(
        self,
        docid: str,
        update_file_member_list: Optional[List[Dict[str, Any]]] = None,
        del_file_member_list: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        修改文档通知范围及权限
        
        该接口用于修改文档、表格、智能表格通知范围列表，可以新增文档、表格、智能表格通知范围并设置权限、
        修改已有范围的权限以及删除文档、表格、智能表格通知范围内的人员
        
        Args:
            docid: 操作的文档id
            update_file_member_list: 更新文档通知范围的列表, 批次大小最大100
                                   每个项包含：type, auth, userid/tmp_external_userid
            del_file_member_list: 删除的文档通知范围列表，批次大小最大一百
                                每个项包含：type, userid/tmp_external_userid
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.base_url}mod_doc_member"
        data = {"docid": docid}
        
        if update_file_member_list:
            data["update_file_member_list"] = update_file_member_list
        if del_file_member_list:
            data["del_file_member_list"] = del_file_member_list
            
        return self._make_request(url, data)
    
    def modify_document_safety_setting(
        self,
        docid: str,
        enable_readonly_copy: Optional[bool] = None,
        watermark: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        修改文档安全设置
        
        该接口用于修改文档、表格、智能表格的安全设置
        
        Args:
            docid: 操作的文档id
            enable_readonly_copy: 是否允许只读成员复制、下载文档，有值则覆盖
            watermark: 水印设置，包含：
                      - margin_type: 水印疏密度，1:稀疏，2:紧密
                      - show_visitor_name: 是否展示访问者名字水印，有值则覆盖
                      - show_text: 是否展示文本水印，有值则覆盖
                      - text: 文字水印的文字，有值则覆盖
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.base_url}mod_doc_safty_setting"
        data = {"docid": docid}
        
        if enable_readonly_copy is not None:
            data["enable_readonly_copy"] = enable_readonly_copy
        if watermark is not None:
            data["watermark"] = watermark
            
        return self._make_request(url, data)
    
    def query_sheet_privilege(
        self,
        docid: str,
        type_: int,
        rule_id_list: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        查询智能表格子表权限
        
        该接口用于查询智能表格子表权限详情
        
        Args:
            docid: 智能表ID，通过新建文档接口创建后获得
            type_: 权限规则类型，1-全员权限，2-额外权限
            rule_id_list: 需要查询的规则id列表，查询额外权限时填写
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "rule_list": [     # 权限列表
                    {
                        "rule_id": 1,               # 规则id（当type为2时有值）
                        "type": 1,                  # 权限规则类型，1-全员权限，2-额外权限
                        "name": "全员权限",         # 权限名称，仅当type为2时有效
                        "priv_list": [             # 针对不同子表设置内容权限
                            {
                                "sheet_id": "q979lj",        # 子表ID
                                "priv": 2,                  # 子表权限: 1-全部权限；2-可编辑；3-仅浏览；4-无权限
                                "can_insert_record": true,  # 是否可以新增记录
                                "can_delete_record": true,  # 是否可以删除记录
                                "can_create_modify_delete_view": true,  # 是否可以增、删、改视图
                                "field_priv": {            # 按字段配置权限
                                    "field_range_type": 2,  # 子表权限对所有字段生效还是部分字段生效：1-所有字段；2-部分字段
                                    "field_rule_list": [   # 按字段分别配置权限
                                        {
                                            "field_id": "fsMGQS",      # 字段id
                                            "field_type": "FIELD_TYPE_TEXT",  # 字段类型
                                            "can_edit": false,         # 可编辑
                                            "can_insert": true,        # 可首次提交
                                            "can_view": true           # 可查看
                                        }
                                    ],
                                    "field_default_rule": {  # field_rule_list里未指定字段和后续新增字段的默认配置
                                        "can_edit": false,
                                        "can_insert": false,
                                        "can_view": true
                                    }
                                },
                                "record_priv": {           # 按记录配置权限
                                    "record_range_type": 1  # 子表权限对记录生效范围：1-全部记录；2-满足任意条件的记录；3-满足全部条件的记录
                                }
                            }
                        ]
                    }
                ]
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_priv_base_url}get_sheet_priv"
        data = {
            "docid": docid,
            "type": type_
        }
        
        if rule_id_list:
            data["rule_id_list"] = rule_id_list
            
        return self._make_request(url, data)
    
    def update_sheet_privilege(
        self,
        docid: str,
        type_: int,
        rule_id: Optional[int] = None,
        name: Optional[str] = None,
        priv_list: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        更新智能表格子表权限
        
        该接口用于设置全员权限或者成员额外权限的权限详情
        
        Args:
            docid: 智能表ID，通过新建文档接口创建后获得
            type_: 权限规则类型，1-全员权限，2-额外权限。每个智能表格有且只有一个全员权限
            rule_id: 当type为2时必填
            name: 更新权限名称，仅当type为2时有效
            priv_list: 针对不同子表设置内容权限列表，每个项包含：
                      - sheet_id: 子表ID
                      - priv: 子表权限: 1-全部权限；2-可编辑；3-仅浏览；4-无权限
                      - can_insert_record: 是否可以新增记录
                      - can_delete_record: 是否可以删除记录
                      - can_create_modify_delete_view: 是否可以增、删、改视图
                      - field_priv: 按字段配置权限
                      - record_priv: 按记录配置权限
                      - clear: 清除子表的设置，恢复默认权限
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_priv_base_url}update_sheet_priv"
        data = {
            "docid": docid,
            "type": type_
        }
        
        if type_ == 2 and rule_id is not None:
            data["rule_id"] = rule_id
        if name:
            data["name"] = name
        if priv_list:
            data["priv_list"] = priv_list
            
        return self._make_request(url, data)
    
    def create_rule(
        self,
        docid: str,
        name: str
    ) -> Dict[str, Any]:
        """
        新增智能表格指定成员额外权限
        
        该接口用于新增智能表格指定成员额外权限
        
        Args:
            docid: 智能表ID，通过新建文档接口创建后获得
            name: 权限规则名称，不可重复
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "rule_id": 1       # 成员权限规则id
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_priv_base_url}create_rule"
        data = {
            "docid": docid,
            "name": name
        }
        
        return self._make_request(url, data)
    
    def modify_rule_member(
        self,
        docid: str,
        rule_id: int,
        add_member_range: Optional[Dict[str, List[str]]] = None,
        del_member_range: Optional[Dict[str, List[str]]] = None
    ) -> Dict[str, Any]:
        """
        更新智能表格指定成员额外权限
        
        该接口用于更新智能表格指定成员额外权限，成员最多可设置50个
        
        Args:
            docid: 智能表ID，通过新建文档接口创建后获得
            rule_id: 需要更新的id
            add_member_range: 新增成员，包含userid_list
            del_member_range: 删除成员，包含userid_list
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_priv_base_url}mod_rule_member"
        data = {
            "docid": docid,
            "rule_id": rule_id
        }
        
        if add_member_range:
            data["add_member_range"] = add_member_range
        if del_member_range:
            data["del_member_range"] = del_member_range
            
        return self._make_request(url, data)
    
    def delete_rule(
        self,
        docid: str,
        rule_id_list: List[int]
    ) -> Dict[str, Any]:
        """
        删除智能表格指定成员额外权限
        
        该接口用于删除智能表格指定成员额外权限
        
        Args:
            docid: 智能表ID，通过新建文档接口创建后获得
            rule_id_list: 需要删除的规则id列表
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.smartsheet_priv_base_url}delete_rule"
        data = {
            "docid": docid,
            "rule_id_list": rule_id_list
        }
        
        return self._make_request(url, data)
    
    # ==================== 收集表管理相关接口 ====================
    
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
        创建收集表
        
        该接口用于创建收集表。
        
        Args:
            form_title: 收集表标题
            form_desc: 收集表描述
            form_header: 收集表表头背景图链接
            form_question: 收集表的问题列表
            form_setting: 收集表设置
            spaceid: 空间spaceid
            fatherid: 父目录fileid, 在根目录时为空间spaceid
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "formid": "FORMID" # 收集表id
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.form_base_url}create_form"
        data = {
            "form_info": {
                "form_title": form_title
            }
        }
        
        if form_desc:
            data["form_info"]["form_desc"] = form_desc
        if form_header:
            data["form_info"]["form_header"] = form_header
        if form_question:
            data["form_info"]["form_question"] = form_question
        if form_setting:
            data["form_info"]["form_setting"] = form_setting
        if spaceid:
            data["spaceid"] = spaceid
        if fatherid:
            data["fatherid"] = fatherid
            
        return self._make_request(url, data)
    
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
        编辑收集表
        
        该接口用于编辑收集表。
        
        Args:
            formid: 收集表id
            oper: 操作类型。1：全量修改问题；2：全量修改设置
            form_title: 收集表标题（操作1修改）
            form_desc: 收集表描述（操作1修改）
            form_header: 收集表表头背景图链接（操作1修改）
            form_question: 收集表的问题列表（操作1修改）
            form_setting: 收集表设置（操作2修改）
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok"     # 错误码说明
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.form_base_url}modify_form"
        data = {
            "formid": formid,
            "oper": oper
        }
        
        if form_title:
            data["form_info"] = {"form_title": form_title}
        if form_desc:
            if "form_info" not in data:
                data["form_info"] = {}
            data["form_info"]["form_desc"] = form_desc
        if form_header:
            if "form_info" not in data:
                data["form_info"] = {}
            data["form_info"]["form_header"] = form_header
        if form_question:
            if "form_info" not in data:
                data["form_info"] = {}
            data["form_info"]["form_question"] = form_question
        if form_setting:
            if "form_info" not in data:
                data["form_info"] = {}
            data["form_info"]["form_setting"] = form_setting
            
        return self._make_request(url, data)
    
    def get_form_info(self, formid: str) -> Dict[str, Any]:
        """
        获取收集表信息
        
        该接口用于读取收集表的信息
        
        Args:
            formid: 操作的收集表ID
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,      # 错误码
                "errmsg": "ok",    # 错误码说明
                "form_info": {     # 收集表信息
                    "formid": "FORMID1",           # 收集表id
                    "form_title": "api创建的收集表_周期",  # 收集表标题
                    "form_desc": "这是描述",        # 收集表描述
                    "form_header": "URL",          # 收集表表头背景图链接
                    "form_question": {            # 收集表的问题列表
                        "items": [                # 问题列表
                            # 问题详情
                        ]
                    },
                    "form_setting": {             # 收集表的设置
                        # 设置详情
                    },
                    "repeated_id": [              # 收集表的周期id，用于获取答案列表和具体的回答
                        "REPEAT_ID1"
                    ]
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.form_base_url}get_form_info"
        data = {"formid": formid}
        
        return self._make_request(url, data)
    
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
        收集表的统计信息查询
        
        该接口用于获取收集表的统计信息、已回答成员列表和未回答成员列表
        
        Args:
            repeated_id: 操作的收集表的repeated_id,来源于get_form_info的返回
            req_type: 请求类型 1:只获取统计结果 2:获取已提交列表 3:获取未提交列表
            start_time: 拉取已提交列表时必填，其余type不填。筛选开始时间，以当天的00:00:00开始筛选
            end_time: 拉取已提交列表时必填，其余type不填。筛选结束时间，以当天的23:59:59结束筛选
            limit: 分页拉取时批次大小，最大10000
            cursor: 分页拉取的游标，首次不传
        
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "fill_cnt": 1,             # 已填写次数
                "fill_user_cnt": 1,        # 已填写人数
                "unfill_user_cnt": 90,     # 未填写人数
                "submit_users": [          # 已填写人列表（当req_type为2时）
                    {
                        "userid": "USERID1",        # 企业内成员的id，匿名填写不返回
                        "tmp_external_userid": "TMP_EXTERNAL_USERID1",  # 外部用户临时id
                        "submit_time": 1668418200,   # 提交时间
                        "answer_id": 1,              # 答案id
                        "user_name": "USER_NAME1"    # 名字，匿名填写不返回
                    }
                ],
                "unfill_users": [          # 未填写人列表（当req_type为3时）
                    {
                        "userid": "USERID1",        # 企业内成员的id
                        "user_name": "USER_NAME1"    # 名字
                    }
                ],
                "has_more": false,         # 是否还有更多
                "cursor": 1                # 下次分页拉取返回的cursor
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.form_base_url}get_form_statistic"
        data = {
            "repeated_id": repeated_id,
            "req_type": req_type
        }
        
        if start_time is not None and end_time is not None:
            data["start_time"] = start_time
            data["end_time"] = end_time
        if limit is not None:
            data["limit"] = limit
        if cursor is not None:
            data["cursor"] = cursor
            
        return self._make_request(url, data)
    
    def get_form_answer(
        self,
        repeated_id: str,
        answer_ids: List[int]
    ) -> Dict[str, Any]:
        """
        读取收集表答案
        
        该接口用于读取收集表的答案
        
        Args:
            repeated_id: 操作的收集表周期id
            answer_ids: 需要拉取的答案列表，批次大小最大100
            
        Returns:
            Dict: API响应数据
            {
                "errcode": 0,              # 错误码
                "errmsg": "ok",            # 错误码说明
                "answer": {                # 答案
                    "answer_list": [       # 答案列表
                        {
                            "answer_id": 15,        # 答案id
                            "user_name": "USER_NAME1",  # 用户名
                            "ctime": 1668430580,    # 创建时间
                            "mtime": 1668430580,    # 修改时间
                            "reply": {             # 该用户的答案明细
                                "items": [         # 每个问题的答案
                                    {
                                        "question_id": 1,      # 问题id
                                        "text_reply": "Ndjnd", # 文本答案
                                        "option_reply": [2],   # 选择题答案
                                        "file_extend_reply": [ # 文件题答案列表
                                            {
                                                "name": "FILE_NAME1",  # 文件名
                                                "fileid": "FILEID1"   # 文件id
                                            }
                                        ]
                                    }
                                ]
                            },
                            "answer_status": 1,     # 答案状态 1:正常 3:统计者移除此答案或删除
                            "tmp_external_userid": "TMP_EXTERNAL_USERID1"  # 外部用户临时id
                        }
                    ]
                }
            }
            
        Raises:
            requests.RequestException: 网络请求异常
        """
        url = f"{self.form_base_url}get_form_answer"
        data = {
            "repeated_id": repeated_id,
            "answer_ids": answer_ids
        }
        
        return self._make_request(url, data)