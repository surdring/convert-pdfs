# NCV6.5产品手册-应收管理

产品手册- V6.5

应收管理

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权 ..... 2  
名词解释 ..... 5  
第一章 概述 ..... 6  
1.1 产品概述 ..... 6  
1.2 产品价值 ..... 7  
第二章 应用场景 ..... 9  
2.1 日常业务 ..... 9  
2.1.1 应收立账 ..... 9  
2.1.2 收款业务 ..... 17  
2.1.3 应收核销 ..... 21  
2.1.4 内部往来协同 ..... 31  
2.1.5 并账 ..... 33  
2.2 坏账管理 ..... 36  
2.2.1 业务描述 ..... 36  
2.2.2 业务流程 ..... 37  
2.2.3 功能清单 ..... 37  
2.2.4 产品解决方案 ..... 37  
2.3 汇兑损益 ..... 39  
2.3.1 业务描述 ..... 39  
2.3.2 业务流程 ..... 39  
2.3.3 功能清单 ..... 39  
2.3.4 产品解决方案 ..... 39  
2.4 关账与结账 ..... 44  
2.4.1 业务描述 ..... 44  
2.4.2 业务流程 ..... 45  
2.4.3 功能清单 ..... 45  
2.4.4 产品解决方案 ..... 45  
第三章 初始准备 ..... 47  
3.1 管控模式 ..... 48  
3.2 企业建模平台 ..... 49  
3.2.1 多组织管理 ..... 50  
3.2.2 基础数据维护 ..... 52  
3.2.3 流程平台搭建 ..... 54  
3.2.4 会计平台设置 ..... 55  
3.3 领域级础设置 ..... 57  
3.3.1 基础设置 ..... 57  
3.3.2 应收管理 ..... 58  
第四章 操作指南 ..... 58  
附录 ..... 59  
附录 1：单据流转 ..... 59

附录 2：控制点 ..... 61  
附录 3：本文参见其他手册清单 ..... 66

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供客户业务需求如何与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关应收管理的主要业务场景、流程、以及对应的产品功能的介绍；第三部分介绍了产品启用前的初始准备设置；第四部分列举出关于产品的功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录进行了汇总，列示为单据流转、控制点、与查询报表，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《组织管理手册》----深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助----针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3.《流程管理手册》----提供关于交易类型、流程设计工具的应用指导。

4.《基础数据手册》----可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

## 名词解释

## 债权转移

债权转移指用户进行的应收、收款、应付、付款业务合并或调整的工作。

## 坏账收回

坏账收回指应收款原已确定为坏账，后又被收回的业务。

## 第一章 概述

### 1.1 产品概述

应收管理帮助企业处理所有债权业务及相关管理工作，包括：企业与客户、部门和业务员所形成的应收款、收款业务的管理，为企业提供各种往来款项的处理（转移并账、坏账、核销等）及相关查询、统计功能。通过对应收款项全方位的管理，实现应收业务与销售业务的紧密连接，加强企业对资金流入流出的核算与管理。

产品功能架构及产品业务处理流程分别如图 1.1-1、1.1-2 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_652_1074_1229.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 1.1-1 财务产品功能架构图</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_111_153_1073_1088.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 1.1-2 应收管理业务流程图</div>


### 1.2 产品价值

1. 灵活的收款协议管理：支持分多期收款、固定结算日、账期延期天数管理；预收款可灵活配置是否按收款协议的预收标志核销。

### 2. 应收账款确认环节可灵活配置：

1）出库确认应收账款；

2）出库暂估应收——开发票确认应收；

3）开发票确认应收。

3. 支持跨组织应收管理：出库组织与开票组织不同时，产品可同时记录双方信息，并自动生成双方会计凭证。

4. 支持预收款管理：基于订单预收部分款项，开发票后自动核销。

5. 收款管理：支持本组织收款流程、委托集团资金结算中心收款流程。

6. 内部托收承付：支持委托集团资金结算中心对集团内单位收款流程，自动完成收款方——中心——付款方三方业务协同。

### 7. 多种内部交易处理方式：

1）通过单据协同，自动处理内部往来业务。相关业务单据生成总账凭证后，其内部交易关联关系自动传递到总账，并在总账自动进行内部交易对账处理；

2）供应链内部交易业务生成双方单位的应收应付单据，并将内部交易业务关联关系传递到应收应付，应收应付单据生成双方单位总账凭证时，自动将内部交易业务关系传递到总账，并进行内部交易对账处理。

8. 应收核销：支持自动、手动核销；支持同币种、异币种自动核销；支持录入业务单据过程中即时核销；支持应收冲应付核销；

### 9. 支持债权转移。

### 10. 多种坏账计提方法：

1）支持按应收余额百分比法、销售百分比法、账龄分析法计提坏账准备；

2）支持不同客户按不同计提方法计提坏账准备；影响因素可自由定义。

### 11. 支持应收款到期自动预警。

12. 与票据管理紧密集成，自动进行应收票据处理。

### 13. 多种汇兑损益计算方法：

1) 月末计算汇兑损益；

2）外币余额结清时计算汇兑损益；

3）计算已实现汇兑损益未实现汇兑损益。

4）汇兑损益计算纬度既可按单据，又可按客户执行。

### 14. 支持欧盟成员国的应收单确定税额时，增值税合并计税方式。

## 第二章 应用场景

### 2.1 日常业务

#### 2.1.1 应收立账

##### 2.1.1.1 业务描述

1. 单组织应用：

1) 销售模块的销售出库单或者销售发票进行应收结算，确认后生成应收模块的应收单；

2) 销售管理模块的代垫运费发票形成应收单；

3) 销售出库确认销售收入：

a) 销售出库单暂估，生成未确认应收单；

b) 单到补差模式下销售出库单与销售发票确认后，原未确认应收单形成应收单，与发票的差额形成应收模块的新应收单；

c) 单到回冲模式下原未确认应收单回冲，形成红字应收单，同时按销售发票金额形成新的应收单；

4) 销售费用单直接形成红字应收单；

5) 资产维修维护：应收租金计算单/保险索赔单/资产处置单等资产类单据生成应收单；

6) 由项目销售合同的收款计划生成应收单；

7) 应收模块直接立账时，可根据收款单直接生成应收单，完成收款结算；或直接填录应收单后供收款单用于选择收款。

8) 由销售合同的收款协议生成应收单的行。

9) 由进出口待垫费用发票推式生成应收单。

10）由代理进出口服务发票推式生成应收单。

2. 跨组织应用：

1) 跨组织报销时，报销单据审批生效后，形成报销单位对费用承担单位的应收单；

2) 跨组织销售时，与客户结算时根据销售发票形成对外结算组织的应收单，内部交易结算时根

据内部结算清单形成内部交易双方的应收单和应付单。

##### 2.1.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_316_1032_1527.jpg" alt="Image" width="70%" /></div>

<div style="text-align: center;">图 2.1.1-1 应收立账业务流程</div>


##### 2.1.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="8">供应链</td><td rowspan="4">销售管理</td><td style='text-align: center; word-wrap: break-word;'>销售发票维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>暂估应收处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>销售出库结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>代垫运费发票</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内部交易</td><td style='text-align: center; word-wrap: break-word;'>内部结算清单维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>库存管理</td><td style='text-align: center; word-wrap: break-word;'>销售出库</td></tr><tr><td rowspan="2">运输管理</td><td style='text-align: center; word-wrap: break-word;'>应收运费发票</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>代垫运费发票</td></tr><tr><td rowspan="6">资产管理</td><td rowspan="3">资产租赁管理</td><td style='text-align: center; word-wrap: break-word;'>应收租金计算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对内租出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对外租出</td></tr><tr><td rowspan="2">资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>保险索赔</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产处置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>维修管理</td><td style='text-align: center; word-wrap: break-word;'>工单</td></tr><tr><td rowspan="5">财务会计</td><td rowspan="3">应收管理</td><td style='text-align: center; word-wrap: break-word;'>应收单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未确认应收单管理</td></tr><tr><td rowspan="2">收款管理</td><td style='text-align: center; word-wrap: break-word;'>收款单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单管理</td></tr></table>

##### 2.1.1.4 产品解决方案

1. 由其他业务单据形成应收：

1) 根据业务流定义中对不同业务流程中各单据类型的动作驱动设置（如图 2.1.1-2 所示），各类单据在点击【提交】钮经审批通过或点击【审批】钮确认后生成应收单（对应单据设置了审批流走“提交”，未设审批流走“审批”），包括：

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_156_1061_757.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.1-2 推式生成应收单的单据动作配置示例</div>


a) 代垫运费：【销售管理】→【销售结算】→【代垫运费发票】中的代垫运费发票，确认后形成应收单及对承付商的应付单；

b) 出库结算模式下，【库存管理】→【出库业务】→【销售出库】的销售出库单，确认后生成应收单；

c) 发票结算模式下，【销售管理】→【销售发票】→【销售发票维护】的销售发票，确认后生成应收单；

d) 单到补差模式下，【库存管理】→【出库业务】→【销售出库】的销售出库单，签字后生成应收单；【销售管理】→【销售发票】→【销售发票维护】的销售发票经确认、单据审核后，将价格差异形成补差的应收单；

e) 单到回冲模式下，【库存管理】→【出库业务】→【销售出库】的销售出库单，签字后形成未确认应收单（即暂估应收）；待【销售管理】→【销售发票】→【销售发票维护】的销售发票进行价格确认、单据审核后，系统自动执行单到回冲处理，形成红字未确认应收单和应收单；

f) 当销售费用单在【交易类型】将支付方式设为“生成红字应收”时（如图 2.1.1-3 所示），

【销售管理】→【销售发票】→【销售费用单维护】的销售费用单经审批确认后，生成

<div style="text-align: center;"><img src="imgs/img_in_image_box_157_209_1034_679.jpg" alt="Image" width="73%" /></div>


#### 图 2.1.1-3 销售费用单的交易类型支付方式设置界面示例

g) 【库存管理】→【供应商寄存管理】→【签收途损单】签字后推式生成应收单；

h) 【资产管理】→【资产租赁管理】→【租出管理】→【应收租金计算】节点的应收租金计算单根据预设置流程可推式生成应收单；

i) 【资产管理】→【资产使用管理】→【保险管理】→【保险索赔】节点的保险索赔单据预设置流程可推式生成应收单；

j) 【资产管理】→【维修管理】→【工单】节点的维修工单通过“关联功能-生成应收应付单”（接口方式）生成集团内部关联单位的内部应收/应付单。

k) 【项目管理】→【项目合同管理】→【项目销售合同】→【收款计划】节点的收款计划生效后，根据接口对照关系，生成保存态的应收单：

● 组织本币汇率、组织本币金额、集团本币汇率、集团本币金额、全局本币汇率、全局本币金额由上游的收款计划携带；应付财务组织和结算财务组织若相同则携带且不能修改，不同则财务自动获取；

该类单据不能手动删除、删行；若无后续操作，可由上游单据通过“取消生成应收单”操作，自动删除已生成的应收单；

● 实际收款时且应收单已经核销(全部或部分核销)，核销后将本次核销金额回写上游“收款计划”中的“实际收款金额”；

该类单据反核销时，会将反核销的金额回传上游收款计划，回写“收款计划”的“实际

收款金额”。

● 销售出库单生成暂估应收单，销售出库单、途损单、销售发票等生成应收单时，默认携带批次号，若是应收单复制时则清空批次号；单据红冲时保留批次号。

1) 【供应链】→【合同管理】→【销售合同】→【销售合同维护】节点的合同收款协议维护生效后：

● 来源于合同的销售发票生成应收单时，应收单的收款协议按照销售合同的收款协议生成，应收单不再根据收款协议拆分；

● 销售发票生成的应收单与收款单核销时，需按应收单的协议行回写销售合同的收款协议行的实际收款金额。

### 2. 应收管理自主生成：

1) 【应收管理】→【应收日常业务】→【应收单录入】节点,手工录入应收单或参照收款单生成应收单:

2）收款结算模式：新增时选“主收款单”，在弹出的参照窗中选择收款单确定后即可形成新增应收。该方式为系统预定义的收款结算流程，用户可在【企业建模平台】→【流程管理】→【业务流】节点中选择“AR02收款结算”修改。操作过程如图2.1.1-4所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_165_971_517.jpg" alt="Image" width="70%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">主收款单 生成 应收单</td></tr></table>

已选：1 张单据，共 1 行


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td colspan="2">应收单录入</td></tr></table>

#### 图 2.1.1-4 选择收款单新增应收单（收款结算流程）操作示例

3) 选择收款模式：新增时选“自制”，此时流程起点为应收单，录入各项必输信息后保存即可，此后收款单生成时可选择应收单，此为产品预定义的收款结算流程，用户可在【企业建模平台】→【流程管理】→【业务流】节点中选择“AR01 选择收款”查看并修改。

### 3. 跨组织应收单的形成：

1）跨组织报销时，各类费用报销单若报销单位和费用承担单位不同，则费用类报销单在审批后生成报销组织（跨组报销的处理参见报销管理手册），如图图2.1.1-5所示：

生成A、B两组织凭证：B组织凭证（借：应收-X客户贷：内部往来-A）、A组织（借：内部往来-B贷：收入）。

### 4. 应收立账：

1）在【应收管理】→【应收日常业务】→【应收单管理】节点，查询到已保存的应收单，点击【审批】生效，此时系统根据会计平台中应收单预置的转换模板生成凭证，至此应收立账完成。

## 注意：

应收立账必须在会计平台针对 D0 应收单提前完成凭证转换的相关设置，包括入账规则设置、分类定义、转换模板各项设置（相关操作详见《会计平台》手册），否则应收单不能通过审核确认，无法完成立账。

### 5. 单据录入与单据管理的差别：

1）从功能上看：单据录入节点执行基本的增、删、改操作；单据管理节点除新增外，可以执行审核、制单、即时核销、挂起、红冲等操作；

2) 从应用上看，应收单录入与应收单管理的操作用户不同。

6. 应收单支持影像查看功能，可以支持应收单的扫描件的上传和查询。

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_1264_1050_1421.jpg" alt="Image" width="72%" /></div>


7. 进出口待垫费用发票推式生成应收单。在【进出口】→【贸易费用】→【待垫费用发票】节点，由待垫费用发票推式生成应收单。

8. 代理进口服务发票推式生成应收单。在在【进出口】→【代理进口】→【代理发票】→【代理发票维护】节点，由代理发票推式生成应收单。

9. 代理出口服务发票推式生成应收单。在在【进出口】→【代理出口】→【发票管理】→【代理发票】节点，由代理发票推式生成应收单。

#### 2.1.2 收款业务

##### 2.1.2.1 业务描述

1. 订单/合同生成预收：销售订单/销售合同形成预收——销售发票立应收——自动核销。

2. 单组织选择收款：应收单生效——选择应收单生成收款单——自动核销——生成凭证，支持不同流程的应收单合并收款。

3. 委托资金组织收款：收款单——委托收款书——到账通知。

4. 资金集中结算时，根据资金组织的结算信息直接生成收款单据：委托收款单转账成功/内转单转账成功——生成成员单位的结算信息——成员单位通过“关联结算信息”生成收款单据。

5. 欧盟电子支付时，支持直接借记和直接借记退回业务（参见《NCV6.5 产品手册-欧盟电子支付》）。

6. 支持按应收跨组织代收款业务，按应收单维护的权限范围，可跨组织拉单形成收款单，收款单位和应收单位间形成内部往来。

7. 收款单需支持手续费，共享服务模式下可跨组织代收款。

8. 收款单生成凭证后，可对一些科目、部门等项作调整。

9. 提供内置的收款金额取数函数，支持根据收款金额计算返利。

10. 由应收票据生成收款单，并将票据信息自动带到收款单：资金管理-商业汇票-应收票据-收票登记。

11\. 由客户允许报销的营销费用，例如，如价保费用、返利费用、入场费、装修补贴、保证金利息……生成收款单：客户费用单——收款单。

12\. 由进出口合同推式生成收款单。

##### 2.1.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_228_155_992_857.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 2.1.2-1 收款业务流程</div>


##### 2.1.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="4">购销存</td><td rowspan="3">销售管理</td><td style='text-align: center; word-wrap: break-word;'>销售订单-销售订单维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>销售订单-销售收款核销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户费用单-收款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合同管理</td><td style='text-align: center; word-wrap: break-word;'>销售合同-销售合同维护</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">应收管理</td><td style='text-align: center; word-wrap: break-word;'>收款单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单管理</td></tr><tr><td rowspan="4">资金管理</td><td rowspan="2">现金管理</td><td style='text-align: center; word-wrap: break-word;'>划账业务-结账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>划账业务-到账通知</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金结算</td><td style='text-align: center; word-wrap: break-word;'>委托收款</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商业汇票</td><td style='text-align: center; word-wrap: break-word;'>收票登记</td></tr></table>

##### 2.1.2.4 产品解决方案

### 1. 订单/合同收生成：

1) 【销售管理】→【销售订单】→【销售订单维护】节点，按销售订单保存时录入表头的收款金额，或点击“订单收款/收款核销”均可生成收款单，保存状态的销售订单可删除，销售订单删除后收款单仍存在，需手工删除或等待后续冲销；

2) 【合同管理】→【销售合同】→【销售合同维护】节点，按合同销售时，可由已生效的销售合同点击“收款”钮，推式生成收款单；已生成收款单后的销售合同不能回退(取消生效和取消审批)；

3）销售发票推式生成的应收单优先与来自销售订单的收款单核销，核销干净后再与来自销售合同的收款单核销。

### 2. 应收管理自主生成：

【应收管理】→【收款日常业务】→【收款单录入】节点,手工录入收款单或参照应收单生成收款单，支持不同流程的应收单合并生成收款单：

1) 选择收款模式: 新增时选“主应收单”, 在弹出的参照窗中选择应收单确定后即可形成新增收款; 选择收款模式: :新增时选“主应收单”, 在弹出的参照窗中选择应收单, 编辑并确定后即可形成新增收款, 编辑中支持修改收款单的主组织（跨组织拉单实现跨组织代收业务）:

a) 跨组织拉单后，单据的主组织允许修改----修改后，单据日期、起算日期、往来对象、客户、应收类型、业务流程、币种、单据金额保留，不能被清空。其他字段依主组织的变化而变化；

b) 跨组织拉单的范围根据人员的功能权限确定，有哪个组织应收单维护的权限，才可以参照哪个组织的应收单生成收款单拉单；

c) 支持异币种跨组织拉单，并自动核销。

d) 代收业务仅支持拉单自动核销，不支持手工核销、即时核销、自动核销。

e) 跨组织拉单若涉及使用组织级参数时，需要使用下游单据组织的参数。

f) 发生代收业务时，代收款项不影响客户信用的虚增。

1）收款结算模式：新增时选“自制”，录入各项必输信息后保存即可，此时应收单生成时可选择收款单。

### 3. 委托资金组织收款：

1) 【应收管理】→【收款日常业务】→【收款单录入】节点形成收款单；

2) 【应收管理】→【收款日常业务】→【收款单管理】节点对收款单审批生效；

3) 【资金管理】→【现金管理】→【划账业务】→【结算】节点，查询到收款单后点击“提交资金组织”，形成委托收款书。

4. 资金集中结算时依据资金组织结算信息，直接生成收付单据：

1) 【资金管理】→【资金结算】→【委托收款】节点中的委托收款单转账成功可生成成员单位的结算信息；

2）该委托收款单中收款方成员单位在【应收管理】→【收款日常业务】→【收款单录入】/【收款单管理】节点中，可通过点击“辅助功能-关联结算信息”按钮，在弹出的独立结算信息查询界面中查询出并选择一条独立结算信息，确定后由系统自动关联，之后保存，即生成收款成员单位的收款单据；

3）由结算信息关联生成的业务单据审批、签字后，单据流程即结束，不再执行结算、支付操作；

4）关联结算信息生成的收款单删除时只删除业务单据，不删除原结算信息，原结算信息返回为独立结算信息状态；

5）若为承付模式则必须收款单先逆向操作后，内转单才能取消转账、反审批，之后付款单才能逆向操作。

5. 收款单业务信息页签的表头表体上提供“现金账户”字段，可参照当前组织可见的现金账户，并支持同步到结算信息中，由上游业务推生收款单时由上游业务携带，会计平台增加的现金账户则由现金管理来处理。但要注意收款单表体中“现金账户”与“银行账户”互斥，即同一行中录入了现金账户则不能再录入银行账户。

6. 收款单据表体行提供字段“是否抵扣金额”，用于判断是冲抵行还是结算行，勾选表示为冲抵行；冲抵行数据不传结算，结算行参与结算。结算行和冲抵行都参与单据的核销。

7. 收款单根据组织级参数 “AR36 贷方引用信息指定字段” 的设置取值，可选择 “单据号、合同号、订单号、发票号、出库单号、摘要、自定义项 1~30” 等字段，一旦设定（应先修改默认单据模板为显示），则结算方式为直接借记时，贷方引用信息标准及贷方引用信息指定字段必输，做直接借记退回业务时，付款单的贷方引用信息字段由收款单信息携带。

### 8. 收款立账：

在【应收管理】→【收款日常业务】→【收款单管理】节点，查询到已保存的收款单，点击【审批】生效，此时系统根据会计平台中收款单预置的转换模板生成凭证。

9. 收录登记生成收款单，【资金管理】→【商业汇票】→【应收票据】→【收票登记】：

1）收票登记提交、审批后，点击关联功能“收款单”按钮，弹出收款单录入界面，并将票据信

息自动携带到收款单，完成收款单后保存；

2) 删除收款单时自动释放收票登记与收款单的关联关系；

3) 修改收款单中票据编号保存后，与原收票登记关联关系解除，与新的票据建立关联关系。

10. 客户费用单生成收款单，【供应链】→【销售管理】→【销售发票】→【客户费用单】：

1）交易类型管理，供应链基础设置，客户费用单配置勾选“审核自动生成收款单”，则客户费用单审批时自动推式生成保存态的收款单，生成的收款单采用后台生成，不弹出收款单的维护界面。

11\. 收款单支持影像查看功能，支持收款单扫描件的上传和查看。

#### 2.1.3 应收核销

##### 2.1.3.1 业务描述

核销是日常进行的收款核销应收款的工作，用于建立应收单、收款单、应付单、付款单间的核销记录，通常核指的是“审核、核实”，销指的是“注销、销账”。核销信息是准确反映各账龄段债权债务的依据。

1. 应收核销业务通常包括：

1) 赊销：应收与收款核销

3) 抵账：应收与应付核销、收款与付款核销

2) 预售：预收与应收核销

4) 红蓝对冲：相同借/贷方向单据抵销

5) 同/异币种核销：相同/不同币种单据间的核销

2. 核销的处理模式分为：

1）手动核销：由用户按单据或者按单据表体行指定借贷方的核销单据，手动核销支持同币种（带折扣）核销、异币种核销、红蓝对冲、赊销、抵账、预售。

2）自动核销；根据设置的相关条件由系统自动完成核销；或预置核销方案，设定后台核销任务后，由系统自动定时核销。自动核销支持同币种核销、异币种核销、赊销业务。

3) 即时核销：录入业务单据过程中即时核销，核销支持分配，补差。

##### 2.1.3.2 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="5">财务会计</td><td rowspan="5">应收管理</td><td style='text-align: center; word-wrap: break-word;'>应收日常业务-应收单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>日常日常业务-收款单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核销处理-核销方案设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核销处理-自动核销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核销处理-手动核销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>系统平台</td><td style='text-align: center; word-wrap: break-word;'>后台任务中心-后台任务部署</td></tr></table>

##### 2.1.3.3 产品解决方案

### 1. 手动核销：

手工核销按财务组织执行，提供包括核销、模拟核销、核销记录查询和反核销等功能。

1）在【财务会计】→【应收管理】→【核销处理】→【手动核销】节点，先过滤出待核销处理的单据：点击【查询】钮，分别在“查询条件”、“常用条件”、“核销规则”等页签中设置相关查询条件后确定，如图2.1.3-1所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>姓名/部门</td><td style='text-align: center; word-wrap: break-word;'>111</td><td style='text-align: center; word-wrap: break-word;'>查询条件</td><td style='text-align: center; word-wrap: break-word;'>发现条件</td><td style='text-align: center; word-wrap: break-word;'>×</td><td style='text-align: center; word-wrap: break-word;'>查询规则</td><td style='text-align: center; word-wrap: break-word;'>满足值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1. 输入过去关键字</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>* 普通</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑ 规则</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2. 收录任务数</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>主键ID</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>* 索引范围工</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3. 宽域ID</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单级类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4. 单级类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>交易类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>包含</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5. 交易类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单级大类</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>* 1条，你家单条，订单条，您自投的</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6. 仅用规则日</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>借用规则日</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>介于</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>F</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7. 类别编号</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单级编号</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>包含</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>F</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8. 类别口味</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单级日期</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>介于</td><td style='text-align: center; word-wrap: break-word;'>* 2011-01-01</td><td style='text-align: center; word-wrap: break-word;'>F</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9. 单级详情</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单级环境系统</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10. 单级未报表</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单级未报表</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11. 录入人</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>录入人</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12. 审核人</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>审核人</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>等于</td><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13. 客户</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14. 保存方案</td><td style='text-align: center; word-wrap: break-word;'>3000万元</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>取消(☐)</td></tr></table>

保存方案 显地方


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>标准名称</td><td style='text-align: center; word-wrap: break-word;'>标准条件</td><td style='text-align: center; word-wrap: break-word;'>实际条件</td><td style='text-align: center; word-wrap: break-word;'>标准规则</td><td style='text-align: center; word-wrap: break-word;'>满足值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>输入信号或数字信号</td><td style='text-align: center; word-wrap: break-word;'>输出编码</td><td style='text-align: center; word-wrap: break-word;'>实际输出厂厂</td><td style='text-align: center; word-wrap: break-word;'>Q</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>软件参数</td><td style='text-align: center; word-wrap: break-word;'>本方</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 主输出</td><td style='text-align: center; word-wrap: break-word;'>本方对各参数</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 类型类型</td><td style='text-align: center; word-wrap: break-word;'>本方对各类型</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 交易类型</td><td style='text-align: center; word-wrap: break-word;'>本方交易类型</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 交易类型</td><td style='text-align: center; word-wrap: break-word;'>本方交易类型</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 通用控制日</td><td style='text-align: center; word-wrap: break-word;'>本方交易日期</td><td style='text-align: center; word-wrap: break-word;'>2011-01-01</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2011-01-01</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 参数编号</td><td style='text-align: center; word-wrap: break-word;'>本方交易日期</td><td style='text-align: center; word-wrap: break-word;'>2011-01-01</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2011-01-01</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 单板日期</td><td style='text-align: center; word-wrap: break-word;'>公共条件</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 单板所属区</td><td style='text-align: center; word-wrap: break-word;'>部门</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 单板来源区</td><td style='text-align: center; word-wrap: break-word;'>地区分类</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 录入人</td><td style='text-align: center; word-wrap: break-word;'>表头科目</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>表头科目</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 审核人</td><td style='text-align: center; word-wrap: break-word;'>收支项目</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>结算结算组织</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>- 客户</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保存方案</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>确定行</td><td style='text-align: center; word-wrap: break-word;'>取表行</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1163_504_1494.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_574_1174_1030_1510.jpg" alt="Image" width="38%" /></div>

<div style="text-align: center;">图 2.1.3-1 手动核销查询操作界面</div>


2）查询出待核销单据后，可手工在本方（应收单）和对方（收款单）之间勾选单据；或在本方/贷方的一方勾选后，点击【按借方匹配】/【按贷方匹配】钮，再点击【核销】即完成手工核销（如图2.1.3-2所示）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_325_1045_754.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.1.3-2 手动核销操作界面</div>


3）手动核销前可先做模拟核销，点击【模拟核销】钮，可查看核销明细情况，此时再点击【核销】可完成手动核销，或点击【查询】钮放弃当前模拟核销（如图2.1.3-3所示）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_896_1039_1103.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 2.1.3-3 手动模拟核销操作界面</div>


4）已核销处理过的单据，无论是应收单还是收款单，单据上表体的“原币余额”及“组织本币余额”

减除掉已核销的金额，直至为 0 后，不再参与核销，如图 2.1.3-4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_179_151_1012_517.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 2.1.3-4 已核销应收单界面示意</div>


5）已核销过的应收/收款单，可通过点击【核销查询】钮，输入相应查询条件后，系统提供查询出的已核销明细记录（如图2.1.3-3），此时【反核销】加亮，点击该按钮可执行反核销。

6) 根据查询条件设置的不同，手工核销可选择按异币种核销或按同币种核销、红监对冲、预售、抵账等业务模式，例如：要执行应收冲应付的抵账模式，在查询时应在“查询条件”页签将“应收单、应付单”选入单据大类，并在“常用条件”页签指定对方核销对象为“应付单”，如图 2.1.3-5 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_194_189_999_631.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_198_729_1088_939.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.1.3-5 应收冲应付查询设置界面示意</div>


7) 核销时按参数“AR2 核销方式（按单据核销、按表体核销）的约束，若设为“按单据核销核销”，则在核销或债权转移等处理时，系统将符合条件的数据按一张单据一条记录列示待处理；若设为“按表体核销”，则系统将符合条件的数据按一条单据表体行一条记录列示。

8) 明细反核销：对核销结果的部分明细进行反核销，生成红字凭证。

9) 同币种核销分配算法（以“按借方数据分配”为例）：

a) 将贷方第一条记录的选中标志选中；

b) 将借方的“本次结算”合计数与贷方已选的第一条记录的原币余额比较大小：若借方的“本次结算”合计数<贷方第一条记录的原币余额，则自动将此记录的本次结算赋值为等于借方的“本次结算”合计数；若借方的“本次结算”合计数>贷方第一条记录的原币余额，则自动为将记录的本次结算赋值为等于当前记录的原币余额；

c) 然后继续选中下一条记录，用借方分配剩余的金额进行以下的分配；

d）将（借方的“本次结算”合计数-已分配金额）与贷方选中记录的原币余额比较大小：若（借方的“本次结算”合计数-已分配金额）<贷方选中记录的原币余额，则自动为此记录的本次结算赋值为等于（借方的“本次结算”合计数-已分配金额）；若（借方的“本次结算”合计数-已分配金额）>贷方选中记录的原币余额，则自动为此记录的本次结算赋值为等于当前记录的原币余额；依此类推，直到将借方结算金额全部分配完成。

<div style="text-align: center;">e) 同币种核销算法举例见表 2.1.3-1（按借方数据分配）</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">借方（应收单）</td><td colspan="4">贷方（收款单）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>选中</td><td style='text-align: center; word-wrap: break-word;'>原币余额</td><td style='text-align: center; word-wrap: break-word;'>结算金额</td><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>选中</td><td style='text-align: center; word-wrap: break-word;'>原币余额</td><td style='text-align: center; word-wrap: break-word;'>结算金额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'>200</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>2000</td><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>300</td><td style='text-align: center; word-wrap: break-word;'>300</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>400</td><td style='text-align: center; word-wrap: break-word;'>400</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1500</td><td style='text-align: center; word-wrap: break-word;'>200</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

#### 表 2.1.3-1

10）异币种核销分配算法如下（仍以“按借方数据分配”为例）：

a) 将贷方第一条记录的选中标志选中；

b) 将借方的“中币结算”合计数与贷方已选的第一条记录的（原币余额*贷方币种对中币汇率）比较大小：

● 若借方的“中币结算”合计数<贷方第一条记录的（原币余额*贷方币种对中币汇率），则自动为此记录的中币结算赋值为等于借方的“中币结算”合计数，再计算当前记录的本次结算=中币结算/贷方币种对中币汇率；

● 若借方的“本次结算”合计数>贷方第一条记录的原币余额，则自动为此记录的本次结算赋值为等于当前记录的原币余额，再计算当前记录的中币结算=本次结算*贷方币种对中币汇率；

c) 继续选中下一条记录，用借方分配剩余的金额进行以下的分配；

d） 将（借方的“中币结算”合计数-已分配中币结算金额）与贷方选中记录的（原币余额*贷方币种对中币汇率）比较大小：

● 若（借方的“中币结算”合计数-已分配中币结算金额）<贷方选中记录的（原币余额*贷方币种对中币汇率），则自动为此记录的中币结算赋值为等于（借方的“中币结算”合计数-已分配中币结算金额）；

● 若（借方的“中币结算”合计数-已分配中币结算金额）>贷方选中记录的（原币余额*贷方币种对中币汇率），则自动为此记录的本次结算赋值为等于当前记录的原币余额，然后再计算当前记录的中币结算=本次结算*贷方币种对中币汇率；

e) 依此类推，直到将借方结算金额全部分配完成。

f) 异币种核销算法举例见表 2.1.3-2（按借方数据分配）：

● 说明：借方币种为美元，中币为人民币，贷方币种为港币，美元对中币汇率为 8，港币对中币汇率为 2，允许误差为 5


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">借方（应收单）（美元）</td><td colspan="5">贷方（收款单）（港币）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>选中</td><td style='text-align: center; word-wrap: break-word;'>原币余额</td><td style='text-align: center; word-wrap: break-word;'>结算金额</td><td style='text-align: center; word-wrap: break-word;'>中币结算</td><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>选中</td><td style='text-align: center; word-wrap: break-word;'>原币余额</td><td style='text-align: center; word-wrap: break-word;'>结算金额</td><td style='text-align: center; word-wrap: break-word;'>中币结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>4000</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1200</td><td style='text-align: center; word-wrap: break-word;'>1200</td><td style='text-align: center; word-wrap: break-word;'>2400</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>2000</td><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>4800</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1300</td><td style='text-align: center; word-wrap: break-word;'>1300</td><td style='text-align: center; word-wrap: break-word;'>2600</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1400</td><td style='text-align: center; word-wrap: break-word;'>1400</td><td style='text-align: center; word-wrap: break-word;'>2800</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1500</td><td style='text-align: center; word-wrap: break-word;'>500</td><td style='text-align: center; word-wrap: break-word;'>1000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3000</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>合计</td><td style='text-align: center; word-wrap: break-word;'>1100</td><td style='text-align: center; word-wrap: break-word;'>8800</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>合计</td><td style='text-align: center; word-wrap: break-word;'>4400</td><td style='text-align: center; word-wrap: break-word;'>8800</td></tr></table>

#### 表 2.1.3-2

● 当用户指定了借方的原币结算金额 1100，并根据对中币的汇率计算出中币结算金额为 8800 后，点击【按借方匹配贷方】，则贷方兰字部分的选中标志和结算金额及中币结算金额由系统自动生成。

● 反之，如果用户指定了贷方的结算数据，点击按钮【按贷方匹配借方】时，则按贷方结算金额相应分配到借方结算金额上。

## 注意：

● 借贷核销，是指系统给每个单据大类赋予了一个方向，应收单是借方，收款单是贷方，应付单是贷方，付款单是借方。

● 若当前会计期间已结账，不能再进行手工核销处理。

● 核销处理若已经通过会计平台生成总账会计凭证，则不能反核销。

● 单据核算时如果勾选了红蓝对冲，则红蓝对冲规则如下：

同一单据内相同往来对象值红蓝对冲；

不同单据相同往来对象红蓝对冲；

同一单据内不同往来对象值红蓝对冲；

不同单据不同往来对象值红蓝对冲。

红冲生成的红字单据需与蓝字单据的表体行一一对应。

红冲生成的红字单据允许修改、删除、增加表体行，新增行必须为红字且不支持自动红蓝对冲。

红冲单据币种原单据币种相同时，红冲单据的金额应等于原单据的金额(绝对值)，并自动核销；若币种不同，则自动进行异币种红蓝对冲，对冲金额为对冲表体行的全部余额。

仅当存在蓝字表体行且表体行的余额不为 0，或表体行与其他单据无任何与核销关系时，方可使用红冲功能。

● 核销时包括折扣金额时，应将折扣录入到应收单方向，并且本次结算金额不包括折扣金额，例如：应收单 666 与收款单 660 核销，折扣为 6，则应收单的结算金额应录入 660 而不是 666；折扣金额录入在应收单方，而不是收款单方向，如下表所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>单据类型</td><td style='text-align: center; word-wrap: break-word;'>原币余额</td><td style='text-align: center; word-wrap: break-word;'>折扣</td><td style='text-align: center; word-wrap: break-word;'>结算金额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收单</td><td style='text-align: center; word-wrap: break-word;'>666</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>660</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单</td><td style='text-align: center; word-wrap: break-word;'>660</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>660</td></tr></table>

11）同币种核销、异币种核销、同币种红蓝对冲需按批次计算汇差（下文不再赘述）。

### 2. 自动核销：

自动核销分人为触发核销和按预置任务自动核销。

1）预设核销方案：在【财务会计】→【应收管理】→【核销处理】→【核销方案设置】节点，点击【增加】钮，预定义自动核销的检索条件、核销规则及核销方式。

2）人为触发自动核销：在【财务会计】→【应收管理】→【核销处理】→【自动核销】节点，点击【查询】（或【方案-加载方案】）钮，完成查询条件设置后，系统即自动按所设的查询

条件完成核销。

a） 查询条件的设置与手动核销相仿，但与手动核销的查询设置相比，增加了“核销方式页签”供用户勾选操作；

b) 自 NCV6.3 起自动核销支持异币种核销。

3）按预置任务自动核销：在【企业建模平台】→【系统平台】→【后台任务中心】→【后台任务部署】节点(需以集团管理员身份登录)，点击【增加】钮，设置常规属性、条目信息、其他配置等属性项后（如图所示），系统将按所设属性自动触发核销任务。

<div style="text-align: center;"><img src="imgs/img_in_image_box_137_481_1058_958.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.1.3-6 后台部署自动核销的设置界面示意</div>


4）异币种自动核销：

a）拉单（允许整单拉单、部分拉单、合并拉单）时若上下游单据币种不同，下游单据在审核时自动取上游单据进行核销，核销时上下游单据的表体行执行严格的一一对应。

b) 核销关键数据如下表（单据操作界面不反应中间币种折算）


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>异币种核销类型</td><td style='text-align: center; word-wrap: break-word;'>中间币种</td><td style='text-align: center; word-wrap: break-word;'>对中间币种汇率</td><td style='text-align: center; word-wrap: break-word;'>折本汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收冲收款</td><td style='text-align: center; word-wrap: break-word;'>收款单原币币种</td><td style='text-align: center; word-wrap: break-word;'>收款单日期对应汇率</td><td style='text-align: center; word-wrap: break-word;'>收款单日期对应汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款冲应收</td><td style='text-align: center; word-wrap: break-word;'>应收单原币币种</td><td style='text-align: center; word-wrap: break-word;'>应收单日期对应汇率</td><td style='text-align: center; word-wrap: break-word;'>收款单日期对应汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应付冲付款</td><td style='text-align: center; word-wrap: break-word;'>付款单原币币种</td><td style='text-align: center; word-wrap: break-word;'>付款单日期对应汇率</td><td style='text-align: center; word-wrap: break-word;'>付款单日期对应汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款冲应付</td><td style='text-align: center; word-wrap: break-word;'>应付单原币币种</td><td style='text-align: center; word-wrap: break-word;'>应付单日期对应汇率</td><td style='text-align: center; word-wrap: break-word;'>付款单日期对应汇率</td></tr></table>

c) 核销算法参见手工异币种核销算法。

d) 异币种自动核销同时计算汇兑损益，算法同已实现汇兑损益算法一致。

e) 异币种拉单核销时，按核销批次计算汇差。

### 3. 即时核销：

录入业务单据过程中即时核销。

1）在【财务会计】→【应收管理】→【应收日常业务】→【应收单管理】节点，选择已生效单据中原币余额不为零的表体记录，点击【按表体核销】钮，再选择“按表体核销”或“按整单核销”，即可执行即时核销的相关处理；

2）即时核销可支持核销、补差、分配等处理：

a) 核销：借贷方本次结算合计原币金额相等时，在弹出的核销窗口中点击【核销】按钮，系统根据已匹配的借贷方单据进行核销处理；

b) 补差：借贷方本次结算合计原币金额不等时，在弹出的核销窗口中点击【补差】钮，弹出即时核销补差处理界面，指定相关信息后，系统自动生成一张已审核单据，保证借贷方本次结算合计原币金额相等，并且自动将借贷方本次结算金额核销完毕；

c) 分配：在弹出的核销窗口中点击【分配】按钮，系统自动将本方单据的本次结算金额，按对方单据的显示顺序依次分配到本次结算金额中，直至分配完或者无法分配为止。分配作为易用性功能，由系统帮助自动匹配。

3) 即时核销处理算法包括：

a) 进行红蓝对冲，包括：同一单据内相同往来对象的红蓝对冲；不同单据相同往来对象的红蓝对冲；同一单据内不同往来对象的红蓝对冲；不同单据不同往来对象的红蓝对冲；

b) 进行借贷核销。

## 注意：

补差处理中驱动生成的单据不必经过审批流确认；

即时核销的处理结果，在手工核销、自动核销的历史记录中进行查询和反操作；

红字单据（本方或对方）即时核销不支持补差。

4）现销业务中，销售应收结算形成的应收单，与建立订单收款核销关系的收款单自动作应收收款核销。

5) 即时核销的相关按钮操作请参阅相关节点的产品帮助。

#### 2.1.4 内部往来协同

##### 2.1.4.1 业务描述

1. 内部单位间发生往来业务，可通过单据协同快速生成对方待确认单据；

2. 应收管理的内部往来协同分为应收单和收款单的协同确认。

##### 2.1.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_297_535_889_1032.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 2.1.4-1 内部往来协同业务流程</div>


##### 2.1.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>客户信息---客户-集团</td></tr><tr><td rowspan="3">财务会计</td><td rowspan="3">应收管理</td><td style='text-align: center; word-wrap: break-word;'>初始设置-单据协同设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收日常业务-应收协同确认</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款日常业务-收款协同确认</td></tr></table>

##### 2.1.4.4 产品解决方案

1. 单据协同设置按集团统一设置，各财务组织调用；

2. 协同发生的基础控制：

1） 在【财务会计】→【应收管理】→【初始设置】→【单据协同设置】节点，点击【增加】钮，设置进行业务协同的发送方/接收方的对应业务系统、财务组织、交易类型等属性；

2) 【企业建模】→【基础数据】→【客户信息】→【客户-集团】节点，设置内部客商，将之关联到接收方的财务组织，将该内部客商分配到发送方的财务组织，并在发送方公司的客商基本档案中勾选收付协同；

3. 往来发起方的应付单/付款单生效后，根据单据协同设置中预置的协同流程，传递单据给接收方；

4. 在【财务会计】→【应收管理】→【应收日常业务】→【应收单协同确认】（或【收款日常业务】→【收款单协同确认】）节点，接收方查询到发起方传来的待确认应收单/收款单后，点击【确认】、【保存】钮，则协同过来的应收单/收款单生效，此时发起方不能再对源头的应付单/付款单进行删改等回退性操作。

5. 协同确认时生成双方的“内部交易结算号”，由上游内部交易单据传递过来（将上游单据传来的结算清单的单据号作为当前单据的内部交易结算号，往来报销业务则取上游报销单的单据号作为当前单据的内部交易结算号），其他方式不可生成；协同时生成双方单据上记录的内部交易结算号应相同；协同确认时若表体行拆分，则自动复制相同的内部交易结算号。

6. 接收方确认了往来单据后视同本方应收单/收款单的录入完成，但由于是来自于协同单据，通常情况下不能执行删除、修改等回退操作，只能进行审批生效、挂起、红冲、核销、形成会计凭证等后续业务处理。若希望可删、改协同单据，应调整参数“AR20 协同单据是否可以删除的取值。

7. 内部往来协同受参数“AR16 单据协同、AR17 协同单据是否可以再协同、AR18 协同单据是否控制总金额、AR20 协同单据是否可以删除”约束：

1）AR16 单据协同：用于指定推动生成被协同方单据的时机，可选项包括“不处理、保存、审核或签字确认”，默认为保存；不处理表示不参与单据协同；选为“保存”则指单据保存即触发对方单位生成协同单据；选为“审核或签字确认”则只有当满足协同条件的单据经审核确认或签字确认后，才会推动形成对方单位的协同单。

2）AR17 协同单据是否可以再协同：默认为否，勾选时表示协同生成的单据可再次引发协同；不勾选则系统来源为"协同单据"的单据不参与再次协同。注意：表体中只要有一行有内部结算号，则该张单据将不允许再协同。

3） AR18 协同单据是否控制总金额：默认不勾选，若勾选则协同生成的单据在修改后，单据总金额必须等于协同金额，保存时时校验；若不勾选，则协同生成单据的金额修改时不作限制。

4） AR20 协同单据是否可以删除：勾选则协同单据可删，不勾选则协同单据不能删除；默认为不勾选（即不允删除）。

8. 内部往来协同支持在“期初关闭”前新增期初单据的录入，新增时可选“应收类型/收款类型”，默认为“应收单/收款单”。

#### 2.1.5 并账

##### 2.1.5.1 业务描述

1. 并账指进行应收/收款业务合并或调整的工作。

2. 将应收/收款业务在客商之间、客商与部门之间、客商与业务员之间进行转入、转出，实现应收/收款业务的调整，解决应收/收款业务在不同对象间入错户或合并户问题。

##### 2.1.5.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_899_867_1257.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">图 2.1.5-1 并账业务流程</div>


##### 2.1.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>应收管理</td><td style='text-align: center; word-wrap: break-word;'>应收日常业务-应收单管理</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="4"></td><td rowspan="4"></td><td style='text-align: center; word-wrap: break-word;'>收款日常业务-收款单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收日常业务-债权转移</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款日常业务-收款并账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>查询/账表（客户总账表、客户余额表…）</td></tr></table>

##### 2.1.5.4 产品解决方案

1. 在【财务会计】→【应收管理】→【应收日常业务】→【债权转移】（或【收款日常业务】→【收款并账】节点，点击【查询】过滤待调整的应收单，查询出结果后，勾选待处理的单据，录入转移金额后，点击【转移】钮完成并账/转移操作。

2. 转账并账只能针对已生效、未挂起和余额不为零的单据进行处理。

3. 转移、并账的结果只改变余额、生成凭证、影响帐表查询结果，并不改变原始业务单据。

4. 并账支持相同对象下的不同属性值转移，例如 A 往来对象下有两个部门 A1、A2 时，支持将 A1 的应收款转给 A2。

5. 并账转移处理记录完成后，可提供查询如下：

1) 【债权转移】/【收款并账】功能节点中点击【转移记录】查看；

2) 【应收单】/【收款单】功能节点中点击【联查-联查处理情况】查看；

3) 【财务会计】→【应收管理】→【查询】下的客户总账表、客户余额表、客户明细账、应收收款情况查询等节点下查看（如图 2.1.5-2 所示）；


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>债权转移</td><td style='text-align: center; word-wrap: break-word;'>客户余额表</td><td colspan="5">客户明细账</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>授权转移</td><td style='text-align: center; word-wrap: break-word;'>客户余额表</td><td style='text-align: center; word-wrap: break-word;'>客户明细账</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>债权转移</td><td style='text-align: center; word-wrap: break-word;'>客户余额表</td><td colspan="4">客户明细表</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_169_1238_994_1474.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 2.1.5-2 并账后客户余额表查询示例</div>

4) 【财务会计】→【应收管理】→【账表】下的客户应收账款分析、客户收款账龄分析等节点下查看。

6. 应收已经结账则不能执行转移并账操作；转移记录一旦通过会计平台生成了总账会计凭证，则不能取消转移。

### 2.2 坏账管理

#### 2.2.1 业务描述

1. 坏账管理包括：坏账计提、坏账发生、坏账收回的业务处理。

2. 坏计提方法包括：应收余额百分比法、销售收入百分比法、账龄分析法。

3. 要求支持多方法多维度计提坏账准备：

1）计提对象：可按往来对象（全部、客户、部门、业务员）分别设置计提方案，同一往来对象下，还可细分计提因素形成不同的计提子方案。

2) 针对不同计提方案设置不同的计提频率及计提方法。

3）可配置每一子方案的计提基数，并分别维护每一子方案的期初余额。

4. 坏账发生时，冲减对应的坏账准备。

5. 提供坏账收回处理（对应收款已确定为坏账后又被收回）。

#### 2.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_292_249_939_807.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 2.2-1 坏账处理业务流程</div>


#### 2.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="7">财务会计</td><td style='text-align: center; word-wrap: break-word;'>基础档案及规则</td><td style='text-align: center; word-wrap: break-word;'>账龄区间设置-集团/组织</td></tr><tr><td rowspan="6">应收管理</td><td style='text-align: center; word-wrap: break-word;'>坏账计提方案</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>计提比率设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账计提</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账损失</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账收回</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账查询</td></tr></table>

#### 2.2.4 产品解决方案

1. 【财务会计】→【应收管理】→【坏账处理】→【坏账计提方案】节点，选择财务组织，根据不同往来对象、计提方式、计提频率、计提因素等维度的组合分别设置坏账计提方案：

1） 每个计提方案可按客户、部门、业务员分设；

2） 按计提方案分别设置计提方式，计提方式支持销货百分比法、应收余额百分比法、应收账款分析法，选择应收账款分析法时，需指定账龄方案；

3）计提频率可选择年、季、月；

4）计提因素可选择客户类型、客户、项目、地区分类、收支项目、部门、业务员、信用等级、币种、交易类型、表头科目、表体科目等，计提因素选定后按指定的计提因素的不同取值组合形成子计提方案；

5）按子计提方案录入期初余额，指定基数算法，基数可从应收、应付、收款、付款、预收、预付中勾选；

6) 计提坏账准备的方案和各方案的计提方法、计提期间、期初余额、计提基数算法。

2. 注意：计提方案启用后才可执行坏账计提处理，往来对象相同的多个计提方案只能启用一个，存有计提数据的计提方案不能反启用，即使原方案已封存。

3. 【财务会计】→【应收管理】→【坏账处理】→【坏账计提比率】节点，根据计提方案所定的计提频率，分别对每个子计提方案的期间设定计提比率，某期间计提后该期间的计提比率将不能再被修改。

4. 【财务会计】→【应收管理】→【坏账处理】→【坏账计提比率】节点，选中坏账计提的方案，点击【快速计提】按钮，系统自动生成应收账款总额及坏账计提数据。

5. 【财务会计】→【应收管理】→【坏账处理】→【坏账损失】节点，点击【坏账发生】钮，选定发生坏账的应收业务单据，确定一定期间内应收款发生的坏账。

1) 坏账损失发生时，冲减对应的坏账准备；

2）坏账损失发生自动生成红字应收单，并对红蓝应收单自动核销。

3) 坏账损失若已通过会计平台生成总账会计凭证，则不能取消坏账发生操作。

6. 【财务会计】→【应收管理】→【坏账处理】→【坏账收回】节点，点击【坏账收回】钮，处理一定期间内所发生的应收坏账收回业务：

1) 坏账收回只针对收款单进行处理；

2) 对坏账收回的收款单自动生成一张蓝字应收单，并进行自动核销。

3) 坏账收回若已通过会计平台生成总账会计凭证，则不能取消坏账收回操作。

7. 债权转移时，受参数“AR29 债权转移时订单客户是否同步转移”约束，若勾选则债权转移时订单客户同步转移。

### 2.3 汇兑损益

#### 2.3.1 业务描述

1. 汇兑损益处理支持三种处理方式：

1) 月末计算汇兑损益：每一笔应收在收到款时不计算汇兑损益，而是在月末统一计算汇兑损益，月末计算汇兑损益时，支持选择汇兑损益计提的纬度是按单据还是按客户计提；

2）外币余额结清时计算汇兑损益：每一笔应收在全额收到款时，计算出该笔应收业务的汇兑损益；

3) 计算已实现汇兑损益：对已收到款的业务计算出汇兑损益计入“已实现汇兑损益”，对未收到款的业务月末统一计入“未实现汇兑损益”，次月初冲回。

2. 汇兑损益提供试算功能。

3. 计算已实现汇兑损益时包括收款单、付款单。

#### 2.3.2 业务流程

略。

#### 2.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>应收管理</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益</td></tr><tr><td rowspan="2">企业建模平台</td><td rowspan="2">基础数据</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr></table>

#### 2.3.4 产品解决方案

1. 根据参数 “汇兑损益计算维度、汇兑损益方式” 参数的设置，进行汇兑损益计算：

1) 【财务会计】→【应收管理】→【期末处理】→【汇兑损益】节点，在主界面选择计算日期、财务组织及拟计算汇兑损益的币种，勾选“选择标志”后，点【下一步】，【试算损益】按钮被激活，点击点击【计算损益】，系统即自动计算所选币种的汇兑损益并自动显示当前算出的损

益报告，此时点击〖损益记录〗/〖联查明细〗，即可查看计算汇兑损益的结果。如图 2.3-1—2.3-4 所示.

所示；


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>业务参数设置-组织</td><td style='text-align: center; word-wrap: break-word;'>应收单管理</td><td style='text-align: center; word-wrap: break-word;'>外币汇率-全局</td><td style='text-align: center; word-wrap: break-word;'>收款单管理</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.3-1 汇兑处理操作示例_参数设置</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>业务参数设置-组织</td><td style='text-align: center; word-wrap: break-word;'>应收单管理</td><td style='text-align: center; word-wrap: break-word;'>外币汇率-全局</td><td style='text-align: center; word-wrap: break-word;'>收款单管理</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>修改</td><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>折算模式</td><td style='text-align: center; word-wrap: break-word;'>日汇率</td><td style='text-align: center; word-wrap: break-word;'>期间汇率</td><td style='text-align: center; word-wrap: break-word;'>平均汇率</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="442">日</td><td rowspan="442">外币汇率
0001基准汇率方案
- 欧元-人民币
- 港币-人民币
- 美元-人民币
0002香港汇率方案
02港币-人民币</td><td rowspan="442">年度月份</td><td rowspan="442">2011-04</td><td rowspan="442">Q</td><td rowspan="442"></td><td rowspan="442"></td><td rowspan="442"></td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

<div style="text-align: center;">图 2.3-2 汇兑处理操作示例_汇率设置</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_152_1084_664.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.3-3 汇兑处理操作示例 选择计算</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_110_722_1088_1141.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.3-4 汇兑处理操作示例_处理结果</div>


2) 调整汇率取对应组织的期间汇率值；

3）当组织级参数“汇兑损益计算纬度”设置为“客户”时，损益处理结果按“客商”维度进行分组小计，并将汇总数据生成总账凭证；若客商为空，则将客商为空的作为一个维度值进行小计；若组织级参数“汇兑损益计算纬度”设置为“单据”，则损益处理结果按币种纬度小计。

4) 汇兑损益算法示例（以应收与收款核销业务为例）：

## 一、 发生的业务数据：

1、2月1日应收某客户美元1000，汇率7.1，折合本位币7100元。

2、2月15日收款美元500，汇率7.5，折合本位币3750元

核销上述收款并计算已实现汇兑损益，则应收及收款单记录（默认以收款单汇率作为核销汇率）：

应收单：1000（7100）

核销—>500*7.5 3750 500（3350）

已汇兑损益—>500*(7.5-7.1)=200 500 (3550)

收款单：500（3750）

核销—>500*7.5 3750 0（0）

3、2月28日计算未实现汇兑损益，汇率7.9则未实现汇兑损益为：

应收单：

1000（7100）

核销—>500*7.5 3750 500（3350）

已汇兑损益—>500*(7.5-7.1)=200 500(3550)

未实现汇兑损益—>500(7.9-7.1)=400 500(3950)

4、3月初回冲未实现汇兑损益

应收单：1000（7100）

核销->500*7.5 3750 500（3350）

已汇兑损益->500*(7.5-7.1)=200 500(3550)

未实现汇兑损益->500(7.9-7.1)=400 500(3950)

回冲未实现汇兑损益->400 500(3550)

5、3月10日收款美元 200，汇率 7.2，折合本位币 1440 元

核销上述收款并计算已实现汇兑损益，则应收及收款单记录：（默认以收款单汇率作为核销汇率）

应收单：

核销—>500*7.5 3750 500（3350）

已汇兑损益—>500*(7.5-7.1)=200 500(3550)

未实现汇兑损益—>500(7.9-7.1)=400 500(3950)

回冲未实现汇兑损益—>-400 500(3550)

核销—>200*7.2 1440 300（2110）

已汇兑损益—>200*(7.2-7.1)=20 300(2130)

收款单：

200（1440）

核销— $ >200 \times 7.2 $ 1440 0（0）

6、3月15日收款美元300，汇率7.4，折合本位币2220元

7、核销上述收款并计算已实现汇兑损益，则应收及收款单记录：（默认以收款单汇率作为核销汇率）

应收单：

1000（7100）

核销—>500*7.5 3750 500（3350）

已汇兑损益—>500*(7.5-7.1)=200 500(3550)

未实现汇兑损益—>500(7.9-7.1)=400 500(3950)

回冲未实现汇兑损益—->-400 500(3550)

核销—>200*7.2 1440 300（2110）

已汇兑损益—>200*(7.2-7.1)=20 300(2130)

核销—>300*7.4 2220 0（90）

已汇兑损益—>300*(7.4-7.1)=90 0(0)

收款单：

300（2220）

核销—>300*7.4 2220 0（0）

## 账表及单据分析

应收单分析：

应收单：

1000（7100）

已汇兑损益—>500*(7.5-7.1)=200 500(3550)

未实现汇兑损益—>500(7.9-7.1)=400 500(3950)

月初冲回未实现汇兑损益 -400 500（3550）

核销—>200*7.2 1440 300（2110）

已汇兑损益—>200*(7.2-7.1)=20 300(2130)

核销—>300*7.4 2220 0（-90）

已汇兑损益—>300*(7.4-7.1)=90 0(0)

则从应收单处理记录上，可以很方便地看到此笔业务实现了汇兑损益 310 元账表分析

明细账如下表所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>日期</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>应收额</td><td style='text-align: center; word-wrap: break-word;'>收款额</td><td style='text-align: center; word-wrap: break-word;'>余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2月1日</td><td style='text-align: center; word-wrap: break-word;'>应收</td><td style='text-align: center; word-wrap: break-word;'>7100</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>7100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2月15日</td><td style='text-align: center; word-wrap: break-word;'>收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3750</td><td style='text-align: center; word-wrap: break-word;'>3350</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>已实现汇兑损益</td><td style='text-align: center; word-wrap: break-word;'>200</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3550</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2月28日</td><td style='text-align: center; word-wrap: break-word;'>未实现汇兑损益</td><td style='text-align: center; word-wrap: break-word;'>400</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3950</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3月1日</td><td style='text-align: center; word-wrap: break-word;'>未实现汇兑损益回冲</td><td style='text-align: center; word-wrap: break-word;'>-400</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3550</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3月10日</td><td style='text-align: center; word-wrap: break-word;'>收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1440</td><td style='text-align: center; word-wrap: break-word;'>2110</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>已实现汇兑损益</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2130</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3月15日</td><td style='text-align: center; word-wrap: break-word;'>收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2220</td><td style='text-align: center; word-wrap: break-word;'>-90</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>已实现汇兑损益</td><td style='text-align: center; word-wrap: break-word;'>90</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

5）汇兑损益处理的不同处理方式如下图所示：

6) 汇兑损益计算结果通过会计平台生成凭证传递到总账。

2. 产品根据参数“AR10 本月汇兑损益是否计算”（参数值包括不检查、检查但不控制、检查并且控制；默认为不检查的设置）的取值，进行汇兑损益计算：只有当“AR5 汇兑损益方式”参数值选择月末计算时，参数“AR10 本月汇兑损益是否计算”才能调整。

3. 根据参数“AR28 未确认（暂估）单据是否计提汇兑损益”来确定是否对暂估应收计提汇兑损益。

### 2.4 关联与结账

#### 2.4.1 业务描述

1. 集团业务多人协同并发工作下，为保证上下游模块间业务数据的一致，需要分出关账与结账状态。

2. 关账\（批量关账）用于关闭本模块的输入，已关账期内禁止接受上游业务数据，与下游模块相关的业务数据同时禁止修改，用于明确各岗位责任，并及时发现相关环节衔接的问题。

3. 月末结账用于关闭一个模块的输出，除查询外，封闭当前期间的一切业务操作，并检查当期单据生效、收款单核销、单据生成凭证、单据计算汇兑损益的完成情况。

4. 关账在先，结账在后；业务上可能会跨会计期间关账。

#### 2.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_343_238_896_942.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 2.4-1 关联与结账处理流程</div>


#### 2.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织关联</td></tr><tr><td rowspan="5">财务会计</td><td rowspan="5">应收管理</td><td style='text-align: center; word-wrap: break-word;'>组织批量关联</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>期末处理-关联</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>期末处理-批量关联</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核销处理/坏账处理/汇兑损益</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>月末结账</td></tr></table>

#### 2.4.4 产品解决方案

### 1. 关联：

1) 【财务会计】→【应收管理】→【期末处理】→【关联】节点，选业务单元，会计期间后点击【关联】钮，即可完成关联操作；或者在【财务会计】→【应收管理】→【期末处理】→【批量关联】节点，先选会计期间方案及会计期间，再选取多个财务组织单元后，点击【批量关联】钮，可完成同时对多个组织的关联操作。

2) 【企业建模平台】→【组织管理】→【组织关联】，选业务单元，“应收管理”模块、会计期间后点击【关联】钮，也可完成关联操作。

3）应收管理的【关联】与建模平台的【关联】：建模平台的【关联】是平台级控制，可操作的模块更多，操作人员权限上有严格要求，但两个关联节点仅就操作次序上并无先后差别，两者中以最后操作的结果为准。

4）第一个会计期关账处理前，必须先关闭期初。

5) 关联检查增加一项警告类的检查项：检查存货核算系统是否已关账。

2. 某会计期关账后，当前期间的期初余额、应收日常业务、收款日常业务不能再执行录入、修改等操作。

3. 关联后结账前，仍可进行关联期间的核销、坏账计提、损益计算、查询等操作。

4. 根据上游单据的业务日期，查找所归属的会计期间，判断本模块该期间是否关联，若未关联则本模块单据取该期间；若已关联，则取该期间之后的第一个未关联期间。

5. 某会计期关账后，当前期间的业务单据禁止录入、修改；已关账期间的业务发生数不能再修改。

### 6. 按期间结账：

1) 【财务会计】→【应收管理】→【期末处理】→【月末结账】节点，选财务组织，勾选会计期间后点击【下一步】钮，再点击【完成结账】可完成结账操作。

2）结账时封闭结账期内除查询外的其他一切业务操作，并检查当期单据生效、收款单核销、单据生成凭证、单据计算汇兑损益的完成情况，根据相应参数的设置值按其流程处理。

3) 增加一项警告类的检查项：协同的单据是否已全部确认。

7. 若某会计期末关账，也可直接执行结账处理，此时由系统自动先执行“关账”再执行“结账”操作。

8. 不同参数对业务流程的约束：

1）AR5 汇兑损益处理方式：当该参数取选项值的“月末计算”（选项值分为月末计算、外币余额结清时计算、计算已实现汇兑损益，“月末计算”为系统默认项）时，在月末结账前对所有原币余额不为零、或者本币余额不为零的外币单据（应收单、收款单）计算汇兑损益，该参数与参数“AR10 本月汇兑损益是否计算”取值组合生效。

2）AR7 截止到本月单据全部生效：月末结账时检查本月单据生效状态，按其参数取值（不检查、检查但不控制、检查并且控制；默认为不检查），若设为“检查且控制”时，若有单据未生效则不允许结账。

3) AR8 截止到本月单据全部核销：月末结账时检查本月单据是否核销完毕，按其参数取值（不检查、检查但不控制、检查并且控制；默认为不检查），若设为“检查且控制”时，若有收款单未核销完毕则不允许结账。

4）AR9 截止到本月单据全部生成会计凭证：月末结账时检查本月单据是否已全部生成会计凭证，按其参数取值（不检查、检查但不控制、检查并且控制；默认为不检查），若设为“检查且控制”时，若有单据未生成会计凭证则不允许结账。

5) AR22 总账关账是否检查本系统状态：默认为勾选，若勾选则要求总账模块在关账前要检查应收管理是否已结账，若应收未结账则总账不能关账；若未勾选，则总账关账不受应收关账不否的影响。

## 第三章 初始准备

应收管理初始准备工作如图 3-1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_145_1069_953.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3-1 应收管理初始准备示意图</div>


### 3.1 管控模式

管控模式用于初始化时进行档案规则的配置，即针对每个档案根据最常规的应用方案设置其默认规则。用户可以在每个档案可支持的规则范围内进行调整，调整档案的规则时，需要同时受档案间的约束规则约束。

管控模式属全局级节点，由拥有权限的用户（系统管理员）维护并查看全局内的全部数据，这些数据在数据库内唯一。

一个档案只能在可选择的管控模式范围内选择，按照“管控模式”配置的不同，档案将分为全局级、集团级、组织级的多个节点，通过集团管理员完成功能授权后交由指定操作员使用。

管控模式设置包括：管理模式配置、可见性范围和唯一性范围；管控模式配置是定义节点可维护数据的

最大范围；可见性范围是决定用户可以查看、使用基础数据的最大范围；唯一性范围是决定基础数据唯一性的范围。

当档案中存在数据时，管控模式只能往细化调整，即切换后的管控模式要包含当前管控模式决定的所有节点，且调整后管控模式的唯一性校验范围只能小于等于原管控模式的唯一性校验范围；

管控模式影响到后续业务方案的实现，是业务建模中的重要环节，系统对企业建模平台中大部分基础档案支持管控模式，应收管理模块中需要设置管控模式的档案包括：收款协议、客户分类、客户地区分类、客户信息。产品正式使用前务必对所有业务分析清楚，多角度判断有无错漏后再设定。

收款协议、客户基本分类、客户基本信息等基础档案管理通过“管控模式”中的设置，可提供集团统管、集团管控部分信息、下属组织自行管理部分信息等多种模式，实现统分结合、统而不僵、管放适当的集团管控目的。

关于管控模式的具体应用设置参见“NCV6.33 系统管理产品手册”内容。

<div style="text-align: center;"><img src="imgs/img_in_image_box_157_667_1034_1234.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 3.1-1 应收管理所需档案的管控模式界面示意</div>


### 3.2 企业建模平台

企业建模平台由集团管理员负责，需完成组织管理（即组织管理）、基础数据（档案）、流程管理等方面的设置，才能顺利实现应收管理模块的业务操作各项功能。

#### 3.2.1 多组织管理

通过设置财务组织、库存组织、销售组织、采购组织等相关业务组织，支持多组织架构，同时还可以通过交叉、多级、跨组织的业务委托关系，实现集团应收业务的多组织业务协同。

组织建立在系统中包括业务单元、销售业务委托关系，具体操作应用请参见“NCV6.33 多组织管理手册”。

##### 2.1.4.1 组织管理-组织结构定义

### 1. 业务单元

公司、分公司、办事处可以建模为业务单元，勾选了“财务”属性后，该组织即成为财务组织，可以使用应收模块。

当一个业务单元同时具有财务、销售属性时，表示该组织同时具有销售业务职能和应收核算职能，此即为传统的单组织业务处理、核算模式；若一个业务单元只具有财务、销售属性之一时，相互间通过销售业务委托关系完成销售到应收核算的业务处理。

集团内的各业务单元间可以互为内部客商，通过在【业务单元】节点点击【辅助功能-生成内部客商】实现。

承担应收管理职能的业务单元需要指定启用期间，可在【业务单元】节点点击【辅助功能-业务期初期间】进行指定。

##### 2.1.4.2 功能节点与主组织对照表


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">路径</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td><td style='text-align: center; word-wrap: break-word;'>NC6.33 主组织</td></tr><tr><td rowspan="10">应收管理</td><td rowspan="3">-初始设置</td><td style='text-align: center; word-wrap: break-word;'>单据协同设置</td><td rowspan="2">集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报表初始化</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报表初始化</td><td style='text-align: center; word-wrap: break-word;'>全局</td></tr><tr><td rowspan="2">-期初余额</td><td style='text-align: center; word-wrap: break-word;'>应收期初</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款期初</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="5">应收日常业务</td><td style='text-align: center; word-wrap: break-word;'>应收单录入</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收单管理</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收单协同确认</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>债权转移</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未确认应收单管理</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="4">收款日常业务</td><td style='text-align: center; word-wrap: break-word;'>收款单录入</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单管理</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单协同确认</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款并账</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="3">核销处理</td><td style='text-align: center; word-wrap: break-word;'>核销方案设置</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自动核销</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>手动核销</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="6">坏账处理</td><td style='text-align: center; word-wrap: break-word;'>坏账计提方案</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>计提比率设置</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账计提</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账损失</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账收回</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账查询</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="2">催款</td><td style='text-align: center; word-wrap: break-word;'>催款语气</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>催款单</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="3">期末处理</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>关账</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>月末结账</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="6">查询</td><td style='text-align: center; word-wrap: break-word;'>客户总账表</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户余额表</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户明细账</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收收款情况查询</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收对账单</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>明细联查</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td rowspan="6">账表</td><td style='text-align: center; word-wrap: break-word;'>客户应收账款分析</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户收款账龄分析</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户应收欠款分析</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户收款分析</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户收款预测</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收报警单</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr></table>

##### 2.1.4.3 跨组织部门、人员参照

1\. 相关单据调整(包括：应收单、应付单、收款单、付款单、期初应收/应付/收款/付款、未

确认应收、暂估应付、期初暂估应付单）

1) 应收单/收款单/期初应收/期初收款/未确认应收/应付单/付款单/期初应付/期初付款/暂估应付/期初暂估应付单据的销售组织、销售部门、销售人员、采购组织、采购部门、采购人员变更为业务组织、业务部门、业务人员；

2) 业务组织的参照为业务单元，业务单元的参照范围为根据主组织(财务组织)的财务核算委托关系的所有业务单元；

3) 业务部门的参照范围：业务组织下所有部门，并且包含业务员的来源所属组织的部门，如：A 组织和 B 组织无财务核算委托关系，但 A 组织的人员在 B 组织做事，业务发生在 B 组织，所以在做部门参照时同样可以参照到 A 组织的部门；

4) 业务人员的参照范围：业务员的参照范围同业务部门的参照范围；

5) 自制单据时，业务组织默认等于财务组织；

6) 单据默认显示业务组织、业务部门、业务人员，单据模板的部门、人员默认不显示。

2. 转移并账、核销、汇兑损益、坏账处理、单据协同、账表查询等功能涉及业务组织、部门、人员的参照都做相应的调整。

#### 3.2.2 基础数据维护

基础数据维护在系统中包括参数设置，客户信息和结算信息中相关基本档案，具体操作应用参见“NCV6.33 基础数据手册”。

##### 2.1.5.1 参数设置

即使对于同一业务应用场景或业务流程，不同的核算对象也会有不同的应用要求、控制范围和处理方式；产品实现上 NCV6.33 可以通过设置不同的变量来满足，使得应用效果和业务流程可以适当地配置，这些变量被称之为参数，配置过程即为参数设置过程。具体操作是指在参数设置平台中输入和设置系统所提供的参数值，使业务在执行相关处理时通过系统设置的参数值判断应如何控制。

NCV6.33 根据参数内容的影响范围分为全局、集团、组织（业务单元）三个层次：

1） 全局级参数：是指参数仅能在全局中进行设置，影响范围是整个全局，是系统级统一设置的参数。例如上机日志明细级别……等；

2) 集团级参数：是指参数可以在各个集团中进行设置，影响范围是本集团，不同集团间参数无控制

关系。例如集团本位币、数量小数位、会计平台启用时间……等；

3) 组织级参数：是指参数根据所影响业务范围的主组织进行设置，对于存在上下级关系类型的组织，上级组织的参数对下级组织起控制作用。例如：科目显示名称模式（主体账簿级）、采购最高库存控制（采购组织级）……等。

应收管理模块在 V6x 中仅提供业务单元级参数，相关参数参阅本文“附录 2 单据参数”内容。

##### 2.1.5.2 公共信息

应收管理涉及的公共信息包括：会计期间、币种、外币汇率、部门档案、人员档案等。其中会计期间、币种、外币汇率、人员档案由集团管理员在【企业建模平台】→【基础数据】→【公共信息】中按各自功能子节点进入后设置；部门档案则在【企业建模平台】→【组织管理】→【组织结构】节点中按业务单元分别设置，供应收模块日常单据调用。

外币汇率的期间汇率提供给汇兑损益处理调用。

##### 2.1.5.3 客户信息

客户信息包括渠道类型、客户基本分类、客户销售分类、客户档案等,前三者为客户档案提供了销售业务维护的各个分类，应收管理模块关注的是客户档案信息，客户档案信息中以财务页签为重点。

## 客户

客户档案是 NC 系统最核心的基本档案之一，应用于 NC 系统众多领域，主要记录集团企业内、外部客户的具体业务信息，通过基本信息、财务信息、销售信息和信用控制信息 4 个页签分别进行维护。

客户档案初始维护时，只有基本信息页签可以维护，其他信息页签必须通过“分配”按钮分配相关组织后才可显示出来，并将分配的相关组织带入相关组织页签，形成行记录信息，后续可以补充维护相关其他信息内容，但不能再增加行记录信息，系统支持【删除】，相当于取消分配处理操作；

基本信息页签主要包括：是否供应商、对应供应商、客户类型、上级客户、散户等，上级客户即客户总公司编码，通过指定上级客户实现客户的上下级关系，可以实现大型商超客户的统一结算地结算、按客户总公司询价、按客户总公司信用（额度、账期）检查控制等应用；

财务信息页签主要包括：是否催款、是否协同和内控账期天数等，内控账期天数是集团内相关组织对应的财务组织对客户信用账期设置的天数，流程配置中通过函数"客户超内控账期天数"是按此天数进行信用检查控制；只有勾选了“是否协同”，才能执行“单据协同设置”及完成往来协同操作。

##### 2.1.5.4 结算信息—收款协议

收款协议主要对设备、周转材料（如液压支柱）、施工用物资（如照明设备）等大宗贸易的分期收款业务，通过收款协议编制分期收款的时点、比例、结算方式和折扣等重要交易因素，对销售合同、销售订单、销售发票的销售收款计划跟踪，实现客户应收账款分析、收款预测、信用管控等管理工作。收款协议主要提供给销售、应收管理模块应用。

收款协议包括：分期收款的期数、收款比例、预收款、起效日期、起效日期延迟天数、账期天数、出账日、固定结账日、生效月、附加月、结算方式、质保金和现金折扣；设置固定结账日与设置账期是两种场景，每一期付款只能二选一。V60 支持分多期收款的款项管理，支持固定结账日（附加月功能），支持不同协议行根据业务需要取不同起算日期进行应收款项管理。

V6.5 支持信用卡的协议作为收款协议，以出账日作为立账日，固定结账日作为结算日期。

#### 3.2.3 流程平台搭建

针对不同业务类型支持灵活自定义业务流，业务流定义基于“交易类型”配置相应的业务单据流程、销售结算规则等，实现多种销售业务类型处理的需要，强调以流程为导向完成日常的业务管理操作；

流程平台的搭建在系统中包括交易类型设置和流程设计，具体操作应用请参见“NCV6.33 流程管理手册”。

### 1. 交易类型管理

交易类型是一个业务的上下游环节进行衔接时所遵循的约束规则。当上下游单据之间采用不同的交易类型流转，即采用不同的约束规则进行业务处理会得到不同的业务结果；通过交易类型的设置，可以让同样的单据流派生出不同的业务流形态。

V6.0 应收应付支持的单据类型有应收单 F0、收款单 F2、应付单 F1、付款单 F3；预置有应收单 D0、收款单 D2、应付单 D1、付款单 D3 四个交易类型；支持自定义交易类型后发布供业务录入使用。

V6.3 起应收单提供 “是否行合并计税税额” 选项，默认为否。为否时逐行计算增值税；若勾选，则将应收单表体明细行中具有相同 VAT code 的明细行的无税金额先汇总，然后再计算该 VAT code 的总税额，再逐个 VAT code 进行税额汇总。具体处理方式如下：

对整单中客户、税码、税率、扣税类别、购销类型相同的，作为一组，合计计算税基，再计算税额。

● 重新计算的税额 - 原来的计算结果各行税额合计的差额，作为尾差，挤入本组某一行税额；再对

此行调用税额维护的算法，影响无税优先算法无税金额。

➢ 增行、插入行、编辑任何一行的数量、金额，多行合并税额计算，差异挤入当前编辑行；

➢ 删行带来的差异挤入本组最后一行；

直接编辑某行税额，不重新处理多行合计 VAT 计算，仅本行的非优先金额有变化，其他数据没有变化；

其他原因导致的数量/单价/金额等变化，原则上都按照上述规则处理；

复制/黏贴单据表体行时，不重新计算税额。

税码为空时，不参与行合并计算税额。

● 打印模板支持打印辅助信息区的税务信息。

### 2. 业务流定义

用于设置非流程单据与流程单据之间接口关系，如销售订单生成预收款单、销售发票生成应收单等；“业务流定义”只支持对流程单据进行配置，单据接口定义是对通过业务流定义单据间关系的补充；单据接口定义支持按照单据交易类型进行细分设置。

V60 应收应付预置 9 个业务流程，4 个启用（选择收款、收款结算、选择付款、付款结算），其余 5 个默认停用状态（收款单推委托收款书、收款单推内转单、付款单推委托付款书、付款单推内转单、付款排程）；若预置业务流程不敷使用，用户可以自己新增业务流，按照业务流四要素匹配原则，不同的交易类型单据可走不同的流程，生效后生成不同业务的凭证。

<div style="text-align: center;"><img src="imgs/img_in_image_box_180_943_1051_1218.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 3.2.3-1 业务流定义示意图</div>


#### 3.2.4 会计平台设置

应收管理产品中，支持通过财务会计平台生成总账会计凭证的单据和业务处理，有关会计平台设置的具体操作请参阅《会计平台应用手册》，初始应用步骤包括：

1. 在【企业建模平台】→【会计平台】→【通用平台】→【平台设置】节点，确定生成凭证的单据

及生成处理方式，产品支持按过滤条件选择不同生成总账凭证及是否汇总，如图 3.2.4-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_139_203_1056_845.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 3.2.4-1 会计平台设置界面示意</div>


2. 在【企业建模平台】→【会计平台】→【通用平台】→【入账设置-集团】/【入账设置-业务单元】节点，确定各类单据的影响因素及其所作用范围，产品支持统计型的自定义项作为影响因素，自定义项需在【平台配置】的【影响因素定义】和【单据因素关联】预置。

3. 在【企业建模平台】→【会计平台】→【通用平台】→【分类定义-集团】/【分类定义-业务单元】节点，指定各类业务的入账科目。

4. 在【企业建模平台】→【会计平台】→【通用平台】→【转换模板-集团】/【转换模板-业务单元】节点设置各类业务单据生成凭证的生成方式、生成总账正式凭证还是临时凭证、单据表头表体的入账应选的科目分类等具体信息项。

注意当勾选了“处理失败则阻止单据生效”，则相应单据确认时必须生成凭证。

在转换模板设置功能节点中所对应的单据类型如表 3.2.4-1 所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>凭证模板设置中的单据类型</td><td style='text-align: center; word-wrap: break-word;'>应收管理中的单据或者业务处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>未确认应收单</td><td style='text-align: center; word-wrap: break-word;'>暂估应收，单据审核后传财务会计平台</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收单</td><td style='text-align: center; word-wrap: break-word;'>应收单，单据审核后传财务会计平台</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单</td><td style='text-align: center; word-wrap: break-word;'>收款单，单据审核或签字确认后传财务会计平台</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>付款单</td><td style='text-align: center; word-wrap: break-word;'>付款单，单据审核或签字确认后传财务会计平台</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核销单</td><td style='text-align: center; word-wrap: break-word;'>核销处理，包括即时核销、手工核销、自动核销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收并账单</td><td style='text-align: center; word-wrap: break-word;'>债权转移中转出户为客户，方向为应收的转移</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款转预收单</td><td style='text-align: center; word-wrap: break-word;'>单据管理功能节点中，单据表头“预收款”字段未选的已生效状态的收款单，通过【预收】按钮，将单据表头“预收款”字段改为已选。对应业务描述即收款单转为预收款单。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账计提单</td><td style='text-align: center; word-wrap: break-word;'>坏账计提处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账损失单</td><td style='text-align: center; word-wrap: break-word;'>往来对象为客户的应收单的坏账发生处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>坏账收回单</td><td style='text-align: center; word-wrap: break-word;'>往来对象为客户的坏账收回处理，对应两个凭证模板，即坏账收回处理可以生成两张总账会计凭证。坏账收回的处理流程可以分为以下三个步骤：选择收款单、系统自动生成兰字应收单、生成的兰字应收单与选择的收款单核销。系统自动生成兰字应收单步骤，对应应收坏账收回单凭证模板，可以生成会计凭证“借：应收账款，贷：坏账准备”。生成的兰字应收单与选择的收款单核销步骤，对应应收坏账收回核销单凭证模板，可以生成会计凭证“借：应收账款，贷：应收账款”。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>损益单</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益方式为“计算已实现汇兑损益”时，汇兑损益处理生成的凭证</td></tr></table>

<div style="text-align: center;">表 3.2.4-1</div>


### 3.3 领域级础设置

#### 3.3.1 基础设置

### 1. 账龄区间设置

账龄区间设置用于提前设置往来账款的时间长度，以便总账、应收管理、应付管理三个模块使用。账龄区间按集团统一设定，供各财务组织选用。

### 2. 基础档案对照

跨组织间业务协同时，各财务组织间因会计制度、核算口径、业务细化程度的不同，会导致同一业务在不同组织间入账科目的不同，同时也会记入不同的辅助核算类型，因而需要建立一套在两个不同组织间基本档案的对照关系，且由于科目的对照关系可以在折算规则上建立，基本档案对照只针对除科目外其他基本档案的处理。具体操作应用参阅相关节点的在线帮助。

#### 3.3.2 应收管理

### 1. 单据协同设置

各财务组织间发生协同业务时，需要预置财务组织间按交易类型间的协同关系，并对一对协同关系下的字段间对照进行设置。具体操作应用请参见“NCV6.33 帮助文件”。

### 2. 期初余额

期初余额用于录入期初应收款、期初预付款和期初未核销付款等期初数据，产品以期初单据的形式来实现期初数据的录入。

作为应收管理产品初始准备工作中的重要环节，期初余额的处理有其特点，包括：

1）期初单据除了由外部系统导入外，只能由本模块统增加，同样期初余额查询也只能查询本模块增加的期初数据。

2) 期初单据保存即审核，因而单据日期和审核日期、录入人和审核人相同。

3) 期初单据除不限制起算日期外，其他方面与正常的单据录入规则相同。

4）产品提供按财务组织的期初关闭/取消关闭功能，用户在期初关闭前完成期初单据的增、改、删处理；但启用后的第一个会计期间结账后，期初关闭将不能取消。

5）期初单据反映产品启用期间之前的业务，所以外币期初单据的汇率值无法取自汇率档案，需要手工指定。

6）期初单据不支持审批流、不传财务会计平台和管理会计平台，不进行任何预算、账户额度等业务控制。

## 第四章 操作指南

本手册具体详细操作应用，请登录 NC 系统参见相关产品帮助。

## 附录

## 附录 1：单据流转

单据流转主要通过业务流定义和单据接口定义实现。

业务流定义是定义企业业务流程的流程配置平台，可以任意根据用户的实际业务重新梳理业务单据、动作及组件，包括每种单据的来源单据是什么、又驱动生成哪些单据、完成什么动作、动作生效的约束条件以及动作生效后将配置哪些组件等，对发生的各种业务进行事前、事中、事后的控制，以此更好满足集团企业个性化管控需求；业务流定义只支持对流程单据进行配置。

非流程单据与流程单据在产品应用上的区别在于——流程单据支持通过“业务流定义”配置上下业务单据流转，而非流程单据则是通过“单据接口定义”进行设置与上下游单据发生关联。典型的流程单据如销售订单、发货单、销售出库单、销售发票、运输单、调入申请、调拨订单等。非流程单据的上下游衔接如预订单生成销售订单、销售合同生成销售订单、销售发票生成应收单等。

是否为非流程单据，是通过【应用管理平台】→【开发配置工具】→【交易管理】→【单据类型管理】来设置的，在产品中实际上成为后台的默认设置。

### 1. 应收单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>模块</td><td style='text-align: center; word-wrap: break-word;'>上游单据</td><td style='text-align: center; word-wrap: break-word;'>下游单据</td></tr><tr><td rowspan="6">供应链</td><td style='text-align: center; word-wrap: break-word;'>销售管理</td><td style='text-align: center; word-wrap: break-word;'>销售发票</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>销售管理</td><td style='text-align: center; word-wrap: break-word;'>销售费用单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运输管理</td><td style='text-align: center; word-wrap: break-word;'>应收运费发票</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运输管理</td><td style='text-align: center; word-wrap: break-word;'>代垫运费发票</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内部交易</td><td style='text-align: center; word-wrap: break-word;'>内部结算清单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>库存管理</td><td style='text-align: center; word-wrap: break-word;'>销售出库单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="5">资产管理</td><td style='text-align: center; word-wrap: break-word;'>维修管理</td><td style='text-align: center; word-wrap: break-word;'>工单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="2">资产租赁管理</td><td style='text-align: center; word-wrap: break-word;'>应收租金计算单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对内/对外租出单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>保险索赔单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>资产处置</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="2">财务会计</td><td style='text-align: center; word-wrap: break-word;'>报销管理</td><td style='text-align: center; word-wrap: break-word;'>费用类报销单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收管理</td><td style='text-align: center; word-wrap: break-word;'>收款单</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>应收管理</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>收款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>存货核算</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>销售成本结转单</td></tr></table>

### 2. 未确认应收单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>模块</td><td style='text-align: center; word-wrap: break-word;'>上游单据</td><td style='text-align: center; word-wrap: break-word;'>下游单据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>供应链</td><td style='text-align: center; word-wrap: break-word;'>库存管理</td><td style='text-align: center; word-wrap: break-word;'>销售出库单</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

### 3. 收款单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>模块</td><td style='text-align: center; word-wrap: break-word;'>上游单据</td><td style='text-align: center; word-wrap: break-word;'>下游单据</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>流转条件</td></tr><tr><td rowspan="3">供应链</td><td style='text-align: center; word-wrap: break-word;'>合同管理</td><td style='text-align: center; word-wrap: break-word;'>销售合同</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>销售管理</td><td style='text-align: center; word-wrap: break-word;'>销售订单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>销售管理</td><td style='text-align: center; word-wrap: break-word;'>销售报价单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">财务会计</td><td rowspan="2">应收管理</td><td style='text-align: center; word-wrap: break-word;'>应收单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应收单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>固定资产卡片（租金附卡）</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">资金管理</td><td rowspan="2">现金管理</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>收款单（结算页签）</td><td style='text-align: center; word-wrap: break-word;'>关联</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>到账通知</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金结算</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>委托收款书</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

### 4. 与总账对账

应收模块进行应收科目的细化核算，提供明细数据和汇总数据给总账模块，并向总账模块提供明细数据的联查业务单据（或处理记录）：

<div style="text-align: center;"><img src="imgs/img_in_image_box_182_153_1007_914.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 附录 1-1</div>


1）汇总数据的算法取余额表的算法：即查询对象为对账条件中设置的查询对象，过滤条件为对账条件中设置的对账条件；然后分别按期初、本期借方、本期贷方、期末余额提供给总账对账接口。

2）对账数据包括：单据、核销处理记录、并账处理记录、坏账处理记录等。

3) 明细数据：将组成汇总数据的明细数据提供给对账接口，对账接口将总账明细与应收明细根据会计平台的线索生成对账明细。

要求用户当月的业务（转移并账、核销处理、坏账处理）均必须全部生成当月凭证，不允许跨月生成凭证。

## 附录 2：控制点

### 1. 单据参数


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>模块</td><td style='text-align: center; word-wrap: break-word;'>所属组织</td><td style='text-align: center; word-wrap: break-word;'>代码</td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>相关参数</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">与范围</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="18">应收管理</td><td rowspan="18">组织</td><td style='text-align: center; word-wrap: break-word;'>AR1</td><td style='text-align: center; word-wrap: break-word;'>核销顺序</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR2</td><td style='text-align: center; word-wrap: break-word;'>核销方式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR5</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益方式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR7</td><td style='text-align: center; word-wrap: break-word;'>截止到本月单据全部生效</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR8</td><td style='text-align: center; word-wrap: break-word;'>截止到本月收款单全部核销</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR9</td><td style='text-align: center; word-wrap: break-word;'>截止到本月单据全部生成凭证</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR10</td><td style='text-align: center; word-wrap: break-word;'>本月汇兑损益是否全部计算</td><td style='text-align: center; word-wrap: break-word;'>AR5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR16</td><td style='text-align: center; word-wrap: break-word;'>单据协同</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR17</td><td style='text-align: center; word-wrap: break-word;'>协同单据是否可以再协同</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR18</td><td style='text-align: center; word-wrap: break-word;'>协同单据是否控制总金额</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR20</td><td style='text-align: center; word-wrap: break-word;'>协同单据是否可以删除</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR21</td><td style='text-align: center; word-wrap: break-word;'>销售价格优先策略</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR22</td><td style='text-align: center; word-wrap: break-word;'>总账关账是否检查本系统结账状态</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR28</td><td style='text-align: center; word-wrap: break-word;'>暂估（未确认）单据是否计提汇兑损益</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR29</td><td style='text-align: center; word-wrap: break-word;'>债权转移时订单客户是否同步转移</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR32</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益计算维度</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR35</td><td style='text-align: center; word-wrap: break-word;'>预收款是否按收款协议的预收付标志核销</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AR36</td><td style='text-align: center; word-wrap: break-word;'>贷方引用信息指定字段</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

附录 3：查询报表为适应组织架构调整日益频繁的要求，NC6.1 起账表查询支持财务组织多版本（但暂不支持财务组织体系多版本），可按最新的组织体系、指定版本显示该版本下当前组织的编码和名称。涉及财务组织多版本的单据包括应收单、收款单，单据上涉及财务组织多版本的包括表头和表体部分，具体为主组织、结算财务组织、销售组织、利润中心、部门、销售部门等。

参照显示按查询日期范围的截止日期对应版本(截止日期及以前启用的最新版本)，如果没有截止日期，则取最新版本。修改查询日期后，系统并不自动刷新财务组织参照，但在再次打开参照时会根据修改后的查询日期刷新参照内容。

## 1 ) 查询

a) 客户总账表：

● 提供应收款、预收款按总账账页格式列示（本期借方、本期贷方、期末余额）的查询功能，可按财务组织查询在指定会计期内发生的业务汇总情况以及累计汇总情况。

查询条件包括：往来对象（客户、部门、业务员）、查询的应收范围（全部应收/已确认应收/未确认应收）、单据状态（已生效/已保存/已审核）、币种、起止期联合筛选查询结

果。

● 财务组织不能为空。

## b) 客户余额表：

查询在指定期间内所发生的应收、收款以及余额的汇总情况。余额表的查询范围包括应收和未核销的收款，查询结果支持向明细账的穿透联查。

● 查询条件包括：往来对象（客户、部门、业务员）、查询的应收范围（全部应收/已确认应收/未确认应收）、单据状态（已生效/已保存/已审核）、币种、起止期，按各项条件联合筛选查询结果。

● 查询条件中财务组织不能为空。

## c) 客户明细账：

● 查询指定会计期内发生的应收以及收款明细情况，可对指定记录行联查单据及相应的余额表。查询结果支持向客户余额表穿透查询，以及联查单据/处理情况/凭证；查询结果支持按日小计。

查询条件包括：往来对象（客户、部门、业务员）、查询的应收范围（全部应收/已确认应收/未确认应收）、单据状态（已生效/已保存/已审核）、币种、起止期，按各项条件联合筛选查询结果。

● 查询条件中财务组织不能为空

## d) 应收收款情况查询：

查询指定查询对象在一定期间内发生的应收以及收款及其余额情况。查询结果支持联查单据和凭证。

● 根据往来对象（客户、部门、业务员）所选择项的不同，对应的往来查询对象（客户/部门/人员）及财务组织不能为空

● 可以按查询的应收范围（全部应收/已确认应收/未确认应收）和单据状态（已生效/已保存/已审核）及币种、起止期联合筛选查询结果。

## e) 应收对账单：

● 应收对账单够查询一定时期内的应收明细记录，查询结果按查询条件中的查询对象汇总、明细同时列示，支持单据联查(如图附 3-1 所示)。

● 可以按查询的应收范围（全部应收/已确认应收/未确认应收）和单据状态（已生效/已保存/已审核）及币种、起止期联合筛选查询结果。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>应收对账单</td><td style='text-align: center; word-wrap: break-word;'>明细联查</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>查询</td><td style='text-align: center; word-wrap: break-word;'>刷新</td><td style='text-align: center; word-wrap: break-word;'>联查单据</td><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>查询对象</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币余额</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>无锡加工厂</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2,500.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>华中公司</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>华东公司</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>118,767.15</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>西安市金龙致尧百货经销部</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-27,881.15</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>西安市金龙致尧百货经销部</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>港币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>50,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>金汇商厦</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>27,064.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>西安物美</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-3,550.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>家乐福总店</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4,662.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>日期</td><td style='text-align: center; word-wrap: break-word;'>客户</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>单据类型</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>单据号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>无锡加工厂</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>期初</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>2011-02-14</td><td style='text-align: center; word-wrap: break-word;'>无锡加工厂</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>应收单</td><td style='text-align: center; word-wrap: break-word;'>D02011042600...</td><td style='text-align: center; word-wrap: break-word;'>5,500.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>本日小计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5,500.00</td><td style='text-align: center; word-wrap: break-word;'>5,500.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>2011-02-15</td><td style='text-align: center; word-wrap: break-word;'>无锡加工厂</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应收债权转移（并出）</td><td style='text-align: center; word-wrap: break-word;'>-3,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>本日小计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-3,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>总计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2,500.00</td></tr></table>

<div style="text-align: center;">图 附录 3-1 应收对账单查询界面示例</div>


## 2 ) 账表

账表分析采用报表控件，以自定义报表分析的模式，通过“订阅-执行-发布”各步骤，可将分析结果推送给指定的操作人员（如图附3-2所示）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_125_251_1048_1264.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 附录 3-2 账表分析设置</div>


账表分析包括客户应收账款分析、客户收款账龄分析、客户应收欠款分析、客户收款预测、应收报警单等，因各类分析的查询条件基本一致，下面以客户应收账款分析为例说明查询条件的应用。

a) 客户应收账款分析：

● 提供根据查询对象按账龄或按日期进行不同角度的应收款账龄分析。

● 分析的查询条件包括：查询对象（由账表初始化预指定）、截止日期、分析模式（按账龄/按日

期）、分析方向（应收-收款）、分析日期（到期日/单据日期/审批日期/生效日期/内控到期日期）、分析方式（最终余额/点余额）、往来对象（客户/部门/业务员）、分析范围（全部应收/已确认应收/未确认应收）、单据状态（全部）已保存/已审核/已生效）、财务组织（支持多选）

● 若分析模式选择按账龄，则弹出‘账龄区间’界面定义账龄区间的显示区间及其显示名称；若分析模式选择按日期，则弹出‘日期区间’界面定义日期区间、显示区间及其显示名称。

● 按最终余额则查询到系统最终处理时的系统处理情况及余额；按点余额则查询到查询日期时的系统处理情况及余额。

b) 客户应收欠款分析：查询查询相关时点某客户的欠款金额，以及欠款组成情况。

c) 客户收款账龄分析：查询按账龄区间或按日期区间为查询条件的收款账龄分析。

d) 客户收款分析：分析在一段时间内的款项回收情况，按款项构成分析或按结算方式分析。

e) 客户收款预测：预测某段期间内将要收到的资金。

f) 应收报警单：是产品提供的对应收款进行报警的功能，可根据报警条件设置来查询已过期或将要到期的往来款项。

## 附录 3：本文参见其他手册清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>手册名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-基础数据》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-流程管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-会计平台》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-欧盟电子支付》</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_492_392_698_542.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform
