
对象定义
========

__目录__

-  [Category](#category)  分类
-  [Goods](#goods)  商品信息
-  [GoodsAttribute](#goodsattribute)  商品扩展属性
-  [GoodsPic](#goodspic)  商品图片
-  [Navigation](#navigation)  导航条
-  [Sort](#sort)  分类
-  [User](#user)  用户

#category

分类

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| cid	 | ID | String	 |		 | 8	   | True	  |		   |	 |
| name	 | 名字 | String	 |		 | 24 	   | True	  |		   |	 |
| products | 产品列表 | List: [Product](#product) | | | False | None | |
| type	 | 类别 | String	 |		 | 8	   | True	  |		   |	 |

#product

商品信息

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| attribute | 属性 | Reference: [ProductsAttribute](#productsattribute) | | | False | | |
| category | 类别 | Reference: [Category](#category) | | | False |     |	 	 |
| name	 | 名字 | String |  		 | 64	   | True	  |		   |	 |
| updated_at | 更新时间 | DateTime | |	   | True	  |	now	   |	 |
| pic	 | 图片 | List: Embedded [ProductPic](#productpic) | | | False | | |
| material | 材料 | String |      | 16      | False |      | 材料种类 |
| style  | 风格 | String |        | 16      | False |      | 风格种类 |

#productpic

产品图片  -- 内嵌对象

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| created_at | 创建时间 | DateTime | |	   | True	  |	now	   |	 |
| name   | 名字 | String | 		 | 32	   | True	  |		   |	 |
| path   | 路径 | String |  		 | 128	   | True	  |		   |	 |






#productsattribute

商品扩展属性

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |

#navigation

导航条

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id     |      | ObjectId |	 |		   | False    | None   |	 |
| display | 显示 | Bool |		 |		   | True	  | True   | True:显示 |
| name	 | 名字 | String | 1		 | 16	   | True	  |		   |	 |
| pic	 | 图片 | String |		 | 128	   | False	  |		   |	 |
| type   | 类型 | String |		 |		   | False    | None   |	 |
| url	 | 链接 | String |		 | 128	   | False	  |		   |	 |

#sort

分类

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| name	 | 名字 | String	 |		 | 16 	   | True	  |		   |	 |
| sn	 | 序号 | String	 |		 | 8	   | True	  |		   |	 |

#user

用户

| 字段名 | 说明 | 类型 | 最小长度 | 最大长度 | 必填字段 | 缺省值 | 备注 |
|------- | -----| ---- | ------- | ------- | -------- | ------ | --- |
| id	 |		| ObjectId |	 |		   | False	  | None   |	 |
| email	 | 邮箱 | String  |		 |64	   | False	  |		   |	 |
| gender | 性别 | String  |		 | 10	   | False	  |	woman  |	 |
| level	 | 等级 | Int  |			 |		   | True	  |	0	   | 会员级别 |
| password | 用户口令 | String | | 64	   | True	  |        |	 |
| receipt | 收货信息 | List: Embedded: [ReceiptInformation](#receiptinformation) | | | False | | |
| role	 | 角色 | String |		 | 10	   | True	  | user   | user:用户;operator:操作员;superuser:超级管理员 |
| status | 状态 | Bool |			 |		   | False	  |		   | 0:禁用;1:启用 |
| telephone | 手机号 | String |	 | 16 	   | True	  |	None   |	 |
| real_name | 真实姓名 | String | | 16	   | False	  |	None   |     |
