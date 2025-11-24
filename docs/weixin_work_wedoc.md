# 管理文档

新建文档

最后更新：2025/07/16

该接口用于新建文档、表格及智能表格，新建收集表可前往 [收集表管理](#43942) 查看。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/create\_doc?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"spaceid": "SPACEID",
	"fatherid": "FATHERID",
	"doc_type": 3,
	"doc_name": "DOC_NAME",
	"admin_users": ["USERID1", "USERID2", "USERID3"]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| spaceid | string | 否 | 空间spaceid。若指定`spaceid`，则`fatherid`也要同时指定 |
| fatherid | string | 否 | 父目录fileid, 在根目录时为空间spaceid |
| doc\_type | uint32 | 是 | 文档类型, 3:文档 4:表格 10:智能表格 |
| doc\_name | string | 是 | 文档名字（注意：文件名最多填255个字符, 超过255个字符会被截断） |
| admin\_users | string\[\] | 否 | 文档管理员userid |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"url": "URL",
	"docid": "DOCID"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| url | string | 新建文档的访问链接 |
| docid | string | 新建文档的docid。docid仅在创建时返回，需要开发者妥善保存 |


重命名文档

最后更新：2024/10/28

该接口用于对指定文档、表格、智能表格及收集表进行重命名。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/rename\_doc?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"formid": "FORMID",
	"new_name": "NEW_NAME"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 否 | 文档docid（docid、formid只能填其中一个） ，仅可修改应用自己创建的文档 |
| formid | string | 否 | 收集表id（docid、formid只能填其中一个） ，仅可修改应用自己创建的收集表 |
| new\_name | string | 是 | 重命名后的文档名 （注意：文档名最多填255个字符, 英文算1个, 汉字算2个, 超过255个字符会被截断） |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


删除文档

最后更新：2024/10/28

该接口用于删除指定文档、表格、智能表格及收集表进行重命名。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/del\_doc?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"formid": "FORMID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 否 | 文档docid（docid、formid只能填其中一个），仅可删除应用自己创建的文档 |
| formid | string | 否 | 收集表id（docid、formid只能填其中一个），仅可删除应用自己创建的收集表 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


获取文档基础信息

最后更新：2024/05/30

该接口用于获取指定文档、表格、智能表格及收集表的基础信息。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/get\_doc\_base\_info?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档docid |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"doc_base_info": {
		"docid": "DOCID",
		"doc_name": "DOC_NAME",
		"create_time": 1717071093,
		"modify_time": 1717071093,
		"doc_type": 3
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| docid | string | 文档docid |
| doc\_name | string | 文档名字 |
| create\_time | uint64 | 文档创建时间 |
| modify\_time | uint64 | 文档最后修改时间 |
| doc\_type | uint32 | 3: 文档 4: 表格 10:智能表格 |


分享文档

最后更新：2024/05/30

该接口用于获取文档、表格、智能表格及收集表的分享链接。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/doc\_share?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
    "docid":"DOCID",
    "formid": "FORMID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 否 | 文档id（docid、formid只能填其中一个） |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能访问该应用创建的文档

**返回示例**

```json
{
    "errcode":0,
    "errmsg":"ok",
    "share_url":"URL1"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| share\_url | string | 文档分享链接 |


# 管理文档内容

编辑文档内容

最后更新：2025/07/17

目录

-   [编辑文档内容](#%E7%BC%96%E8%BE%91%E6%96%87%E6%A1%A3%E5%86%85%E5%AE%B9)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [UpdateRequest](#updaterequest)
-         [Range](#range)
-         [Location](#location)
-         [ReplaceText](#replacetext)
-         [InsertText](#inserttext)
-         [DeleteContent](#deletecontent)
-         [InsertImage](#insertimage)
-         [InsertPageBreak](#insertpagebreak)
-         [InsertTable](#inserttable)
-         [InsertParagraph](#insertparagraph)
-         [TextProperty](#textproperty)
-         [UpdateTextProperty](#updatetextproperty)

## [](#%E7%BC%96%E8%BE%91%E6%96%87%E6%A1%A3%E5%86%85%E5%AE%B9)编辑文档内容

该接口可以对一个在线文档批量执行多个更新操作。

**注意：**

1.  批量更新请求，若其中有一个操作报错则全部更新操作不生效。
2.  单次批量更新操作数量 <= 30。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/document/batch\_update?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"verison": 10,
	"requests": [
		{
			"insert_text": {
				"text": "text content",
				"location": {
					"index": 10
				}
			}
		},
		{
			"insert_table": {
				"rows": 2,
				"cols": 2,
				"location": {
					"index": 10
				}
			}
		}
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| version | uint32 | 否 | 操作的文档版本, 该参数可以通过获取文档内容接口获得。操作后文档版本将更新一版。要更新的文档版本与最新文档版本相差不能超过100个。 |
| requests | object\[\] | 是 | 更新操作列表，详见 [UpdateRequest](#UpdateRequest) |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

由于请求参数比较复杂，在本节分Object分别说明

### [](#updaterequest)UpdateRequest

更新文档的操作，每个UpdateRequest的Object中能同时填一个字段，填入多个的只会有一个生效  
**示例**

```javascript
{
	"replace_text": {
	},
	"delete_content": {
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| replace\_text | object([ReplaceText](#ReplaceText)) | 替换指定位置文本内容 |
| insert\_text | object([InsertText](#InsertText)) | 在指定位置插入文本内容 |
| delete\_content | object([DeleteContent](#DeleteContent)) | 删除指定位置内容 |
| insert\_image | object([InsertImage](#InsertImage) | 在指定位置插入图片 |
| insert\_page\_break | object([InsertPageBreak](#InsertPageBreak)) | 在指定位置插入分页符 |
| insert\_table | object([InsertTable](#InsertTable)) | 在指定位置插入表格 |
| insert\_paragraph | object([InsertParagraph](#InsertParagraph)) | 在指定位置插入段落 |
| update\_text\_property | object([UpdateTextProperty](#UpdateTextProperty)) | 更新指定位置文本属性 |

### [](#range)Range

表示从start\_index开始的一段范围  
**示例**

```javascript
{
	"start_index": 10,
	"length": 5
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| start\_index | uint32 | 起始位置，从0开始 |
| length | uint32 | 长度 |

### [](#location)Location

标准文档中的一个位置  
**示例**

```javascript
{
	"index": 10
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| index | uint32 | 位置 |

### [](#replacetext)ReplaceText

**示例**

```javascript
{
	"text": "hello world",
	"ranges": [
			{
				"start_index": 10,
				"length": 5
			}
	]
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| text | string | 要替换的文本 |
| ranges | object\[\]([Range](#Range)) | 要替换的文档范围，可同时替换多个位置的文本, rangs个数不超过10。 |

### [](#inserttext)InsertText

插入文本  
**示例**

```javascript
{
	"text": "hello world",
	"location": {
		"index": 10
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| text | string | 要插入的文本 |
| location | object([Location](#Location)) | 插入的位置 |

### [](#deletecontent)DeleteContent

删除指定位置内容  
**示例**

```javascript
{
	"range": {
		"start_index": 10,
		"length": 5
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| range | object([Range](#Range)) | 要删除的范围 |

### [](#insertimage)InsertImage

插入图片  
**示例**

```javascript
{
	"image_id": "https://https://wework.qpic.cn/wwpic/xxxxxx",
	"location": {
		"index": 10
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| image\_id | string | 图片url，通过[上传图片接口](#53863)获得 |
| location | object([Location](#Location)) | 插入的位置 |
| width | uint32 | 图片的宽，单位是像素（px） |
| height | uint32 | 图片的高， 单位是像素（px） |

### [](#insertpagebreak)InsertPageBreak

插入分页符  
**示例**

```javascript
{
	"location": {
		"index": 10
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| location | object([Location](#Location)) | 插入的位置 |

### [](#inserttable)InsertTable

在指定位置插入表格，表格大小限制：

-   行数`<=100`
-   列数`<=60`
-   单元格总数`<=1000`

**示例**

```javascript
{
	"rows": 3,
	"cols": 3,
	"location": {
		"index": 10
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| rows | uint32 | 表格行数 |
| cols | uint32 | 表格列数 |
| location | object([Location](#Location)) | 插入的位置 |

### [](#insertparagraph)InsertParagraph

在指定位置插入段落  
**示例**

```javascript
{
	"location": {
		"index": 10
	}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| location | object([Location](#Location)) | 插入的位置 |

### [](#textproperty)TextProperty

文本属性  
**示例**

```javascript
{
	"bold": true,
	"color": "000000",
	"background_color": "0000FF"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| blod | bool | 是否加粗 |
| color | string | 文字颜色，十六进制RRGGBB格式 |
| background\_color | string | 文字的背景颜色，十六进制RRGGBB 格式 |

### [](#updatetextproperty)UpdateTextProperty

更新指定范围的文本属性  
**示例**

```javascript
{
	"text_property": {
	},
	"ranges": [
	]
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| text\_property | object([TextProperty](#TextProperty)) | 文本属性 |
| ranges | object\[\]([Range](#Range)) | 更新文本属性的范围，ranges个数不超过10 |


获取文档数据

最后更新：2023/10/19

目录

-   [获取文档数据](#%E8%8E%B7%E5%8F%96%E6%96%87%E6%A1%A3%E6%95%B0%E6%8D%AE)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [Node](#node)
-         [Type](#type)
-         [Property](#property)
-         [SectionProperty](#sectionproperty)
-         [PageSize](#pagesize)
-         [PageOrientation](#pageorientation)
-         [PageOrientation](#pageorientation-3)
-         [PageMargins](#pagemargins)
-         [ParagraphProperty](#paragraphproperty)
-         [NumberProperty](#numberproperty)
-         [Spacing](#spacing)
-         [LineSpacingRule](#linespacingrule)
-         [Indent](#indent)
-         [AlignmentType](#alignmenttype)
-         [TextDirection](#textdirection)
-         [RunProperty](#runproperty)
-         [Shading](#shading)
-         [TextVerticalAlign](#textverticalalign)
-         [TableProperty](#tableproperty)
-         [TableWidth](#tablewidth)
-         [TableHorizontalAlignmentType](#tablehorizontalalignmenttype)
-         [TableLayoutType](#tablelayouttype)
-         [TableWidthType](#tablewidthtype)
-         [TableRowProperty](#tablerowproperty)
-         [TableCellProperty](#tablecellproperty)
-         [Borders](#borders)
-         [BorderProperty](#borderproperty)
-         [VerticalAlignment](#verticalalignment)
-         [DrawingProperty](#drawingproperty)
-         [Inline](#inline)
-         [InlinePicture](#inlinepicture)
-         [RelativeRect](#relativerect)
-         [ShapeProperties](#shapeproperties)
-         [Transform2D](#transform2d)
-         [PositiveSize2D](#positivesize2d)
-         [InlineAddon](#inlineaddon)
-         [AddonSourceType](#addonsourcetype)
-         [Anchor](#anchor)
-         [AnchorPicture](#anchorpicture)
-         [PositionHorizontal](#positionhorizontal)
-         [RelativeFromHorizontal](#relativefromhorizontal)
-         [PositionVertical](#positionvertical)
-         [RelativeFromVertical](#relativefromvertical)
-         [WrapSquare](#wrapsquare)
-         [WrapText](#wraptext)

## [](#%E8%8E%B7%E5%8F%96%E6%96%87%E6%A1%A3%E6%95%B0%E6%8D%AE)获取文档数据

该接口用于获取文档数据

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/document/get?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档的docid |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"version": 10,
	"document": {
		...
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| version | uint32 | 文档版本 |
| document | object([Node](#node)) | 文档内容根节点，详见[Node](#node) |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

由于返回结果比较复杂，在本节分Object分别说明

### [](#node)Node

构成文档内容的节点

**示例**

```javascript
{
	"begin": 0,
	"end": 20,
	"property": {
		...
	},
	"type": "Document",
	"children": [
		...
	],
	"text": "text content"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| begin | uint32 | 起始位置 |
| end | uint32 | 结束位置 |
| property | object([Property](#property)) | 该节点的属性 |
| type | string | 节点类型，详见[Type](#type) |
| children | object([Node](#node)) | 子节点 |
| text | string | 文本内容，当节点类型为 Text 时有效 |

### [](#type)Type

Node类型的枚举值描述

**示例**

```javascript
{
	"type": "Document"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| Document | Doc 文档 |
| MainStory | 文档主节点，文档主体内容 |
| Section | 节 |
| Paragraph | 段落 |
| Table | 表格 |
| TableRow | 表格行 |
| TableCell | 表格单元格 |
| Text | 一个具有相同属性集合的文本容器 |
| Drawing | 图形化对象 , 例如图表、图片等 |

### [](#property)Property

节点属性

**示例**

```javascript
{
	"section_property": {...},
	"paragraph_property": {...},
	"run_property": {...},
	"table_property": {...},
	"table_row_property": {...},
	"table_cell_property": {...},
	"drawing_property": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| section\_property | object([SectionProperty](#sectionproperty)) | section 属性 |
| paragraph\_property | object([ParagraphProperty](#paragraphproperty) | 段落属性 |
| run\_property | object([RunProperty](#runproperty)) | 文本属性 |
| table\_property | object([TableProperty](#tableproperty)) | 表格属性 |
| table\_row\_property | object([TableRowProperty](#tablerowproperty)) | 表格行属性 |
| table\_cell\_property | object([TableCellProperty](#tablecellproperty)) | 表格单元属性 |
| drawing\_property | object([DrawingProperty](#drawingproperty)) | drawing 属性 |

### [](#sectionproperty)SectionProperty

**示例**

```javascript
{
  "page_size": {...},
  "page_margins": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| page\_size | object([PageSize](#pagesize)) | 页面尺寸 |
| page\_margins | object([PageMargins](#pagemargins)) | 页边距 |

### [](#pagesize)PageSize

用于描述页面的大小

**示例**

```javascript
{
  "width": 10,
  "height": 10,
  "orientation": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| width | double | 页面宽度 |
| height | double | 页面高度 |
| orientation | object([PageOrientation](#pageorientation)) | 页面方向 |

### [](#pageorientation)PageOrientation

**示例**

```javascript
{
  "width": 10,
  "height": 10,
  "orientation": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| width | double | 页面宽度 |
| height | double | 页面高度 |
| orientation | string | 页面方向，详见[PageOrientation](#pageorientation) |

### [](#pageorientation-3)PageOrientation

页面方向

**示例**

```javascript
{
	"orientation": "PAGE_ORIENTATION_PORTRAIT"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| PAGE\_ORIENTATION\_UNSPECIFIED | 未知 |
| PAGE\_ORIENTATION\_PORTRAIT | 纵向 |
| PAGE\_ORIENTATION\_LANDSCAPE | 横向 |

### [](#pagemargins)PageMargins

页边距，指定了一个 Section 中所有页面的页边距属性

**示例**

```javascript
{
  "top": 10,
  "right": 10,
  "bottom": 10,
  "left": 10
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| top | double | 上边距 |
| right | double | 右边距 |
| bottom | double | 下边距 |
| left | double | 左边距 |

### [](#paragraphproperty)ParagraphProperty

段落属性

**示例**

```javascript
{
  "number_property": {...},
  "spacing": {...},
  "indent": {...},
  "alignment_type": "ALIGNMENT_TYPE_CENTER",
  "text_direction": "TEXT_DIRECTION_RIGHT_TO_LEFT"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| number\_property | object([NumberProperty](#numberproperty)) | 段落的编号属性 |
| spacing | object([Spacing](#spacing)) | 段落间距 |
| indent | object([Indent](#indent)) | 段落缩进 |
| alignment\_type | string | 文字水平方向的对齐类型, 详见[AlignmentType](#44153/alignmenttype) |
| text\_direction | string | 文字方向，详见[TextDirection](#textdirection) |

### [](#numberproperty)NumberProperty

段落的编号属性，描述该段落的项目符号、数字编号

**示例**

```javascript
{
  "nesting_level": 1,
  "number_id": "2"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| nesting\_level | uint32 | 编号缩进层级 |
| number\_id | string | 编号 ID，一个列表中的每个段落编号 ID 相同 |

### [](#spacing)Spacing

段落间距

**示例**

```javascript
{
  "before": 10,
  "after":10,
  "line": 10,
  "line_rule": "LINE_SPACING_RULE_AUTO"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| before | double | 段后间距，单位是像素（px） |
| after | double | 段前间距，单位是像素（px） |
| line | double | 行间距数值，单位是像素（px） |
| line\_rule | [LineSpacingRule](#linespacingrule) | 行间距格式 |

### [](#linespacingrule)LineSpacingRule

行间距规则

**示例**

```javascript
{
	"line_rule": "LINE_SPACING_RULE_AUTO"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| PAGE\_ORIENTATION\_UNSPECIFIED | 未知 |
| LINE\_SPACING\_RULE\_AUTO | 自动 |
| LINE\_SPACING\_RULE\_EXACT | 精确值 |
| LINE\_SPACING\_RULE\_AT\_LEAST | 最小行间距 |

### [](#indent)Indent

段落缩进

**示例**

```javascript
{
  "left": 10,
  "left_chars": 10,
  "right": 10,
  "right_chars": 10,
  "hanging": 10,
  "hanging_chars":10,
  "first_line": 10,
  "first_line_chars": 10,
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| left | double | 缩进左侧，单位是像素（px） |
| left\_chars | uint32 | 缩进左侧字符数，单位 1/20 字符宽度 |
| right | double | 缩进右侧，单位是像素（px） |
| right\_chars | uint32 | 缩进右侧字符数，单位 1/20 字符宽度 |
| hanging | double | 垂直悬挂，单位是像素（px） |
| hanging\_chars | uint32 | 垂直悬挂字符数，单位 1/20 字符宽度 |
| first\_line | double | 首行缩进，单位是像素（px） |
| first\_line\_chars | uint32 | 首行缩进字符数，单位 1/20 字符宽度 |

### [](#alignmenttype)AlignmentType

水平方向对齐类型

**示例**

```javascript
{
	"alignment_type": "ALIGNMENT_TYPE_CENTER"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| ALIGNMENT\_TYPE\_UNSPECIFIED | 未知 |
| ALIGNMENT\_TYPE\_CENTER | 指定文本应以文档中两个文本边距之间的中线为中心 |
| ALIGNMENT\_TYPE\_BOTH | 指定文本应在文档的两个文本边距之间对齐 |
| ALIGNMENT\_TYPE\_DISTRIBUTE | 指定文本应在文档的两个文本边距之间对齐，这种对齐方式会增加一行中每个字符中间的距离 |
| ALIGNMENT\_TYPE\_LEFT | 指定文本对齐文档的左边距 |
| ALIGNMENT\_TYPE\_RIGHT | 指定文本对齐文档的右边距 |

### [](#textdirection)TextDirection

文字方向类型枚举  
**示例**

```javascript
{
	"text_direction": "TEXT_DIRECTION_RIGHT_TO_LEFT"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| TEXT\_DIRECTION\_UNSPECIFIED | 未知 |
| TEXT\_DIRECTION\_RIGHT\_TO\_LEFT | 从右至左 |
| TEXT\_DIRECTION\_LEFT\_TO\_RIGHT | 从左至右 |

### [](#runproperty)RunProperty

text 的属性

**示例**

```javascript
{
  "font": "",
  "bold": false,
  "italics": false, 
  "underline": false,
  "strike": false,
  "color": "0000FF",
  "spacing": 10, 
  "size": 10,
  "shading": {...},
  "vertical_align": "RUN_VERTICAL_ALIGN_BASELINE",
  "is_placeholder": false
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| font | string | 字体 |
| bold | bool | 文字是否加粗 |
| italics | bool | 文字是否斜体表示 |
| underline | bool | 文字是否下划线 |
| strike | bool | 文字是否被删除线贯穿 |
| color | string | 文字的颜色，颜色使用十六进制，RRGGBB格式 |
| spacing | double | 字符的间距 |
| size | double | 文字的大小，单位是半个点（half-points），即 1/144 英寸 |
| shading | object([Shading](#shading)) | 文字阴影 |
| vertical\_align | string | 垂直对齐类型，指出当前字符串是否是上标、下标，详见[TextVerticalAlign](#textverticalalign) |
| is\_placeholder | bool | 本节点是否占位符 |

### [](#shading)Shading

阴影

**示例**

```javascript
{
  "foreground_color": "FFFFFF",
  "background_color": "000000"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| foreground\_color | string | 前景色，颜色使用十六进制RRGGBB 格式 |
| background\_color | string | 背景色，颜色使用十六进制 RRGGBB格式 |

### [](#textverticalalign)TextVerticalAlign

竖直对齐类型枚举  
**示例**

```javascript
{
	"vertical_align": "RUN_VERTICAL_ALIGN_BASELINE"
}
```

**字段说明**

| 枚举值 | 描述 |   |
| --- | --- | --- |
| RUN\_VERTICAL\_ALIGN\_UNSPECIFIED | 0 | 未知 |
| RUN\_VERTICAL\_ALIGN\_BASELINE | 1 | 对齐基线 |
| RUN\_VERTICAL\_ALIGN\_SUPER\_SCRIPT | 2 | 上标 |
| RUN\_VERTICAL\_ALIGN\_SUB\_SCRIPT | 3 | 下标 |

### [](#tableproperty)TableProperty

表格属性，指定了一组表格宽度的属性。这个属性对所有的表格行和表格单元都会生效，但是可以被表格行和表格单元的属性覆盖。

**示例**

```javascript
{
  "table_width": {...},
  "horizontal_alignment_type": "TABLE_HORIZONTAL_ALIGNMENT_TYPE_CENTER",
  "table_layout": "TABLE_LAYOUT_TYPE_FIXED"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| table\_width | object([TableWidth](#tablewidth)) | 表格宽度，指定该表的首选宽度，单位是像素（px） |
| horizontal\_alignment\_type | string | 表格的水平对齐的方式，详见[TableHorizontalAlignmentType](#tablehorizontalalignmenttype) |
| table\_layout | string | 表格布局，详见[TableLayoutType](#tablelayouttype) |

### [](#tablewidth)TableWidth

表格宽度，指定该表的首选宽度。

**示例**

```javascript
{
  "width": 20,
  "type": "TABLE_LAYOUT_TYPE_FIXED"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| width | double | 表格宽度，单位是像素（px） |
| type | string | 表格宽度类型，详见[TableWidthType](#tablewidthtype) |

### [](#tablehorizontalalignmenttype)TableHorizontalAlignmentType

表格的水平对齐的方式

**示例**

```javascript
{
	"horizontal_alignment_type": "TABLE_HORIZONTAL_ALIGNMENT_TYPE_CENTER"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| TABLE\_HORIZONTAL\_ALIGNMENT\_TYPE\_UNSPECIFIED | 未知 |
| TABLE\_HORIZONTAL\_ALIGNMENT\_TYPE\_CENTER | 指定当前表格位于一行的中间位置 |
| TABLE\_HORIZONTAL\_ALIGNMENT\_TYPE\_LEFT | 与文字边缘的左侧对齐 |
| TABLE\_HORIZONTAL\_ALIGNMENT\_TYPE\_START | 与文字边缘的右侧对齐 |

### [](#tablelayouttype)TableLayoutType

表格布局类型枚举

**示例**

```javascript
{
	"table_layout": "TABLE_LAYOUT_TYPE_FIXED"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| TABLE\_LAYOUT\_TYPE\_UNSPECIFIED | 未知 |
| TABLE\_LAYOUT\_TYPE\_FIXED | 固定宽度 |
| TABLE\_LAYOUT\_TYPE\_AUTO\_FIT | 自适应布局 |

### [](#tablewidthtype)TableWidthType

表格宽度类型

**示例**

```javascript
{
	"type": "TABLE_LAYOUT_TYPE_FIXED"
}
```

**字段说明**

| 枚举值 | 描述 |   |
| --- | --- | --- |
| TABLE\_LAYOUT\_TYPE\_UNSPECIFIED | 0 | 未知 |
| TABLE\_LAYOUT\_TYPE\_FIXED | 1 | 固定宽度 |
| TABLE\_LAYOUT\_TYPE\_AUTO\_FIT | 2 | 自适应布局 |

### [](#tablerowproperty)TableRowProperty

表格行属性

**示例**

```javascript
{
  "is_header": false
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| is\_header | bool | 本行是否是表头 |

### [](#tablecellproperty)TableCellProperty

表格单元属性

**示例**

```javascript
{
  "table_cell_borders": {...},
  "vertical_alignment": "VERTICAL_ALIGNMENT_TOP"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| table\_cell\_borders | object([Borders](#borders)) | 边界属性 |
| vertical\_alignment | string | 垂直方向对齐属性，详见[VerticalAlignment](#44153/verticalalignment) |

### [](#borders)Borders

表格单元的边界属性

**示例**

```javascript
{
  "top": {...},
  "left": {...},
  "bottom": {...},
  "right": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| top | object([BorderProperty](#borderproperty)) | 上边界 |
| left | object([BorderProperty](#borderproperty)) | 左边界 |
| bottom | object([BorderProperty](#borderproperty)) | 底部边界 |
| right | object([BorderProperty](#borderproperty)) | 右边界 |

### [](#borderproperty)BorderProperty

边界属性

**示例**

```javascript
{
  "color" : "000000",
  "width" : 3
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| color | string | 边界颜色，颜色使用十六进制RRGGBB格式 |
| width | uint32 | 边界的宽度，单位是像素（px） |

### [](#verticalalignment)VerticalAlignment

垂直方向对齐属性

**示例**

```javascript
{
  "vertical_alignment": "VERTICAL_ALIGNMENT_TOP"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| VERTICAL\_ALIGNMENT\_\_UNSPECIFIED | 未知 |
| VERTICAL\_ALIGNMENT\_TOP | 对齐顶部 |
| VERTICAL\_ALIGNMENT\_CENTER | 居中对齐 |
| VERTICAL\_ALIGNMENT\_BOTH | 自适应对齐 |
| VERTICAL\_ALIGNMENT\_BOTTOM | 对齐底部 |

### [](#drawingproperty)DrawingProperty

**示例**

```javascript
{
  "inline_keyword": {...},
  "anchor": {...},
  "is_placeholder": false
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| inline\_keyword | object([Inline](#inline)) | Drawing 类型中的实体，如一张图片 |
| anchor | object([Anchor](#anchor)) | Drawing 类型中的悬浮实体，如一张图片 |
| is\_placeholder | bool | 此处是否为占位符 |

### [](#inline)Inline

Drawing 类型中的实体，如一张图片

**示例**

```javascript
{
  "picture": {...},
  "addon": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| picture | object([InlinePicture](#inlinepicture)) | 图片内容 |
| addon | object([InlineAddon](#inlineaddon)) | 插件信息 |

### [](#inlinepicture)InlinePicture

**示例**

```javascript
{
  "uri": "https://xxxxxxx",
  "relative_rect": {...},
  "shape": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| relative\_rect | object([RelativeRect](#relativerect)) | 裁剪范围 |
| shape | object([ShapeProperties](#shapeproperties)) | 形状属性 |

### [](#relativerect)RelativeRect

**示例**

```javascript
{
  "left": 75000,
  "top": 75000,
  "right": 75000,
  "bottom": 75000
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| left | uint32 | 距左侧的距离，单位系数是 0.1%（例如：75000 代表 75%） |
| top | uint32 | 距顶部的距离，单位系数是 0.1%（例如：75000 代表 75%） |
| right | uint32 | 距右侧的距离，单位系数是 0.1%（例如：75000 代表 75%） |
| bottom | uint32 | 距底部的距离，单位系数是 0.1%（例如：75000 代表 75% |

### [](#shapeproperties)ShapeProperties

**示例**

```javascript
{
  "transform": {...}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| transform | object([Transform2D](#transform2d)) | 图片变换，图片在文本中的裁剪和旋转信息 |

### [](#transform2d)Transform2D

**示例**

```javascript
{
  "extent":{
    "cx": 100,
    "cy": 100
  },
  "rotation": 600000
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| extent | object([PositiveSize2D](#positivesize2d)) | 边框，单位是像素（px） |
| rotation | int32 | 旋转角度，单位 1/60000 度。正数代表顺时针旋转，负数代表逆时针旋转 |

### [](#positivesize2d)PositiveSize2D

**示例**

```javascript
{
  "cx": 100,
  "cy": 100
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| cx | integer | 图片宽，单位是像素（px） |
| cy | integer | 图片高，单位是像素（px） |

### [](#inlineaddon)InlineAddon

**示例**

```javascript
{
  "addon_id": "ADDON_ID",
  "addon_source": "ADDON_SOURCE_TYPE_NONE"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| addon\_id | string | 插件 ID |
| addon\_source | string | 插件来源，详见[AddonSourceType](#addonsourcetype) |

### [](#addonsourcetype)AddonSourceType

**示例**

```javascript
{
  "addon_source": "ADDON_SOURCE_TYPE_NONE"
}
```

**字段说明**

| 枚举值 | 描述 |   |
| --- | --- | --- |
| ADDON\_SOURCE\_TYPE\_UNSPECIFIED | 0 | 未知 |
| ADDON\_SOURCE\_TYPE\_NONE | 1 | 无 |
| ADDON\_SOURCE\_TYPE\_LATEX | 2 | 公式 |
| ADDON\_SOURCE\_TYPE\_SIGN | 3 | 签名 |
| ADDON\_SOURCE\_TYPE\_SIGN\_BAR | 4 | 签名占位图 |

### [](#anchor)Anchor

Drawing 类型中浮动的实体，如一张图片

**示例**

```javascript
{
  "picture": {...},
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| picture | object([AnchorPicture](#anchorpicture)) | 图片内容 |

### [](#anchorpicture)AnchorPicture

**示例**

```javascript
{
  "uri": "https://xxxxx",
  "relative_rect": {...},
  "shape": {...},
  "position_horizontal": {...},
  "position_vertical": {...},
  "wrap_none": false,
  "wrap_square": false,
  "wrap_top_and_bottom": false,
  "behind_doc": false, 
  "allow_overlap": false
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| relative\_rect | object([RelativeRect](#relativerect)) | 裁剪范围 |
| shape | object([ShapeProperties](#shapeproperties)) | 形状属性 |
| position\_horizontal | object([PositionHorizontal](#positionhorizontal)) | 水平位置 |
| position\_vertical | object([PositionVertical](#positionvertical)) | 竖直位置 |
| wrap\_none | bool | 非文字包围 |
| wrap\_square | object([WrapSquare](#wrapsquare)) | 四周型环绕 |
| wrap\_top\_and\_bottom | bool | 上下型环绕 |
| behind\_doc | bool | 衬于文字下方 |
| allow\_overlap | bool | 允许重叠 |

### [](#positionhorizontal)PositionHorizontal

**示例**

```javascript
{
  "pos_offset": 10,
  "relative_from": "RELATIVE_FROM_HORIZONTAL_MARGIN"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| pos\_offset | int32 | 位置偏移 |
| relative\_from | string | 相对位置类型，详见[RelativeFromHorizontal](#relativefromhorizontal) |

### [](#relativefromhorizontal)RelativeFromHorizontal

**示例**

```javascript
{
  "relative_from": "RELATIVE_FROM_HORIZONTAL_MARGIN"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| RELATIVE\_FROM\_HORIZONTAL\_UNSPECIFIED | 未知 |
| RELATIVE\_FROM\_HORIZONTAL\_MARGIN | 边缘 |
| RELATIVE\_FROM\_HORIZONTAL\_PAGE | 页 |
| RELATIVE\_FROM\_HORIZONTAL\_COLUMN | 列 |
| RELATIVE\_FROM\_HORIZONTAL\_CHARACTER | 字符 |
| RELATIVE\_FROM\_HORIZONTAL\_LEFT\_MARGIN | 左边缘 |
| RELATIVE\_FROM\_HORIZONTAL\_RIGHT\_MARGIN | 右边缘 |
| RELATIVE\_FROM\_HORIZONTAL\_INSIDE\_MARGIN | 内部边缘 |
| RELATIVE\_FROM\_HORIZONTAL\_OUTSIDE\_MARGIN | 外部边缘 |

### [](#positionvertical)PositionVertical

**示例**

```javascript
{
  "pos_offset": 10,
  "relative_from": "RELATIVE_FROM_VERTICAL_MARGIN"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| pos\_offset | int32 | 位置偏移 |
| relative\_from | string | 相对位置类型，详见[RelativeFromVertical](#relativefromvertical) |

### [](#relativefromvertical)RelativeFromVertical

**示例**

```javascript
{
  "relative_from": "RELATIVE_FROM_VERTICAL_MARGIN"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| RELATIVE\_FROM\_VERTICAL\_UNSPECIFIED | 未知 |
| RELATIVE\_FROM\_VERTICAL\_MARGIN | 边缘 |
| RELATIVE\_FROM\_VERTICAL\_PAGE | 页 |
| RELATIVE\_FROM\_VERTICAL\_PARAGRAPH | 段 |
| RELATIVE\_FROM\_VERTICAL\_LINE | 线 |
| RELATIVE\_FROM\_VERTICAL\_TOP\_MARGIN | 顶端边缘 |
| RELATIVE\_FROM\_VERTICAL\_BOTTOM\_MARGIN | 底部边缘 |
| RELATIVE\_FROM\_VERTICAL\_INSIDE\_MARGIN | 内部边缘 |
| RELATIVE\_FROM\_VERTICAL\_OUTSIDE\_MARGIN | 外部边缘 |

### [](#wrapsquare)WrapSquare

**示例**

```javascript
{
  "wrap_text": "WRAP_TEXT_BOTH_SIDES"
}
```

|  |   |   |
| :-- | --- | --- |
| wrap\_text | string | 四周环绕文字类型，详见[WrapText](#wraptext) |

### [](#wraptext)WrapText

**示例**

```javascript
{
  "wrap_text": "WRAP_TEXT_BOTH_SIDES"
}
```

**字段说明**

| 枚举值 | 描述 |
| --- | --- |
| WRAP\_TEXT\_BOTH\_UNSPECIFIED | 未知 |
| WRAP\_TEXT\_BOTH\_SIDES | 两边 |
| WRAP\_TEXT\_LEFT | 左边 |
| WRAP\_TEXT\_RIGHT | 右边 |
| WRAP\_TEXT\_LARGEST | 最大 |


# 管理表格内容

编辑表格内容

最后更新：2025/11/04

目录

-   [编辑表格内容](#%E7%BC%96%E8%BE%91%E8%A1%A8%E6%A0%BC%E5%86%85%E5%AE%B9)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [UpdateRequest](#updaterequest)
-         [AddSheetRequest](#addsheetrequest)
-         [DeleteSheetRequest](#deletesheetrequest)
-         [UpdateRangeRequest](#updaterangerequest)
-         [DeleteDimensionRequest](#deletedimensionrequest)
-         [UpdateResponse](#updateresponse)
-         [AddSheetResponse](#addsheetresponse)
-         [DeleteSheetResponse](#deletesheetresponse)
-         [UpdateRangeResponse](#updaterangeresponse)
-         [DeleteDimensionResponse](#deletedimensionresponse)

## [](#%E7%BC%96%E8%BE%91%E8%A1%A8%E6%A0%BC%E5%86%85%E5%AE%B9)编辑表格内容

该接口可以对一个在线表格批量执行多个更新操作。

**注意：**

1.  批量更新请求中的各个操作会逐个按顺序执行，直到全部执行完成则请求返回，或者其中一个操作报错则不再继续执行后续的操作。
2.  每一个更新操作在执行之前都会做请求校验（包括权限校验、参数校验等等），如果校验未通过则该更新操作会报错并返回，不再执行后续操作。
3.  单次批量更新请求的操作数量 <= 5。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/spreadsheet/batch\_update?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"requests": [
		{
			"add_sheet_request": {}
		},
		{
			"update_range_request": {}
		},
		{
			"delete_dimension_request": {}
		},
		{
			"delete_sheet_request": {}
		}
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| requests | object\[\] | 是 | 更新操作列表，详见 [UpdateRequest](#UpdateRequest) |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"data": {
		"responses": [
			{
				"add_sheet_response": {}
			},
			{
				"update_range_response": {}
			},
			{
				"delete_dimension_response": {}
			},
			{
				"delete_sheet_response": {}
			}
		]
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| data.responses | object\[\] | 结果列表，详见[UpdateResponse](#UpdateResponse) |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

由于请求参数比较复杂，在本节分Object分别说明

### [](#updaterequest)UpdateRequest

更新请求，在一个UpdateRequest的Object中只能填一个操作

**示例**

```javascript
{
	"add_sheet_request": {}
}
```

```javascript
{
	"update_range_request": {}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| :-- | --- | --- |
| add\_sheet\_request | object([AddSheetRequest](#AddSheetRequest)) | 新增工作表 |
| delete\_sheet\_request | object([DeleteSheetRequest](#DeleteSheetRequest) | 删除工作表 |
| update\_range\_request | object([UpdateRangeRequest](#updaterangerequest)) | 更新范围内单元格内容 |
| delete\_dimension\_request | object([DeleteDimensionRequest](#DeleteDimensionRequest)) | 删除表格连续的行或列 |

### [](#addsheetrequest)AddSheetRequest

新增工作表，新增需满足以下限制：

1.  范围列数 `<=200`
2.  范围内的总单元格数量 `<=10000`

**示例**

```javascript
{
			"title": "sheet_name",
			"row_count": 10,
			"column_count": 10
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| :-- | --- | --- |
| title | string | 工作表名称 |
| row\_count | uint32 | 新增工作表的初始行数 |
| column\_count | uint32 | 新增工作表的初始列数 |

### [](#deletesheetrequest)DeleteSheetRequest

删除工作表

**示例**

```javascript
{
			"sheet_id": "AAAAA"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| :-- | --- | --- |
| sheet\_id | string | 工作表唯一标识 |

### [](#updaterangerequest)UpdateRangeRequest

更新范围内单元格内容请求，单次更新的范围大小需满足以下限制：

1.  范围行数 `<=1000`
2.  范围列数 `<=200`
3.  范围内的总单元格数量 `<=10000`

**示例**

```javascript
{
			"sheet_id": "AAAAA",
			"grid_data": {}
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| :-- | --- | --- |
| sheet\_id | string | 工作表唯一标识 |
| grid\_data | object([GridData](#44380/GridData)) | 写入指定区域的数据 |

### [](#deletedimensionrequest)DeleteDimensionRequest

删除表格连续的行（或列）的请求，注意：

1.  该操作会导致表格缩表
2.  删除的范围遵循 `左闭右开` ———— `[start_index,end_index)` ，如果 `end_index <= start_index` 则该请求报错。

**示例**

```javascript
{
			"sheet_id": "AAAAA",
			"dimension": "ROW"
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| :-- | --- | --- |
| sheet\_id | string | 工作表唯一标识 |
| dimension | string | 声明删除的维度为行或者列。详见 [Dimension](#44380/Dimension) |
| start\_index | uint32 | 删除行列的起始序号（从1开始） |
| end\_index | uint32 | 删除行列的终止序号（从1开始） |

### [](#updateresponse)UpdateResponse

更新操作([UpdateRequest](#UpdateRequest)\])对应的响应结构体类型

**示例**

```javascript
{
  "add_sheet_response": {
  },
  "update_range_response": {
  },
  "delete_dimension_response": {
  },
  "delete_sheet_response": {
  }
}
```

**字段说明**

| 字段 | 类型 | 说明 |
| :-- | --- | --- |
| add\_sheet\_response | object([AddSheetResponse](#AddSheetResponse)) | 新增工作表响应结构体 |
| delete\_sheet\_response | object([DeleteSheetResponse](#DeleteSheetResponse) | 删除工作表响应结构体 |
| update\_range\_response | object([UpdateRangeResponse](#UpdateRangeResponse)) | 更新范围内单元格内容响应结构体 |
| delete\_dimension\_response | object([DeleteDimensionResponse](#DeleteDimensionResponse)) | 删除表格连续的行或列响应结构体 |

### [](#addsheetresponse)AddSheetResponse

新增子表操作的请求响应体结构  
**示例**

```javascript
{
	"properties": {
	}
}
```

| 参数名 | 数据类型 | 描述 |
| :-- | --- | --- |
| properties | object([Properties](#44543/Properties)) | 新增子表的属性 |

### [](#deletesheetresponse)DeleteSheetResponse

删除工作表请求的相应结构体

**示例**

```javascript
{
	"sheet_id": "AABBCC"
}
```

| 参数名 | 数据类型 | 描述 |
| :-- | --- | --- |
| sheet\_id | string | 被删除的工作表的唯一标识 |

### [](#updaterangeresponse)UpdateRangeResponse

编辑区域内单元格内容请求响应体结构

**示例**

```javascript
{
	"updated_cells": 10
}
```

| 参数名 | 数据类型 | 描述 |
| :-- | --- | --- |
| updated\_cells | uint32 | 数据更新的成功的单元格数量 |

### [](#deletedimensionresponse)DeleteDimensionResponse

删除表格连续的行（或列），请求响应体结构  
**示例**

```javascript
{
	"deleted": 10
}
```

| 参数名 | 数据类型 | 描述 |
| :-- | --- | --- |
| deleted | integer | 被删除的行数（或列数） |


获取表格行列信息

最后更新：2024/02/04

## [](#%E8%8E%B7%E5%8F%96%E8%A1%A8%E6%A0%BC%E8%A1%8C%E5%88%97%E4%BF%A1%E6%81%AF)获取表格行列信息

该接口用于获取在线表格的工作表、行数、列数等。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/spreadsheet/get\_sheet\_properties?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 在线表格的docid |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"properties": [
		{
			...
		}
	]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| properties | object\[\]([Properties](#Properties)) | 工作表属性 |

**参数详细说明**

**Properties**  
工作表元数据相关的资源描述

**示例**

```javascript
{
	"sheet_id", "ABCDE",
	"title": "XXXXXX",
	"row_count": 100,
	"column_count": 100
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| sheet\_id | string | 工作表ID，工作表的唯一标识 |
| title | string | 工作表名称 |
| row\_count | uint32 | 表格的总行数 |
| column\_count | uint32 | 表格的总列数 |


获取表格数据

最后更新：2024/07/23

目录

-   [获取表格数据](#%E8%8E%B7%E5%8F%96%E8%A1%A8%E6%A0%BC%E6%95%B0%E6%8D%AE)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [GridData](#griddata)
-         [RowData](#rowdata)
-         [CellData](#celldata)
-         [CellValue](#cellvalue)
-         [CellFormat](#cellformat)
-         [TextFormat](#textformat)
-         [Color](#color)
-         [Link](#link)
-         [Dimension](#dimension)
-   [其他](#%E5%85%B6%E4%BB%96)
-         [A1表示法](#a1%E8%A1%A8%E7%A4%BA%E6%B3%95)
-         [字体列表](#%E5%AD%97%E4%BD%93%E5%88%97%E8%A1%A8)

## [](#%E8%8E%B7%E5%8F%96%E8%A1%A8%E6%A0%BC%E6%95%B0%E6%8D%AE)获取表格数据

本接口用于获取指定范围内的在线表格信息，单次查询的范围大小需满足以下限制：

1.  查询范围行数 `<=1000`
2.  查询范围列数 `<=200`
3.  范围内的总单元格数量 `<=10000`

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/spreadsheet/get\_sheet\_range\_data?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"sheet_id": "AABBCC",
	"range": "A1:B2"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 在线表格唯一标识 |
| sheet\_id | string | 是 | 工作表ID，工作表的唯一标识 |
| range | string | 是 | 查询的范围，格式遵循 [A1表示法](#A1%E8%A1%A8%E7%A4%BA%E6%B3%95) |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"data": {
		"result": {
			
		}
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| data.result | object([GridData](#GridData)) | 表格数据 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

由于返回结果比较复杂，在本节分Object分别说明

### [](#griddata)GridData

GridData定义了表格的具体数据内容

**示例**

```javascript
{
	"start_row": 1,
	"start_column": 1,
	"rows": [
		{}, {}
	]
}
```

| 字段名 | 类型 | 描述 |
| :-- | --- | --- |
| start\_row | uint32 | 起始行编号 （从0开始计算） |
| start\_column | uint32 | 起始列编号 （从0开始计算） |
| rows | object\[\]([RowData](#RowData)) | 各行的数据 |

### [](#rowdata)RowData

行数据的资源描述

**示例**

```javascript
{
	"values": [
		{}, {}
	]
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| values | object\[\]([CellData](#CellData)) | 各个单元格的数据内容 |

### [](#celldata)CellData

单元格的信息

**示例**

```javascript
{
	"cell_value": {},
	"cell_format": {}
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| cell\_value | object([CellValue](#CellValue)) | 单元格的数据内容 |
| cell\_format | object([CellFormat](#CellFormat)) | 单元格的样式信息 |

### [](#cellvalue)CellValue

单元格的数据内容，暂时只支持文本、链接，一个CellValue中只能选填一个字段

**示例**

```javascript
{
		"text": "hello world"
}
```

```javascript
{
	"link": {
		"text": "hello world",
		"url": "http://xxxx.com"
	}
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| text | string | 文本内容 |
| link | object([Link](#Link)) | 超链接内容 |

### [](#cellformat)CellFormat

单元格的样式信息

**示例**  

```javascript
{
	"text_format": {}
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| text\_format | object([TextFormat](#TextFormat)) | 文字样式 |

### [](#textformat)TextFormat

文本样式信息

**示例**

```javascript
{
	"font": "Courier New",
	"font_size": 14,
	"bold": false, 
	"italic": false,
	"strikethrough": false,
	"underline": false,
	"color": {}
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| font | string | 字体名称，表格支持的字体类型: [字体列表](#%E5%AD%97%E4%BD%93%E5%88%97%E8%A1%A8) |
| font\_size | uint32 | 字体大小，最大72 |
| bold | bool | 字体加粗 |
| italic | bool | 斜体 |
| strikethrough | bool | 字体删除线 |
| underline | bool | 下划线 |
| color | object([Color](#Color)) | 字体颜色 |

### [](#color)Color

颜色信息，采用 `RGBA` 表示法

**示例**

```javascript
{
	"red": 0,
	"green": 0,
	"blue": 255,
	"alpha": 255
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| red | uint32 | 红色，取值范围：\[0,255\] |
| green | uint32 | 绿色，取值范围：\[0,255\] |
| blue | uint32 | 蓝色，取值范围：\[0,255\] |
| alpha | uint32 | alpha通道，取值范围：\[0,255\]，默认值为255完全不透明 |

### [](#link)Link

超链接的相关信息

**示例**

```javascript
{
	"url": "https://xxxx",
	"text": "Website"
}
```

| 字段名 | 数据类型 | 描述 |
| :-- | --- | --- |
| url | string | 链接url |
| text | string | 链接标题 |

### [](#dimension)Dimension

声明维度属性为行或者列的字符串枚举值

| 枚举值 | 含义 |
| :-- | --- |
| ROW | 行 |
| COLUMN | 列 |

## [](#%E5%85%B6%E4%BB%96)其他

### [](#a1%E8%A1%A8%E7%A4%BA%E6%B3%95)A1表示法

`A1 表示法` 是比较常见的范围表格数据引用的表示方法，可以表示一个左上角坐标到右下角坐标之间的连续区域。示例：

| 表达式 | 含义 |
| :-- | --- |
| `A1:A1` | 表示一个单元格 `A1` |
| `A1:B5` | 从单元格 `A1` 到单元格 `B5` 的区域 |
| `A1:D1` | 第一行的4个单元格，分别为 `A1` 、 `B1` 、 `C1` 、 `D1` |
| `A1:A3` | 第一列的3个单元格，分别为 `A1` 、 `A2` 、 `A3` |
| `B5:A1` | 不合法的表示，因为 `B5` 在 `A1` 的右下方。 |

### [](#%E5%AD%97%E4%BD%93%E5%88%97%E8%A1%A8)字体列表

在线表格api支持开发者设置单元格内的字体，以下是可供选择的字体列表：

-   Microsoft YaHei
-   SimSun
-   SimHei
-   FangSong
-   KaiTi
-   DFKai-SB
-   STFangsong
-   STKaiti
-   STSong
-   NSimSun
-   Microsoft JhengHei
-   PMingLiU
-   Arial
-   Times New Roman
-   Calibri
-   Comic Sans MS
-   Courier New
-   Georgia
-   Microsoft Uighur
-   Impact
-   Trebuchet MS
-   Verdana
-   Aharoni
-   Andalus
-   AngsanaUPC
-   Angsana New
-   Aparajita
-   Arabic Typesetting
-   Arial Black
-   Arial Narrow
-   Batang
-   BatangChe
-   Bookman Old Style
-   Book Antiqua
-   Bradley Hand ITC
-   BrowalliaUPC
-   Browallia New
-   Cambria
-   Cambria Math
-   Candara
-   Century
-   Century Gothic
-   Consolas
-   Constantia
-   Corbel
-   CordiaUPC
-   Cordia New
-   DaunPenh
-   David
-   DilleniaUPC
-   DokChampa
-   Dotum
-   DotumChe
-   Ebrima
-   Estrangelo Edessa
-   EucrosiaUPC
-   Euphemia
-   Franklin Gothic
-   Franklin Gothic Medium
-   FrankRuehl
-   FreesiaUPC
-   Freestyle Script
-   French Script MT
-   Gabriola
-   Gadugi
-   Garamond
-   Gisha
-   Gulim
-   GulimChe
-   Gungsuh
-   GungsuhChe
-   Haettenschweiler
-   IrisUPC
-   Iskoola Pota
-   JasmineUPC
-   Juice ITC
-   Kalinga
-   Kartika
-   Khmer UI
-   KodchiangUPC
-   Kokila
-   Kristen ITC
-   Lao UI
-   Latha
-   Leelawadee
-   Levenim MT
-   LilyUPC
-   Lucida Console
-   Lucida Handwriting
-   Lucida Sans Unicode
-   Malgun Gothic
-   Mangal
-   Marlett
-   Meiryo
-   Meiryo UI
-   Microsoft Himalaya
-   Microsoft JhengHei UI
-   Microsoft JhengHei UI Light
-   Microsoft New Tai Lue
-   Microsoft PhagsPa
-   Microsoft Sans Serif
-   Microsoft Tai Le
-   Microsoft YaHei UI
-   Microsoft YaHei UI Light
-   Microsoft Yi Baiti
-   MingLiU-ExtB
-   MingLiU\_HKSCS-ExtB
-   MingLiU\_HKSCS
-   Miriam
-   Miriam Fixed
-   Mistral
-   Mongolian Baiti
-   Monotype.com
-   Monotype Corsiva
-   MoolBoran
-   MS Gothic
-   MS Mincho
-   MS Outlook
-   MS PGothic
-   MS PMincho
-   MS UI Gothic
-   MT Extra
-   MV Boli
-   Narkisim
-   Nirmala UI
-   Nyala
-   Palatino Linotype
-   Papyrus
-   Plantagenet Cherokee
-   PMingLiU-ExtB
-   Pristina
-   Raavi
-   Rod
-   Sakkal Majalla
-   Segoe Print
-   Segoe Script
-   Segoe UI Symbol
-   Shonar Bangla
-   Shruti
-   Simplified Arabic Fixed
-   Sylfaen
-   Symbol
-   Tahoma
-   Tempus Sans ITC
-   Traditional Arabic
-   Tunga
-   Utsaah
-   Vani
-   Vijaya
-   Vrinda
-   Webdings
-   Wingdings

# 管理智能表格内容

添加子表

最后更新：2024/09/12

目录

-   [添加子表](#%E6%B7%BB%E5%8A%A0%E5%AD%90%E8%A1%A8)

## [](#%E6%B7%BB%E5%8A%A0%E5%AD%90%E8%A1%A8)添加子表

本接口用于在表格的某个位置添加一个智能表，该智能表不存在视图、记录和字段，可以使用 API 在该智能表中添加视图、记录和字段。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/add\_sheet?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"properties": {
		"title": "智能表",
		"index": 3
	}
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| properties | object | 否 | 智能表属性 |
| properties.title | string | 否 | 智能表标题 |
| properties.index | int32 | 否 | 智能表下标 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"properties": {
		"title": "智能表",
		"index": 3,
		"sheet_id": "123abc"
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| properties | object | 智能表属性 |
| properties.sheet\_id | string | 智能表 ID，创建子表时生成的 6 位随机 ID |
| properties.title | string | 智能表标题 |
| properties.index | int32 | 智能表下标 |


删除子表

最后更新：2024/09/12

目录

-   [删除子表](#%E5%88%A0%E9%99%A4%E5%AD%90%E8%A1%A8)

## [](#%E5%88%A0%E9%99%A4%E5%AD%90%E8%A1%A8)删除子表

本接口用于删除在线表格中的某个智能表。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/delete\_sheet?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 删除的Smartsheet 子表 ID |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

更新子表

最后更新：2024/09/12

目录

-   [更新子表](#%E6%9B%B4%E6%96%B0%E5%AD%90%E8%A1%A8)

## [](#%E6%9B%B4%E6%96%B0%E5%AD%90%E8%A1%A8)更新子表

本接口用于修改表格中某个子表的标题。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/update\_sheet?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"properties": {
		"sheet_id": "123abc",
		"title": "XXXX"
	}
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| properties.sheet\_id | string | 是 | 子表 ID |
| properties.title | string | 否 | 子表标题 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

查询子表

最后更新：2025/07/11

目录

-   [查询子表](#%E6%9F%A5%E8%AF%A2%E5%AD%90%E8%A1%A8)

## [](#%E6%9F%A5%E8%AF%A2%E5%AD%90%E8%A1%A8)查询子表

本接口用于查询一篇在线表格中全部智能表信息。  
**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/get\_sheet?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "xxx",
	"need_all_type_sheet":true
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 否 | 指定子表ID查询 |
| need\_all\_type\_sheet | bool | 否 | 获取所有类型子表。为true时可获取包含仪表盘和说明页在内的所有类型的子表 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"sheet_list": [
        {
            "sheet_id": "123abc",
            "title": "XXXX",
            "is_visible": true,
            "type":"smartsheet"
        },
        {
            "sheet_id": "456abc",
            "title": "仪表盘1",
            "is_visible": true,
            "type": "dashboard"
        },
        {
            "sheet_id": "789abc",
            "title": "如何搭建自己的智能表格",
            "is_visible": true,
            "type": "external"
        }
	]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| sheet\_list | object\[\] 智能表信息 |   |
| sheet\_list.sheet\_id | string | 子表id |
| sheet\_list.title | string | 子表名称 |
| sheet\_list.is\_visible | bool | 子表是否可见 |
| sheet\_list.type | string | 子表类型。"dashboard" 仪表盘。"external" 说明页，"smartsheet" 智能表 |


添加视图

最后更新：2025/05/26

目录

-   [添加视图](#%E6%B7%BB%E5%8A%A0%E8%A7%86%E5%9B%BE)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [View](#view)
-         [ViewType](#viewtype)
-         [GanttViewProperty](#ganttviewproperty)
-         [CalendarViewProperty](#calendarviewproperty)

## [](#%E6%B7%BB%E5%8A%A0%E8%A7%86%E5%9B%BE)添加视图

本接口用于在 Smartsheet 中的某个子表里添加一个新视图。单表最多允许有200个视图。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/add\_view?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"view_title": "XXX",
	"view_type": "VIEW_TYPE_GRID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| view\_title | string | 是 | 视图标题 |
| view\_type | string | 是 | 视图类型。见[ViewType](#viewtype) |
| property\_gantt | obect([GanttViewProperty](#ganttviewproperty)) | 否 | 甘特视图属性,添加甘特图时必填 |
| property\_calendar | object([CalendarViewProperty](#calendarviewproperty)) | 否 | 日历视图属性，添加日历视图时必填 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"view": {
		"view_id": "vFYZUS",
		"view_title": "XXX",
		"view_type": "VIEW_TYPE_GRID"
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| view | object([View](#view)) | 添加视图响应 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#view)View

**示例**

```json
{
	"view_id": "vabcde",
	"view_title": "默认视图",
	"view_type": "VIEW_TYPE_GRID"
}
```

视图信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| view\_id | string | 视图 ID |
| view\_title | string | 视图标题 |
| view\_type | string | 视图类型。见[ViewType](#viewtype) |

### [](#viewtype)ViewType

视图类型：

| 枚举类型 | 描述 |
| :-- | --- |
| VEW\_UNKNOWN | 未知类型视图，传递该值不合法 |
| VIEW\_TYPE\_GRID | 表格视图 |
| VIEW\_TYPE\_KANBAN | 看板视图 |
| VIEW\_TYPE\_GALLERY | 画册视图 |
| VIEW\_TYPE\_GANTT | 甘特视图 |
| VIEW\_TYPE\_CALENDAR | 日历视图 |

### [](#ganttviewproperty)GanttViewProperty

甘特设置

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| start\_date\_field\_id | string | 是 | 时间条起点字段ID，只允许日期类型(`FIELD_TYPE_DATE_TIME`)的字段ID |
| end\_date\_field\_id | string | 是 | 时间条终点字段ID，只允许日期类型(`FIELD_TYPE_DATE_TIME`)的字段ID |

### [](#calendarviewproperty)CalendarViewProperty

日历设置

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| start\_date\_field\_id | string | 是 | 时间条起点字段ID，只允许日期类型(`FIELD_TYPE_DATE_TIME`)的字段ID |
| end\_date\_field\_id | string | 是 | 时间条终点字段ID，只允许日期类型(`FIELD_TYPE_DATE_TIME`)的字段ID |


删除视图

最后更新：2024/09/12

目录

-   [删除视图](#%E5%88%A0%E9%99%A4%E8%A7%86%E5%9B%BE)

## [](#%E5%88%A0%E9%99%A4%E8%A7%86%E5%9B%BE)删除视图

本接口用于在 smartsheet 中的某个子表里删除若干个视图。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/delete\_views?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"view_ids": [
		"VIEWID1", "VIEWID2"
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| view\_ids | string\[\] | 是 | 要删除的视图ID列表 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


更新视图

最后更新：2025/08/20

目录

-   [更新视图](#%E6%9B%B4%E6%96%B0%E8%A7%86%E5%9B%BE)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [View](#view)
-         [ViewProperty](#viewproperty)
-         [SortSpec](#sortspec)
-         [GroupSpec](#groupspec)
-         [FilterSpec](#filterspec)
-         [Condition](#condition)
-         [Operator](#operator)
-         [FilterDataTimeValue](#filterdatatimevalue)
-         [DateTimeType](#datetimetype)
-         [ViewColorConfig](#viewcolorconfig)
-         [ViewColorCondition](#viewcolorcondition)
-         [ViewColorConditionType](#viewcolorconditiontype)
-         [ViewColor](#viewcolor)

## [](#%E6%9B%B4%E6%96%B0%E8%A7%86%E5%9B%BE)更新视图

本接口用于更新 Smartsheet 中的某个视图。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/update\_view?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"view_id": "VIEWID",
	"view_title": "XXX",
	"property": {
	}
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| view\_id | string | 是 | 视图ID |
| view\_title | string | 否 | 视图标题 |
| property | object([ViewProperty](#viewproperty)) | 否 | 视图的排序/过滤/分组/填色配置，详见[ViewProperty](#viewproperty) |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"view": {
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| view | object([View](#view)) | 更新成功的视图内容 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#view)View

**示例**

```json
{
	"view_id": "vabcde",
	"view_title": "默认视图",
	"view_type": "VIEW_TYPE_GRID",
	"property": {
	}
}
```

视图信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| view\_id | string | 视图 ID |
| view\_title | string | 视图标题 |
| view\_type | string | 视图类型。见[ViewType](#53110/viewtype) |
| property | object([ViewProperty](#viewproperty)) | 视图属性 |

### [](#viewproperty)ViewProperty

**示例**

```json
{
	"auto_sort": false,
	"sort_spec": {},
	"filter_spec": {},
	"group_spec": {},
	"is_field_stat_enabled": false,
	"field_visibility": {
		"f1gHSR": false,
		"fabcde": false
	},
	"frozen_field_count": 0,
	"color_config": {
		"conditions": [{
			"id": "4840474257",
			"type": "VIEW_COLOR_CONDITION_TYPE_CELL",
			"color": "chromeAmberLighten_5",
			"condition": {
				"field_id": "fRCjJz",
				"field_type": "FIELD_TYPE_TEXT",
				"operator": "OPERATOR_CONTAINS",
				"string_value": {
					"value": [
						"5555"
					]
				}
			}
		}]
	}
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| auto\_sort | bool | 否 | 记录变更后自动重新排序 |
| sort\_spec | object([SortSpec](#sortspec)) | 否 | 排序设置 |
| group\_spec | object([GroupSpec](#groupspec)) | 否 | 分组设置 |
| filter\_spec | object([FilterSpec](#filterspec)) | 否 | 过滤设置 |
| is\_field\_stat\_enabled | bool | 否 | 是否使用数据统计 |
| field\_visibility | object | 否 | 类似map。 key为字段ID, value为布尔值表示是否显示 |
| frozen\_field\_count | int32 | 否 | 冻结列数量，从首列开始 |
| color\_config | object([ViewColorConfig](#viewcolorconfig)) | 否 | 填色设置 |

### [](#sortspec)SortSpec

**示例**

```json
{
	 "sort_infos": [
	 	{
			"field_id": "FIELDID1",
			"desc": false
		},
		{
			"field_id": "FIELDID2",
			"desc": true
		}
	 ]
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| sort\_infos | object\[\] | 否 | 参与排序的字段列表 |
| sort\_infos.field\_id | string | 是 | 字段id |
| sort\_infoes.desc | bool | 否 | 是否降序 |

### [](#groupspec)GroupSpec

**示例**

```json
{
	 "groups": [
	 	{
			"field_id": "FIELDID1",
			"desc": false
		},
		{
			"field_id": "FIELDID2",
			"desc": true
		}
	 ]
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| groups | object\[\] | 否 | 参与分组的字段列表 |
| groups.field\_id | string | 是 | 字段id |
| groups.desc | bool | 否 | 是否降序 |

### [](#filterspec)FilterSpec

**示例**

```json
{
	"conjunction": "CONJUNCTION_AND",
	"conditions": [
	]
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| conjunction | string | 是 | 多个conditions之间是以and(`CONJUNCTION_AND`)还是or(`CONJUNCTION_OR`)进行组合 |
| conditions | object\[\]([Condition](#condition)) | 是 | 判断条件 |

### [](#condition)Condition

**注：不同字段类型支持的筛选不同，需要根据智能表格不同字段类型实际支持的筛选条件进行组合**

**示例1**  
过滤`FIELDID1`字段包含文本`hello world`的记录

```json
{
	"field_id": "FIELDID1",
	"operator": "OPERATOR_CONTAINS",
	"string_value": {
		"value": ["hello world"]
	}
}
```

**示例2**  
过滤`FIELDID2`字段为用户`USERID1`的记录

```json
{
	"field_id": "FIELDID2",
	"operator": "OPERATOR_IS",
	"user_value": {
		"value": ["USERID1"]
	}
}
```

**示例3**  
过滤`FIELDID3`字段为日期`2025年5月14日`的记录

```json
{
	"field_id": "FIELDID3",
	"field_type": "FIELD_TYPE_DATE_TIME",
	"operator": "OPERATOR_IS",
	"date_time_value": {
		"type": "DATE_TIME_TYPE_DETAIL_DATE",
		"value": [
			"1747152000000"
		]
	}
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| field\_id | string | 是 | 字段ID |
| field\_type | stiring | 是 | 字段类型 |
| operator | string | 是 | 判断类型。见[Operator](#operator) |
| string\_value.value | string\[\] | 否 | 文本、网址、电话、邮箱、地理位置、单选、多选等列类型使用。选项列为选项ID；其它为文本值 |
| number\_value.value | double | 否 | 数字、进度列类型使用 |
| bool\_value.value | bool | 否 | 复选框列类型使用 |
| user\_value.value | string\[\] | 否 | 人员、创建人、最后编辑人列类型使用，值为成员ID |
| date\_time\_value | object([FilterDataTimeValue](#filterdatetimevalue)) | 否 | 日期、创建时间、最后编辑时间列类型使用 |

### [](#operator)Operator

| 筛选值判断操作类型 | 说明 |
| :-- | --- |
| OPERATOR\_UNKNOWN | 未知 |
| OPERATOR\_IS | 等于 |
| OPERATOR\_IS\_NOT | 不等于 |
| OPERATOR\_CONTAINS | 包含 |
| OPERATOR\_DOES\_NOT\_CONTAIN | 不包含 |
| OPERATOR\_IS\_GREATER | 大于 |
| OPERATOR\_IS\_GREATER\_OR\_EQUAL | 大于或等于 |
| OPERATOR\_IS\_LESS | 小于 |
| OPERATOR\_IS\_LESS\_OR\_EQUAL | 小于或等于 |
| OPERATOR\_IS\_EMPTY | 为空 |
| OPERATOR\_IS\_NOT\_EMPTY | 不为空 |

### [](#filterdatatimevalue)FilterDataTimeValue

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| type | string | 是 | 日期类型。见[DateTimeType](#datetimetype) |
| value | string\[\] | 是 | 具体日期值，type为具体日期(`DATE_TIME_TYPE_DETAIL_DATE`) |

### [](#datetimetype)DateTimeType

| 日期值类型 | 说明 |
| :-- | --- |
| DATE\_TIME\_TYPE\_DETAIL\_DATE | 具体时间 |
| DATE\_TIME\_TYPE\_TODAY | 今天 |
| DATE\_TIME\_TYPE\_TOMORROW | 明天 |
| DATE\_TIME\_TYPE\_YESTERDAY | 昨天 |
| DATE\_TIME\_TYPE\_CURRENT\_WEEK | 本周 |
| DATE\_TIME\_TYPE\_LAST\_WEEK | 上周 |
| DATE\_TIME\_TYPE\_CURRENT\_MONTH | 本月 |
| DATE\_TIME\_TYPE\_THE\_PAST\_7\_DAYS | 过去 7 天内 |
| DATE\_TIME\_TYPE\_THE\_NEXT\_7\_DAYS | 接下来 7 天内 |
| DATE\_TIME\_TYPE\_LAST\_MONTH | 上月 |
| DATE\_TIME\_TYPE\_THE\_PAST\_30\_DAYS | 过去 30 天内 |
| DATE\_TIME\_TYPE\_THE\_NEXT\_30\_DAYS | 接下来 30 天内 |

### [](#viewcolorconfig)ViewColorConfig

**示例**

```json
{
	"conditions": [
	]
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| conditions | object\[\]([ViewColorCondition](#viewcolorcondition)) | 是 | 判断条件 |

### [](#viewcolorcondition)ViewColorCondition

**示例**

```json
{
	"id": "5599107762",
	"type": "VIEW_COLOR_CONDITION_TYPE_CELL",
	"color": "chromeOrangeLighten_5",
	"condition": {
		"field_id": "fMPZMg",
		"field_type": "FIELD_TYPE_NUMBER",
		"operator": "OPERATOR_IS",
		"number_value": {
			"value": 5
		}
	}
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| id | string | 否 | 填色id，新增时不需要传入，更新时传入 |
| type | string | 是 | 填色类型,见([ViewColorConditionType](#viewcolorconditiontype)) |
| color | string | 是 | 颜色，见([ViewColor](#viewcolor)) |
| conditions | object\[\]([Condition](#condition)) | 是 | 判断条件 |

### [](#viewcolorconditiontype)ViewColorConditionType

| 填色类型 | 说明 |
| :-- | --- |
| VIEW\_COLOR\_CONDITION\_TYPE\_ROW | 行 |
| VIEW\_COLOR\_CONDITION\_TYPE\_COLUMN | 列 |
| VIEW\_COLOR\_CONDITION\_TYPE\_CELL | 单元格 |

### [](#viewcolor)ViewColor

| 颜色值 | 描述 |
| :-- | --- |
| fillColorGray\_5 | 灰色\_5 |
| accentBlueLighten\_5 | 蓝色\_5 |
| chromeCyanLighten\_5 | 青色\_5 |
| chromeMintLighten\_5 | 薄荷色\_5 |
| chromeRedLighten\_5 | 红色\_5 |
| chromeOrangeLighten\_5 | 橙色\_5 |
| chromeAmberLighten\_5 | 琥珀色\_5 |
| chromeVioletLighten\_5 | 紫色\_5 |
| chromePinkLighten\_5 | 粉色\_5 |
| fillColorGray\_4 | 灰色\_4 |
| accentBlueLighten\_4 | 蓝色\_4 |
| chromeCyanLighten\_4 | 青色\_4 |
| chromeMintLighten\_4 | 薄荷色\_4 |
| chromeRedLighten\_4 | 红色\_4 |
| chromeOrangeLighten\_4 | 橙色\_4 |
| chromeAmberLighten\_4 | 琥珀色\_4 |
| chromeVioletLighten\_4 | 紫色\_4 |
| chromePinkLighten\_4 | 粉色\_4 |
| fillColorGray\_3 | 灰色\_3 |
| accentBlueLighten\_3 | 蓝色\_3 |
| chromeCyanLighten\_3 | 青色\_3 |
| chromeMintLighten\_3 | 薄荷色\_3 |
| chromeRedLighten\_3 | 红色\_3 |
| chromeOrangeLighten\_3 | 橙色\_3 |
| chromeAmberLighten\_3 | 琥珀色\_3 |
| chromeVioletLighten\_3 | 紫色\_3 |
| chromePinkLighten\_3 | 粉色\_3 |


查询视图

最后更新：2025/09/03

目录

-   [查询视图](#%E6%9F%A5%E8%AF%A2%E8%A7%86%E5%9B%BE)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [View](#view)
-         [ViewType](#viewtype)
-         [ViewProperty](#viewproperty)
-         [SortSpec](#sortspec)
-         [GroupSpec](#groupspec)
-         [FilterSpec](#filterspec)
-         [Condition](#condition)
-         [FieldType](#fieldtype)
-         [Operator](#operator)
-         [FilterDataTimeValue](#filterdatatimevalue)
-         [DateTimeType](#datetimetype)
-         [ViewColorConfig](#viewcolorconfig)
-         [ViewColorCondition](#viewcolorcondition)
-         [ViewColorConditionType](#viewcolorconditiontype)
-         [ViewColor](#viewcolor)

## [](#%E6%9F%A5%E8%AF%A2%E8%A7%86%E5%9B%BE)查询视图

本接口用于获取 Smartsheet 中某个子表里全部视图信息。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/get\_views?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
    "docid": "DOCID",
    "sheet_id": "ezPcdA",
    "view_ids": [
        "vPpw9C",
        "vfM2tt"
    ],
    "offset": 0,
    "limit": 1
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| view\_ids | string\[\] | 否 | 需要查询的视图 ID 数组 |
| offset | uint32 | 否 | 偏移量，初始值为 0 |
| limit | uint32 | 否 | 分页大小 , 每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，如果总数大于 1000，一次性返回 1000 个视图，当总数小于 1000 时，返回全部视图；limit 最大值为 1000 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "total": 2,
    "has_more": true,
    "next": 1,
    "views": [
    ]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| total | uint32 | 符合筛选条件的视图总数 |
| has\_more | bool | 是否还有更多项 |
| next | uint32 | 下次下一个搜索结果的偏移量 |
| views | Object\[\]([View](#view)) | 视图数据 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#view)View

**示例**

```json
{
    "view_id": "vabcde",
    "view_title": "默认视图",
    "view_type": "VIEW_TYPE_GRID"
}
```

视图信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| view\_id | string | 视图 ID |
| view\_title | string | 视图标题 |
| view\_type | string | 视图类型。见[ViewType](#viewtype) |
| property | object([ViewProperty](#viewproperty)) | 视图属性 |

### [](#viewtype)ViewType

视图类型：

| 枚举类型 | 描述 |
| :-- | --- |
| VEW\_UNKNOWN | 未知类型视图，传递该值不合法 |
| VIEW\_TYPE\_GRID | 表格视图 |
| VIEW\_TYPE\_KANBAN | 看板视图 |
| VIEW\_TYPE\_GALLERY | 画册视图 |
| VIEW\_TYPE\_GANTT | 甘特视图 |

### [](#viewproperty)ViewProperty

**示例**

```json
{
    "auto_sort": false,
    "sort_spec": {},
    "filter_spec": {
    },
    "group_spec": {},
    "is_field_stat_enabled": false,
    "field_visibility": {
        "f1gHSR": false,
        "fabcde": false
    },
    "frozen_field_count": 0,
    "color_config": {
        "conditions": [{
            "id": "4840474257",
            "type": "VIEW_COLOR_CONDITION_TYPE_CELL",
            "color": "chromeAmberLighten_5",
            "condition": {
                "field_id": "fRCjJz",
                "field_type": "FIELD_TYPE_TEXT",
                "operator": "OPERATOR_CONTAINS",
                "string_value": {
                    "value": [
                        "5555"
                    ]
                }
            }
        }]
    }
}
```

**参数说明**

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| auto\_sort | bool | 记录变更后自动重新排序 |
| sort\_spec | object([SortSpec](#sortspec)) | 排序设置 |
| gourp\_spec | object([GroupSpec](#groupspec)) | 分组设置 |
| filter\_spec | object([FilterSpec](#filterspec)) | 过滤设置 |
| is\_field\_stat\_enabled | bool | 是否使用数据统计 |
| field\_visibility | object | 类似map。 key为字段ID, value为布尔值表示是否显示 |
| frozen\_field\_count | int32 | 冻结列数量，从首列开始 |
| color\_config | object([ViewColorConfig](#viewcolorconfig)) | 填色设置 |

### [](#sortspec)SortSpec

**示例**

```json
{
     "sort_infos": [
        {
            "field_id": "FIELDID1",
            "desc": false
        },
        {
            "field_id": "FIELDID2",
            "desc": true
        }
     ]
}
```

**参数说明**

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| sort\_infos | object\[\] | 参与排序的字段列表 |
| sort\_infos.field\_id | string | 字段id |
| sort\_infoes.desc | bool | 是否降序 |

### [](#groupspec)GroupSpec

**示例**

```json
{
     "groups": [
        {
            "field_id": "FIELDID1",
            "desc": false
        },
        {
            "field_id": "FIELDID2",
            "desc": true
        }
     ]
}
```

**参数说明**

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| groups | object\[\] | 参与分组的字段列表 |
| groups.field\_id | string | 字段id |
| groups.desc | bool | 是否降序 |

### [](#filterspec)FilterSpec

**示例**

```json
{
    "conjunction": "CONJUNCTION_AND",
    "conditions": [
    ]
}
```

**参数说明**

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| conjunction | string | 多个conditions之间是以and(`CONJUNCTION_AND`)还是or(`CONJUNCTION_OR`)进行组合 |
| conditions | object\[\]([Condition](#condition)) | 判断条件 |

### [](#condition)Condition

**注：不同字段类型支持的筛选不同，需要根据智能表格不同字段类型实际支持的筛选条件进行组合**

**示例1**  
过滤`FIELDID1`字段包含文本`hello world`的记录

```json
{
    "field_id": "FIELDID1",
    "field_type": "FIELD_TYPE_TEXT",
    "operator": "OPERATOR_CONTAINS",
    "string_value": {
        "value": [
            "hello world"
        ]
    }
}
```

**示例2**  
过滤`FIELDID2`字段为用户`USERID1`的记录

```json
{
    "field_id": "FIELDID2",
    "field_type": "FIELD_TYPE_USER",
    "operator": "OPERATOR_IS",
    "user_value": {
        "value": ["USERID1"]
    }
}
```

**示例3**  
过滤`FIELDID3`字段为日期`2025年5月14日`的记录

```json
{
    "field_id": "FIELDID3",
    "field_type": "FIELD_TYPE_DATE_TIME",
    "operator": "OPERATOR_IS",
    "date_time_value": {
        "type": "DATE_TIME_TYPE_DETAIL_DATE",
        "value": [
            "1747152000000"
        ]
    }
}
```

**参数说明**

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| field\_id | string | 字段ID |
| field\_type | string | 字段类型。见[FieldType](#fieldtype) |
| operator | string | 判断类型。见[Operator](#operator) |
| string\_value.value | string\[\] | 文本、网址、电话、邮箱、地理位置、单选、多选等列类型使用。选项列为选项ID；其它为文本值 |
| number\_value.value | double | 数字、进度列类型使用 |
| bool\_value.value | bool | 复选框列类型使用 |
| user\_value.value | string\[\] | 人员、创建人、最后编辑人列类型使用，值为成员ID |
| date\_time\_value | object([FilterDataTimeValue](#filterdatetimevalue)) | 日期、创建时间、最后编辑时间列类型使用 |

### [](#fieldtype)FieldType

| 字段类型 | 说明 |
| :-- | --- |
| FIELD\_TYPE\_TEXT | 文本 |
| FIELD\_TYPE\_NUMBER | 数字 |
| FIELD\_TYPE\_CHECKBOX | 复选框 |
| FIELD\_TYPE\_DATE\_TIME | 日期 |
| FIELD\_TYPE\_IMAGE | 图片 |
| FIELD\_TYPE\_ATTACHMENT | 文件 |
| FIELD\_TYPE\_USER | 人员 |
| FIELD\_TYPE\_URL | 链接 |
| FIELD\_TYPE\_SELECT | 多选 |
| FIELD\_TYPE\_CREATED\_USER | 创建人 |
| FIELD\_TYPE\_MODIFIED\_USER | 最后编辑人 |
| FIELD\_TYPE\_CREATED\_TIME | 创建时间 |
| FIELD\_TYPE\_MODIFIED\_TIME | 最后编辑时间 |
| FIELD\_TYPE\_PROGRESS | 进度 |
| FIELD\_TYPE\_PHONE\_NUMBER | 电话 |
| FIELD\_TYPE\_EMAIL | 邮箱 |
| FIELD\_TYPE\_SINGLE\_SELECT | 单选 |
| FIELD\_TYPE\_LOCATION | 地理位置 |

### [](#operator)Operator

| 筛选值判断操作类型 | 说明 |
| :-- | --- |
| OPERATOR\_UNKNOWN | 未知 |
| OPERATOR\_IS | 等于 |
| OPERATOR\_IS\_NOT | 不等于 |
| OPERATOR\_CONTAINS | 包含 |
| OPERATOR\_DOES\_NOT\_CONTAIN | 不包含 |
| OPERATOR\_IS\_GREATER | 大于 |
| OPERATOR\_IS\_GREATER\_OR\_EQUAL | 大于或等于 |
| OPERATOR\_IS\_LESS | 小于 |
| OPERATOR\_IS\_LESS\_OR\_EQUAL | 小于或等于 |
| OPERATOR\_IS\_EMPTY | 为空 |
| OPERATOR\_IS\_NOT\_EMPTY | 不为空 |

### [](#filterdatatimevalue)FilterDataTimeValue

| 参数名 | 类型 | 描述 |   |
| :-- | --- | --- | --- |
| type | string | 日期类型。见[DateTimeType](#datetimetype) |   |
| value | string\[\] | 是 | 具体日期值，type为具体日期(`DATE_TIME_TYPE_DETAIL_DATE`)时必填 |

### [](#datetimetype)DateTimeType

| 日期值类型 | 说明 |
| :-- | --- |
| DATE\_TIME\_TYPE\_DETAIL\_DATE | 具体时间 |
| DATE\_TIME\_TYPE\_TODAY | 今天 |
| DATE\_TIME\_TYPE\_TOMORROW | 明天 |
| DATE\_TIME\_TYPE\_YESTERDAY | 昨天 |
| DATE\_TIME\_TYPE\_CURRENT\_WEEK | 本周 |
| DATE\_TIME\_TYPE\_LAST\_WEEK | 上周 |
| DATE\_TIME\_TYPE\_CURRENT\_MONTH | 本月 |
| DATE\_TIME\_TYPE\_THE\_PAST\_7\_DAYS | 过去 7 天内 |
| DATE\_TIME\_TYPE\_THE\_NEXT\_7\_DAYS | 接下来 7 天内 |
| DATE\_TIME\_TYPE\_LAST\_MONTH | 上月 |
| DATE\_TIME\_TYPE\_THE\_PAST\_30\_DAYS | 过去 30 天内 |
| DATE\_TIME\_TYPE\_THE\_NEXT\_30\_DAYS | 接下来 30 天内 |

### [](#viewcolorconfig)ViewColorConfig

**示例**

```json
{
    "conditions": [
    ]
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| conditions | object\[\]([ViewColorCondition](#viewcolorcondition)) | 是 | 判断条件 |

### [](#viewcolorcondition)ViewColorCondition

**示例**

```json
{
    "id": "5599107762",
    "type": "VIEW_COLOR_CONDITION_TYPE_CELL",
    "color": "chromeOrangeLighten_5",
    "condition": {
        "field_id": "fMPZMg",
        "field_type": "FIELD_TYPE_NUMBER",
        "operator": "OPERATOR_IS",
        "number_value": {
            "value": 5
        }
    }
}
```

**参数说明**

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| id | string | 否 | 填色id，新增时不需要传入，更新时传入 |
| type | string | 是 | 填色类型,见([ViewColorConditionType](#viewcolorconditiontype)) |
| color | string | 是 | 颜色，见([ViewColor](#viewcolor)) |
| conditions | object\[\]([Condition](#condition)) | 是 | 判断条件 |

### [](#viewcolorconditiontype)ViewColorConditionType

| 填色类型 | 说明 |
| :-- | --- |
| VIEW\_COLOR\_CONDITION\_TYPE\_ROW | 行 |
| VIEW\_COLOR\_CONDITION\_TYPE\_COLUMN | 列 |
| VIEW\_COLOR\_CONDITION\_TYPE\_CELL | 单元格 |

### [](#viewcolor)ViewColor

| 颜色值 | 描述 |
| :-- | --- |
| fillColorGray\_5 | 灰色\_5 |
| accentBlueLighten\_5 | 蓝色\_5 |
| chromeCyanLighten\_5 | 青色\_5 |
| chromeMintLighten\_5 | 薄荷色\_5 |
| chromeRedLighten\_5 | 红色\_5 |
| chromeOrangeLighten\_5 | 橙色\_5 |
| chromeAmberLighten\_5 | 琥珀色\_5 |
| chromeVioletLighten\_5 | 紫色\_5 |
| chromePinkLighten\_5 | 粉色\_5 |
| fillColorGray\_4 | 灰色\_4 |
| accentBlueLighten\_4 | 蓝色\_4 |
| chromeCyanLighten\_4 | 青色\_4 |
| chromeMintLighten\_4 | 薄荷色\_4 |
| chromeRedLighten\_4 | 红色\_4 |
| chromeOrangeLighten\_4 | 橙色\_4 |
| chromeAmberLighten\_4 | 琥珀色\_4 |
| chromeVioletLighten\_4 | 紫色\_4 |
| chromePinkLighten\_4 | 粉色\_4 |
| fillColorGray\_3 | 灰色\_3 |
| accentBlueLighten\_3 | 蓝色\_3 |
| chromeCyanLighten\_3 | 青色\_3 |
| chromeMintLighten\_3 | 薄荷色\_3 |
| chromeRedLighten\_3 | 红色\_3 |
| chromeOrangeLighten\_3 | 橙色\_3 |
| chromeAmberLighten\_3 | 琥珀色\_3 |
| chromeVioletLighten\_3 | 紫色\_3 |
| chromePinkLighten\_3 | 粉色\_3 |


添加字段

最后更新：2025/06/06

目录

-   [添加字段](#%E6%B7%BB%E5%8A%A0%E5%AD%97%E6%AE%B5)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [AddField](#addfield)
-         [FieldType](#fieldtype)
-         [NumberFieldProperty](#numberfieldproperty)
-         [CheckboxFieldProperty](#checkboxfieldproperty)
-         [DateTimeFieldProperty](#datetimefieldproperty)
-         [AttachmentFieldProperty](#attachmentfieldproperty)
-         [UserFieldProperty](#userfieldproperty)
-         [UrlFieldProperty](#urlfieldproperty)
-         [SelectFieldProperty](#selectfieldproperty)
-         [CreatedTimeFieldProperty](#createdtimefieldproperty)
-         [ModifiedTimeFieldProperty](#modifiedtimefieldproperty)
-         [ProgressFieldProperty](#progressfieldproperty)
-         [SingleSelectFieldProperty](#singleselectfieldproperty)
-         [ReferenceFieldProperty](#referencefieldproperty)
-         [LocationFieldProperty](#locationfieldproperty)
-         [LocationFieldProperty](#locationfieldproperty-3)
-         [AutoNumberFieldProperty](#autonumberfieldproperty)
-         [CurrencyFieldProperty](#currencyfieldproperty)
-         [WwGroupFieldProperty](#wwgroupfieldproperty)
-         [PercentageFieldProperty](#percentagefieldproperty)
-         [BarcodeFieldProperty](#barcodefieldproperty)

## [](#%E6%B7%BB%E5%8A%A0%E5%AD%97%E6%AE%B5)添加字段

本接口用于在智能表中的某个子表里添加一列或多列新字段。单表最多允许有150个字段。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/add\_fields?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"fields": [{
		"field_title": "TITLE",
		"field_type": "FIELD_TYPE_TEXT"
	}]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| fields | object \[\] [(AddFiled)](#addfield) | 是 | 字段详情 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"fields": [{
		"field_id": "FIELDID",
		"field_title": "TITLE",
		"field_type": "FIELD_TYPE_TEXT"
	}]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| fields | object \[\] [(Filed)](#field) | 字段详情 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#addfield)AddField

字段信息：

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHJ4PSI4IiBmaWxsPSIjQjM2NzFEIi8+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04IDNDNy40NDc3MiAzIDcgMy40NDc3MiA3IDRWOEM3IDguNTUyMjggNy40NDc3MiA5IDggOUM4LjU1MjI4IDkgOSA4LjU1MjI4IDkgOFY0QzkgMy40NDc3MiA4LjU1MjI4IDMgOCAzWk04IDExQzcuNDQ3NzIgMTEgNyAxMS40NDc3IDcgMTJDNyAxMi41NTIzIDcuNDQ3NzIgMTMgOCAxM0M4LjU1MjI4IDEzIDkgMTIuNTUyMyA5IDEyQzkgMTEuNDQ3NyA4LjU1MjI4IDExIDggMTFaIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==)注意

字段属性与字段类型是匹配的，一种字段类型对应一种字段属性  

| 参数名 | 类型 | 是否必填 | 描述 |
| :-- | --- | --- | --- |
| field\_title | string | 是 | 字段标题 |
| field\_type | string | 是 | 字段类型，见[FieldType](#53114/fieldtype) ，必须为原属性 |
| property\_number | object([NumberFieldProperty](#53114/numberfieldproperty)) | 是 | `数字` 类型的字段属性 |
| property\_checkbox | object([CheckboxFieldProperty](#53114/checkboxfieldproperty)) | 否 | `复选框` 类型的字段属性 |
| property\_date\_time | object([DateTimeFieldProperty](#53114/datetimefieldproperty)) | 是 | `日期` 类型的字段属性 |
| property\_attachment | object([AttachmentFieldProperty](#53114/attachmentfieldproperty)) | 否 | `文件` 类型的字段属性 |
| property\_user | object([UserFieldProperty](#53114/userfieldproperty)) | 否 | `人员` 类型的字段属性 |
| property\_url | object([UrlFieldProperty](#53114/urlfieldproperty)) | 是 | `超链接` 类型的字段属性 |
| property\_select | object([SelectFieldProperty](#53114/selectfieldproperty)) | 是 | `多选` 类型的字段属性 |
| property\_created\_time | object([CreatedTimeFieldProperty](#53114/createdtimefieldproperty)) | 是 | `创建时间` 类型的字段属性 |
| property\_modified\_time | object([ModifiedTimeFieldProperty](#53114/modifiedtimefieldproperty)) | 是 | `最后编辑时间` 类型的字段属性 |
| property\_progress | object([ProgressFieldProperty](#53114/progressfieldproperty)) | 是 | `进度` 类型的字段属性 |
| property\_single\_select | object([SingleSelectFieldProperty](#53114/singleselectfieldproperty)) | 是 | `单选` 类型的字段属性 |
| property\_reference | object([ReferenceFieldProperty](#53114/referencefieldproperty)) | 是 | `引用` 类型的字段属性 |
| property\_location | object([LocationFieldProperty](#53114/locationfieldproperty)) | 是 | `地理位置` 类型的字段属性 |
| property\_auto\_number | object([AutoNumberFieldProperty](#53114/autonumberfieldproperty)) | 是 | `自动编号` 类型的字段属性 |
| property\_currency | object([CurrencyFieldProperty](#53114/autonumberfieldproperty)) | 是 | `货币` 类型的字段属性 |
| property\_ww\_group | object([WwGroupFieldProperty](#53114/wwgroupfieldproperty)) | 否 | `群` 类型的字段属性 |
| property\_percentage | object([PercentageFieldProperty](#53114/percentagefieldproperty)) | 否 | `百分数` 类型的字段属性 |
| property\_barcode | object([BarcodeFieldProperty](#53114/barcodefieldproperty)) | 否 | `条码` 类型的字段属性 |

### [](#fieldtype)FieldType

| 字段类型 | 说明 |
| --- | --- |
| FIELD\_TYPE\_TEXT | 文本 |
| FIELD\_TYPE\_NUMBER | 数字 |
| FIELD\_TYPE\_CHECKBOX | 复选框 |
| FIELD\_TYPE\_DATE\_TIME | 日期 |
| FIELD\_TYPE\_IMAGE | 图片 |
| FIELD\_TYPE\_ATTACHMENT | 文件 |
| FIELD\_TYPE\_USER | 成员 |
| FIELD\_TYPE\_URL | 超链接 |
| FIELD\_TYPE\_SELECT | 多选 |
| FIELD\_TYPE\_CREATED\_USER | 创建人 |
| FIELD\_TYPE\_MODIFIED\_USER | 最后编辑人 |
| FIELD\_TYPE\_CREATED\_TIME | 创建时间 |
| FIELD\_TYPE\_MODIFIED\_TIME | 最后编辑时间 |
| FIELD\_TYPE\_PROGRESS | 进度 |
| FIELD\_TYPE\_PHONE\_NUMBER | 电话 |
| FIELD\_TYPE\_EMAIL | 邮件 |
| FIELD\_TYPE\_SINGLE\_SELECT | 单选 |
| FIELD\_TYPE\_REFERENCE | 关联 |
| FIELD\_TYPE\_LOCATION | 地理位置 |
| FIELD\_TYPE\_CURRENCY | 货币 |
| FIELD\_TYPE\_WWGROUP | 群 |
| FIELD\_TYPE\_AUTONUMBER | 自动编号 |
| FIELD\_TYPE\_PERCENTAGE | 百分数 |
| FIELD\_TYPE\_BARCODE | 条码 |

### [](#numberfieldproperty)NumberFieldProperty

数字类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| decimal\_places | int([DecimalPlaces](#53117/decimalplaces)) | 表示小数点的位数，即数字精度 |
| use\_separate | bool | 是否使用千位符，设置此属性后数字字段将以英文逗号分隔千分位，如 1,000 |

### [](#checkboxfieldproperty)CheckboxFieldProperty

复选框类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| checked | bool | 新增时是否默认勾选 |

### [](#datetimefieldproperty)DateTimeFieldProperty

日期类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| format | string([Format](#53117/format)) | 设置日期格式 |
| auto\_fill | bool | 新建记录时，是否自动填充时间 |

### [](#attachmentfieldproperty)AttachmentFieldProperty

文件类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| display\_mode | string([DisplayMode](#53117/displaymode)) | 设置日期格式 |

### [](#userfieldproperty)UserFieldProperty

成员类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| is\_multiple | bool | 允许添加多个人员 |
| is\_notified | bool | 添加人员时通知用户，关闭后不通知 |

### [](#urlfieldproperty)UrlFieldProperty

超链接类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string([LinkType](#53117/linktype)) | 超链接展示样式 |

### [](#selectfieldproperty)SelectFieldProperty

多选类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| is\_quick\_add | bool | 是否允许填写时新增选项，用户不需要设置该参数 |
| options | object \[\] \]([Option](#53117/option)) | 多选选项的格式设置 |

### [](#createdtimefieldproperty)CreatedTimeFieldProperty

创建时间类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| format | string([Format](#53117/format)) | 设置日期格式 |

### [](#modifiedtimefieldproperty)ModifiedTimeFieldProperty

最后编辑时间类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| format | string([Format](#53117/format)) | 设置日期格式 |

### [](#progressfieldproperty)ProgressFieldProperty

进度类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| decimal\_places | int([DecimalPlaces](#53117/decimalplaces)) | 小数位数 |

### [](#singleselectfieldproperty)SingleSelectFieldProperty

单选类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| is\_quick\_add | bool | 是否允许填写时新增选项，用户不需要设置该参数 |
| options | object \[\] ([Option](#53117/option)) | 单选选项的格式设置 |

### [](#referencefieldproperty)ReferenceFieldProperty

关联字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| sub\_id | string | 关联的子表id，为空时，表示关联本子表 |
| filed\_id | string | 关联的字段id |
| is\_multiple | bool | 是否允许多选 |
| view\_id | string | 视图id |

### [](#locationfieldproperty)LocationFieldProperty

地理位置字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| input\_type | string([LocationInputType](#53117/locationinputtype)) | 输入类型 |

### [](#locationfieldproperty-3)LocationFieldProperty

地理位置字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| input\_type | string([LocationInputType](#53117/locationinputtype)) | 输入类型 |

### [](#autonumberfieldproperty)AutoNumberFieldProperty

自动编号字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string([NumberType](#53117/numbertype)) | 输入类型 |
| rules | object\[\] ([NumberRule](#53117/numberrule)) | 自定义规则 |
| reformat\_existing\_record | bool | 是否应用于已有编号 |

### [](#currencyfieldproperty)CurrencyFieldProperty

货币类型字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| currency\_type | string([CurrencyType](#53117/currencytype)) | 输入类型 |
| decimal\_places | int([DecimalPlaces](#53117/decimalplaces)) | 表示小数点的位数，即数字精度 |
| use\_separate | bool | 是否使用千位符，设置此属性后数字字段将以英文逗号分隔千分位，如 1,000 |

### [](#wwgroupfieldproperty)WwGroupFieldProperty

群类型的字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| allow\_multiple | bool | 是否允许多个群聊 |

### [](#percentagefieldproperty)PercentageFieldProperty

百分数类型的字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| decimal\_places | int([DecimalPlaces](#53117/decimalplaces)) | 表示小数点的位数，即数字精度 |
| use\_separate | bool | 是否使用千位符，设置此属性后数字字段将以英文逗号分隔千分位，如 1,000 |

### [](#barcodefieldproperty)BarcodeFieldProperty

条码类型的字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| mobile\_scan\_only | bool | 仅限手机扫描录入 |


删除字段

最后更新：2024/09/12

目录

-   [删除字段](#%E5%88%A0%E9%99%A4%E5%AD%97%E6%AE%B5)

## [](#%E5%88%A0%E9%99%A4%E5%AD%97%E6%AE%B5)删除字段

本接口用于删除智能表中的某个子表里的一列或多列字段。。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/delete\_fields?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"field_ids": [
		"FIELDID"
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| field\_ids | string\[\] | 是 | 需要删除的字段id列表 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


更新字段

最后更新：2025/06/06

目录

-   [更新字段](#%E6%9B%B4%E6%96%B0%E5%AD%97%E6%AE%B5)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [UpdateField](#updatefield)

## [](#%E6%9B%B4%E6%96%B0%E5%AD%97%E6%AE%B5)更新字段

本接口用于更新智能中的某个子表里的一个或多个字段的标题和字段属性信息。

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHJ4PSI4IiBmaWxsPSIjQjM2NzFEIi8+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04IDNDNy40NDc3MiAzIDcgMy40NDc3MiA3IDRWOEM3IDguNTUyMjggNy40NDc3MiA5IDggOUM4LjU1MjI4IDkgOSA4LjU1MjI4IDkgOFY0QzkgMy40NDc3MiA4LjU1MjI4IDMgOCAzWk04IDExQzcuNDQ3NzIgMTEgNyAxMS40NDc3IDcgMTJDNyAxMi41NTIzIDcuNDQ3NzIgMTMgOCAxM0M4LjU1MjI4IDEzIDkgMTIuNTUyMyA5IDEyQzkgMTEuNDQ3NyA4LjU1MjI4IDExIDggMTFaIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==)注意

该接口只能更新字段名、字段属性，不能更新字段类型。  

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/update\_fields?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"fields": [{
		"field_id": "FIELD_ID",
		"field_title": "TITLE",
		"field_type": "FIELD_TYPE_TEXT"
	}]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| fields | object \[\][(UpdateField)](#updatefield) | 是 | 字段详情 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"fields": [{
		"field_id": "FIELDID",
		"field_title": "TITLE",
		"field_type": "FIELD_TYPE_TEXT"
	}]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| fields | object \[\][(Field)](#53117/field) | 字段详情 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#updatefield)UpdateField

字段信息：

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHJ4PSI4IiBmaWxsPSIjQjM2NzFEIi8+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04IDNDNy40NDc3MiAzIDcgMy40NDc3MiA3IDRWOEM3IDguNTUyMjggNy40NDc3MiA5IDggOUM4LjU1MjI4IDkgOSA4LjU1MjI4IDkgOFY0QzkgMy40NDc3MiA4LjU1MjI4IDMgOCAzWk04IDExQzcuNDQ3NzIgMTEgNyAxMS40NDc3IDcgMTJDNyAxMi41NTIzIDcuNDQ3NzIgMTMgOCAxM0M4LjU1MjI4IDEzIDkgMTIuNTUyMyA5IDEyQzkgMTEuNDQ3NyA4LjU1MjI4IDExIDggMTFaIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==)注意

字段属性与字段类型是匹配的，一种字段类型对应一种字段属性  
更新时field\_title和property\_number至少需要传一个，field\_title不能被更新为原值  

| 参数名 | 类型 | 是否必填 | 描述 |
| :-- | --- | --- | --- |
| field\_id | string | 是 | 字段 ID，更新字段属性时需要填写该字段，但字段 ID 不能被更新 |
| field\_title | string | 否 | 字段标题，需要更新为的字段标题 |
| field\_type | string | 是 | 字段类型，见[FieldType](#53114/fieldtype) ，必须为原属性 |
| property\_text | object | 否 | `文本` 类型的字段属性为空 |
| property\_number | object([NumberFieldProperty](#53114/numberfieldproperty)) | 否 | `数字` 类型的字段属性 |
| property\_checkbox | object([CheckboxFieldProperty](#53114/checkboxfieldproperty)) | 否 | `复选框` 类型的字段属性 |
| property\_date\_time | object([DateTimeFieldProperty](#53114/datetimefieldproperty)) | 否 | `日期` 类型的字段属性 |
| property\_attachment | object([AttachmentFieldProperty](#53114/attachmentfieldproperty)) | 否 | `文件` 类型的字段属性 |
| property\_user | object([UserFieldProperty](#53114/userfieldproperty)) | 否 | `人员` 类型的字段属性 |
| property\_url | object([UrlFieldProperty](#53114/urlfieldproperty)) | 否 | `超链接` 类型的字段属性 |
| property\_select | object([SelectFieldProperty](#53114/selectfieldproperty)) | 否 | `多选` 类型的字段属性 |
| property\_created\_user | object | 否 | `创建人` 类型的字段属性为空 |
| property\_modified\_user | object | 否 | `最后编辑人` 类型的字段属性为空 |
| property\_created\_time | object([CreatedTimeFieldProperty](#53114/createdtimefieldproperty)) | 否 | `创建时间` 类型的字段属性 |
| property\_modified\_time | object([ModifiedTimeFieldProperty](#53114/modifiedtimefieldproperty)) | 否 | `最后编辑时间` 类型的字段属性 |
| property\_progress | object([ProgressFieldProperty](#53114/progressfieldproperty)) | 否 | `进度` 类型的字段属性 |
| property\_single\_select | object([SingleSelectFieldProperty](#53114/singleselectfieldproperty)) | 否 | `单选` 类型的字段属性 |
| property\_reference | object([PropertyReference](#53114/propertyreference)) | 否 | `引用` 类型的字段属性 |
| property\_location | object([LocationFieldProperty](#53114/locationfieldproperty)) | 否 | `地理位置` 类型的字段属性 |
| property\_auto\_number | object([AutoNumberFieldProperty](#53114/autonumberfieldproperty)) | 否 | `自动编号` 类型的字段属性 |
| property\_currency | object([CurrencyFieldProperty](#53114/autonumberfieldproperty)) | 否 | `货币` 类型的字段属性 |
| property\_ww\_group | object([WwGroupFieldProperty](#53114/wwgroupfieldproperty)) | 否 | `群` 类型的字段属性 |
| property\_percentage | object([PercentageFieldProperty](#53114/percentagefieldproperty)) | 否 | `百分数` 类型的字段属性 |
| property\_barcode | object([BarcodeFieldProperty](#53114/barcodefieldproperty)) | 否 | `条码` 类型的字段属性 |

查询字段

最后更新：2025/11/05

目录

-   [查询字段](#%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [Field](#field)
-         [FieldType](#fieldtype)
-         [NumberFieldProperty](#numberfieldproperty)
-         [CheckboxFieldProperty](#checkboxfieldproperty)
-         [DateTimeFieldProperty](#datetimefieldproperty)
-         [AttachmentFieldProperty](#attachmentfieldproperty)
-         [UserFieldProperty](#userfieldproperty)
-         [UrlFieldProperty](#urlfieldproperty)
-         [SelectFieldProperty](#selectfieldproperty)
-         [CreatedTimeFieldProperty](#createdtimefieldproperty)
-         [ModifiedTimeFieldProperty](#modifiedtimefieldproperty)
-         [ProgressFieldProperty](#progressfieldproperty)
-         [SingleSelectFieldProperty](#singleselectfieldproperty)
-         [ReferenceFieldProperty](#referencefieldproperty)
-         [LocationFieldProperty](#locationfieldproperty)
-         [AutoNumberFieldProperty](#autonumberfieldproperty)
-         [CurrencyFieldProperty](#currencyfieldproperty)
-         [WwGroupFieldProperty](#wwgroupfieldproperty)
-         [PercentageFieldProperty](#percentagefieldproperty)
-         [BarcodeFieldProperty](#barcodefieldproperty)
-         [DecimalPlaces](#decimalplaces)
-         [Format](#format)
-         [LinkType](#linktype)
-         [Option](#option)
-         [Style](#style)
-         [DisplayMode](#displaymode)
-         [LocationInputType](#locationinputtype)
-         [NumberType](#numbertype)
-         [NumberRule](#numberrule)
-         [CreateTimeFormat](#createtimeformat)
-         [NumberRuleType](#numberruletype)
-         [CurrencyType](#currencytype)

## [](#%E6%9F%A5%E8%AF%A2%E5%AD%97%E6%AE%B5)查询字段

本接口用于获取智能表中某个子表下字段信息，该接口可以完成下面三种功能：获取全部字段信息、依据字段名获取对应字段、依据字段 ID 获取对应字段信息。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/get\_fields?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"offset": 0,
	"limit": 10
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| view\_id | string | 否 | 视图 ID |
| field\_ids | string \[\] | 否 | 由字段 ID 组成的 JSON 数组 |
| field\_titles | string \[\] | 否 | 由字段标题组成的 JSON 数组 |
| offset | int | 否 | 偏移量，初始值为 0 |
| limit | int | 否 | 分页大小 , 每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，如果总数大于 1000，一次性返回 1000 个字段，当总数小于 1000 时，返回全部字段；limit 最大值为 1000 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"total": 1,
	"fields": [{
		"field_id": "ID1",
		"field_title": "TITLE1",
		"field_type": "FIELD_TYPE_TEXT"
	}]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| total | Object | 字段总数 |
| fields | object \[\][(Field)](#field) | 字段详情 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#field)Field

字段信息：

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHJ4PSI4IiBmaWxsPSIjQjM2NzFEIi8+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04IDNDNy40NDc3MiAzIDcgMy40NDc3MiA3IDRWOEM3IDguNTUyMjggNy40NDc3MiA5IDggOUM4LjU1MjI4IDkgOSA4LjU1MjI4IDkgOFY0QzkgMy40NDc3MiA4LjU1MjI4IDMgOCAzWk04IDExQzcuNDQ3NzIgMTEgNyAxMS40NDc3IDcgMTJDNyAxMi41NTIzIDcuNDQ3NzIgMTMgOCAxM0M4LjU1MjI4IDEzIDkgMTIuNTUyMyA5IDEyQzkgMTEuNDQ3NyA4LjU1MjI4IDExIDggMTFaIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==)注意

字段属性与字段类型是匹配的，一种字段类型对应一种字段属性  

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| field\_id | string | 字段 ID |
| field\_title | string | 字段标题 |
| field\_type | string | 字段类型，见[FieldType](#fieldtype) |
| property\_number | object([NumberFieldProperty](#numberfieldproperty)) | `数字` 类型的字段属性 |
| property\_checkbox | object([CheckboxFieldProperty](#checkboxfieldproperty)) | `复选框` 类型的字段属性 |
| property\_date\_time | object([DateTimeFieldProperty](#datetimefieldproperty)) | `日期` 类型的字段属性 |
| property\_attachment | object([AttachmentFieldProperty](#attachmentfieldproperty)) | `文件` 类型的字段属性 |
| property\_user | object([UserFieldProperty](#userfieldproperty)) | `人员` 类型的字段属性 |
| property\_url | object([UrlFieldProperty](#urlfieldproperty)) | `超链接` 类型的字段属性 |
| property\_select | object([SelectFieldProperty](#selectfieldproperty)) | `多选` 类型的字段属性 |
| property\_created\_time | object([CreatedTimeFieldProperty](#createdtimefieldproperty)) | `创建时间` 类型的字段属性 |
| property\_modified\_time | object([ModifiedTimeFieldProperty](#modifiedtimefieldproperty)) | `最后编辑时间` 类型的字段属性 |
| property\_progress | object([ProgressFieldProperty](#progressfieldproperty)) | `进度` 类型的字段属性 |
| property\_single\_select | object([SingleSelectFieldProperty](#singleselectfieldproperty)) | `单选` 类型的字段属性 |
| property\_reference | object([PropertyReference](#propertyreference)) | `引用` 类型的字段属性 |
| property\_location | object([LocationFieldProperty](#locationfieldproperty)) | `地理位置` 类型的字段属性 |
| property\_auto\_number | object([AutoNumberFieldProperty](#autonumberfieldproperty)) | `自动编号` 类型的字段属性 |
| property\_currency | object([CurrencyFieldProperty](#autonumberfieldproperty)) | `货币` 类型的字段属性 |
| property\_ww\_group | object([WwGroupFieldProperty](#wwgroupfieldproperty)) | `群` 类型的字段属性 |
| property\_percentage | object([PercentageFieldProperty](#percentagefieldproperty)) | `百分数` 类型的字段属性 |
| property\_barcode | object([BarcodeFieldProperty](#barcodefieldproperty)) | `条码` 类型的字段属性 |

### [](#fieldtype)FieldType

| 字段类型 | 说明 |
| --- | --- |
| FIELD\_TYPE\_TEXT | 文本 |
| FIELD\_TYPE\_NUMBER | 数字 |
| FIELD\_TYPE\_CHECKBOX | 复选框 |
| FIELD\_TYPE\_DATE\_TIME | 日期 |
| FIELD\_TYPE\_IMAGE | 图片 |
| FIELD\_TYPE\_ATTACHMENT | 文件 |
| FIELD\_TYPE\_USER | 成员 |
| FIELD\_TYPE\_URL | 超链接 |
| FIELD\_TYPE\_SELECT | 多选 |
| FIELD\_TYPE\_CREATED\_USER | 创建人 |
| FIELD\_TYPE\_MODIFIED\_USER | 最后编辑人 |
| FIELD\_TYPE\_CREATED\_TIME | 创建时间 |
| FIELD\_TYPE\_MODIFIED\_TIME | 最后编辑时间 |
| FIELD\_TYPE\_PROGRESS | 进度 |
| FIELD\_TYPE\_PHONE\_NUMBER | 电话 |
| FIELD\_TYPE\_EMAIL | 邮件 |
| FIELD\_TYPE\_SINGLE\_SELECT | 单选 |
| FIELD\_TYPE\_REFERENCE | 关联 |
| FIELD\_TYPE\_LOCATION | 地理位置 |
| FIELD\_TYPE\_FORMULA | 公式 |
| FIELD\_TYPE\_CURRENCY | 货币 |
| FIELD\_TYPE\_WWGROUP | 群 |
| FIELD\_TYPE\_AUTONUMBER | 自动编号 |
| FIELD\_TYPE\_PERCENTAGE | 百分数 |
| FIELD\_TYPE\_BARCODE | 条码 |

### [](#numberfieldproperty)NumberFieldProperty

数字类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| decimal\_places | int([DecimalPlaces](#decimalplaces)) | 表示小数点的位数，即数字精度 |
| use\_separate | bool | 是否使用千位符，设置此属性后数字字段将以英文逗号分隔千分位，如 1,000 |

### [](#checkboxfieldproperty)CheckboxFieldProperty

复选框类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| checked | bool | 新增时是否默认勾选 |

### [](#datetimefieldproperty)DateTimeFieldProperty

日期类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| format | string([Format](#format)) | 设置日期格式 |
| auto\_fill | bool | 新建记录时，是否自动填充时间 |

### [](#attachmentfieldproperty)AttachmentFieldProperty

文件类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| display\_mode | string([DisplayMode](#displaymode)) | 展示样式 |

### [](#userfieldproperty)UserFieldProperty

成员类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| is\_multiple | bool | 允许添加多个人员 |
| is\_notified | bool | 添加人员时通知用户，关闭后不通知 |

### [](#urlfieldproperty)UrlFieldProperty

超链接类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string([LinkType](#linktype)) | 超链接展示样式 |

### [](#selectfieldproperty)SelectFieldProperty

多选类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| is\_quick\_add | bool | 是否允许填写时新增选项，用户不需要设置该参数 |
| options | object \[\] \]([Option](#option)) | 多选选项的格式设置 |

### [](#createdtimefieldproperty)CreatedTimeFieldProperty

创建时间类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| format | string([Format](#format)) | 设置日期格式 |

### [](#modifiedtimefieldproperty)ModifiedTimeFieldProperty

最后编辑时间类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| format | string([Format](#format)) | 设置日期格式 |

### [](#progressfieldproperty)ProgressFieldProperty

进度类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| decimal\_places | int([DecimalPlaces](#decimalplaces)) | 小数位数 |

### [](#singleselectfieldproperty)SingleSelectFieldProperty

单选类型字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| is\_quick\_add | bool | 是否允许填写时新增选项，用户不需要设置该参数 |
| options | object \[\] ([Option](#option)) | 单选选项的格式设置 |

### [](#referencefieldproperty)ReferenceFieldProperty

关联字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| sub\_id | string | 关联的子表id，为空时，表示关联本子表 |
| filed\_id | string | 关联的字段id |
| is\_multiple | bool | 是否允许多选 |
| view\_id | string | 视图id |

### [](#locationfieldproperty)LocationFieldProperty

地理位置字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| input\_type | string([LocationInputType](#locationinputtype)) | 输入类型 |

### [](#autonumberfieldproperty)AutoNumberFieldProperty

自动编号字段属性信息：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string([NumberType](#numbertype)) | 输入类型 |
| rules | object\[\] ([NumberRule](#numberrule)) | 自定义规则 |
| reformat\_existing\_record | bool | 是否应用于已有编号 |

### [](#currencyfieldproperty)CurrencyFieldProperty

货币类型字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| currency\_type | string([CurrencyType](#currencytype)) | 输入类型 |
| decimal\_places | int([DecimalPlaces](#53117/decimalplaces)) | 表示小数点的位数，即数字精度 |
| use\_separate | bool | 是否使用千位符，设置此属性后数字字段将以英文逗号分隔千分位，如 1,000 |

### [](#wwgroupfieldproperty)WwGroupFieldProperty

群类型的字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| allow\_multiple | bool | 是否允许多个群聊 |

### [](#percentagefieldproperty)PercentageFieldProperty

百分数类型的字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| decimal\_places | int([DecimalPlaces](#53117/decimalplaces)) | 表示小数点的位数，即数字精度 |
| use\_separate | bool | 是否使用千位符，设置此属性后数字字段将以英文逗号分隔千分位，如 1,000 |

### [](#barcodefieldproperty)BarcodeFieldProperty

条码类型的字段属性

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| mobile\_scan\_only | bool | 仅限手机扫描录入 |

### [](#decimalplaces)DecimalPlaces

小数点后的位数：

| 数值 | 描述 |
| :-- | --- |
| \-1 | 显示原值 |
| 0 | 代表整数 |
| 1 | 精确到小数点后一位（1.0） |
| 2 | 精确到小数点后两位（1.00） |
| 3 | 精确到小数点后三位（1.000） |
| 4 | 精确到小数点后四位（1.0000） |

### [](#format)Format

日期格式：

| 字符串 | 描述 |
| :-- | --- |
| yyyy"年"m"月"d"日" | 2018 年 4 月 20 日 |
| yyyy-mm-dd" | 2018-04-20 |
| yyyy/m/d | 2018/4/20 |
| m"月"d"日" | 4 月 20 日 |
| yyyy"年"m"月"d"日" dddd | 2018 年 4 月 20 日 星期五 |
| yyyy"年"m"月"d"日" hh:mm | 2018 年 4 月 20 日 14:00 |
| yyyy-mm-dd hh:mm | 2018-04-20 14:00 |
| m/d/yyyy | 4/20/2018 |
| d/m/yyyy | 20/4/2018 |

### [](#linktype)LinkType

超链接展示样式可选值：

| 样式 | 描述 |
| :-- | --- |
| LINK\_TYPE\_PURE\_TEXT | 文字 |
| LINK\_TYPE\_ICON\_TEXT | 图标文字 |

### [](#option)Option

Option 参数：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| id | string | 选项 ID |
| text | string | 要填写的选项内容 |
| style | int([Style](#style)) | 选项颜色 |

### [](#style)Style

选项颜色：

| 数值 | 描述 |
| :-- | --- |
| 1 | 浅红1 |
| 2 | 浅橙1 |
| 3 | 浅天蓝1 |
| 4 | 浅绿1 |
| 5 | 浅紫1 |
| 6 | 浅粉红1 |
| 7 | 浅灰1 |
| 8 | 白 |
| 9 | 灰 |
| 10 | 浅蓝1 |
| 11 | 浅蓝2 |
| 12 | 蓝 |
| 13 | 浅天蓝2 |
| 14 | 天蓝 |
| 15 | 浅绿2 |
| 16 | 绿 |
| 17 | 浅红2 |
| 18 | 红 |
| 19 | 浅橙2 |
| 20 | 橙 |
| 21 | 浅黄1 |
| 22 | 浅黄2 |
| 23 | 黄 |
| 24 | 浅紫2 |
| 25 | 紫 |
| 26 | 浅粉红2 |
| 27 | 粉红 |

### [](#displaymode)DisplayMode

展示样式

| 展示样式 | 说明 |
| --- | --- |
| DISPLAY\_MODE\_LIST | 列表样式 |
| DISPLAY\_MODE\_GRID | 宫格样式 |

### [](#locationinputtype)LocationInputType

地理位置输入类型

| 地理位置输入类型 | 说明 |
| --- | --- |
| LOCATION\_INPUT\_TYPE\_MANUAL | 手动输入 |
| LOCATION\_INPUT\_TYPE\_AUTO | 自动定位 |

### [](#numbertype)NumberType

自动编号类型

| 自动编号类型 | 说明 |
| --- | --- |
| NUMBER\_TYPE\_INCR | 自增数字类型 |
| NUMBER\_TYPE\_CUSTOM | 自定义类型 |

### [](#numberrule)NumberRule

| 自动编号规则 | 类型 |  | 说明 |
| --- | --- | --- | --- |
| type | string[NumberRuleType](#numberruletype) | 规则类型 |   |
| value | string | 存放创建时间格式[CreateTimeFormat](#createtimeformat) 或固定字符，自增数字位数 |   |

### [](#createtimeformat)CreateTimeFormat

| 格式 | 说明 |
| --- | --- |
| YYYYMMDD | 20240301 |
| YYYYMM | 202403 |
| MMDD | 0301 |
| YYYY | 2024 |
| MM | 03 |
| DD | 01 |

### [](#numberruletype)NumberRuleType

数字规则类型

| 数字规则类型 | 说明 |
| --- | --- |
| NUMBER\_RULE\_TYPE\_INCR | 自增id |
| NUMBER\_RULE\_TYPE\_FIXED\_CHAR | 固定字符 |
| NUMBER\_RULE\_TYPE\_TIME | 创建时间 |

### [](#currencytype)CurrencyType

货币符号

| 货币符号类型 | 说明 |
| --- | --- |
| CURRENCY\_TYPE\_CNY | 人民币 |
| CURRENCY\_TYPE\_USD | 美元 |
| CURRENCY\_TYPE\_EUR | 欧元 |
| CURRENCY\_TYPE\_GBP | 英镑 |
| CURRENCY\_TYPE\_JPY | 日元 |
| CURRENCY\_TYPE\_KRW | 韩元 |
| CURRENCY\_TYPE\_HKD | 港元 |
| CURRENCY\_TYPE\_MOP | 澳门元 |
| CURRENCY\_TYPE\_TWD | 新台币 |
| CURRENCY\_TYPE\_AED | 阿联酋迪拉姆 |
| CURRENCY\_TYPE\_AUD | 澳大利亚元 |
| CURRENCY\_TYPE\_BRL | 巴西雷亚尔 |
| CURRENCY\_TYPE\_CAD | 加拿大元 |
| CURRENCY\_TYPE\_CHF | 瑞士法郎 |
| CURRENCY\_TYPE\_IDR | 印尼卢比 |
| CURRENCY\_TYPE\_INR | 印度卢比 |
| CURRENCY\_TYPE\_MXN | 墨西哥比索 |
| CURRENCY\_TYPE\_MYR | 马来西亚林吉特 |
| CURRENCY\_TYPE\_PHP | 菲律宾比索 |
| CURRENCY\_TYPE\_PLN | 波兰兹罗提 |
| CURRENCY\_TYPE\_RUB | 俄罗斯卢布 |
| CURRENCY\_TYPE\_SGD | 新加坡元 |
| CURRENCY\_TYPE\_THB | 泰国铢 |
| CURRENCY\_TYPE\_TRY | 土耳其里拉 |
| CURRENCY\_TYPE\_VND | 越南盾 |


添加记录

最后更新：2025/11/06

目录

-   [添加记录](#%E6%B7%BB%E5%8A%A0%E8%AE%B0%E5%BD%95)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [CellValueKeyType](#cellvaluekeytype)
-         [AddRecord](#addrecord)
-         [CommonRecord](#commonrecord)
-         [Value](#value)
-         [CellTextValue](#celltextvalue)
-         [CellImageValue](#cellimagevalue)
-         [CellAttachmentValue](#cellattachmentvalue)
-         [CellUserValue](#celluservalue)
-         [CellUrlValue](#cellurlvalue)
-         [Option](#option)
-         [CellLocationValue](#celllocationvalue)

## [](#%E6%B7%BB%E5%8A%A0%E8%AE%B0%E5%BD%95)添加记录

本接口用于在 Smartsheet 中的某个子表里添加一行或多行新记录。单表最多允许有100000行记录，15000000个单元格。  
**注意**  
不能通过添加记录接口给创建时间、最后编辑时间、创建人和最后编辑人四种类型的字段添加记录。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/add\_records?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"key_type": "CELL_VALUE_KEY_TYPE_FIELD_TITLE",
	"records": [{
		"values": {
			"FIELD_TITLE": [{
				"type": "text",
				"text": "文本内容"
			}]
		}
	}]
}
```

或

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"key_type": "CELL_VALUE_KEY_TYPE_FIELD_ID",
	"records": [{
		"values": {
			"FIELD_ID": [{
				"type": "text",
				"text": "文本内容"
			}]
		}
	}]
}
```

-   FIELD\_TITLE和FIELD\_ID需要替换为字段标题或者字段ID

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| key\_type | string([CellValueKeyType](#cellvaluekeytype)) | 否 | 返回记录中单元格的key类型，默认用标题 |
| records | Object\[\]([AddRecord](#addrecord)) | 是 | 需要添加的记录的具体内容组成的 JSON 数组 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "records": [
			
    ]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| records | Object\[\]([CommonRecord](#commonrecord)) | 由添加成功的记录的具体内容组成的 JSON 数组 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#cellvaluekeytype)CellValueKeyType

记录([CommonRecord](#commonrecord) 或 [AddRecord](#addrecord))中key的类型

| 枚举类型 | 描述 |
| :-- | --- |
| CELL\_VALUE\_KEY\_TYPE\_FIELD\_TITLE | key用字段标题表示 |
| CELL\_VALUE\_KEY\_TYPE\_FIELD\_ID | key用字段 ID 表示 |

### [](#addrecord)AddRecord

添加记录：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| values | Object | 记录的具体内容，key 为字段标题或字段 ID ，value 详见([Value](#value)) |

### [](#commonrecord)CommonRecord

在 Smartsheet 的某个表格中添加记录响应、更新记录请求和更新记录响应的通用参数：

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| record\_id | string | 记录 ID |
| values | Object | 记录的具体内容，key 为字段标题或字段 ID ，value 详见([Value](#value)) |

### [](#value)Value

各种类型的字段对应的单元格的值

| 字段类型 | 单元格值类型 | 描述 |
| :-- | --- | --- |
| 文本(FIELD\_TYPE\_TEXT) | Object\[\]([CellTextValue](#celltextvalue)) |   |
| 数字(FIELD\_TYPE\_NUMBER) | double |   |
| 复选框(FIELD\_TYPE\_CHECKBOX) | bool |   |
| 日期(FIELD\_TYPE\_DATE\_TIME) | string(以毫秒为单位的unix时间戳) |   |
| 图片(FIELD\_TYPE\_IMAGE) | Object\[\]([CellImageValue](#cellimagevalue)) |   |
| 文件(FIELD\_TYPE\_ATTACHMENT) | Object\[\]([CellAttachmentValue](#cellattchmentvalue)) |   |
| 成员(FIELD\_TYPE\_USER) | Object\[\]([CellUserValue](#celluservalue)) |   |
| 链接(FIELD\_TYPE\_URL) | Object\[\]([CellUrlValue](#cellurlvalue)) | 数组类型为预留能力，目前只支持展示一个链接，建议只传入一个链接 |
| 多选(FIELD\_TYPE\_SELECT) | Object\[\]([Option](#option)) |   |
| 进度(FIELD\_TYPE\_PROGRESS) | double |   |
| 电话(FIELD\_TYPE\_PHONE\_NUMBER) | string |   |
| 邮箱(FIELD\_TYPE\_EMAIL) | string |   |
| 单选(FIELD\_TYPE\_SINGLE\_SELECT) | Object\[\]([Option](#option)) |   |
| 地理位置(FIELD\_TYPE\_LOCATION) | Object\[\]([CellLocationValue](#celllocationvalue)) | 长度不大于1的数组。 |
| 货币(FIELD\_TYPE\_CURRENCY) | double |  |
| 百分数(FIELD\_TYPE\_PERCENTAGE) | double |  |

### [](#celltextvalue)CellTextValue

文本类型字段的单元值类型

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string | 内容为文本(值为`text`)、内容为链接(值为`url`) |
| text | string | 单元格内容 |
| link | string | 当type时`url`时，表示链接跳转url |

### [](#cellimagevalue)CellImageValue

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| id | string | 图片 ID,自定义id |
| title | string | 图片标题 |
| image\_url | string | 图片链接，通过[上传图片](#53863)接口获取 |
| width | int32 | 图片宽度 |
| height | int32 | 图片高度 |

### [](#cellattachmentvalue)CellAttachmentValue

**示例**

```json
{
	"doc_type": 2,
	"file_ext": "SMARTSHEET",
	"file_id": "FILEID",
	"file_type": "70",
	"file_url": "https://doc.weixin.qq.com/smartsheet/xxx",
	"name": "智能表格",
	"size": 3267
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| name | string | 文件名 |
| size | int32 | 文件大小 |
| file\_ext | string | 文件扩展名。文件夹为空，文件为对应文件拓展名，收集表为FORM，文档为DOC，表格为SHEET，幻灯片为SLIDE，思维导图为MIND，流程图为FLOWCHART，智能表为SMARTSHEET |
| file\_id | string | 文件ID |
| file\_url | string | 文件url ，如果是微盘文档则通过[获取分享链接](#44667)获得，如果是文档，则为文档url |
| file\_type | string | 文件类型。文件夹为Folder，微盘文件为Wedrive，收集表为30，文档为50，表格是51，幻灯片为52，思维导图为54，流程图为55，智能表为70 |
| doc\_type | string | 文件类型，用于区分文件夹和文件 |

### [](#celluservalue)CellUserValue

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| user\_id | string | 成员ID |

### [](#cellurlvalue)CellUrlValue

数组类型为预留能力，目前只支持展示一个链接，建议只传入一个链接  
**示例**

```json
{
	"link": "https://developer.work.weixin.qq.com/document/path/97392",
	"text": "企业微信开发者中心",
	"type": "url"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string | 填`url` |
| text | string | 链接显示文本 |
| link | string | 链接跳转url |

### [](#option)Option

**示例**

```json
{
	"id": "1"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| id | string | 选项ID，当选项存在时，通过ID识别选项，当需要新增选项，则不填写此字段 |
| style | int([Style](#53117/style)) | 选项颜色。新增选项时填写 |
| text | string | 要填写的选项内容。新增选项时填写，已经存在时优先匹配已经存在的选项，否则会新增选项 |

### [](#celllocationvalue)CellLocationValue

**示例**

```json
{
	"id": "14313005936863363130",
	"latitude": "23.10647",
	"longitude": "113.32446",
	"source_type": 1,
	"title": "广州塔"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| source\_type | uint32 | 填`1`，表示来源为`腾讯地图`。目前只支持腾讯地图来源 |
| id | string | 地点ID |
| latitude | string | 纬度 |
| longitude | string | 经度 |
| title | string | 地点名称 |


删除记录

最后更新：2024/09/12

目录

-   [删除记录](#%E5%88%A0%E9%99%A4%E8%AE%B0%E5%BD%95)

## [](#%E5%88%A0%E9%99%A4%E8%AE%B0%E5%BD%95)删除记录

本接口用于删除 Smartsheet 的某个子表中的一行或多行记录。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/delete\_records?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"record_ids": [
		"re9IqD",
		"rpS0P9"
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| record\_ids | string\[\] | 是 | 要删除的记录 ID |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

更新记录

最后更新：2024/09/12

目录

-   [更新记录](#%E6%9B%B4%E6%96%B0%E8%AE%B0%E5%BD%95)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [CellValueKeyType](#cellvaluekeytype)
-         [UpdateRecord](#updaterecord)
-         [CommonRecord](#commonrecord)

## [](#%E6%9B%B4%E6%96%B0%E8%AE%B0%E5%BD%95)更新记录

本接口用于更新 Smartsheet 中的某个子表里的一行或多行记录。  
**注意**  
不能通过更新记录接口给创建时间、最后编辑时间、创建人和最后编辑人四种类型的字段更新记录。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/update\_records?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"key_type": "CELL_VALUE_KEY_TYPE_FIELD_TITLE",
	"records": [
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| key\_type | string([CellValueKeyType](#cellvaluekeytype)) | 否 | 返回记录中单元格的key类型 |
| records | Object\[\]([UpdateRecord](#updaterecord)) | 是 | 由需要更新的记录组成的 JSON 数组 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "records": [
    ]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| records | Object\[\]([CommonRecord](#commonrecord)) | 由更新成功的记录的具体内容组成的 JSON 数组 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#cellvaluekeytype)CellValueKeyType

记录([CommonRecord](#commonrecord))中key的类型

| 枚举类型 | 描述 |
| :-- | --- |
| CELL\_VALUE\_KEY\_TYPE\_FIELD\_TITLE | key用字段标题表示 |
| CELL\_VALUE\_KEY\_TYPE\_FIELD\_ID | key用字段 ID 表示 |

### [](#updaterecord)UpdateRecord

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| record\_id | string | 记录 ID |
| values | Object | 记录的具体内容，key 为字段标题或字段 ID ，value 详见([Value](#53118/value)) |

### [](#commonrecord)CommonRecord

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| record\_id | string | 记录 ID |
| values | Object | 记录的具体内容，key 为字段标题或字段 ID ，value 详见([Value](#value)) |


查询记录

最后更新：2025/08/08

目录

-   [查询记录](#%E6%9F%A5%E8%AF%A2%E8%AE%B0%E5%BD%95)
-   [参数详细说明](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)
-         [CellValueKeyType](#cellvaluekeytype)
-         [Sort](#sort)
-         [Record](#record)
-         [Value](#value)
-         [CellTextValue](#celltextvalue)
-         [CellImageValue](#cellimagevalue)
-         [CellAttachmentValue](#cellattachmentvalue)
-         [CellUserValue](#celluservalue)
-         [CellUrlValue](#cellurlvalue)
-         [Option](#option)
-         [CellLocationValue](#celllocationvalue)
-         [CellAutoNumberValue](#cellautonumbervalue)

## [](#%E6%9F%A5%E8%AF%A2%E8%AE%B0%E5%BD%95)查询记录

本接口用于获取 Smartsheet 中某个子表下记录信息，该接口可以完成下面三种功能：获取全部记录信息、依据字段名和记录 ID 获取对应记录、对记录进行排序。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/get\_records?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"view_id": "vCRl8n",
	"record_ids": [],
	"key_type": "CELL_VALUE_KEY_TYPE_FIELD_TITLE",
	"field_titles": [],
	"field_ids": [],
	"sort": [],
	"offset": 0,
	"limit": 100,
	"ver": 160,
	"filter_spec": {
		"conjunction": "CONJUNCTION_AND",
		"conditions": [{
			"field_id": "f53B4X",
			"field_type": "FIELD_TYPE_TEXT",
			"operator": "OPERATOR_CONTAINS",
			"string_value": {
				"value": [
					"123"
				]
			}
		}]
	}
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | Smartsheet 子表ID |
| view\_id | string | 否 | 视图 ID |
| record\_ids | string\[\] | 否 | 由记录 ID 组成的 JSON 数组 |
| key\_type | string([CellValueKeyType](#cellvaluekeytype)) | 否 | 返回记录中单元格的key类型 |
| field\_titles | string\[\] | 否 | 返回指定列，由字段标题组成的 JSON 数组 ，key\_type 为 `CELL_VALUE_KEY_TYPE_FIELD_TITLE` 时有效 |
| field\_ids | string\[\] | 否 | 返回指定列，由字段 ID 组成的 JSON 数组 ，key\_type 为 `CELL_VALUE_KEY_TYPE_FIELD_ID` 时有效 |
| sort | Object\[\]([Sort](#sort)) | 否 | 对返回记录进行排序 |
| offset | uint32 | 否 | 偏移量，初始值为 0 |
| limit | uint32 | 否 | 分页大小 , 每页返回多少条数据；当不填写该参数或将该参数设置为 0 时，如果总数大于 1000，一次性返回 1000 行记录，当总数小于 1000 时，返回全部记录；limit 最大值为 1000 |
| ver | uint32 | 否 | 版本号 |
| filter\_spec | object([FilterSpec](#53112/filterspec)) | 否 | 过滤设置，不支持和sort一起使用 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok",
	   "ver":160
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| total | uint32 | 符合筛选条件的视图总数 |
| has\_more | bool | 是否还有更多项 |
| next | uint32 | 下次下一个搜索结果的偏移量 |
| records | Object\[\]([Record](#record)) | 由查询记录的具体内容组成的 JSON 数组 |
| ver | uint32 | 版本号 |

## [](#%E5%8F%82%E6%95%B0%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E)参数详细说明

### [](#cellvaluekeytype)CellValueKeyType

记录([Record](#record))中key的类型

| 枚举类型 | 描述 |
| :-- | --- |
| CELL\_VALUE\_KEY\_TYPE\_FIELD\_TITLE | key用字段标题表示 |
| CELL\_VALUE\_KEY\_TYPE\_FIELD\_ID | key用字段 ID 表示 |

### [](#sort)Sort

**示例**  
字段标题为`文本列`的降序排序，字段标题为`数字列`的升序序排序。需要一个Sort数组：

```json
[
	{
		"field_title": "文本列",
		"desc": true
	},
	{
		"field_title": "数字列",
		"desc": false
	}
]
```

在 Smartsheet 的某个表格中对记录进行排序的参数：

| 参数名 | 类型 | 是否必须 | 描述 |
| :-- | --- | --- | --- |
| field\_title | string | 是 | 需要排序的字段标题 |
| desc | bool | 否 | 是否进行降序排序，默认值为 false |

### [](#record)Record

Smartsheet 的某个表格中记录相关的参数：  
**示例1**  
按`字段标题`返回各行的单元格内容

```json
{
    "record_id": "r5ud8u",
    "create_time": "1715846245084",
    "update_time": "1715846248810",
    "values": {
        "文本字段1-标题": [
            {
                "type": "text",
                "text": "XXXX"
            }
        ],
        "数字字段1-标题": 123
    },
    "creator_name":"NAME",
    "updater_name":"NAME"
}
```

**示例2**  
按`字段ID`返回各行的单元格内容

```json
{
    "record_id": "r5ud8u",
    "create_time": "1715846245084",
    "update_time": "1715846248810",
    "values": {
        "TextField1Id": [
            {
                "type": "text",
                "text": "XXXX"
            }
        ],
        "NumField1Id": 123
    },
		"creator_name":"NAME",
		"updater_name":"NAME"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| record\_id | string | 记录 ID |
| create\_time | string | 记录的创建时间 |
| update\_time | string | 记录的更新时间 |
| values | Object | 记录的具体内容，key 为字段标题或字段 ID ，value 详见([Value](#value)) |
| creator\_name | string | 创建者名字 |
| updater\_name | string | 最后编辑者名字 |

### [](#value)Value

各种类型的字段对应的单元格的值

| 字段类型 | 单元格值类型 | 描述 |
| :-- | --- | --- |
| 文本(FIELD\_TYPE\_TEXT) | Object\[\]([CellTextValue](#celltextvalue)) |   |
| 数字(FIELD\_TYPE\_NUMBER) | double |   |
| 复选框(FIELD\_TYPE\_CHECKBOX) | bool |   |
| 日期(FIELD\_TYPE\_DATE\_TIME) | string(以毫秒为单位的unix时间戳) |   |
| 图片(FIELD\_TYPE\_IMAGE) | Object\[\]([CellImageValue](#cellimagevalue)) |   |
| 文件(FIELD\_TYPE\_ATTACHMENT) | Object\[\]([CellAttachmentValue](#cellattchmentvalue)) |   |
| 成员(FIELD\_TYPE\_USER) | Object\[\]([CellUserValue](#celluservalue)) |   |
| 链接(FIELD\_TYPE\_URL) | Object\[\]([CellUrlValue](#cellurlvalue)) | 数组类型为预留能力，目前只支持展示一个链接，建议只传入一个链接 |
| 多选(FIELD\_TYPE\_SELECT) | Object\[\]([Option](#option)) |   |
| 进度(FIELD\_TYPE\_PROGRESS) | double |   |
| 电话(FIELD\_TYPE\_PHONE\_NUMBER) | string |   |
| 邮箱(FIELD\_TYPE\_EMAIL) | string |   |
| 单选(FIELD\_TYPE\_SINGLE\_SELECT) | Object\[\]([Option](#option)) |   |
| 地理位置(FIELD\_TYPE\_LOCATION) | Object\[\]([CellLocationValue](#celllocationvalue)) | 长度不大于1的数组。 |
| 关联(FIELD\_TYPE\_REFERENCE) | string \[\] | 关联的记录id |
| 货币(FIELD\_TYPE\_CURRENCY) | double |  |
| 自动编号(FIELD\_TYPE\_AUTONUMBER) | Object\[\]([CellAutoNumberValue](#cellautonumbervalue) |  |
| 百分数(FIELD\_TYPE\_PERCENTAGE) | double |  |

### [](#celltextvalue)CellTextValue

文本类型字段的单元值类型

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string | 内容为文本(值为`text`)、内容为链接(值为`url`) |
| text | string | 单元格内容 |
| link | string | 当type时`url`时，表示链接跳转url |

### [](#cellimagevalue)CellImageValue

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| id | string | 图片 ID |
| title | string | 图片标题 |
| image\_url | string | 图片url |
| width | int32 | 图片宽度 |
| height | int32 | 图片高度 |

### [](#cellattachmentvalue)CellAttachmentValue

**示例**

```json
{
	"doc_type": 2,
	"file_ext": "SMARTSHEET",
	"file_type": "70",
	"file_url": "https://doc.weixin.qq.com/smartsheet/xxx",
	"name": "智能表格",
	"size": 3267
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| name | string | 文件名 |
| size | int32 | 文件大小 |
| file\_ext | string | 文件扩展名 |
| file\_url | string | 文件url |
| file\_type | string | 文件类型，文件夹为Folder，微盘文件为Wedrive，文件夹为Folder，微盘文件为Wedrive，收集表为30，文档为50，表格是51，幻灯片为52，思维导图为54，流程图为55，智能表为70 |
| doc\_type | string | 接口返回的文件类型，1为文件夹，2为文件 |

### [](#celluservalue)CellUserValue

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| user\_id | string | 成员ID |
| tmp\_external\_userid | string | 外部用户临时id，同一个用户在不同的智能表中返回的该id不一致。可进一步通过[tmp\_external\_userid的转换](#46252)接口转换成external\_userid，方便识别外部用户的身份。 |

### [](#cellurlvalue)CellUrlValue

数组类型为预留能力，目前只支持展示一个链接，建议只传入一个链接  
**示例**

```json
{
	"link": "https://developer.work.weixin.qq.com/document/path/97392",
	"text": "企业微信开发者中心",
	"type": "url"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| type | string | 填`url` |
| text | string | 链接显示文本 |
| link | string | 链接跳转url |

### [](#option)Option

**示例**

```json
{
	"id": "1",
	"style": 1,
	"text": "one"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| id | string | 选项ID |
| style | uint32 | 选项颜色[(Style)](#53117/style) |
| text | string | 选项内容 |

### [](#celllocationvalue)CellLocationValue

**示例**

```json
{
	"id": "14313005936863363130",
	"latitude": "23.10647",
	"longitude": "113.32446",
	"source_type": 1,
	"title": "广州塔"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| source\_type | uint32 | 填`1`，表示来源为`腾讯地图`。目前只支持腾讯地图来源 |
| id | string | 地点ID |
| latitude | string | 纬度 |
| longitude | string | 经度 |
| title | string | 地点名称 |

### [](#cellautonumbervalue)CellAutoNumberValue

**示例**

```json
{
	"seq": "3",
	"text": "3"
}
```

| 参数名 | 类型 | 描述 |
| :-- | --- | --- |
| seq | string | 序号 |
| text | string | 展示的文本 |


添加编组

最后更新：2025/08/20

## [](#%E6%B7%BB%E5%8A%A0%E7%BC%96%E7%BB%84)添加编组

本接口用于在智能表中的某个子表里添加编组。单表最多允许有150个编组。每个编组最多允许有150个字段。字段只能同时存在于一个编组。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/add\_field\_group?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"name":"编组名称",
	"children": [
		{
			"field_id": "field_id"
		},
		{
			"field_id": "field_id"
		}]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| name | string | 是 | 编组名称，不能和已有名称重复 |
| children | object\[\] | 否 | 编组内容 |
| children.field\_id | string | 否 | 字段id |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"field_group": {
		"field_group_id": "FIELD_GROUP_ID",
		"name": "编组名称",
		"children": [{
				"field_id": "FIELD_ID"
			},
			{
				"field_id": "FIELD_ID"
			}
		]
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| field\_group | object | 编组 |
| field\_group.field\_group\_id | string | 编组id |
| field\_group.name | string | 编组名称 |
| field\_group.children | object\[\] | 编组内容 |
| field\_group.children.field\_id | string | 字段id |


删除编组

最后更新：2025/08/19

目录

-   [删除编组](#%E5%88%A0%E9%99%A4%E7%BC%96%E7%BB%84)

## [](#%E5%88%A0%E9%99%A4%E7%BC%96%E7%BB%84)删除编组

本接口用于删除智能表的某个子表中的一个或多个编组。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/delete\_field\_groups?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "123Abc",
	"field_group_ids": [
		"fgCLYCF",
		"fgCLYCM"
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 子表ID |
| field\_group\_ids | string\[\] | 是 | 要删除的编组 ID |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


更新编组

最后更新：2025/09/03

## [](#%E6%9B%B4%E6%96%B0%E7%BC%96%E7%BB%84)更新编组

本接口用于在智能表中的某个子表里更新已有编组。每个编组最多允许有150个字段。字段只能同时存在于一个编组。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/update\_field\_group?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"field_group_id":"FIELD_GROUP_ID",
	"name":"编组名称",
	"children": [
		{
			"field_id": "FIELD_ID"
		},
		{
			"field_id": "FIELD_ID"
		}]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| field\_group\_id | string | 是 | 编组id |
| name | string | 否 | 编组名称，不能和已有名称重复 |
| children | object\[\] | 否 | 编组内容 |
| children.field\_id | string | 否 | 字段id |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"field_group": {
		"field_group_id": "FIELD_GROUP_ID",
		"name": "编组名称",
		"children": [{
				"field_id": "FIELD_ID"
			},
			{
				"field_id": "FIELD_ID"
			}
		]
	}
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| field\_group\_id | string | 编组id |
| name | string | 编组名称 |
| children | object\[\] | 编组内容 |
| children.field\_id | string | 字段id |


获取编组

最后更新：2025/08/18

## [](#%E8%8E%B7%E5%8F%96%E7%BC%96%E7%BB%84)获取编组

本接口用于在智能表中的某个子表里获取已有的编组。

**请求方式**：POST(HTTPS)  
**请求地址**：https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/get\_field\_groups?access\_token=ACCESS\_TOKEN

**请求包体**：

```json
{
	"docid": "DOCID",
	"sheet_id": "SHEETID",
	"offset":0,
	"limit":10
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| :-- | --- | --- | --- |
| docid | string | 是 | 文档的docid |
| sheet\_id | string | 是 | 表格ID |
| offset | uint32 | 否 | 偏移量，初始值为 0 |
| limit | uint32 | 否 | 分页大小 , 每页返回多少条数据 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"total": 1,
	"has_more": false,
	"next": 0,
	"field_groups": [{
		"field_group_id": "FIELD_GROUP_ID",
		"name": "编组名称",
		"children": [{
			"field_id": "FIELD_ID"
		}]
	}]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| :-- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| total | uint32 | 编组数量 |
| has\_more | bool | 是否还有更多数据 |
| next | uint32 | 下一偏移位置 |
| field\_groups | obj\[\] | 编组列表 |
| field\_groups.field\_group\_id | string | 编组id |
| field\_groups.name | string | 编组名称 |
| field\_groups.children | object\[\] | 编组内容 |
| field\_groups.children.field\_id | string | 字段id |


# 设置文档权限

获取文档权限信息

最后更新：2024/05/30

该接口用于获取文档、表格、智能表格的查看规则、文档通知范围及权限、安全设置信息

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/doc\_get\_auth?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid":"DOCID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 文档id |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能访问该应用创建的文档

**返回示例**

```json
{
    "errcode":0,
    "errmsg":"ok",
    "access_rule":{
        "enable_corp_internal":true,
        "corp_internal_auth":1,
        "enable_corp_external":true,
        "corp_external_auth":1,
        "corp_internal_approve_only_by_admin":true,
        "corp_external_approve_only_by_admin":true,
        "ban_share_external":false
    },
    "secure_setting":{
        "enable_readonly_copy":false,
        "watermark":{
            "margin_type":2,
            "show_visitor_name":false,
            "show_text":false,
            "text":""
        },
        "enable_readonly_comment":false
    },
    "doc_member_list":[
        {
            "type":1,
            "userid":"USERID1",
            "auth":7
        },
        {
            "type":1,
            "tmp_external_userid":"TMP_EXTERNAL_USERID2",
            "auth":1
        }
    ],
    "co_auth_list":[
        {
            "type":2,
            "departmentid":1,
            "auth":1
        }
    ]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| access\_rule | object | 文档的查看规则 |
| enable\_corp\_internal | bool | 是否允许企业内成员浏览文档 |
| corp\_internal\_auth | uint32 | 企业内成员主动查看文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写） |
| enable\_corp\_external | bool | 是否允许企业外成员浏览文档 |
| corp\_external\_auth | uint32 | 企业内成员主动查看文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写） |
| corp\_internal\_approve\_only\_by\_admin | bool | 企业内成员浏览文档是否必须由管理员审批，enable\_corp\_internal为false时，只能为true |
| corp\_external\_approve\_only\_by\_admin | bool | 企业外成员浏览文档是否必须由管理员审批，enable\_corp\_external和ban\_share\_external均为false时，该参数只能为true |
| ban\_share\_external | bool | 是否允许企业外成员浏览文档 |
| enable\_readonly\_copy | bool | 仅浏览权限的成员是否允许导出、复制、打印 |
| watermark | object | 文档水印设置 |
| margin\_type | uint32 | 水印密度 1:稀疏 2:紧密 |
| show\_visitor\_name | bool | 是否展示访问者名字 |
| show\_text | bool | 是否展示水印文字 |
| text | bytes | 水印文字 |
| doc\_member\_list | obj\[\] | 文档通知范围及权限列表 |
| type | uint32 | 文档通知范围成员种类 1:user, 只支持成员 |
| userid | bytes | 企业成员的userid |
| tmp\_external\_userid | string | 外部用户临时id。同一个用户在不同的文档中返回的该id不一致。 |
| auth | uint32 | 该文档通知范围成员的权限 1:只读 2:读写（目前仅智能表可设置为读写） 7:管理员 |
| co\_auth\_list | object | 文档查看权限特定部门列表，可以直接浏览文档 |
| type | uint32 | 特定部门列表 2:部门, 目前只支持部门 |
| departmentid | uint64 | 特定部门id |
| auth | uint32 | 权限类型 1:只读,2:读写（目前仅智能表可设置为读写） |


修改文档查看规则

最后更新：2024/08/21

该接口用于修改文档、表格、智能表格查看规则。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/mod\_doc\_join\_rule?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
    "docid":"DOCID",
    "enable_corp_internal":true,
    "corp_internal_auth":1,
    "enable_corp_external":true,
    "corp_external_auth":1,
    "corp_internal_approve_only_by_admin":true,
    "corp_external_approve_only_by_admin":true,
    "ban_share_external":false,
    "update_co_auth_list":true,
    "co_auth_list":[
        {
            "departmentid":1,
            "auth":1,
            "type":2
        }
    ]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 操作的docid |
| enable\_corp\_internal | bool | 否 | 是否允许企业内成员浏览文档, 有值则覆盖 |
| corp\_internal\_auth | uint32 | 否 | 企业内成员主动查看文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写）, 有值则覆盖 |
| enable\_corp\_external | uint32 | 否 | 是否允许企业外成员浏览文档, 有值则覆盖 |
| corp\_external\_auth | uint32 | 否 | 企业外成员主浏览文档后获得的权限类型 1:只读 2:读写（目前仅智能表可设置为读写）, 有值则覆盖 |
| corp\_internal\_approve\_only\_by\_admin | bool | 否 | 企业内成员加入文档是否必须由管理员审批，enable\_corp\_internal为false时，只能为true，有值则覆盖。设置为true之前，文档需要有至少一个管理员。 |
| corp\_external\_approve\_only\_by\_admin | bool | 否 | 企业外成员加入文档是否必须由管理员审批，enable\_corp\_external和ban\_share\_external均为false时，该参数只能为true，有值则覆盖。设置为true之前，文档需要有至少一个管理员。 |
| ban\_share\_external | bool | 否 | 是否禁止文档分享到企业外, 有值则覆盖 |
| update\_co\_auth\_list | bool | 否 | 是否更新文档查看权限的特定部门, true时更新特定部门列表 |
| co\_auth\_list | object\[\] | 否 | 需要更新文档查看权限特定部门时, 覆盖之前部门, 特别的: 列表为空则清空 |
| departmentid | uint64 | 否 | 文档查看权限特定部门id |
| auth | uint32 | 否 | 文档特定部门权限 1:只读 2:读写（目前仅智能表可设置为读写） |
| type | uint32 | 否 | 文档特定部门类型 2:部门, 目前只支持部门 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能操作该应用创建的文档

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


修改文档通知范围及权限

最后更新：2024/05/30

该接口用于修改文档、表格、智能表格通知范围列表，可以新增文档、表格、智能表格通知范围并设置权限、修改已有范围的权限以及删除文档、表格、智能表格通知范围内的人员

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/mod\_doc\_member?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
    "docid":"DOCID",
    "update_file_member_list":[
        {
            "type":1,
            "auth":7,
            "userid":"USERID1"
        }
     ],
    "del_file_member_list":[
        {
            "type":1,
            "userid":"USERID2"
        },
        {
            "type":1,
            "tmp_external_userid":"TMP_EXTERNAL_USERID2"
        }
   ]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 操作的文档id |
| update\_file\_member\_list | obj\[\] | 否 | 更新文档通知范围的列表, 批次大小最大100 |
| type | uint32 | 是 | 文档通知范围的类型 1:用户。文档通知范围仅支持按人配置 |
| auth | uint32 | 是 | 文档通知范围内人员获得的权限 1:只读权限 2:读写权限（目前仅智能表可设置为读写权限） 7:管理员权限，文档管理员最多三个 |
| userid | string | 否 | 企业内成员的ID |
| tmp\_external\_userid | string | 否 | 外部用户临时id。同一个用户在不同的文档中返回的该id不一致。 |
| del\_file\_member\_list | obj\[\] | 否 | 删除的文档通知范围列表，批次大小最大一百 |
| type | uint32 | 是 | 文档通知范围的类型 1:用户。文档通知范围仅支持按人配置 |
| userid | string | 否 | 企业内成员的ID |
| tmp\_external\_userid | string | 否 | 外部用户临时id。同一个用户在不同的文档中返回的该id不一致。 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能操作该应用创建的文档

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

修改文档安全设置

最后更新：2024/05/30

该接口用于修改文档、表格、智能表格的安全设置

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/mod\_doc\_safty\_setting?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
    "docid":"DOCID",
    "enable_readonly_copy":false,
    "watermark":{
        "margin_type":1,
        "show_visitor_name":true,
        "show_text":true,
        "text":"test mark"
    }
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 操作的文档id |
| enable\_readonly\_copy | bool | 否 | 是否允许只读成员复制、下载文档，有值则覆盖 |
| watermark | object | 否 | 水印设置 |
| margin\_type | uint32 | 否 | 水印疏密度，1:稀疏，2:紧密 |
| show\_visitor\_name | bool | 否 | 是否展示访问者名字水印，有值则覆盖 |
| show\_text | bool | 否 | 是否展示文本水印，有值则覆盖 |
| text | string | 否 | 文字水印的文字，有值则覆盖 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能操作该应用创建的文档

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

管理智能表格内容权限

最后更新：2024/11/21

目录

-   [智能表内容权限概述](#%E6%99%BA%E8%83%BD%E8%A1%A8%E5%86%85%E5%AE%B9%E6%9D%83%E9%99%90%E6%A6%82%E8%BF%B0)
-         [权限明细](#%E6%9D%83%E9%99%90%E6%98%8E%E7%BB%86)
-         [生效成员](#%E7%94%9F%E6%95%88%E6%88%90%E5%91%98)
-   [查询智能表格子表权限](#%E6%9F%A5%E8%AF%A2%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E5%AD%90%E8%A1%A8%E6%9D%83%E9%99%90)
-   [更新智能表格子表权限](#%E6%9B%B4%E6%96%B0%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E5%AD%90%E8%A1%A8%E6%9D%83%E9%99%90)
-   [新增智能表格指定成员额外权限](#%E6%96%B0%E5%A2%9E%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E6%8C%87%E5%AE%9A%E6%88%90%E5%91%98%E9%A2%9D%E5%A4%96%E6%9D%83%E9%99%90)
-   [更新智能表格指定成员额外权限](#%E6%9B%B4%E6%96%B0%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E6%8C%87%E5%AE%9A%E6%88%90%E5%91%98%E9%A2%9D%E5%A4%96%E6%9D%83%E9%99%90)
-   [删除智能表格指定成员额外权限](#%E5%88%A0%E9%99%A4%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E6%8C%87%E5%AE%9A%E6%88%90%E5%91%98%E9%A2%9D%E5%A4%96%E6%9D%83%E9%99%90)

## [](#%E6%99%BA%E8%83%BD%E8%A1%A8%E5%86%85%E5%AE%B9%E6%9D%83%E9%99%90%E6%A6%82%E8%BF%B0)智能表内容权限概述

智能表格可设置**内容权限**以详细配置文档成员对表格内容的操作权限。  
内容权限由全员权限以及至多20条成员额外权限组成。

### [](#%E6%9D%83%E9%99%90%E6%98%8E%E7%BB%86)权限明细

每条权限可以针对不同子表配置字段权限、记录权限、视图权限。

### [](#%E7%94%9F%E6%95%88%E6%88%90%E5%91%98)生效成员

对于全员权限，生效成员即是全部文档成员。  
对于成员额外权限，可以配置生效的成员范围。

## [](#%E6%9F%A5%E8%AF%A2%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E5%AD%90%E8%A1%A8%E6%9D%83%E9%99%90)查询智能表格子表权限

该接口用于查询智能表格子表权限详情

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/content\_priv/get\_sheet\_priv?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"type": 2,
	"rule_id_list": [
		"RULEID1", "RULEID2"
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 智能表ID，通过[新建文档接口](#43939)创建后获得 |
| type | uint32 | 是 | 权限规则类型，1-全员权限，2-额外权限 |
| rule\_id\_list | uint32 \[\] | 否 | 需要查询的规则id列表，查询额外权限时填写 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"rule_list": [{
		"rule_id": 1,
		"type": 1,
		"name": "全员权限",
		"priv_list": [{
				"sheet_id": "q979lj",
				"priv": 2,
				"can_insert_record": true,
				"can_delete_record": true,
				"record_priv": {
					"record_range_type": 1
				},
				"field_priv": {
					"field_range_type": 2,
					"field_rule_list": [{
						"field_id": "fsMGQS",
						"field_type": "FIELD_TYPE_TEXT",
						"can_edit": false,
						"can_insert": true,
						"can_view": true
					}],
					"field_default_rule": {
						"can_edit": false,
						"can_insert": false,
						"can_view": true
					}
				},
				"can_create_modify_delete_view": true
			},
			{
				"sheet_id": "kQ65QQ",
				"priv": 1
			}
		]
	}]
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| rule\_list | object\[\] | 权限列表 |
| rule\_list.type | uint32 | 权限规则类型，1-全员权限，2-额外权限。每个智能表格有且只有一个全员权限 |
| rule\_list.rule\_id | uint32 | 当type为2时必填 |
| rule\_list.name | string | 权限名称，仅当type为2时有效 |
| rule\_list.priv\_list | object\[\] | 针对不同子表设置内容权限 |
| rule\_list.priv\_list.sheet\_id | string | 子表ID |
| rule\_list.priv\_list.priv | string | 子表权限: 1-全部权限；2-可编辑；3-仅浏览；4-无权限 |
| rule\_list.priv\_list.can\_insert\_record | bool | 是否可以新增记录。仅当子表权限为`可编辑`时有意义 |
| rule\_list.priv\_list.can\_delete\_record | bool | 是否可以删除记录。仅当子表权限为`可编辑`时有意义 |
| rule\_list.priv\_list.can\_create\_modify\_delete\_view | bool | 是否可以增、删、改视图。 |
| rule\_list.priv\_list.field\_priv | object | 按字段配置权限 |
| rule\_list.priv\_list.field\_priv.field\_range\_type | uint32 | 子表权限对所有字段生效还是部分字段生效：1-所有字段；2-部分字段。当值为2时可以配置各个字段独立的权限 |
| rule\_list.priv\_list.field\_priv.field\_rule\_list | object\[\] | 按字段分别配置权限 |
| rule\_list.priv\_list.field\_priv.field\_rule\_list.field\_id | string | 字段id |
| priv\_list.priv\_list.field\_priv.field\_rule\_list.field\_type | string | 字段类型，见[FieldType](#53114/fieldtype) |
| rule\_list.priv\_list.field\_priv.field\_rule\_list.can\_edit | bool | 可编辑 |
| rule\_list.priv\_list.field\_priv.field\_rule\_list.can\_insert | bool | 可首次提交 |
| rule\_list.priv\_list.field\_priv.field\_rule\_list.can\_view | bool | 可查看 |
| rule\_list.priv\_list.field\_priv.field\_default\_rule | object | field\_rule\_list里未指定字段和后续新增字段的默认配置，与field\_rule\_list一样可指定can\_edit/can\_insert/can\_view三个权限 |
| rule\_list.priv\_list.record\_priv | object | 按记录配置权限，priv=2或3时必填 |
| rule\_list.priv\_list.record\_priv.record\_range\_type | uint32 | 子表权限对记录生效范围：1-全部记录；2-满足任意条件的记录；3-满足全部条件的记录 |
| rule\_list.priv\_list.record\_priv.record\_rule\_list | object\[\] | 记录的条件列表，当record\_range\_type为2或3时生效 |
| rule\_list.priv\_list.record\_priv.record\_rule\_list.field\_id | string | 字段id，只有人员、单选、多选三种类型的字段有效。当field\_id为`CREATED_USER`时表示记录创建者 |
| rule\_list.priv\_list.record\_priv.record\_rule\_list.field\_type | string | 是字段类型，见[FieldType](#53114/fieldtype) |
| rule\_list.priv\_list.record\_priv.record\_rule\_list.oper\_type | uint32 | 逻辑判断类型：1-包含自己（人员字段）；2-包含value；3-不包含value；4-等于value；5-不等于value；6-为空；7-非空； |
| rule\_list.priv\_list.record\_priv.record\_rule\_list.value | string\[\] | 用于单选、多选字段的option\_id |
| rule\_list.priv\_list.record\_priv.other\_priv | uint32 | 当记录不满足条件的时的权限类型：1-不可编辑 2-不可查看 |
| rule\_list.priv\_list.clear | bool | 清除子表的设置，恢复默认权限 |

## [](#%E6%9B%B4%E6%96%B0%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E5%AD%90%E8%A1%A8%E6%9D%83%E9%99%90)更新智能表格子表权限

该接口用于设置全员权限或者成员额外权限的权限详情

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/content\_priv/update\_sheet\_priv?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"type": 2,
	"rule_id": 2,
	"name": "NAME",
	"priv_list": [{
		"sheet_id": "SHEETID",
		"priv": 1,
		"can_insert_record": true,
		"can_delete_record": true,
		"can_create_modify_delete_view": true,
		"field_priv": {
			"field_range_type": 2,
			"field_rule_list": [{
					"field_id": "FIELDID1",
					"can_edit": true,
					"can_insert": true,
					"can_view": true
				},
				{
					"field_id": "FIELDID2",
					"can_edit": false,
					"can_insert": true,
					"can_view": true
				}
			]
		},
		"record_priv": {
			"record_range_type": 2,
			"record_rule_list": [{
					"field_id": "FIELDI1",
					"field_type": "FIELD_TYPE_TEXT",
					"oper_type": 1
				},
				{
					"field_id": "CREATED_USER",
					"oper_type": 1
				},
				{
					"field_id": "FIELDID2",
					"oper_type": 2,
					"field_type": "FIELD_TYPE_SELECT",
					"value": [
						"OPTION1", "OPTION2", "OPTION3"
					]
				}
			]
		},
		"clear": false
	}]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 智能表ID，通过[新建文档接口](#43939)创建后获得 |
| type | uint32 | 是 | 权限规则类型，1-全员权限，2-额外权限。每个智能表格有且只有一个全员权限 |
| rule\_id | uint32 | 否 | 当type为2时必填 |
| name | string | 否 | 更新权限名称，仅当type为2时有效 |
| priv\_list | object\[\] | 否 | 针对不同子表设置内容权限 |
| priv\_list.sheet\_id | string | 是 | 子表ID |
| priv\_list.priv | string | 是 | 子表权限: 1-全部权限；2-可编辑；3-仅浏览；4-无权限 |
| priv\_list.can\_insert\_record | bool | 否 | 是否可以新增记录。仅当子表权限为`可编辑`时有意义 |
| priv\_list.can\_delete\_record | bool | 否 | 是否可以删除记录。仅当子表权限为`可编辑`时有意义 |
| priv\_list.can\_create\_modify\_delete\_view | bool | 否 | 是否可以增、删、改视图。 |
| priv\_list.field\_priv | object | 否 | 按字段配置权限 |
| priv\_list.field\_priv.field\_range\_type | uint32 | 是 | 子表权限对所有字段生效还是部分字段生效：1-所有字段；2-部分字段。当值为2时可以配置各个字段独立的权限 |
| priv\_list.field\_priv.field\_rule\_list | object\[\] | 是 | 按字段分别配置权限 |
| priv\_list.field\_priv.field\_rule\_list.field\_id | string | 是 | 字段id |
| priv\_list.field\_priv.field\_rule\_list.field\_type | string | 是 | 字段类型，见[FieldType](#53114/fieldtype) |
| priv\_list.field\_priv.field\_rule\_list.can\_edit | bool | 是 | 可编辑 |
| priv\_list.field\_priv.field\_rule\_list.can\_insert | bool | 是 | 可首次提交 |
| priv\_list.field\_priv.field\_rule\_list.can\_view | bool | 是 | 可查看 |
| priv\_list.field\_priv.field\_default\_rule | object | 否 | field\_rule\_list里未指定字段和后续新增字段的默认配置，与field\_rule\_list一样可指定can\_edit/can\_insert/can\_view三个权限。type为1时必填，type为2时不可指定field\_default\_rule |
| priv\_list.record\_priv | object | 否 | 按记录配置权限，priv=2或3时必填 |
| priv\_list.record\_priv.record\_range\_type | uint32 | 是 | 子表权限对记录生效范围：1-全部记录；2-满足任意条件的记录；3-满足全部条件的记录 |
| priv\_list.record\_priv.record\_rule\_list | object\[\] | 否 | 记录的条件列表，当record\_range\_type为2或3时生效 |
| priv\_list.record\_priv.record\_rule\_list.field\_id | string | 是 | 字段id，只有人员、单选、多选三种类型的字段有效。当field\_id为`CREATED_USER`时表示记录创建者 |
| priv\_list.record\_priv.record\_rule\_list.field\_type | string | 否 | 字段类型[FieldType](#53114/fieldtype)，当field\_id为`CREATED_USER`时不填此字段，其他类型必填 |
| priv\_list.record\_priv.record\_rule\_list.oper\_type | uint32 | 是 | 逻辑判断类型：1-包含自己（人员字段）；2-包含value；3-不包含value；4-等于value；5-不等于value；6-为空；7-非空； |
| priv\_list.record\_priv.record\_rule\_list.value | string\[\] | 是 | 用于单选、多选字段的option\_id |
| priv\_list.record\_priv.other\_priv | uint32 | 是 | 当记录不满足条件的时的权限类型：1-不可编辑 2-不可查看 |
| priv\_list.clear | bool | 否 | 清除子表的设置，恢复默认权限 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

## [](#%E6%96%B0%E5%A2%9E%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E6%8C%87%E5%AE%9A%E6%88%90%E5%91%98%E9%A2%9D%E5%A4%96%E6%9D%83%E9%99%90)新增智能表格指定成员额外权限

该接口用于新增智能表格指定成员额外权限

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/content\_priv/create\_rule?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"name": "NAME"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 智能表ID，通过[新建文档接口](#43939)创建后获得 |
| name | string | 是 | 权限规则名称，不可重复 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "rule_id": 1
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| rule\_id | uint32 | 成员权限规则id |

## [](#%E6%9B%B4%E6%96%B0%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E6%8C%87%E5%AE%9A%E6%88%90%E5%91%98%E9%A2%9D%E5%A4%96%E6%9D%83%E9%99%90)更新智能表格指定成员额外权限

该接口用于更新智能表格指定成员额外权限，成员最多可设置50个

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/content\_priv/mod\_rule\_member?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"rule_id": 3,
	"add_member_range": {
		"userid_list": [
			"userid1"
		]
	},
	"del_member_range": {
		"userid_list": [
			"userid2"
		]
	}
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 智能表ID，通过[新建文档接口](#43939)创建后获得 |
| rule\_id | uint32 | 是 | 需要更新的id |
| add\_member\_range | object | 否 | 新增成员 |
| add\_member\_range.userid\_list | string \[\] | 否 | 新增成员的userid |
| del\_member\_range | object | 否 | 删除成员 |
| del\_member\_range.userid\_list | string \[\] | 否 | 删除成员的userid |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

## [](#%E5%88%A0%E9%99%A4%E6%99%BA%E8%83%BD%E8%A1%A8%E6%A0%BC%E6%8C%87%E5%AE%9A%E6%88%90%E5%91%98%E9%A2%9D%E5%A4%96%E6%9D%83%E9%99%90)删除智能表格指定成员额外权限

该接口用于删除智能表格指定成员额外权限

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/smartsheet/content\_priv/delete\_rule?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
	"docid": "DOCID",
	"rule_id_list": [
		2
	]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| docid | string | 是 | 智能表ID，通过[新建文档接口](#43939)创建后获得 |
| rule\_id\_list | uint32 \[\] | 是 | 需要删除的规则id列表 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |

# 管理收集表

创建收集表

最后更新：2025/08/18

目录

-   [question\_extend\_setting字段描述](#question-extend-setting%E5%AD%97%E6%AE%B5%E6%8F%8F%E8%BF%B0)
-         [文本](#%E6%96%87%E6%9C%AC)
-         [单选](#%E5%8D%95%E9%80%89)
-         [多选](#%E5%A4%9A%E9%80%89)
-         [位置](#%E4%BD%8D%E7%BD%AE)
-         [图片](#%E5%9B%BE%E7%89%87)
-         [文件](#%E6%96%87%E4%BB%B6)
-         [日期](#%E6%97%A5%E6%9C%9F)
-         [时间](#%E6%97%B6%E9%97%B4)
-         [时长](#%E6%97%B6%E9%95%BF)
-         [体温](#%E4%BD%93%E6%B8%A9)
-         [部门](#%E9%83%A8%E9%97%A8)
-         [成员](#%E6%88%90%E5%91%98)

该接口用于创建收集表。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/create\_form?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
  "spaceid": "SPACEID",
  "fatherid": "FATHERID",
  "form_info": {
    "form_title": "FORM_TITLE",
    "form_desc": "FORM_DESC",
    "form_header": "FORM_HEADER",
    "form_question": {
      "items": [
        {
          "question_id": 1,
          "title": "TITLE",
          "pos": 1,
          "status": 1,
          "reply_type": 1,
          "must_reply": false,
          "note": "NOTE",
          "option_item": [
            {
              "key": 1,
              "value": "VALUE",
              "status": 1
            }
          ],
          "placeholder": "PLACEHOLDER",
          "question_extend_setting": {}
        }
      ]
    },
    "form_setting": {
      "fill_out_auth": 0,
      "fill_in_range": {
        "userids": [
          "USER_1",
          "USER_2",
          "USER_3"
        ],
        "departmentids": [
          10001,
          10002,
          10003
        ]
      },
      "setting_manager_range": {
        "userids": [
          "USER_4",
          "USER_5",
          "USER_6"
        ]
      },
      "timed_repeat_info": {
        "enable": false,
        "week_flag": 0,
        "remind_time": 0,
        "repeat_type": 0,
        "skip_holiday": false,
        "day_of_month": 1,
        "fork_finish_type": 0
      },
      "allow_multi_fill": false,
      "timed_finish": 0,
      "can_anonymous": false,
      "can_notify_submit": false
    }
  }
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| spaceid | string | 否 | 空间spaceid |
| fatherid | string | 否 | 父目录fileid, 在根目录时为空间spaceid |
| form\_info | obj | 是 | 收集表信息 |
| form\_title | string | 是 | 收集表标题 |
| form\_desc | string | 否 | 收集表描述 |
| form\_header | string | 否 | 收集表表头背景图链接 |
| form\_question | object | 是 | 收集表的问题列表 |
| items | object\[\] | 是 | 问题数组。不超过200个。 |
| question\_id | uint32 | 是 | 问题id，从1开始。如果是家校范围收集表，id从2开始。 |
| title | string | 是 | 问题描述 |
| pos | uint32 | 是 | 问题序号，从1开始。 |
| status | uint32 | 是 | 问题状态。1：正常；2：被删除 |
| reply\_type | uint32 | 是 | 问题类型。1：文本；2：单选；3：多选；5：位置；9：图片；10：文件；11：日期；14：时间；15：下拉列表；16：体温；17：签名；18：部门；19：成员 22：时长 |
| must\_reply | bool | 是 | 是否必答 |
| note | string | 否 | 问题备注 |
| placeholder | string | 否 | 编辑提示 |
| question\_extend\_setting | object | 否 | 问题的额外设置。不同问题类型有相应的设置，详见[question\_extend\_setting字段描述](#43942/question_extend_setting) |
| option\_item | object\[\] | 是 | 单选/多选/下拉列表题的选项列表 |
| key | uint32 | 是 | 选项key（1，2，3...） |
| value | string | 是 | 选项内容 |
| status | uint32 | 是 | 选项状态。1：正常；2：被删除 |
| form\_setting | object | 否 | 收集表设置 |
| fill\_out\_auth | uint32 | 否 | 填写权限。0：所有人；1：企业内指定人/部门；4:家校所有范围。默认为0，所有人可填写。 |
| fill\_in\_range | object | 否 | 指定的可填写的人/部门。当`timed_repeat_info.enable`为`true`时必填 |
| userids | string\[\] | 否 | 企业成员userid列表 |
| departmentids | uint64\[\] | 否 | 部门id列表 |
| setting\_manager\_range | object | 否 | 收集表管理员 |
| timed\_repeat\_info | object | 否 | 定时重复设置项 |
| timed\_repeat\_info.enable | bool | 否 | 是否开启定时重复 |
| timed\_repeat\_info.remind\_time | uint32 | 否 | 提醒时间，为第一次提醒的时间戳。重复提醒的时间根据timed\_repeat\_info的相关字段计算。  
如remind\_time设置为当天10:00的时间戳，同时repeated\_type设置了每天重复，那么每天的10:00都会触发提醒。 |
| timed\_repeat\_info.repeat\_type | uint32 | 否 | 重复类型。0：每周；1：每天；2：每月 |
| timed\_repeat\_info.week\_flag | uint32 | 否 | 每周几重复，按bit组合，只能repeat\_type = 0 时填写。  
bit 0: 周一； bit 1: 周二；bit 2: 周三；bit 3: 周四； bit 4: 周五；bit 5: 周六 bit 6: 周日。如`1`表示周一，`2`表示周二，`4`表示周三，`96`表示周六和周日 |
| timed\_repeat\_info.skip\_holiday | bool | 否 | 自动跳过节假日，只能repeat\_type = 1 时填写。 |
| timed\_repeat\_info.day\_of\_month | uint32 | 否 | 每月的第几天（1 - 31），只能repeat\_type = 2时填写 |
| timed\_repeat\_info.fork\_finish\_type | uint32 | 否 | 是否允许补填。0：允许；1：仅当天；2：最后五天内；3：一个月内；4：下一次生成前 |
| allow\_multi\_fill | bool | 否 | 是否允许每人提交多份。默认false |
| timed\_finish | uint32 | 否 | 定时关闭。定时重复与定时结束互斥，若都填，优先定时重复 |
| can\_anonymous | bool | 否 | 是否支持匿名填写。默认false |
| can\_notify\_submit | bool | 否 | 是否有回复时提醒。默认false |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "formid": "FORMID"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| formid | string | 收集表id |

## [](#question-extend-setting%E5%AD%97%E6%AE%B5%E6%8F%8F%E8%BF%B0)question\_extend\_setting字段描述

### [](#%E6%96%87%E6%9C%AC)文本

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.text\_setting | object | 否 | 文本题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.text\_setting.validation\_type | uint32 | 否 | 校验类型。0: 字符个数 1: 数字 2: 电子邮箱 3: 网址 4: 身份证 5: 手机号（大陆地区） 6: 固定电话。  
默认值为0。 |
| question\_extend\_setting.text\_setting.validation\_detail | uint32 | 否 | 校验详情。1: 字符数不超过 2: 字符数不小于 3: 字符数等于 4: 数字没有限制 5: 数字大于 6: 数字大于等于 7: 数字小于 8: 数字小于等于 9: 数字在范围之间 10: 数字不在范围之间 11: 数字为整数。 |
| question\_extend\_setting.text\_setting.char\_len | uint32 | 否 | 字符长度 |
| question\_extend\_setting.text\_setting.number\_min | double | 否 | 数字的区间左端 |
| question\_extend\_setting.text\_setting.number\_max | double | 否 | 数字的区间右端 |

使用限制：

| validation\_type | 适用的validation\_detail以及字段 |
| --- | --- |
| 0 | 1: 字符数不超过 2: 字符数不小于 3: 字符数等于。要求`char_len`必须有值且大于0，最大4000 |
| 1 | 4: 数字没有限制 5: 数字大于(`number_min`) 6: 数字大于等于(`number_min`) 7: 数字小于(`number_max`) 8: 数字小于等于(`number_max`) 9: 数字在范围之间(`number_min`、`number_max`) 10: 数字不在范围之间(`number_min`、`number_max`) 11: 数字为整数 |

### [](#%E5%8D%95%E9%80%89)单选

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.radio\_setting | object | 否 | 单选校验设置。不填则不会校验 |
| question\_extend\_setting.radio\_setting.add\_other\_option | bool | 否 | 是否增加“其他”选项 |

### [](#%E5%A4%9A%E9%80%89)多选

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.checkbox\_setting | object | 否 | 多选校验设置。不填则不会校验 |
| question\_extend\_setting.checkbox\_setting.add\_other\_option | bool | 否 | 是否增加“其他”选项 |
| question\_extend\_setting.checkbox\_setting.type | uint32 | 否 | 多选类型。0: 不限制可选数量 1: 至少选择 2: 最多选择 3: 固定选择。结合`number`使用。默认为0 |
| question\_extend\_setting.checkbox\_setting.number | uint32 | 否 | 多选题可勾选的数量的限制，`type`为`1`、`2`、`3`需指定并且大于0的值。不能超过选项`option_item`个数 |

> 如 { ... "checkbox\_setting": {"type": 1, "number": 2} ...}，表示至少勾选2个选项。

### [](#%E4%BD%8D%E7%BD%AE)位置

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.location\_setting | object | 否 | 地址题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.location\_setting.location\_type | uint32 | 否 | 位置类型。0: 省/市/区/街道+详细地址 1: 省/市 2: 省/市/区 3: 省/市/区/街道 4: 自动定位 |
| question\_extend\_setting.location\_setting.distance\_type | uint32 | 否 | 允许定位范围。0: 当前位置 1: 附近100米 2: 附近200米 3: 附近300米，`location_type`为`4`适用 |

### [](#%E5%9B%BE%E7%89%87)图片

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.image\_setting | object | 否 | 图片题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.image\_setting.camera\_only | bool | 否 | 是否仅限手机拍照。默认为 false |
| question\_extend\_setting.image\_setting.upload\_image\_limit | object | 否 | 数量和大小限制信息 |
| question\_extend\_setting.image\_setting.upload\_image\_limit.count\_limit\_type | uint32 | 否 | 数量限制类型。0: 等于`count`数量 1: 小于等于`count`数量 |
| question\_extend\_setting.image\_setting.upload\_image\_limit.count | uint32 | 否 | 限制的数量。默认9张，取值范围: \[1, 9\] |
| question\_extend\_setting.image\_setting.upload\_image\_limit.max\_size | uint64 | 否 | 单个文件大小限制MB。不填该字段表示无限制，可填写的最大值为3000 |

### [](#%E6%96%87%E4%BB%B6)文件

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.file\_setting | object | 否 | 文件题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.file\_setting.upload\_file\_limit | object | 否 | 数量和大小限制信息 |
| question\_extend\_setting.file\_setting.upload\_file\_limit.count\_limit\_type | uint32 | 否 | 数量限制类型。0: 等于`count`数量 1: 小于等于`count`数量 |
| question\_extend\_setting.file\_setting.upload\_file\_limit.count | uint32 | 否 | 限制的数量。默认9个，取值范围: \[1, 9\] |
| question\_extend\_setting.file\_setting.upload\_file\_limit.max\_size | uint64 | 否 | 单个文件大小限制MB。不填该字段表示无限制，可填写的最大值为3000 |

### [](#%E6%97%A5%E6%9C%9F)日期

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.date\_setting | object | 否 | 日期题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.date\_setting.date\_format\_type | uint32 | 否 | 日期格式。0: 年/月/日/时/分 1: 年/月/日 2: 年/月 |

### [](#%E6%97%B6%E9%97%B4)时间

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.time\_setting | object | 否 | 时间题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.time\_setting.time\_format\_type | uint32 | 否 | 时间格式。0: 时分 1: 时分秒 |

### [](#%E6%97%B6%E9%95%BF)时长

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.duration\_setting | object | 否 | 时长题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.duration\_setting.time\_scale | uint32 | 否 | 时间刻度。1: 按天 2: 按小时。默认为1 |
| question\_extend\_setting.duration\_setting.date\_type | uint32 | 否 | 日期类型。1: 自然日 2: 工作日（跳过双休和法定节假日）。默认为1 |
| question\_extend\_setting.duration\_setting.day\_range | uint32 | 否 | 单位换算，多少小时/天，`time_scale`为`2`适用。取值范围：\[1, 24\] ，默认为24 |

### [](#%E4%BD%93%E6%B8%A9)体温

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.temperature\_setting | object | 否 | 体温题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.temperature\_setting.unit\_type | uint32 | 否 | 温度单位。0: 摄氏度 1: 华氏度 。默认为0 |

### [](#%E9%83%A8%E9%97%A8)部门

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.department\_setting | object | 否 | 部门题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.department\_setting.allow\_multiple\_selection | bool | 否 | 是否允许多选，默认不允许 |

### [](#%E6%88%90%E5%91%98)成员

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| question\_extend\_setting.member\_setting | object | 否 | 成员题的题目设置，不填时将使用默认设置 |
| question\_extend\_setting.member\_setting.allow\_multiple\_selection | bool | 否 | 是否允许多选，默认不允许 |

编辑收集表

最后更新：2025/01/03

该接口用于编辑收集表。

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/modify\_form?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
  "oper": 1,
  "formid": "FORMID",
  "form_info": {
    "form_title": "FORM_TITLE",
    "form_desc": "FORM_DESC",
    "form_header": "FORM_HEADER",
    "form_question": {
      "items": [
        {
          "question_id": 1,
          "title": "TITLE",
          "pos": 1,
          "status": 1,
          "reply_type": 1,
          "must_reply": false,
          "note": "NOTE",
          "option_item": [
            {
              "key": 1,
              "value": "VALUE",
              "status": 1
            }
          ],
          "placeholder": "PLACEHOLDER",
          "question_extend_setting": {}
        }
      ]
    },
    "form_setting": {
      "fill_out_auth": 0,
      "fill_in_range": {
        "userids": [
          "USER_1",
          "USER_2",
          "USER_3"
        ],
        "departmentids": [
          10001,
          10002,
          10003
        ]
      },
      "setting_manager_range": {
        "userids": [
          "USER_4",
          "USER_5",
          "USER_6"
        ]
      },
      "timed_repeat_info": {
        "enable": false,
        "week_flag": 0,
        "remind_time": 0,
        "repeat_type": 0,
        "skip_holiday": false,
        "day_of_month": 1,
        "fork_finish_type": 0
      },
      "allow_multi_fill": false,
      "timed_finish": 0,
      "can_anonymous": false,
      "can_notify_submit": false
    }
  }
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| oper | uint32 | 是 | 操作类型。1：全量修改问题；2：全量修改设置 |
| formid | string | 是 | 收集表id |
| form\_title | string | 否 | 收集表标题（操作1修改） |
| form\_desc | string | 否 | 收集表描述（操作1修改） |
| form\_header | string | 否 | 收集表表头背景图链接（操作1修改） |
| form\_question | object | 否 | 收集表的问题列表（操作1修改） |
| items | object\[\] | 是 | 问题数组 |
| question\_id | uint32 | 是 | 问题id，从1开始。如果是家校范围收集表，id从2开始。 |
| title | string | 是 | 问题描述 |
| pos | uint32 | 是 | 问题序号，从1开始。 |
| status | uint32 | 是 | 问题状态。1：正常；2：被删除 |
| reply\_type | uint32 | 是 | 问题类型。1：文本；2：单选；3：多选；5：位置；9：图片；10：文件；11：日期；14：时间；15：下拉列表；16：体温；17：签名；18：部门；19：成员 22：时长 |
| must\_reply | bool | 是 | 是否必答 |
| note | string | 否 | 问题备注 |
| placeholder | string | 否 | 编辑提示 |
| question\_extend\_setting | object | 否 | 问题的额外设置。不同问题类型有相应的设置，详见[question\_extend\_setting字段描述](#43942/question_extend_setting) |
| option\_item | object\[\] | 是 | 单选/多选/下拉列表题的选项列表 |
| key | uint32 | 是 | 选项key（1，2，3...） |
| value | string | 是 | 选项内容 |
| status | uint32 | 是 | 选项状态。1：正常；2：被删除 |
| form\_setting | object | 否 | 收集表设置（操作2修改） |
| fill\_out\_auth | uint32 | 是 | 填写权限。0：所有人；1：企业内指定人/部门。若收集表当前为家校范围，则无法修改。 |
| fill\_in\_range | object | 否 | 指定的可填写的人/部门 |
| userids | string\[\] | 否 | 企业成员userid列表 |
| departmentids | uint64\[\] | 否 | 部门id列表 |
| setting\_manager\_range | object | 否 | 收集表管理员 |
| timed\_repeat\_info | object | 否 | 定时重复设置项 |
| timed\_repeat\_info.enable | bool | 否 | 是否开启定时重复 |
| timed\_repeat\_info.remind\_time | uint32 | 否 | 提醒时间 |
| timed\_repeat\_info.repeat\_type | uint32 | 否 | 重复类型。0：每周；1：每天；2：每月 |
| timed\_repeat\_info.week\_flag | uint32 | 否 | 每周几重复，只能repeat\_type = 0 时填写。1：星期一；2：星期二；4：星期三；8：星期四；16：星期五；32：星期六；64：星期日 |
| timed\_repeat\_info.skip\_holiday | bool | 否 | 自动跳过节假日，只能repeat\_type = 1 时填写。 |
| timed\_repeat\_info.day\_of\_month | uint32 | 否 | 每月的第几天（1 - 31），只能repeat\_type = 2时填写 |
| timed\_repeat\_info.fork\_finish\_type | uint32 | 否 | 是否允许补填。0：允许；1：仅当天；2：最后五天内；3：一个月内；4：下一次生成前 |
| allow\_multi\_fill | bool | 否 | 是否允许每人提交多份。默认false |
| timed\_finish | uint32 | 否 | 定时关闭。定时重复与定时结束互斥，若都填，优先定时重复 |
| can\_anonymous | bool | 否 | 是否支持匿名填写。默认false |
| can\_notify\_submit | bool | 否 | 是否有回复时提醒。默认false |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限

**返回示例**

```json
{
	"errcode": 0,
	"errmsg": "ok"
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |


获取收集表信息

最后更新：2023/03/15

该接口用于读取收集表的信息

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/get\_form\_info?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
    "formid":"FORMID"
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| formid | string | 是 | 操作的收集表ID |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能操作该应用创建的文档

**返回示例**

```json
{
    "errcode":0,
    "errmsg":"ok",
    "form_info":{
        "formid":"FORMID1",
        "form_title":"api创建的收集表_周期",
        "form_desc":"这是描述",
        "form_header":"URL",
        "form_question":{
            "items":[
                {
                    "question_id":1,
                    "title":"问题1",
                    "pos":1,
                    "status":1,
                    "reply_type":1,
                    "must_reply":true,
                    "note":"问题备注1",
                    "placeholder":"提示1"
                },
                {
                    "question_id":2,
                    "title":"问题2",
                    "pos":2,
                    "status":1,
                    "reply_type":2,
                    "must_reply":false,
                    "note":"问题备注2",
                    "option_item":[
                        {
                            "key":1,
                            "value":"A",
                            "status":1
                        },
                        {
                            "key":2,
                            "value":"B",
                            "status":1
                        },
                        {
                            "key":3,
                            "value":"C",
                            "status":1
                        }
                    ],
                    "placeholder":"提示2"
                }
            ]
        },
        "form_setting":{
            "fill_out_auth":1,
            "fill_in_range":{
                "departmentids":[
                    1
                ],
                "userids": [
                    "USERID1",
                    "USERID2"
            },
            "setting_manager_range":{
                "userids":[
                    "USERID1",
                    "USERID2"
                ]
            },
            "timed_repeat_info":{
                "enable":true,
                "remind_time":1668389400,
                "rule_ctime":1668418140,
                "rule_mtime":1668418140,
                "repeat_type":1,
                "skip_holiday":false
            },
            "allow_multi_fill":false,
            "timed_finish":0,
            "can_anonymous":false,
            "can_notify_submit":true
        },
        "repeated_id":[
            "REPEAT_ID1"
        ]
    }
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| form\_info | object | 收集表信息 |
| formid | string | 收集表id |
| form\_title | string | 收集表标题 |
| form\_desc | string | 收集表描述 |
| form\_header | string | 收集表表头背景图链接 |
| form\_question | object | 收集表的问题列表 |
| form\_setting | object | 收集表的设置 |
| repeated\_id | string\[\] | 收集表的周期id，用于获取答案列表和具体的回答 |

收集表的统计信息查询

最后更新：2023/03/07

该接口用于获取收集表的统计信息、已回答成员列表和未回答成员列表

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/get\_form\_statistic?access\_token=ACCESS\_TOKEN

**请求包体**

```json
// 仅获取统计结果
{
    "repeated_id":"REPEATED_ID1",
    "req_type":1
}
// 获取已提交的列表
{
    "repeated_id":"REPEATED_ID2",
    "req_type":2,
    "start_time":1667395287,
    "end_time":1668418369,
    "limit":20,
    "cursor":1
}
// 获取未提交的列表
{
    "repeated_id":"REPEATED_ID3",
    "req_type":3,
    "limit":20,
    "cursor":1
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| repeated\_id | string | 是 | 操作的收集表的repeated\_id,来源于get\_form\_info的返回 |
| req\_type | uint32 | 是 | 请求类型 1:只获取统计结果 2:获取已提交列表 3:获取未提交列表 |
| start\_time | uint64 | 否 | 拉取已提交列表时必填，其余type不填。筛选开始时间，以当天的00:00:00开始筛选 |
| end\_time | uint64 | 否 | 拉取已提交列表时必填，其余type不填。筛选结束时间，以当天的23:59:59结束筛选 |
| limit | uint64 | 否 | 分页拉取时批次大小，最大10000 |
| cursor | uint64 | 否 | 分页拉取的游标，首次不传 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能操作该应用创建的文档

**返回示例**

```json
// req_type = 1 仅获取统计信息
{
    "errcode":0,
    "errmsg":"ok",
    "fill_cnt":1,
    "fill_user_cnt":1,
    "unfill_user_cnt":90
}
// req_type = 2,获取已提交列表
{
    "errcode":0,
    "errmsg":"ok",
    "fill_cnt":1,
    "fill_user_cnt":1,
    "unfill_user_cnt":90,
    "submit_users":[
        {
            "userid":"USERID1",
            "submit_time":1668418200,
            "answer_id":1,
            "user_name":"USER_NAME1"
        },
        {
            "tmp_external_userid":"TMP_EXTERNAL_USERID1",
            "submit_time":1668418200,
            "answer_id":2,
            "user_name":"USER_NAME2"
        }
     ],
    "has_more":false,
    "cursor":1
}
// req_type = 3,获取未提交列表，仅当限制提交范围时有结果
{
    "errcode":0,
    "errmsg":"ok",
    "fill_cnt":1,
    "fill_user_cnt":1,
    "unfill_user_cnt":90,
    "unfill_users":[
        {
            "userid":"USERID1",
            "user_name":"USER_NAME1"
        }
    ],
    "has_more":false,
    "cursor":1
} 
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| fill\_cnt | uint64 | 已填写次数 |
| fill\_user\_cnt | uint64 | 已填写人数 |
| unfill\_user\_cnt | uint64 | 未填写人数 |
| submit\_users | object\[\] | 已填写人列表 |
| tmp\_external\_userid | string | 外部用户临时id，匿名填写不返回，同一个用户在不同的收集表中返回的该id不一致。  
可进一步通过[tmp\_external\_userid的转换](#46252)接口转换成external\_userid，方便识别外部填写人的身份。 |
| userid | string | 企业内成员的id，匿名填写不返回 |
| submit\_time | uint64 | 提交时间 |
| answer\_id | uint64 | 答案id |
| user\_name | string | 名字，匿名填写不返回 |
| userid | string | 企业内成员的id，匿名填写不返回 |
| unfill\_users | object\[\] | 未填写人列表 |
| user\_name | string | 名字 |
| userid | string | 企业内成员的id |
| has\_more | bool | 是否还有更多 |
| cursor | uint64 | 上次分页拉取返回的cursor |


读取收集表答案

最后更新：2023/07/12

该接口用于读取收集表的答案

**请求方式**：POST（**HTTPS**）  
**请求地址**: https://qyapi.weixin.qq.com/cgi-bin/wedoc/get\_form\_answer?access\_token=ACCESS\_TOKEN

**请求包体**

```json
{
    "repeated_id":"REPEATED_ID1",
    "answer_ids":[
        1
    ]
}
```

**参数说明**

| 参数 | 类型 | 是否必须 | 说明 |
| --- | --- | --- | --- |
| repeated\_id | string | 是 | 操作的收集表周期id |
| answer\_ids | uint64\[\] | 是 | 需要拉取的答案列表，批次大小最大100 |

**权限说明**

-   自建应用需配置到“[可调用应用](#43883)”列表中的应用secret所获取的accesstoken来调用（[accesstoken如何获取？](#10013/%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token)）
-   第三方应用需具有“文档”权限
-   代开发自建应用需具有“文档”权限
-   只能操作该应用创建的文档

**返回示例**

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "answer": {
    "answer_list": [
      {
        "answer_id": 15,
        "user_name": "USER_NAME1",
        "ctime": 1668430580,
        "mtime": 1668430580,
        "reply": {
          "items": [
            {
              "question_id": 1,
              "text_reply": "Ndjnd"
            },
            {
              "question_id": 2,
              "option_reply": [
                2
              ]
            },
            {
              "question_id": 3,
              "text_reply": "20:53"
            },
            {
              "question_id": 4,
              "text_reply": "73℃"
            },
            {
              "question_id": 5,
              "file_extend_reply": [
                {
                  "name": "FILE_NAME1",
                  "fileid": "FILEID1"
                }
              ]
            },
            {
              "question_id": 6,
              "text_reply": "四川省/成都市/武侯区/天府三街(峰汇中心)"
            },
            {
              "question_id": 7,
              "text_reply": "test"
            },
            {
              "question_id": 8,
              "option_reply": [
                1
              ]
            },
            {
              "question_id": 9,
              "text_reply": "2022年11月"
            },
            {
              "question_id": 10,
              "option_reply": [
                5
              ]
            },
            {
              "question_id": 11,
              "option_reply": [
                3
              ],
              "option_extend_reply": [
                {
                  "option_reply": 3,
                  "extend_text": "test"
                }
              ]
            },
            {
              "question_id": 12,
              "department_reply": {
                "list": [
                  {
                    "department_id": 3
                  }
                ]
              }
            },
            {
              "question_id": 13,
              "member_reply": {
                "list": [
                  {
                    "userid": "zhangsan"
                  }
                ]
              }
            },
            {
              "question_id": 14,
              "duration_reply": {
                "begin_time": 1586136317,
                "end_time": 1586236317,
                "time_scale": 0,
                "day_range": 0,
                "days": 1.0,
                "hours": 2.5
              }
            }
          ]
        },
        "answer_status": 1,
        "tmp_external_userid": "TMP_EXTERNAL_USERID1"
      }
    ]
  }
}
```

**参数说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| errcode | int32 | 错误码 |
| errmsg | string | 错误码说明 |
| answer | object | 答案 |
| answer\_list | object\[\] | 答案列表 |
| answer\_id | uint64 | 答案id |
| user\_name | string | 用户名 |
| ctime | uint64 | 创建时间 |
| mtime | uint64 | 修改时间 |
| reply | object | 该用户的答案明细 |
| items | object\[\] | 每个问题的答案 |
| question\_id | uint64 | 问题id |
| text\_reply | string | 答案 |
| option\_reply | uint32\[\] | 选择题答案，多选题有多个答案 |
| option\_extend\_reply | object\[\] | 选择题，其他选项列表 |
| option\_extend\_reply.option\_reply | uint32 | 其他选项的答案id |
| option\_extend\_reply.extend\_text | string | 其他选项的答案字符串 |
| file\_extend\_reply | object\[\] | 文件题答案列表 |
| file\_extend\_reply.name | string | 文件题答案的文件名 |
| file\_extend\_reply.fileid | string | 文件题答案的文件id |
| department\_reply | object | 部门题答案 |
| department\_reply.list | object\[\] | 部门题选择的部门列表 |
| department\_reply.list\[\].department\_id | object\[\] | 部门id |
| member\_reply | object | 成员题答案 |
| member\_reply.list | object\[\] | 成员选择的成员列表 |
| member\_reply.list\[\].userid | object\[\] | 成员id |
| duration\_reply | object | 时长题答案 |
| duration\_reply.begin\_time | uint32 | 开始时间，时间戳 |
| duration\_reply.end\_time | uint32 | 结束时间，时间戳 |
| duration\_reply.time\_scale | uint32 | 时间刻度。1: 按天 2: 按小时 |
| duration\_reply.day\_range | uint32 | 单位换算，多少小时/天。`time_scale`为`2`返回 |
| duration\_reply.days | float | 天数。`time_scale`为`1`返回 |
| duration\_reply.hours | float | 小时数。`time_scale`为`2`返回 |
| answer\_status | uint32 | 答案状态 1:正常 3:统计者移除此答案或删除 |
| tmp\_external\_userid | string | 外部用户临时id，匿名填写不返回，同一个用户在不同的收集表中返回的该id不一致。  
可进一步通过[tmp\_external\_userid的转换](#46252)接口转换成外部联系人的external\_userid，方便识别外部填写人的身份。 |
| userid | string | 用户id，匿名填写不返回 |