# NCV6.5产品手册-网上报账

产品手册- V6.5

网上报账

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

名词解释 ..... 4  
第一章 概述 ..... 5  
1.1. 产品概述 ..... 5  
1.2. 产品价值 ..... 5  
第二章 应用场景 ..... 8  
2.1. 费用管理 ..... 8  
2.1.1. 业务单位的报账处理 ..... 8  
2.1.2. 共享服务中心的报账处理 ..... 23  
2.2. 应付管理 ..... 31  
2.2.1. 业务描述 ..... 31  
2.2.2. 业务流程 ..... 33  
2.2.3. 功能清单 ..... 33  
2.2.4. 产品解决方案 ..... 33  
2.3. 应收管理 ..... 37  
2.3.1. 业务描述 ..... 37  
2.3.2. 业务流程 ..... 38  
2.3.3. 功能清单 ..... 40  
2.3.4. 产品解决方案 ..... 40  
2.4. 现金管理 ..... 40  
2.4.1. 业务描述 ..... 40  
2.4.2. 业务流程 ..... 41  
2.4.3. 功能清单 ..... 41  
2.4.4. 产品解决方案 ..... 41  
2.5. 营销费用管理 ..... 43  
2.5.1. 业务描述 ..... 43  
2.5.2. 业务流程 ..... 44  
2.5.3. 功能清单 ..... 45  
2.5.4. 产品解决方案 ..... 46  
第三章 初始准备 ..... 47  
3.1. 门户创建 ..... 47  
3.2. 发布交易类型成为节点 ..... 48  
3.3. 定义单据模板 ..... 49  
3.4. 新建打印模板 ..... 53  
3.5. 组织建模 ..... 55  
3.6. 作业处理平台 ..... 55  
第四章 操作指南 ..... 55  
附录 1：本文参见其他手册清单 ..... 56

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供业务需求与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关本模块的主要业务场景、流程、以及对应的业务功能的介绍；第三部分是初始准备设置；第四部分是关于本模块功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。第五部分是演示导航，是大解决方案的节选，作为读者快速熟悉产品的参照。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录中对一些可能需要对照查询的关键点进行了补充说明，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《NC 培训手册-组织建模》-----深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助----针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《NC 培训手册-流程平台》----提供关于交易类型、流程设计工具的应用指导。

4. 《NC 培训手册-基础数据》-----可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

5. 《NC 培训手册-共享服务》——共享服务对网上报账的支持。

## 名词解释

暂无。

## 第一章 概述

#### 1.1. 产品概述

原 “网上报销” 产品改名为 “网上报账”，以 “网上报账” 产品作为企业全员发起财务相关业务流程的统一入口门户，新增基于不同角色视角的报账人门户、审批人门户。其中报账人门户可以填制单据、查看未完成单据、已完成单据；审批人门户可以查看待审批、已审批任务。本版暂时只纳入费用报账相关单据、应收单、应付单、收款单、付款单、付款申请，可以发起费用、应收、应付、资金收付款项业务流程，把企业财务管理的所有业务过程通过系统进行统一管理，通过流程显性化企业的管理制度，并降低人为干预的风险。

网上报账是所有财务前端业务的前台入口，主要完成企业全员应用时实际报账人发起的费用借款报销、应收应付、资金收付款业务流程，各级业务领导对业务进行审批的过程。费用管理、应收管理、应付管理则是企业财务部应用的产品，帮助企业财务部费用会计、应收应付会计等专岗对费用借款报销、应收应付、资金收付款业务进行审批、结算及核算处理。

V6.5 起支持共享服务：所有单据支持影像扫描与查看、在共享服务作业平台上进行作业派单。

网上报账产品中的报销单、借款单、费用申请单、预提单支持在共享服务中心作业平台中进行处理，共享服务中心作业平台处理时可以自定义单据模板样式、修改有限的单据字段、查看单据关联的影像、预览凭证；支持单据是否需要扫描影像、单据是否加急，加急状态的单据在共享服务中心会被优先提单及审核。

#### 1.2. 产品价值

### 1. 支持灵活的单据类型扩展

报销的各交易类型（包括自定义交易类型）均可发布为 Portal 端的节点，可根据业务需要在对应节点录入单据。单据录入节点可完成对借款单、报销单、还款单的查询、新增、修改、删除、复制、联查、打印等功能，同时按照审批权限，审批人可完成对借款单、报销单、还款单的审批相关操作。

### 2. 支持全员 portal 端的报销业务

支持用户在 portal 端处理个人借款、报销、还款的业务单据。

➢ 支持邮件审批、登录系统审批、手机移动审批多种审批方式。

➢ 支持联查审批情况和预算执行情况、资金计划。

➢ 支持打印审批信息。

### 3. 支持影像管理

1) 支持针对单据类型或交易类型设置影像扫描方式；

2）支持在移动终端制单时同步拍发票，单据保存时发票影像会直接传至影像中心；

3) 支持专岗扫描和制单人扫描两种扫描流程；

### 4. 应收管理

应收管理帮助企业处理所有债权业务及相关管理工作。

NC6.5 起，应收单与收款单支持共享服务业务流程：

1）应收单、收款单支持在轻量端【网上报账】产品中进行录入与审核。

2) 应收单、收款单支持工作流及共享服务作业派单处理。

3) 应收单、收款单支持在网上报账的报账人门户中“我要填单”、“我的单据”、“我的审批”中可见。

4) NC 端应收单、收款单支持影像查看。

5) 【网上报账】中的应收单、收款单支持影像扫描与影像查看。

### 5. 应付管理

应付管理帮助企业处理所有债务业务及相关管理工作.

1) 应付单与付款单支持在轻量端【网上报账】产品中进行录入与审核。

NC6.5 起，应付单与付款单支持共享服务业务流程：

2) 应付单与付款单支持工作流及共享服务作业派单处理。

3) 应付单与付款单支持在网上报账的报账人门户中“我要填单”、“我的单据”、“我的审批”中可见。

4) NC 端应付单与付款单支持影像查看。

5) 【网上报账】中的应付单与付款单支持影像扫描与影像查看。

6) 应付单支持在轻量端【网上报账】模块中拉式生成付款申请，支持多对一生成付款申请。

7) 支持一张付款申请按分单规则自动推式生成多张付款单。

### 6. 费用管理

费用管理在 V6.3 前命名为 “报销管理”，原用于帮助企业实现员工基于互联网进行费用报销，帮助企业处理所有日常费用报销业务。V6.3 起提供对费用管理与核算应用的支持，实现了报销前的费用申请控制、报销过程中及其后的费用分摊与结转、待摊费用摊销，并提供更多的查询统计报告。

V6.5 起增加与改进特性主要包括：

费用管理本版为了配合共享服务方案，支持共享服务作业平台功能，调整费用管理单据可支持工作流，使共享服务中心能够审核费用管理的单据。支持工作流的单据包括费用申请单、预提单、借款单、报销单（含还款单）、费用调整单。其他特性还包括：

1) 费用申请单、借款单、报销单、预提单、费用调整单支持影像查看。

2）借款单、报销单支持自动结算。

3）借款单、报销单交易类型上增加选项“手工结算”，不勾选时，单据生效时自动结算。

4）借款单、报销单表体增加“合同号”，支持关联付款合同，并回写合同执行数。

## 第二章 应用场景

#### 2.1. 费用管理

##### 2.1.1. 业务单位的报账处理

##### 2.1.1.1 业务描述

费用管理支持共享服务：费用管理产品中的报销单、借款单、费用申请单、预提单支持在共享服务中心作业平台中进行处理，共享服务中心作业平台处理时可以自定义单据模板样式、修改有限的单据字段、查看单据关联的影像、预览凭证；支持单据是否需要扫描影像、单据是否加急，加急状态的单据在共享服务中心会被优先提单及审核。

##### 2.1.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_262_1038_1076.jpg" alt="Image" width="78%" /></div>


##### 2.1.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="4">网上报账</td><td style='text-align: center; word-wrap: break-word;'>填写单据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务领导审批</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>扫描影像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计初审</td></tr></table>

##### 2.1.1.4 产品解决方案

网上报账可填写的单据包括：费用申请单、预提单、借款单、报销单。以下以差旅报销单填写为例，其他单据填写同报销单。

### 1. 直接填写报销单

1）以业务员身份登录系统。登录地址为：服务器IP地址+/portal，

如： $ \underline{\text{http://20.12.19.116:6357/portal。}} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_214_509_1022_995.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 2.1.1.4-1 共享服务登录</div>


## 2 ）在【报销人门户】中点击【我要填单】。

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_1106_1013_1520.jpg" alt="Image" width="71%" /></div>

<div style="text-align: center;">图 2.1.1.4-2 报账人门户填单</div>


3）在弹出的界面中选择【差旅费报销单】。

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_249_1028_665.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-3 选择报销单类型</div>


4）填写单据内容，点击【提交】，将单据提交给下一流程环节。

<div style="text-align: center;"><img src="imgs/img_in_image_box_167_763_1030_1186.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-4 提交单据</div>


### 2. 报销单参照申请单生成

1）打开报销单增加单据界面，点击【新增】按钮下的【费用申请单】。

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_1326_1027_1538.jpg" alt="Image" width="72%" /></div>

<div style="text-align: center;">图 2.1.1.4-5 参照费用申请单</div>


2）在弹出的费用申请单查询界面输入查询条件，点击【确定】，查询出所需的费用申请单。

<div style="text-align: center;"><img src="imgs/img_in_image_box_180_280_1009_856.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 2.1.1.4-6 查询费用申请单</div>


3）在查询出的费用申请单界面，选择待参照的费用申请单，点击【确定】，生成相应的报销单。

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_165_1059_757.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.1.1.4-7 选择费用申请单</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_154_839_1039_1176.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.1.1.4-8 参照生成的报销单</div>


### 3. 报销单冲借款

1）填写单据后，点击【业务处理】按钮下的【冲借款】进行冲借款操作。

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_188_1033_526.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.1.1.4-9 冲借款</div>


2）在弹出的界面选择待冲销的借款单，确认或修改冲借款金额。点击【确定】，完成冲借款操作。

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_647_1057_1166.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.1.1.4-10 填写冲借款金额</div>


3）点击【提交】，将单据提交给下一流程环节。

### 4. 报销单核销预提单

1）填写报销单据后，点击【业务处理】按钮下的【核销预提】进行冲借款操作。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_163_1097_531.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.1.1.4-11 核销预提</div>


2）在弹出的界面选择待核销的预提单，确认核销金额。点击【确定】，完成核销预提操作。

<div style="text-align: center;"><img src="imgs/img_in_image_box_154_693_1081_1392.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.1.1.4-12 选择核销的预提单</div>


3）点击【提交】，将单据提交给下一流程环节。

### 5. 业务领导审批

1）以系统管理员登陆，在【业务系统初始化】系统参数设置，增加 MP0001 参数，这一参数是为了避免来回切换审批界面而设置的，可以控制是否使用审批工作台，启用则可以使用审批工作台审批所有单据。审批工作台除了可以审批来自网上报账的单据，还可以审批来自 NC 端的单据，审批工作台可以查看 PDF 格式单据，界面如下：

<div style="text-align: center;"><img src="imgs/img_in_image_box_155_404_1017_949.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-13 审批工作台</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_155_1025_1019_1523.jpg" alt="Image" width="72%" /></div>


___

<div style="text-align: center;">图 2.1.1.4-14 审批工作台审批</div>


<div style="text-align: center;">← → ☐ 20.10.129.68:6588/mp/index.html#</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_161_210_1026_760.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-15 待审单据查看</div>


2）若不使用启用 MP0001 参数，则只能使用审批人门户审批来自网上报账的单据。

路径：【审批人门户】

业务领导在【审批人门户】选中待审批的单据，打开单据界面。

<div style="text-align: center;"><img src="imgs/img_in_image_box_155_950_1016_1365.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-16 单据查询</div>


业务领导查看单据内容，填写审批意见，点击【提交】进行审批操作。

<div style="text-align: center;"><img src="imgs/img_in_image_box_153_187_1085_728.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 2.1.1.4-17 单据审批</div>


### 6. 影像扫描（专岗）

路径：【网上报账】-【我的待办】

扫描专岗在【我的待办】中可找到报销人已提交并流转到扫描专岗的单据。【扫描方式配置】中影像扫描方式需设置为“专岗扫描”。

在【我的待办中】选择待扫描影像的单据

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_1030_1074_1261.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2.1.1.4-18 影像扫描</div>


在报销单据界面，点击【影像扫描】，弹出影像扫描界面。

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_151_1078_683.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.1.1.4-19 影像扫描</div>


点击【设备】选择相应的扫描设备，点击【扫描】扫描影像，扫描后，点击【保存】，将影像上传到影像系统。

<div style="text-align: center;"><img src="imgs/img_in_image_box_232_841_1042_1278.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 2.1.1.4-20 上传影像</div>


## 附：制单人扫描影像

影像扫描也可由填单人操作。

路径：【网上报账】-【差旅费报销单】

报销人在保存单据后，可打开影像系统扫描并上传影像。【扫描方式配置】中影像扫描方式需设置为“报销人扫描”。

在报销单据界面，点击【影像扫描】，弹出影像扫描界面。

<div style="text-align: center;"><img src="imgs/img_in_image_box_155_322_1078_673.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.1.1.4-21 影像界面</div>


点击【设备】选择相应的扫描设备，点击【扫描】扫描影像，扫描后，点击【保存】，将影像上传到影像系统。

<div style="text-align: center;"><img src="imgs/img_in_image_box_240_847_1050_1284.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 2.1.1.4-22 上传影像</div>


### 7. 会计初审

## 1 ）单张单据审批

路径：【审批人门户】

初审会计在【审批人门户】选中待审批的单据，打开单据界面。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="9">共4条数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>操作</td><td style='text-align: center; word-wrap: break-word;'>接收时间</td><td style='text-align: center; word-wrap: break-word;'>单据编号</td><td style='text-align: center; word-wrap: break-word;'>交易类型</td><td style='text-align: center; word-wrap: break-word;'>提交人</td><td style='text-align: center; word-wrap: break-word;'>金额</td><td style='text-align: center; word-wrap: break-word;'>单据日期</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'>流程</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12 15:22:54</td><td style='text-align: center; word-wrap: break-word;'>264X201411120010</td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'>业务员A</td><td style='text-align: center; word-wrap: break-word;'>1,230.00</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'>流程</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12 15:22:53</td><td style='text-align: center; word-wrap: break-word;'>264X201411120011</td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'>业务员A</td><td style='text-align: center; word-wrap: break-word;'>300.00</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'>流程</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12 15:22:53</td><td style='text-align: center; word-wrap: break-word;'>264X201411120012</td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'>业务员A</td><td style='text-align: center; word-wrap: break-word;'>2,300.00</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'>流程</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12 15:22:52</td><td style='text-align: center; word-wrap: break-word;'>264X201411120013</td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'>业务员A</td><td style='text-align: center; word-wrap: break-word;'>500.00</td><td style='text-align: center; word-wrap: break-word;'>2014-11-12</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.1.1.4-23 审批单据</div>


初审会计查看单据内容，并点击【影像查看】，查看上传的影像，

<div style="text-align: center;"><img src="imgs/img_in_image_box_183_483_1092_1014.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2.1.1.4-24 查看影像</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_200_1032_656.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.1.1.4-25 查看影像</div>


填写审批意见，点击【提交】进行审批操作。

<div style="text-align: center;"><img src="imgs/img_in_image_box_169_775_1066_1298.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.1.1.4-26 审批单据</div>


## 2 ）批量审批

路径：【网上报账】-【我的待办】

初审会计在【我的待办】中，可通过条码或二维扫描查询出待处理单据进行单据审批。选中【连续扫描】，可以查询出多条待办后批量审批。选中多条待办，点击【审批】弹出审批审批界面。

<div style="text-align: center;"><img src="imgs/img_in_image_box_183_256_1051_462.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-27 查找单据</div>


➢ 在批量审批界面，初审会计填写审批意见，点击【确定】，将所选全部待办任务审批通过。

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_565_1046_900.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1.4-28 批量审批</div>


报账单位的会计人员对报账单据初审完成后，根据工作流设置即进入共享服务平台上进行处理。

##### 2.1.2. 共享服务中心的报账处理

##### 2.1.2.1 业务描述

管理员做模板配置，配置好后，共享服务中心的业务人员就可以通过门户或任务处理节点处理业务了。这些操作都是在 portal 端完成的。

##### 2.1.2.2 业务流程


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">操作流程</td></tr><tr><td rowspan="5">初始化阶段</td><td style='text-align: center; word-wrap: break-word;'>管理员</td><td style='text-align: center; word-wrap: break-word;'>组长（科长）</td><td style='text-align: center; word-wrap: break-word;'>作业人员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模板设置</td><td style='text-align: center; word-wrap: break-word;'></td><td rowspan="2"><img src="imgs/img_in_seal_box_720_554_910_807.jpg" alt="Image"" /></td></tr><tr><td rowspan="3">任务查询</td><td style='text-align: center; word-wrap: break-word;'>作业组长门户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>作业任务管理</td><td rowspan="2">作业任务处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>任务查询</td></tr></table>

##### 2.1.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="6">共享服务</td><td rowspan="4">任务处理</td><td style='text-align: center; word-wrap: break-word;'>作业任务门户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>作业任务处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>作业组长门户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>作业任务处理</td></tr><tr><td rowspan="2">任务查询</td><td style='text-align: center; word-wrap: break-word;'>任务查询-管理员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>任务查询-组长</td></tr></table>

##### 2.1.2.4 产品解决方案

## 一、 任务处理阶段

## 1 组员

1) 作业人员门户

组长登录后可以看到【作业人员门户】，在该门户包含下面几部分内容，该门户也支持用户自己配置内容。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_540_1060_1023.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2.4-1 作业人员门户</div>


待办：作业人员登录门户后，可在门户首页的待办里看到待自己处理的任务数；鼠标点击后超链接到作业任务处理界面。

今日已办：当前作业人员在当天处理的任务总数。如果一个人对同一条任务即负责审核又负责复核，则在该统计时算一条；鼠标点击后超链接到作业任务处理界面。

今日排名：当前作业人员当日已处理任务总量在部门内的名次。

工作量：当前作业人员在当年每个月已处理的任务总量和平均任务量曲线图。

工作时间：当前作业人员在审核（复核）某个单据类型的工作总时间和平均工作时间曲线图。

待办任务：当前在作业人员手里的任务。可以直接对任务进行操作，且点击任务可以直接链接到作业任务处理界面。

## 2 ) 作业任务处理

路径：【共享服务】-【任务处理】-【作业任务处理】

a) 待处理页签：该页签内显示当前作业人员手里需要处理的任务。

<div style="text-align: center;"><img src="imgs/img_in_image_box_176_330_1047_832.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.2.4-2 作业任务处理界面</div>


## ☑ 按钮

【提取】：当作业人员手里没有待处理的任务时，点击提取，可以通过预置提取规则提取可处理的任务，展现在列表界面上。

【定向提取】：当作业人员需要按照某种条件提取任务时，可以应用定向提取按钮，输入提取条件后根据提取规则加条件定向过滤出可处理的任务，展现在列表界面上。

【申请调整】：当作业人员发现手里的任务不属于自己处理，需要组长重新分配改任务，可以点击申请调整按钮，输入申请调整原因，该任务的状态就修改为待调整。

【挂起】：当作业人员发现手里的任务暂时不处理，可以点击挂起按钮，把该任务挂起。当该任务能处理的时候，需要将该任务取消挂起之后再进行处理。

【查看影像】：当作业人员选中列表中的任务后，可以通过查看影像按钮查看该单据挂有的影像。

【查看历史】：当作业人员想查看该任务的处理历史时，可以通过查看历史按钮查看该任务的所有历史操作。

【查看原因】：当作业人员想查看组长的调整原因、分配原因，可以通过查看原因按钮查看该任务的调整

等原因。

## 注意：

➢ 需要定义消息模板以及消息接收人

业务人员审核时，支持驳回至制单人、影像扫描环节和会计初审环节，驳回时支持重走流程和不重走流程两种方式。重走流程则再次提交后，按照流程重新进行流转；不重走流程则再次提交后，直接到审核人员手里。

业务人员复核时，只支持驳回到审核人员手里。

驳回的任务不需要再次提取，直接到审核人手里。

审核环节，支持预览凭证。

## b) 待提取页签

该页签内显示该作业人员已经处理完成的任务。

<div style="text-align: center;"><img src="imgs/img_in_image_box_189_768_1049_1256.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2.4-3 作业任务已处理</div>


## ☑ 按钮

【查看影像】：当作业人员选中列表中的任务后，可以通过查看影像按钮查看该单据挂有的影像。

【查看历史】：当作业人员想查看该任务的处理历史时，可以通过查看历史按钮查看该任务的所有历史操作。

【查看原因】：当作业人员想查看组长的调整原因、分配原因，可以通过查看原因按钮查看该任务的调整等原因。

## c) 已驳回页签

该页签内显示该作业人员已经驳回的任务。

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_368_1048_863.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2.4-4 作业任务已驳回</div>


## ☑ 按钮

【查看影像】：当作业人员选中列表中的任务后，可以通过查看影像按钮查看该单据挂有的影像。

【查看历史】：当作业人员想查看该任务的处理历史时，可以通过查看历史按钮查看该任务的所有历史操作。

【查看原因】：当作业人员想查看组长的调整原因、分配原因，可以通过查看原因按钮查看该任务的调整等原因。

## 2 组长

## 1 ) 作业组长门户

组长登录后可以看到【作业组长门户】，在该门户包含下面几部分内容，该门户也支持用户自己配置内容。

<div style="text-align: center;"><img src="imgs/img_in_image_box_182_163_1052_705.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.2.4-5 作业组长门户配置</div>


待调整：显示该组长所管理的所有组员提交的申请调整的还未调整的任务的数量。点击该区域可以超链接到作业任务管理界面。

待提取：显示该组长所管理的范围内未被作业人员提取的任务的总数量。点击该区域可以超链接到作业任务管理界面。

在手任务：显示目前该组长所管理的组员手里的任务总量，审核、复核任务分开显示。

组任务统计：显示该组长所管理组在本年、本月、本周、今天累计已处理任务总量以及在所有组之间的排名；。

今日排名：显示该组长所管理的每个组员在当日处理的任务总量在组内的排名，并显示平均任务量。

工作时间：显示该组长所管理的组员在当日审核或复核某种单据类型的工作总时间和组内平均时间。

## 2 ）作业任务管理

路径：【共享服务】-【任务处理】-【作业任务管理】

组长应用该节点修改任务的紧急程度、调整任务等。

## a) 待调整页签

该页签内显示组长所管辖的作业人员申请调整的任务。表头上的筛选条件是对下面列表界面中可见内容的筛选。

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_182_1045_696.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.2.4-6 作业任务待调整</div>


## b) 待提取页签

该页签内显示组长所管辖的范围内还未被作业人员提取到的任务。

<div style="text-align: center;"><img src="imgs/img_in_image_box_179_847_1042_1348.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2.4-7 作业任务待提取</div>


## ☑ 按钮

【强制分配】：组长可以将待提取的任务强制分配给有权限处理任务的作业人员。

【紧急】：可以调整任务的紧急状态。

## c) 待提取页签

该页签内显示组长所管辖的范围内还未被作业人员提取到的任务。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_299_1040_825.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2.4-8 作业任务已提取</div>


## ☑ 按钮

【重新分配】：组长可以将作业人员手里的任务重新分配给其他人员。

【强制取回】：组长可以将作业人员手里的任务取回，待其他作业人员提取。

【紧急】：可以调整任务的紧急状态。

3) 作业任务查询

路径：【共享服务】-【任务处理】-【任务查询-组长】

组长应用该节点可以查询他管理范围内的所有状态下的任务。

#### 2.2. 应付管理

##### 2.2.1. 业务描述

1. 支持共享服务作业平台派单

V65 版本为配合共享服务方案，支持共享服务作业平台功能，调整应付单、付款单可支持工作流，使

共享服务中心能够审核应付管理的单据。

1）应付单、付款单支持工作流。原审批流也同样支持。

2）支持通过组织参数配置哪些组织使用工作流，哪些组织使用审批流。

3) 支持共享服务中心驳回单据到制单人。

4）支持制单人将共享服务中心驳回的单据直接提交回共享服务中心。

2. 应付单、付款单支持影像扫描与查看；

3. 付款单支持联查付款申请的影像；

4. 在报账人门户 “我要填单” 中可以录入应付单、付款单；

5. 在报账人门户 “未完成单据” 中可以查看当前用户所有的保存态应付单、付款单；

6. 在报账人门户“已完成单据”中可以查看当前用户所有的生效的应付单、付款单；

7. 在审批人门户“待审批”中可以查询需要审批的应付单、付款单并进行审核；

8. 应付单、红字应收单、收款单支持合并拉单生成付款申请；

1）拉单生成付款申请时，申请的金额可改，允许部分拉单；

2）拉单生成付款申请时，可以通过复制行的方式拆行；

3）应付单不支持推式生成付款申请；

9. 一张付款申请单可按分单规则自动推式生成多张付款单。

##### 2.2.2. 业务流程

### 2.1 应付挂账——手工录入应付

<div style="text-align: center;"><img src="imgs/img_in_image_box_877_278_931_322.jpg" alt="Image" width="4%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_256_341_943_616.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_254_645_941_772.jpg" alt="Image" width="57%" /></div>


##### 2.2.3. 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="4">网上报账</td><td style='text-align: center; word-wrap: break-word;'>填写单据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务领导审批</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>扫描影像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计初审</td></tr></table>

##### 2.2.4. 产品解决方案

### 1. 设置工作流

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_1256_1030_1479.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2.4-1 设置应付单工作流</div>

### 2. 制单

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_238_1023_804.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.2.4-2 应付单申请</div>


### 3. 影像扫描

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_901_1029_1447.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2.4-3 影像扫描</div>

### 4. 业务审核

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_220_1030_777.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2.4-4 业务审核</div>


### 5. 会计初审

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_872_1026_1428.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2.4-5 会计初审</div>


### 5. 审核

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_178_1034_731.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.2.4-6 审核</div>


### 6. 复核

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_845_1028_1413.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2.4-7 复核</div>

#### 2.3. 应收管理

##### 2.3.1. 业务描述

### 1. 支持共享服务作业平台派单

V65 版本为配合共享服务方案，支持共享服务作业平台功能，调整应收单、收款单可支持工作流，使共享服务中心能够审核应收管理的单据。

1）应收单、收款单支持工作流。原审批流也同样支持。

2）支持通过组织参数配置哪些组织使用工作流，哪些组织使用审批流。

3) 支持共享服务中心驳回单据到制单人。

4）支持制单人将共享服务中心驳回的单据直接提交回共享服务中心。

2. 应收单、收款单支持影像扫描与查看；

3. 在报账人门户“我要填单”中可以录入应收单、收款单；

4. 在报账人门户 “未完成单据” 中可以查看当前用户所有的保存态应收单、收款单；

5. 在报账人门户“已完成单据”中可以查看当前用户所有的生效的应收单、收款单；

6. 在审批人门户“待审批”中可以查询需要审批的应收单、收款单并进行审核。

##### 2.3.2. 业务流程

### 1. 应收挂账——手工录入应收

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_357_969_696.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_126_751_966_889.jpg" alt="Image" width="70%" /></div>

### 2. 应收挂账——自动生成应收

<div style="text-align: center;"><img src="imgs/img_in_image_box_126_247_969_585.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_128_645_963_779.jpg" alt="Image" width="70%" /></div>


## 3 收款——应收收款

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_872_969_1208.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_127_1271_965_1400.jpg" alt="Image" width="70%" /></div>

##### 2.3.3. 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="4">网上报账</td><td style='text-align: center; word-wrap: break-word;'>填写单据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务领导审批</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>扫描影像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计初审</td></tr></table>

##### 2.3.4. 产品解决方案

参考应付单工作流。

#### 2.4. 现金管理

##### 2.4.1. 业务描述

设立共享服务中心后，仍然保留各单位的银行账户，可逐步取消各单位的出纳岗，将结算事务集中到共享服务中心予以办理。

网上报账业务经共享服务中心审核通过后，提交到共享服务中心资金处处理，由共享服务中心办理结算。

##### 2.4.2. 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_139_248_1050_680.jpg" alt="Image" width="76%" /></div>


##### 2.4.3. 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>付款结算管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>收款结算管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>结算（包含签字、网上支付、手工结算）</td></tr></table>

##### 2.4.4. 产品解决方案

## 1、 报账业务签字

路径：【现金管理】-【结算】--【签字】

功能说明：资金主管签字确认支付。

纸业集团各公司的网上报账业务经共享服务中心审核通过后，提交资金结算处理，各报账单位的报账业务，可以由共享服务中心资金经理集中进行签字处理。

支持业务录入环节不指定支付银行账号，在签字前指定支付银行账号的应用模式，也支持业务录入环节明确支付账号，签字环节主要是复核确认的应用模式。

具体操作如下图:

确定结算方式、支付账号

<div style="text-align: center;"><img src="imgs/img_in_image_box_141_179_1055_451.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2.4.4-1 结算</div>


共享服务中心资金经理确认允许支付，签字。

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_596_1032_851.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.4.4-2 签字</div>


## 2、 报账业务结算

路径：【现金管理】-【结算】-【结算】

功能说明：出纳执行结算，支持的结算方式有网上支付、非网上支付。

纸业集团各公司的网上报账业务经签字完成后，就可以进行支付了，可以由各报账单位财务人员分别支付，也可以由共享服务中心设立出纳岗，集中处理支付业务。

具体操作如下图:

<div style="text-align: center;"><img src="imgs/img_in_image_box_202_1200_1069_1458.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.4.4-3 合并支付</div>

其中：通过网上支付的，需要提供网银支付信息

<div style="text-align: center;"><img src="imgs/img_in_image_box_204_197_1074_550.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.4.4-4 网银补录信息</div>


#### 2.5. 营销费用管理

##### 2.5.1. 业务描述

支持销售业务员先填写客户费用申请单，然后进行费用核报的业务。

支持销售业务员填写助促销品申请单，然后库房根据助促销品申请出库的业务。

##### 2.5.2. 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_222_265_963_1169.jpg" alt="Image" width="62%" /></div>


灰色表示本模块内功能或处理

白色表示其它模块功能或处理

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_172_963_1227.jpg" alt="Image" width="62%" /></div>


##### 2.5.3. 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">协同应用</td><td rowspan="2">网上报账</td><td style='text-align: center; word-wrap: break-word;'>客户费用申请单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>助促销品申请单</td></tr></table>

##### 2.5.4. 产品解决方案

### 1. 业务员填写客户费用申请单、助促销品申请单

在网上报账的【报账人门户】下填写客户费用申请、助促销品申请单据。

单据中有保存、联查等功能可使用，说明如下。

提交与保存：提交表示提交到审批流的下一个环节；保存仅仅暂存已经填写的内容单据，保存时候不做规则校验。

收回：提交单据之后，下一个审批人审批之前可以收回单据。

附件管理：上传查看附件。

➢ 联查：联查单据的审批情况信息。

### 2. 经理审批客户费用申请单、助促销品申请单

登陆共享服务平台，在【审批人门户】中找到需要审批的费用申请单据进行审批。

### 3. 业务员填写客户费用单

在网上报账的【报账人门户】下填写客户费用单。

单据中有保存、联查等功能可使用，说明如下。

提交与保存：提交表示提交到审批流的下一个环节；保存仅仅暂存已经填写的内容单据，保存时候不做规则校验。

收回：提交单据之后，下一个审批人审批之前可以收回单据。

附件管理：上传查看附件。

➢ 联查：联查单据的审批情况信息。

### 4. 经理审批客户费用单

登陆共享服务平台，在【审批人门户】中找到需要审批的费用单据进行审批。

### 5. 库管人员填写助促销品出库单

登陆 NC 系统，在【库管管理】-【助促销品出库单】，找到需要出库的助促销品申请单，完成出库操作。

## 第三章 初始准备

<div style="text-align: center;"><img src="imgs/img_in_image_box_118_291_1078_1020.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3-01 初始准备主要设置</div>


#### 3.1. 门户创建

系统管理员登陆后在系统管理的【客户化配置】--【门户配置】--【布局管理】节点中创建门户的数据。现在系统中预置了首页等门户数据，预置数据都是全局级的。客户可以根据实际情况创建。选中需要修改的页签数据，点击高级设置，可以维护是否启用和是否显示的属性。

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_190_1074_670.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3.1-1 门户创建</div>


#### 3.2. 发布交易类型成为节点

当预置的网上报销的交易类型不能满足客户要求时，可以创建新的交易类型并发布的协同的网上报销模块中；

进入【系统管理】→【客户化配置】→【门户配置】→【节点注册】菜单将在 NC 重量级客户端中定义好的交易类型发布到协同系统中。

在注册节点中选中左树上的协同报销/网上报销相关节点下对应类型，点击新增打开新增卡片。

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_165_936_713.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 3.2-1 发布交易类型成为节点</div>


## 注意：

新生成的节点必须要在权限管理中分配职责权限，新节点才能被用户看到；

#### 3.3. 定义单据模板

当新发布节点后或者当前节点预置的交易类型不满足客户需求时，支持维护个性化的单据模板。

1）进入【系统管理】→【客户化配置】→【模板管理】→【表单配置】菜单，在节点的左树上选中协同报销下需要定义单据，右列表中展示出单据的数据。选中需要配置单据模板的单据，点新增按钮出现新增卡片界面，维护新增卡片界面。

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_183_1091_666.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 3.3-1 定义单据模板</div>


2）选中需要修改的模板点击【设计】按钮，选择需要个性化的区域“单据主界面”，进入模板设置界面修改模板。注：对于新发布的节点，创建新模板后系统自创建默认模板。

<div style="text-align: center;"><img src="imgs/img_in_image_box_182_850_1048_1246.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.3-2 模板设置界面</div>


3）在模板中增加新字段，例如在图中的基本信息区域中增加业务字段。

a) 鼠标在基本信息区域内点击右键出现编辑框，编辑框中出现“删除”、“编辑”、“增加项”

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_172_1048_570.jpg" alt="Image" width="72%" /></div>


main_um > flowlayout0320 > panelv10321 > baseinfo > panelpanel3806 > flowlayout001 > panelh0001 > jkzb_base_info_form

<div style="text-align: center;">图 3.3-3 模板设置编辑框</div>


b) 选中修“编辑”属性框。从数据集中找到需要显示的项，选中到左边的列表中，改为可见项，并且上下调整字段的显示顺序。

<div style="text-align: center;"><img src="imgs/img_in_image_box_269_768_952_1216.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">图 3.3-4 模板编辑</div>


4）在模板中增加一个自定义字段，例如在图中的基本信息中增加一个自定义的字段项。

a) 鼠标在基本信息区域内点击右键出现编辑框，编辑框中出现“删除”、“编辑”、“增加项”

b) 选中“增加项”出现新增卡片界面，维护自定义字段的编码和名称

c) 再右键选“修改”出现基本信息的编辑属性框。在数据集中找到上面步骤新增的项，选中到

左面列表中，改为显示项并调整到合适的位置上。

d) 模板设置界面中选中新增加的项，修改属性中的“编辑类型”属性可调整新增字段的类型。常用的类型有：

字符：选中后本字段在单据为字符型

日期：选中后本字段为日期型

参照：选中后需要在属性中再设置“引用参照”，则本字段在表单中可参照出引用参照的内容

<div style="text-align: center;"><img src="imgs/img_in_image_box_456_506_776_865.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">图 3.3-5 新增字段属性</div>


5） 在模板甲修改一个已有的字段，例如在图中修改“事由”的字段。选中事由字段，修改右下角的字段属性。

<div style="text-align: center;">文件(F) 编辑(E) 查看(V) 收藏克(A) 工具(T) 帮助(H)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_182_1052_1041_1458.jpg" alt="Image" width="72%" /></div>

<div style="text-align: center;">图 3.3-6 修改字段属性</div>


#### 3.4. 新建打印模板

V6.5 网报不需要在 portal 配置打印模板，而是直接调用 NC 端费用管理的模板，以 PDF 格式显示打印。

1）在【交易类型管理】节点自定义一个交易类型：借款申请。将自定义的交易类型“借款申请”进行发布。

<div style="text-align: center;"><img src="imgs/img_in_image_box_186_481_1058_1090.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 3.4-1 借款申请单</div>


2）在【模板设置】--【单据录入】--【借款申请】节点选中根节点，【2611card 费用申请单卡片默认打印模板】复制一个【借款申请打印模板】。点击修改进行模板设置。

<div style="text-align: center;"><img src="imgs/img_in_image_box_188_1213_1011_1586.jpg" alt="Image" width="69%" /></div>

<div style="text-align: center;">图 3.4-2 复制打印模板</div>


3）管理节点分配打印模板，也可以直接到单据管理节点复制根节点模板，分配给相应节点和人员。

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_268_1050_1334.jpg" alt="Image" width="73%" /></div>


## 4 ) 网报端打印。

<div style="text-align: center;">图 3.4-4 打印输出</div>

#### 3.5. 组织建模

参见共享服务手册。

#### 3.6. 作业处理平台

参见共享服务手册。

## 第四章 操作指南

本手册具体详细操作应用，请登录 NC 系统参见相关产品帮助，或登录在线帮助网站。

## 附录

## 附录 1：本文参见其他手册清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>手册名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>《NC 产品手册-企业建模平台》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>《NC 产品手册-共享服务》</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_491_401_698_555.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform

用友网络科技股份有限公司
