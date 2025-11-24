# 企业微信 API SDK

一个用于与企业微信 API 交互的 Python SDK。该库提供了一种简单高效的方式，将您的 Python 应用程序与企业微信集成，支持用户管理、身份验证等功能。SDK 采用简洁的模块化架构，支持静态导入。

## 功能特性

- **静态模块化架构**: 配置、通用函数(access_token)、用户管理和文档管理的独立模块
- **环境配置**: 支持 .env 文件和环境变量，使用 python-dotenv
- **便捷的访问令牌管理**: 自动获取和缓存访问令牌，支持生存时间(TTL)功能
- **用户管理**: 获取用户信息、更新用户档案、将手机号转换为用户ID
- **文档管理**: 全面支持企业微信文档操作(wedoc)，包括文档创建、编辑、共享和权限管理
- **全面的错误处理**: 对 API 错误进行适当的异常处理
- **类型提示**: 全面的类型注解支持，提升 IDE 使用体验
- **线程安全**: 适用于多线程应用程序的并发使用
- **缓存**: 使用 `cachetools` 进行高效的令牌缓存

## 安装

使用 pip 安装包:

```bash
pip install weixin-work-reborn
```

## 快速开始

```python
from weixin_work_reborn import WeChatWorkClient, Config

# 用配置初始化客户端
config = Config()  # 从 .env 文件或环境变量加载
client = WeChatWorkClient(config=config)

# 获取用户信息
user_info = client.get_user("user_id_here")
print(user_info)

# 更新用户信息
result = client.update_user(
    user_id="user_id_here",
    name="新姓名",
    mobile="13800138000",
    email="newemail@example.com"
)
print(result)

# 将手机号转换为用户ID
userid_result = client.mobile_to_userid("13800138000")
print(userid_result)

# 文档管理示例

# 创建新文档
doc_result = client.new_document(
    doc_type=3,  # 3 代表文档, 4 代表表格, 10 代表智能表格
    doc_name="我的新文档"
)
print(f"创建文档ID: {doc_result.get('docid')}")

# 获取文档信息
if 'docid' in doc_result:
    doc_info = client.get_document_base_info(doc_result['docid'])
    print(f"文档信息: {doc_info}")

# 重命名文档
if 'docid' in doc_result:
    rename_result = client.rename_document(
        docid=doc_result['docid'],
        new_name="重命名文档"
    )
    print(f"重命名结果: {rename_result}")
```

## 配置

### 使用 .env 文件 (推荐)

在项目根目录创建 `.env` 文件:

```bash
WEIXIN_WORK_BASE_URL=https://qyapi.weixin.qq.com/
WEIXIN_WORK_CORP_ID=your_corp_id_here
WEIXIN_WORK_APP_SECRET=your_app_secret_here
WEIXIN_WORK_CONTACTS_SYNC_SECRET=your_contacts_sync_secret_here
WEIXIN_WORK_DOC_SECRET=your_doc_secret_here
WEIXIN_WORK_AGENT_ID=your_agent_id_here
```

**注意**: 企业微信 API 针对不同的 API 端点需要不同的密钥：
- `WEIXIN_WORK_APP_SECRET` 用于通用 API 操作（例如获取用户信息、手机号转用户ID）
- `WEIXIN_WORK_CONTACTS_SYNC_SECRET` 专门用于用户管理操作（例如 update_user）
- `WEIXIN_WORK_DOC_SECRET` 用于文档相关的 API 操作（例如创建、读取、写入 wedoc）

然后在代码中：

```python
from weixin_work_reborn import WeChatWorkClient, Config

config = Config()  # 自动从 .env 文件加载
client = WeChatWorkClient(config=config)
```

### 环境变量

或者，您可以设置环境变量：

```bash
export WEIXIN_WORK_BASE_URL="https://qyapi.weixin.qq.com/"
export WEIXIN_WORK_CORP_ID="your_corp_id_here"
export WEIXIN_WORK_APP_SECRET="your_app_secret_here"
export WEIXIN_WORK_CONTACTS_SYNC_SECRET="your_contacts_sync_secret_here"
export WEIXIN_WORK_DOC_SECRET="your_doc_secret_here"
export WEIXIN_WORK_AGENT_ID="your_agent_id_here"
```

**注意**: 企业微信 API 针对不同的 API 端点需要不同的密钥：
- `WEIXIN_WORK_APP_SECRET` 用于通用 API 操作（例如获取用户信息、手机号转用户ID）
- `WEIXIN_WORK_CONTACTS_SYNC_SECRET` 专门用于用户管理操作（例如 update_user）
- `WEIXIN_WORK_DOC_SECRET` 用于文档相关的 API 操作（例如创建、读取、写入 wedoc）

## API 参考

### Config

处理从环境变量和 .env 文件加载配置。

#### 构造函数

```python
Config(env_file=None)
```

- `env_file` (str, 可选): 要加载的特定 .env 文件路径

#### 属性

- `base_url` (str): 企业微信 API 的基础 URL (默认: "https://qyapi.weixin.qq.com/")
- `corp_id` (str): 您的企业微信企业 ID
- `corp_secret` (str): 您的应用密钥
- `agent_id` (str): 您的应用代理 ID

### WeChatWorkClient

与企业微信 API 交互的主要客户端类。

#### 构造函数

```python
WeChatWorkClient(config=None, config_file=None, token_cache_size=100, token_cache_ttl=7000)
```

- `config` (Config, 可选): 包含 API 设置的 Config 对象
- `config_file` (str, 可选): .env 文件路径
- `token_cache_size` (int): 令牌缓存大小 (默认: 100)
- `token_cache_ttl` (int): 缓存令牌的生存时间，以秒为单位 (默认: 7000，略低于 7200 秒的令牌过期时间)

#### 方法

##### get_user(user_id)

通过用户 ID 获取用户信息。

- `user_id` (str): 要检索信息的用户 ID
- 返回: 用户信息字典

##### update_user(userid, **kwargs)

更新用户信息。

- `userid` (str): 必需。用户 ID。对应管理控制台中的账号，在企业内必须唯一。不区分大小写，1-64 字节长
- `name` (str, 可选): 成员名称，1-64 个 UTF8 字符
- `alias` (str, 可选): 别名，1-64 个 UTF8 字符
- `mobile` (str, 可选): 手机号。在企业内必须唯一
- `department` (list, 可选): 成员所属部门 ID 列表，最多 100 个
- `order` (list, 可选): 部门内的排序值，默认为 0。提供部门时生效。数字必须与部门匹配，数字越大优先级越高。有效范围 [0, 2^32)
- `position` (str, 可选): 职位信息，0-128 个 UTF8 字符
- `gender` (str, 可选): 性别。1 为男性，2 为女性
- `email` (str, 可选): 邮箱地址。6-64 字节且格式有效，在企业内必须唯一
- `biz_mail` (str, 可选): 如果企业激活了腾讯企业邮（企业微信邮），设置此选项会创建企业邮箱账户。6-63 字节且格式有效，在企业内必须唯一
- `biz_mail_alias` (dict, 可选): 企业邮箱别名。6-63 字节且格式有效，在企业内必须唯一，最多可设置 5 个别名。更新时会覆盖。传递空结构或空数组可清空当前企业邮箱别名
- `telephone` (str, 可选): 座机。由 1-32 个数字、"-"、"+" 或 "," 组成
- `is_leader_in_dept` (list, 可选): 部门负责人字段，数量必须与部门匹配，指示成员是否为部门负责人。0-否，1-是
- `direct_leader` (list, 可选): 直接主管，可设置企业内的成员为直接主管，最多 1 个
- `avatar_mediaid` (str, 可选): 成员头像 mediaid，通过媒体管理 API 上传获取
- `enable` (int, 可选): 启用/禁用成员。1 为启用，0 为禁用
- `extattr` (dict, 可选): 扩展属性。字段需要先在 WEB 管理中添加
- `external_profile` (dict, 可选): 成员的外部属性
- `external_position` (str, 可选): 外部职位。如果设置，用作显示职位，否则使用职位。最多 12 个中文字符
- `nickname` (str, 可选): 视频账号名（设置后，成员在外显时会显示此视频账号）。必须从绑定到企业微信的视频账号中选择，可在"我的企业"页面访问
- `address` (str, 可选): 地址。最多 128 个字符
- `main_department` (int, 可选): 主部门
- 返回: API 响应字典

##### mobile_to_userid(mobile)

将手机号转换为用户 ID。

- `mobile` (str): 要转换的手机号
- 返回: 包含用户 ID 的 API 响应字典

### 文档管理 (WeDoc) 方法

WeChatWorkClient 现在包含全面的文档管理 (WeDoc) 功能。

##### new_document(doc_type, doc_name, spaceid=None, fatherid=None, admin_users=None)

创建新文档、表格或智能表格。

- `doc_type` (int): 文档类型，3: 文档 4: 表格 10: 智能表格
- `doc_name` (str): 文档名称（最多 255 个字符，超出会被截断）
- `spaceid` (str, 可选): 空间 ID。如果指定 `spaceid`，`fatherid` 也必须指定
- `fatherid` (str, 可选): 父目录文件 ID，在根目录时使用 spaceid
- `admin_users` (list, 可选): 作为文档管理员的用户 ID 列表
- 返回: 包含新文档的 docid 和 URL 的 API 响应字典

##### rename_document(new_name, docid=None, formid=None)

重命名现有文档、表格、智能表格或表单。

- `new_name` (str): 文档的新名称（最多 255 个字符，英文=1，中文=2，超出会被截断）
- `docid` (str, 可选): 文档 docid（docid 或 formid 只能指定其中一个），只能修改应用创建的文档
- `formid` (str, 可选): 表单 ID（docid 或 formid 只能指定其中一个），只能修改应用创建的表单
- 返回: API 响应字典

##### delete_document(docid=None, formid=None)

删除现有文档、表格、智能表格或表单。

- `docid` (str, 可选): 文档 docid（docid 或 formid 只能指定其中一个），只能删除应用创建的文档
- `formid` (str, 可选): 表单 ID（docid 或 formid 只能指定其中一个），只能删除应用创建的表单
- 返回: API 响应字典

##### get_document_base_info(docid)

获取文档、表格、智能表格或表单的基本信息。

- `docid` (str): 文档 docid
- 返回: 包含文档详细信息（名称、创建时间、修改时间、类型）的 API 响应字典

##### share_document(docid=None, formid=None)

获取文档、表格、智能表格或表单的共享链接。

- `docid` (str, 可选): 文档 ID（docid 或 formid 只能指定其中一个）
- `formid` (str, 可选): 表单 ID（docid 或 formid 只能指定其中一个）
- 返回: 包含共享 URL 的 API 响应字典

##### edit_document_content(docid, requests, version=None)

批量编辑文档内容，可执行多个操作。

- `docid` (str): 文档 ID
- `requests` (list): 更新操作列表，支持:
  - replace_text: 替换指定位置的文本内容
  - insert_text: 在指定位置插入文本内容
  - delete_content: 删除指定位置的内容
  - insert_image: 在指定位置插入图片
  - insert_page_break: 在指定位置插入分页符
  - insert_table: 在指定位置插入表格
  - insert_paragraph: 在指定位置插入段落
  - update_text_property: 更新指定位置的文本属性
- `version` (int, 可选): 要编辑的文档版本，从获取文档内容 API 获取
- 返回: API 响应字典

##### get_document_data(docid)

从文档获取内容数据。

- `docid` (str): 文档 ID
- 返回: 包含文档内容和版本的 API 响应字典

##### edit_spreadsheet_content(docid, requests)

编辑表格内容，可执行多个操作。

- `docid` (str): 文档 ID
- `requests` (list): 更新操作列表，支持:
  - add_sheet_request: 添加工作表
  - delete_sheet_request: 删除工作表
  - update_range_request: 更新单元格范围内容
  - delete_dimension_request: 删除连续的行或列
- 返回: API 响应字典

##### get_sheet_properties(docid)

获取表格的行/列信息。

- `docid` (str): 在线表格 docid
- 返回: 包含工作表属性的 API 响应字典

##### get_sheet_range_data(docid, sheet_id, range_str)

获取指定范围的表格数据。

- `docid` (str): 在线表格标识符
- `sheet_id` (str): 工作表 ID（唯一标识符）
- `range_str` (str): A1 表示法的查询范围
- 返回: 包含表格数据的 API 响应字典

##### add_smartsheet(docid, title=None, index=None)

向表格添加智能表格。

- `docid` (str): 文档 ID
- `title` (str, 可选): 智能表格标题
- `index` (int, 可选): 智能表格索引
- 返回: 包含表单详情的 API 响应字典

##### delete_smartsheet(docid, sheet_id)

从在线表格删除智能表格。

- `docid` (str): 文档 ID
- `sheet_id` (str): 要删除的智能表格工作表 ID
- 返回: API 响应字典

##### update_smartsheet(docid, sheet_id, title=None)

更新智能表格标题。

- `docid` (str): 文档 ID
- `sheet_id` (str): 要更新的工作表 ID
- `title` (str, 可选): 新工作表标题
- 返回: API 响应字典

##### query_smartsheet(docid, sheet_id=None, need_all_type_sheet=False)

查询智能表格信息。

- `docid` (str): 文档 ID
- `sheet_id` (str, 可选): 要查询的特定工作表 ID
- `need_all_type_sheet` (bool): 获取所有工作表类型。True 包含仪表板和信息页面
- 返回: 包含工作表列表的 API 响应字典

##### add_view(docid, sheet_id, view_title, view_type, property_gantt=None, property_calendar=None)

向智能表格添加视图。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `view_title` (str): 视图标题
- `view_type` (str): 视图类型: "VIEW_TYPE_GRID", "VIEW_TYPE_KANBAN", "VIEW_TYPE_GALLERY", "VIEW_TYPE_GANTT", "VIEW_TYPE_CALENDAR"
- `property_gantt` (dict, 可选): 甘特图视图属性
- `property_calendar` (dict, 可选): 日历视图属性
- 返回: 包含视图详情的 API 响应字典

##### delete_views(docid, sheet_id, view_ids)

从智能表格删除视图。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `view_ids` (list): 要删除的视图 ID 列表
- 返回: API 响应字典

##### update_view(docid, sheet_id, view_id, view_title=None, property_data=None)

更新智能表格中的视图。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `view_id` (str): 要更新的视图 ID
- `view_title` (str, 可选): 新视图标题
- `property_data` (dict, 可选): 视图设置和配置
- 返回: API 响应字典

##### query_views(docid, sheet_id, view_ids=None, offset=0, limit=0)

查询智能表格中的视图。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `view_ids` (list, 可选): 要查询的视图 ID 列表
- `offset` (int): 偏移量，初始值为 0
- `limit` (int): 页大小
- 返回: 包含视图数据的 API 响应字典

##### add_fields(docid, sheet_id, fields)

向智能表格添加字段。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `fields` (list): 字段详情列表
- 返回: 包含字段详情的 API 响应字典

##### delete_fields(docid, sheet_id, field_ids)

从智能表格删除字段。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `field_ids` (list): 要删除的字段 ID 列表
- 返回: API 响应字典

##### update_fields(docid, sheet_id, fields)

更新智能表格中的字段。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `fields` (list): 字段详情列表
- 返回: API 响应字典

##### query_fields(docid, sheet_id, view_id=None, field_ids=None, field_titles=None, offset=0, limit=0)

查询智能表格中的字段。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `view_id` (str, 可选): 视图 ID
- `field_ids` (list, 可选): 要查询的字段 ID 列表
- `field_titles` (list, 可选): 要查询的字段标题列表
- `offset` (int): 偏移量，初始值为 0
- `limit` (int): 页大小
- 返回: 包含字段详情的 API 响应字典

##### add_records(docid, sheet_id, records, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE")

向智能表格添加记录。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `records` (list): 要添加的记录内容列表
- `key_type` (str): 返回记录中的单元格键类型，默认为 "CELL_VALUE_KEY_TYPE_FIELD_TITLE"
- 返回: 包含记录详情的 API 响应字典

##### delete_records(docid, sheet_id, record_ids)

从智能表格删除记录。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `record_ids` (list): 要删除的记录 ID 列表
- 返回: API 响应字典

##### update_records(docid, sheet_id, records, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE")

更新智能表格中的记录。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `records` (list): 要更新的记录列表
- `key_type` (str): 返回记录中的单元格键类型
- 返回: API 响应字典

##### query_records(docid, sheet_id, view_id=None, record_ids=None, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE", field_titles=None, field_ids=None, sort=None, offset=0, limit=0, ver=None, filter_spec=None)

查询智能表格中的记录。

- `docid` (str): 文档 ID
- `sheet_id` (str): 智能表格工作表 ID
- `view_id` (str, 可选): 视图 ID
- `record_ids` (list, 可选): 要查询的记录 ID 列表
- `key_type` (str): 返回记录中的单元格键类型
- `field_titles` (list, 可选): 按字段标题返回指定列
- `field_ids` (list, 可选): 按字段 ID 返回指定列
- `sort` (list, 可选): 对返回的记录进行排序
- `offset` (int): 偏移量，初始值为 0
- `limit` (int): 页大小
- `ver` (int, 可选): 版本号
- `filter_spec` (dict, 可选): 筛选设置
- 返回: 包含记录数据的 API 响应字典

##### add_field_group(docid, sheet_id, name, children)

向智能表格添加字段组。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `name` (str): 组名，不能与现有名称重复
- `children` (list): 组内容列表
- 返回: API 响应字典

##### delete_field_groups(docid, sheet_id, field_group_ids)

从智能表格删除字段组。

- `docid` (str): 文档 ID
- `sheet_id` (str): 工作表 ID
- `field_group_ids` (list): 要删除的组 ID 列表
- 返回: API 响应字典

##### update_field_group(docid, sheet_id, field_group_id, name=None, children=None)

更新智能表格中的字段组。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `field_group_id` (str): 要更新的组 ID
- `name` (str, 可选): 新组名
- `children` (list, 可选): 新组内容列表
- 返回: API 响应字典

##### get_field_groups(docid, sheet_id, offset=0, limit=10)

从智能表格获取字段组。

- `docid` (str): 文档 ID
- `sheet_id` (str): 表格 ID
- `offset` (int): 偏移量，初始值为 0
- `limit` (int): 页大小
- 返回: 包含组详情的 API 响应字典

##### get_document_auth(docid)

获取文档权限信息。

- `docid` (str): 文档 ID
- 返回: 包含权限详情的 API 响应字典

##### modify_document_join_rule(docid, enable_corp_internal=None, corp_internal_auth=None, enable_corp_external=None, corp_external_auth=None, corp_internal_approve_only_by_admin=None, corp_external_approve_only_by_admin=None, ban_share_external=None, update_co_auth_list=None, co_auth_list=None)

修改文档访问规则。

- `docid` (str): 要操作的文档 ID
- `enable_corp_internal` (bool, 可选): 允许企业内成员浏览
- `corp_internal_auth` (int, 可选): 企业内成员权限类型
- `enable_corp_external` (bool, 可选): 允许企业外成员浏览
- `corp_external_auth` (int, 可选): 企业外成员权限类型
- `corp_internal_approve_only_by_admin` (bool, 可选): 企业内成员需要管理员批准
- `corp_external_approve_only_by_admin` (bool, 可选): 企业外成员需要管理员批准
- `ban_share_external` (bool, 可选): 禁止分享到企业外
- `update_co_auth_list` (bool, 可选): 更新特定部门访问列表
- `co_auth_list` (dict, 可选): 要更新的部门访问列表
- 返回: API 响应字典

##### modify_document_member(docid, update_file_member_list=None, del_file_member_list=None)

修改文档成员范围和权限。

- `docid` (str): 要操作的文档 ID
- `update_file_member_list` (list, 可选): 更新成员范围列表
- `del_file_member_list` (list, 可选): 删除成员范围列表
- 返回: API 响应字典

##### modify_document_safety_setting(docid, enable_readonly_copy=None, watermark=None)

修改文档安全设置。

- `docid` (str): 要操作的文档 ID
- `enable_readonly_copy` (bool, 可选): 允许只读成员复制/下载
- `watermark` (dict, 可选): 水印设置
- 返回: API 响应字典

##### query_sheet_privilege(docid, type_, rule_id_list=None)

查询智能表格权限详情。

- `docid` (str): 智能表格 ID
- `type_` (int): 权限规则类型，1:所有成员，2:额外权限
- `rule_id_list` (list, 可选): 要查询的规则 ID 列表
- 返回: 包含权限的 API 响应字典

##### update_sheet_privilege(docid, type_, rule_id=None, name=None, priv_list=None)

更新智能表格权限。

- `docid` (str): 智能表格 ID
- `type_` (int): 权限规则类型，1:所有成员，2:额外
- `rule_id` (int, 可选): type=2 时必需
- `name` (str, 可选): 权限名称
- `priv_list` (list, 可选): 工作表特定权限列表
- 返回: API 响应字典

##### create_rule(docid, name)

创建智能表格额外成员权限。

- `docid` (str): 智能表格 ID
- `name` (str): 权限规则名称，必须唯一
- 返回: 包含规则 ID 的 API 响应字典

##### modify_rule_member(docid, rule_id, add_member_range=None, del_member_range=None)

更新智能表格额外成员权限。

- `docid` (str): 智能表格 ID
- `rule_id` (int): 要更新的规则 ID
- `add_member_range` (dict, 可选): 添加成员
- `del_member_range` (dict, 可选): 删除成员
- 返回: API 响应字典

##### delete_rule(docid, rule_id_list)

删除智能表格额外成员权限。

- `docid` (str): 智能表格 ID
- `rule_id_list` (list): 要删除的规则 ID 列表
- 返回: API 响应字典

##### create_form(form_title, form_desc=None, form_header=None, form_question=None, form_setting=None, spaceid=None, fatherid=None)

创建表单。

- `form_title` (str): 表单标题
- `form_desc` (str, 可选): 表单描述
- `form_header` (str, 可选): 表单头部背景图片 URL
- `form_question` (dict, 可选): 表单问题列表
- `form_setting` (dict, 可选): 表单设置
- `spaceid` (str, 可选): 空间 ID
- `fatherid` (str, 可选): 父目录文件 ID
- 返回: 包含表单 ID 的 API 响应字典

##### modify_form(formid, oper, form_title=None, form_desc=None, form_header=None, form_question=None, form_setting=None)

修改表单。

- `formid` (str): 表单 ID
- `oper` (int): 操作类型。1: 完全修改问题；2: 完全修改设置
- `form_title` (str, 可选): 表单标题（当 oper=1 时）
- `form_desc` (str, 可选): 表单描述（当 oper=1 时）
- `form_header` (str, 可选): 表单头部背景图片 URL（当 oper=1 时）
- `form_question` (dict, 可选): 表单问题列表（当 oper=1 时）
- `form_setting` (dict, 可选): 表单设置（当 oper=2 时）
- 返回: API 响应字典

##### get_form_info(formid)

获取表单信息。

- `formid` (str): 表单 ID
- 返回: 包含表单详情的 API 响应字典

##### get_form_statistic(repeated_id, req_type, start_time=None, end_time=None, limit=None, cursor=None)

表单统计查询。

- `repeated_id` (str): 从 get_form_info 响应获取的表单 repeated_id
- `req_type` (int): 请求类型 1: 仅统计 2: 提交列表 3: 未提交列表
- `start_time` (int, 可选): 提交列表必需，开始时间
- `end_time` (int, 可选): 提交列表必需，结束时间
- `limit` (int, 可选): 分页批量大小
- `cursor` (int, 可选): 分页游标
- 返回: 包含统计信息的 API 响应字典

##### get_form_answer(repeated_id, answer_ids)

获取表单答案。

- `repeated_id` (str): 表单周期 ID
- `answer_ids` (list): 要获取的答案 ID 列表
- 返回: 包含答案的 API 响应字典

### WeDocAPI

企业微信文档 API 客户端，用于管理文档、表格、智能表格和表单。

#### 构造函数

```python
WeDocAPI(access_token)
```

- `access_token` (str): 企业微信 API 认证的访问令牌

#### 方法

##### new_document(doc_type, doc_name, spaceid=None, fatherid=None, admin_users=None)

创建新文档、表格或智能表格。

- `doc_type` (int): 文档类型 (3: 文档, 4: 表格, 10: 智能表格)
- `doc_name` (str): 文档名称（最多 255 个字符）
- `spaceid` (str, 可选): 空间 ID（如果指定，`fatherid` 也必须指定）
- `fatherid` (str, 可选): 父目录文件 ID，在根目录时使用空间 ID
- `admin_users` (List[str], 可选): 作为文档管理员的用户 ID 列表
- 返回: 包含新文档的 docid 和 URL 的 API 响应字典

##### rename_document(new_name, docid=None, formid=None)

重命名现有文档、表格、智能表格或表单。

- `new_name` (str): 文档的新名称（最多 255 个字符）
- `docid` (str, 可选): 文档 ID（docid 或 formid 只能提供其中一个）
- `formid` (str, 可选): 表单 ID（docid 或 formid 只能提供其中一个）
- 返回: API 响应字典

##### delete_document(docid=None, formid=None)

删除现有文档、表格、智能表格或表单。

- `docid` (str, 可选): 文档 ID（docid 或 formid 只能提供其中一个）
- `formid` (str, 可选): 表单 ID（docid 或 formid 只能提供其中一个）
- 返回: API 响应字典

##### get_document_base_info(docid)

获取文档、表格或智能表格的基本信息。

- `docid` (str): 文档 ID
- 返回: 包含文档详细信息（名称、创建时间、修改时间、类型）的 API 响应字典

##### share_document(docid=None, formid=None)

获取文档、表格、智能表格或表单的共享链接。

- `docid` (str, 可选): 文档 ID（docid 或 formid 只能提供其中一个）
- `formid` (str, 可选): 表单 ID（docid 或 formid 只能提供其中一个）
- 返回: 包含共享 URL 的 API 响应字典

##### edit_document_content(docid, requests, version=None)

批量编辑文档内容，可执行多个操作。

- `docid` (str): 文档 ID
- `requests` (List[Dict]): 要执行的编辑操作列表
- `version` (int, 可选): 要编辑的文档版本
- 返回: API 响应字典

##### get_document_data(docid)

从文档获取内容数据。

- `docid` (str): 文档 ID
- 返回: 包含文档内容和版本的 API 响应字典

##### add_smartsheet(docid, title=None, index=None)

向智能表格添加新工作表。

- `docid` (str): 智能表格的文档 ID
- `title` (str, 可选): 新工作表的标题
- `index` (int, 可选): 新工作表的索引位置
- 返回: 包含工作表详情的 API 响应字典

##### add_view(docid, sheet_id, view_title, view_type, property_gantt=None, property_calendar=None)

向智能表格添加新视图。

- `docid` (str): 智能表格的文档 ID
- `sheet_id` (str): 要添加视图的工作表 ID
- `view_title` (str): 新视图的标题
- `view_type` (str): 视图类型 ("VIEW_TYPE_GRID", "VIEW_TYPE_KANBAN", 等)
- `property_gantt` (dict, 可选): 甘特图视图属性
- `property_calendar` (dict, 可选): 日历视图属性
- 返回: 包含视图详情的 API 响应字典

##### add_fields(docid, sheet_id, fields)

向智能表格添加新字段。

- `docid` (str): 智能表格的文档 ID
- `sheet_id` (str): 要添加字段的工作表 ID
- `fields` (List[Dict]): 要添加的字段定义列表
- 返回: 包含字段详情的 API 响应字典

##### add_records(docid, sheet_id, records, key_type="CELL_VALUE_KEY_TYPE_FIELD_TITLE")

向智能表格添加新记录。

- `docid` (str): 智能表格的文档 ID
- `sheet_id` (str): 要添加记录的工作表 ID
- `records` (List[Dict]): 要添加的记录数据列表
- `key_type` (str): 用于字段标识的键类型
- 返回: 包含记录详情的 API 响应字典

##### get_form_info(formid)

获取表单信息。

- `formid` (str): 表单 ID
- 返回: 包含表单详情的 API 响应字典

##### create_form(form_title, form_desc=None, form_header=None, form_question=None, form_setting=None, spaceid=None, fatherid=None)

创建新表单。

- `form_title` (str): 表单标题
- `form_desc` (str, 可选): 表单描述
- `form_header` (str, 可选): 表单头部背景图片 URL
- `form_question` (dict, 可选): 表单问题和设置
- `form_setting` (dict, 可选): 表单行为设置
- `spaceid` (str, 可选): 表单的空间 ID
- `fatherid` (str, 可选): 父目录文件 ID
- 返回: 包含表单 ID 的 API 响应字典

## 示例

更多示例可在 `examples/` 目录中找到：

- `basic_usage.py`: 基本用法示例
- `advanced_usage.py`: 使用环境变量的高级用法
- `modular_demo.py`: 静态模块化架构演示
- `wedoc_examples.py`: 企业微信文档 (wedoc) 使用示例

### 文档管理示例

以下是如何使用 WeChatWorkClient 进行文档管理的快速示例：

```python
from weixin_work_reborn import WeChatWorkClient, Config

# 用配置初始化客户端
config = Config()  # 从 .env 文件或环境变量加载
client = WeChatWorkClient(config=config)

# 创建新文档
result = client.new_document(
    doc_type=3,  # 3 代表文档，4 代表表格，10 代表智能表格
    doc_name="我的新文档"
)
print(f"创建文档ID: {result.get('docid')}")

# 获取文档信息
if 'docid' in result:
    doc_info = client.get_document_base_info(result['docid'])
    print(f"文档信息: {doc_info}")

# 重命名文档
if 'docid' in result:
    rename_result = client.rename_document(
        docid=result['docid'],
        new_name="重命名文档"
    )
    print(f"重命名结果: {rename_result}")

# 分享文档
if 'docid' in result:
    share_result = client.share_document(docid=result['docid'])
    print(f"分享URL: {share_result.get('share_url')}")
```

## 开发

### 设置

1. 克隆仓库
2. 使用 `uv` (或 `pip`) 安装依赖项：
   ```bash
   # 使用 uv (推荐)
   uv venv
   uv pip install -e ".[dev]"
   ```

### 运行测试

```bash
python -m pytest tests/
```

### 代码格式化

```bash
black .
```

## 贡献

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 为新功能添加测试
5. 运行测试套件
6. 提交拉取请求

## 许可证

本项目根据 MIT 许可证授权 - 详情请参见 [LICENSE](LICENSE) 文件。

## 支持

如果遇到任何问题，请在 [GitHub issues 页面](https://github.com/liudonghua123/weixin-work/issues) 上提交错误报告。

## 关于企业微信 API

有关企业微信 API 的更多信息，请访问 [官方文档](https://developer.work.weixin.qq.com/document/path/90197)。