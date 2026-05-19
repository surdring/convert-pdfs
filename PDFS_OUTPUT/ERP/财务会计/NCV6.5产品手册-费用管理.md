# NCV6.5产品手册-费用管理

费用管理

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权 ..... 2  
导读 ..... 5  
第一章 概述 ..... 6  
1.1 产品概述 ..... 6  
1.2 产品价值 ..... 7  
第二章 应用场景 ..... 8  
2.1 员工直接报销 ..... 8  
2.1.1 业务描述 ..... 8  
2.1.2 业务流程 ..... 8  
2.1.3 功能清单 ..... 8  
2.1.4 产品解决方案 ..... 9  
2.2 员工借款报销 ..... 10  
2.2.1 业务描述 ..... 10  
2.2.2 业务流程 ..... 10  
2.2.3 功能清单 ..... 10  
2.2.4 产品解决方案 ..... 11  
2.3 供应商或客户报销 ..... 13  
2.3.1 业务描述 ..... 13  
2.3.2 业务流程 ..... 14  
2.3.3 功能清单 ..... 14  
2.3.4 产品解决方案 ..... 14  
2.4 代理报销 ..... 15  
2.4.1 业务描述 ..... 15  
2.4.2 业务流程 ..... 16  
2.4.3 功能清单 ..... 16  
2.4.4 产品解决方案 ..... 17  
2.5 跨组织报销 ..... 18  
2.5.1 业务描述 ..... 18  
2.5.2 业务流程 ..... 19  
2.5.3 功能清单 ..... 19  
2.5.4 产品解决方案 ..... 19  
2.6 先申请再报销 ..... 22  
2.6.1 业务描述 ..... 22  
2.6.2 业务流程 ..... 23  
2.6.3 功能清单 ..... 23  
2.6.4 产品解决方案 ..... 24  
2.7 费用分摊与结转 ..... 34  
2.7.1 业务描述 ..... 34  
2.7.2 业务流程 ..... 36  
2.7.3 功能清单 ..... 36  
2.7.4 产品解决方案 ..... 37  
2.8 委托结算中心付款 ..... 45

2.8.1 业务描述 ..... 45  
2.8.2 业务流程 ..... 45  
2.8.3 功能清单 ..... 46  
2.8.4 产品解决方案 ..... 46  
2.9 费用预提 ..... 47  
2.9.1 业务描述 ..... 47  
2.9.2 业务流程 ..... 48  
2.9.3 功能清单 ..... 48  
2.9.4 产品解决方案 ..... 49  
2.10 报销费用调整 ..... 51  
2.10.1 业务描述 ..... 51  
2.10.2 业务流程 ..... 51  
2.10.3 功能清单 ..... 51  
2.10.4 产品解决方案 ..... 52  
2.11 期末处理 ..... 54  
2.11.1 业务描述 ..... 54  
2.11.2 业务流程 ..... 54  
2.11.3 功能清单 ..... 54  
2.11.4 产品解决方案 ..... 55  
第三章 初始准备 ..... 56  
3.1 参数 ..... 56  
3.2 用户关联人员 ..... 59  
3.3 审批流设置 ..... 60  
3.4 交易类型管理 ..... 62  
3.5 报销类型和费用类设置 ..... 64  
3.6 常用单据设置 ..... 65  
3.7 报销标准设置 ..... 66  
3.7.1 报销标准设置 ..... 66  
3.8 借款控制设置 ..... 68  
3.9 费用预算控制 ..... 70  
3.10 期初单据 ..... 73  
3.11 查询对象注册 ..... 73  
附录 ..... 74  
附录 1：费用管理查询报表 ..... 74  
附录 2：跨组织生成凭证的配置及分析 ..... 75  
附录 3：报销单据多表体打印设置 ..... 94

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供客户业务需求如何与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关费用管理的主要业务场景、流程、以及对应的产品功能的介绍；第三部分介绍了费用管理启用前的初始准备设置；第四部分介绍网上报销产品的概述、应用场景和初始准备。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录进行了汇总，列示为费用管理与网上报销查询报表、跨组织生成凭证的配置及分析，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《产品手册-组织管理》——深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助——针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《产品手册-流程管理》----提供关于交易类型、流程设计工具的应用指导。

4. 《产品手册-基础数据》——可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

## 第一章 概述

### 1.1 产品概述

费用管理支持员工自助报销和授权代理报销，提供对借款、报销费用进行预算、资金计划的控制，提供借款余额、借款和费用明细、费用汇总查询，及借款账龄分析报表，从而强化费用报销管理、提高资金支付效率，降低运营和管理成本。通过提供共享服务模式的跨单位借款、跨单位报销，可满足集团级企业对资金集团管控、有效运用资金的需求。

强化了对费用管理与核算方面的应用，增加了对费用申请、费用分摊与结转、待摊费用摊销等业务的支持，并提供更多的查询统计报告，体现在：可跨多个组织分摊费用（含事后结转）；支持待摊费用处理；提供“费用申请——借款——报销”的费用报销流程，对费用申请环节实现事前控制；在项目预算方面，报销单可受项目预算控制等。

在费用管理中设有费用申请单及借款单、报销单的单据大类，预置了常用的借款报销单据类型及模板，业务人员可自主填报借款单、报销单，由管理人员及财务人员对借款、报销单据进行审核、冲销等后续操作。产品同时还支持共享服务模式的跨单位借款、跨单位报销。

费用管理的解决方案如图 1.1-1 所示，每个企业可以根据自身情况，将费用管理和网上报销结合使用，或者单独使用费用管理模块。

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_156_1076_792.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 1.1-1 费用管理解决方案</div>


### 1.2 产品价值

1. 帮助企业员工基于互联网进行费用报销，简化手工报销方式的繁琐程序。

2. 规范报销流程，提高费用报销透明度。

3.凭证自动生成，减轻财务人员工作量。

4. 网银实时支付，降低库存现金量及出纳人员工作量。

5.彻底解决报销排队情况。

6. 报销人员可以实时查询报销情况及历史记录。

7. 帮助集团中、高层管理人员了解各项费用支出情况，控制各项费用的规模。

8. 通过事项审批和预算控制，完善报销过程管理，实现集团财务的事前控制。

9. 支持待摊费用和跨组织分摊，加强企业财务管理。

## 第二章 应用场景

### 2.1 员工直接报销

#### 2.1.1 业务描述

由业务人员自己登陆 NC 系统或网上报销系统录入单据，完成报销业务的全过程。

#### 2.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_263_592_960_1309.jpg" alt="Image" width="58%" /></div>


#### 2.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>客户化配置</td><td style='text-align: center; word-wrap: break-word;'>模板管理-模板设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>差旅费借款单</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单据管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>网上付款</td></tr></table>

#### 2.1.4 产品解决方案

### 1. 报销人填写差旅费报销单

报销人登录 NC 系统，进入【财务会计】→【费用管理】→【单据录入】→【差旅费报销单】，新增报销单。

### 2. 上级业务经理审批报销单

上级业务经理登录 NC 系统，可以在【消息中心】→【已收到消息】→【工作任务】中看到待审批的任务，可以双击该消息进入单据管理界面，还可以直接进入【财务会计】→【费用管理】→【单据管理】中审批该单据，审批人在单据管理节点可以查询、审批自己有权限审批的报销单据，还可以修改单据信息；同时，还可以联查审批情况。

### 3. 财务经理审核报销单

财务经理登录 NC 系统，同样可以在【消息中心】→【已收到消息】→【工作任务】中看到待审批的任务，双击该消息进入单据管理界面可以修改单据单据，然后审批该单据；系统支持由财务人员在单据管理处进行批量冲销借款。支持按借款报销人进行批冲销，也支持按部门进行批冲销，如图 2.1-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_189_992_1060_1374.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1-1 批量冲借款</div>


### 4. 出纳通过 NC 系统进行结算和网上支付

以出纳的角色登录 NC 系统，进入【资金管理】→【现金管理】→【结算】，可以看到该单据的

状态为“审批通过”，结算状态为“未结算”，出纳可以点击【结算】按钮进行结算，然后进入【资金管理】→【现金管理】→【网上付款】，进行网上支付。

5. 在报销单界面增加影像上传和查看功能，同时可查看网上报账中上传的影像。

### 2.2 员工借款报销

#### 2.2.1 业务描述

费用管理支持在报销时进行冲借款操作，报销人在录入单据时，可以选择是否冲借款。

<div style="text-align: center;"><img src="imgs/img_in_image_box_245_584_869_1175.jpg" alt="Image" width="52%" /></div>


#### 2.2.2 业务流程

员工借款报销的业务流程与员工直接报销的业务流程相同。

#### 2.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>差旅费借款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>还款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单据管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>网上支付</td></tr></table>

#### 2.2.4 产品解决方案

1. 报销人填写报销单时，编辑状态下点击“冲借款”按钮，弹出冲借款处理界面，默认过滤出同币种条件下当前报销人所有已审批未两清的借款单；只支持同币种之间的冲销业务，不支持不同币种之间冲销业务。

1）报销人可以一次冲销多张借款单，还可以对一张借款单通过多次冲销来进行核销，即支持一张借款单对应多张报销单的业务处理。例如图 2.2-1 所示，冲销了 2 张借款单，其中一张借款单只冲销了部分金额。

<div style="text-align: center;"><img src="imgs/img_in_image_box_244_788_1075_1159.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 2.2-1 报销充借款</div>


2）系统支持设置是否允许冲销其他人的借款，由组织级参数[ER6—是否允许冲销其他人的借款]控制，如图2.2-2所示，当该参数设置为“是”时，报销人可冲销自己有代理权限的本单位范围内的其他人的借款，否则报销人只能冲销自己的借款。

<div style="text-align: center;"><img src="imgs/img_in_image_box_234_156_1094_508.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2-2 参数[ER6—是否允许冲销其他人的借款]</div>


3）可以设置是否必须冲借款，由组织级参数[ER7-是否必须冲借款]控制的，如图 2.2-3 所示，当该参数设置为“是”时，当报销人有借款未核销时，系统将提示有借款，如图 2.2-4 所示，要求必须进行冲借款。

<div style="text-align: center;"><img src="imgs/img_in_image_box_235_714_1082_1080.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.2-3 参数[ER7-是否必须冲借款]</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_420_1134_897_1405.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">图 2.2-4 必须冲借款提示</div>


2. 在冲报销单据的冲销明细页签可以查看冲销记录，如图 2.2-5 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_155_1085_479.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.2-5 报销单的冲销明细页签</div>


同时在借款单据的冲销明细页签也可以查看冲销记录，如图 2.2-6 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_199_593_1073_922.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.2-6 借款单的冲销明细页签</div>


3. 可以将全部报销金额用来冲销借款，也可以只将部分报销金额用来冲销借款，当报销单金额只冲销了一部分借款金额，就需要通过填写还款单将剩余借款还清。还款单是一种特殊的报销业务，填写还款单时其表体不可编辑，只能通过冲借款进行还款。一笔借款可以通过填写多张还款单完成还款。

4. 借款单收款信息下的栏位“对公支付”改为“收款对象”，可选择的收款对象为“客户”、“供应商”、“员工”，借款单支持对客户、供应商、员工的支付，但只支持对一个客户、供应商、员工的支付。

### 2.3 供应商或客户报销

#### 2.3.1 业务描述

个人报销时要实现对公支付的功能。

#### 2.3.2 业务流程

供应商或客户报销的业务流程与员工直接报销的业务流程相同。

#### 2.3.3 功能清单

供应商或客户报销的功能清单与员工直接报销的功能清单相同。

#### 2.3.4 产品解决方案

1. 报销人填写报销单时，收款对象选择供应商或客户，并填写供应商或客户字段、客商银行账户信息，如图 2.3-1，图 2.3-2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_646_1065_1100.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.3-1 对客户支付</div>


<div style="text-align: center;">图 2.3-2 对供应商支付</div>


2. 当各级人员审批后，出纳结算时，可以看到供应商的账户信息，如图 2.3-2、图 2.3-3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_195_1226_1086_1418.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.3-3 供应商账户信息</div>


<div style="text-align: center;">图 2.3-4 客户账户信息</div>


3. 报销单支持一张单据支付多个员工、客户、供应商。

1）通过在【动态建模平台】→【客户化配置】→【模板管理】→【模板设置】中将表体收款对象、供应商、客户、收款人及其收款账户信息显示，实现一张报销单支付多个员工和客户、供应商的报销。

2）借款单不支持支付多个员工、客户、供应商。

### 2.4 代理报销

#### 2.4.1 业务描述

报销员工委托他人登陆 NC 系统录入借款报销单据，完成借款报销业务的全过程。费用管理支持助理代理报销和临时个人授权代理报销。

针对领导和不具备全员报销条件的企业，支持通过授权代理设置助理，代理领导和员工进行报销单据录入。系统支持按角色进行助理设置，方便代理授权；同时提供代理部门、代理所有人员的便捷设置。

针对个人临时授权，支持设置在特定的时间范围内，由其他人员代理自己进行具体交易类型的报销单据录入。

#### 2.4.2 业务流程


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">代理报销流程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销人</td><td style='text-align: center; word-wrap: break-word;'>助理</td><td style='text-align: center; word-wrap: break-word;'>上级经理</td><td style='text-align: center; word-wrap: break-word;'>财务人员</td><td style='text-align: center; word-wrap: break-word;'>出纳</td></tr><tr><td rowspan="6">填写纸质借款单/报销单</td><td style='text-align: center; word-wrap: break-word;'>填写电子借款单/报销单</td><td style='text-align: center; word-wrap: break-word;'>审批</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>N</td><td style='text-align: center; word-wrap: break-word;'>是否通过</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>打印单据/粘贴原始单据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>审批</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>结算</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>网上付款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

#### 2.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>授权代理设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>个人授权设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>差旅费借款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单据管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>网上付款</td></tr></table>

#### 2.4.4 产品解决方案

代理借款/报销的审批流程与全员代理借款/报销的业务流程基本相同，只是流程的发起者，即借款单/报销单的填报人不是报销人本身，而是其所委托的代理人。

系统支持 2 种代理设置方式：一种是通过【财务会计】->【报销设置】->【初始设置】->【授权代理设置】，用于管理员为业务员设置代替其录入业务单据的角色，并且支持跨业务单元之间的授权代理；一种通过【财务会计】->【报销设置】->【初始设置】->【个人授权设置-集团】，针对个人临时授权，支持设置在特定的时间范围内，由其他人员代理自己进行指定交易类型的报销单据录入。

### 1. 【授权代理设置】

1) 被代理人可以设置为具体的业务员。

2）也可按照部门来设置，即代理人可以代理一个部门所有的业务员。

3) 如果对应的角色选中了“代理本部门”，则表明角色中的每个操作员都可以为自己所在部门的所有人代理录入单据，但这个“本部门”不包括其下级部门，即不能为部门的下级部门代理录入单据。

4）还可以设置代理所有人，所有人指操作员所属单位的所有人员。

步骤 1：以管理员的身份登录 NC，授权报销助理角色可以代理某几个业务员，还可以代理总裁室部门的业务员和本部门的业务员进行报销业务，如图 2.4-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_971_1113_1427.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.4-1 授权代理设置</div>


步骤 2：在员工直接报销模式下，报销人只能录入自己的借款/报销单据。在代理报销模式下，设置了

代理权限时，代理人可以录入自己的及其代理的业务员的借款/报销单据。即，当报销助理角色所对应的用户录入借款单时，“借款人”字段可以参照到自己和其代理的业务员；代理人录入报销单时，“报销人”字段也可以参照到自己和其代理的业务员。

### 2. 【个人授权设置】

用于业务员为自己设置临时代其录入单据的其他用户，一般由业务员自己设置，下面举例说明。

步骤 1：以报销人身份授权代理人可以为其进行“差旅费报销单”的操作，如图 2.4-2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_455_1028_652.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.4-2 个人授权设置</div>


步骤 2：当代理人登录，进入差旅费报销单录入单据时，可以看到报销人一项除了能够选择自己，还可以选择被代理人，即报销人可以为自己和其被代理人进行差旅费报销的业务，如图 2.4-3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_821_1115_1170.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.4-3 差旅费报销单一报销人选择</div>


### 2.5 跨组织报销

#### 2.5.1 业务描述

报销人单位与费用承担单位不同情况下的一种报销业务，如业务员在 A 单位报销，由 A 单位为其支付

报销款项，但费用却由另一分单位 B 来承担。同样，费用管理支持跨组织借款，与跨组织报销的应用相同。

#### 2.5.2 业务流程

<div style="text-align: center;">跨组织报销流程</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>报销人</td><td style='text-align: center; word-wrap: break-word;'>上级管理者</td><td style='text-align: center; word-wrap: break-word;'>承担单位管理者</td><td style='text-align: center; word-wrap: break-word;'>财务人员</td><td style='text-align: center; word-wrap: break-word;'>出纳</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>填写报销单/借款单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>审批</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>是否通过</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>打印单据/贴原始单据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>网上付款</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>审批</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

#### 2.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>差旅费借款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单据管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应收管理</td><td style='text-align: center; word-wrap: break-word;'>应收单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付管理</td><td style='text-align: center; word-wrap: break-word;'>应付单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>结算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>网上支付</td></tr></table>

#### 2.5.4 产品解决方案

1. 报销人填写差旅费报销单，注意其费用支付单位和报销单位不同，如图 2.5-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_188_148_1094_638.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2.5-1 跨组织报销单</div>


2. 上级业务经理审批报销单。

3. 费用承担单位的负责人审批报销单。

4. 财务人员审核报销单。

5. 如果需要生成应收应付单，需将费用管理的参数[ER2-是否生成往来单据]设置为“是”，如图 2.5-2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_209_933_1066_1299.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.5-2 参数[ER2-是否生成往来单据]</div>


则报销单生效后系统会自动生成支付单位和报销单位间应收应付单，点击【联查-联查往来单】可查询到报销单位的应付单、支付单位的应收单，若会计平台预置好了责任凭证模板，还可联查到费用承担单位的责任凭证。如图 2.5-3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_156_1083_663.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_687_1083_1201.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.5-3 应收单管理</div>


同时报销单位的财务人员进入【财务会计】→【应付管理】→【应付日常业务】→【应付单管理】，可以看到该报销单推式生成的应付单，如图 2.5-4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_104_154_1084_546.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.5-4 应付单管理</div>


6. 如果需要生成凭证，需将费用管理的参数[ER2-是否生成往来单据]设置为“否”。（注意：是否生成凭证是由会计平台的平台设置来设置是否生成的。）

7. 出纳通过 NC 系统进行结算和网上支付。

### 2.6 先申请再报销

#### 2.6.1 业务描述

● 企业为达到费用事前控制的目的，要求在办理某些业务（如出差、营销活动）报销之前需先申请才能办理。

企业在年初只是做了一个大概的全面预算，在具体业务培训时，需每次申请明细的费用额度。

企业做的全面预算或费用预算中未包括的费用，需要另行申请。

#### 2.6.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_208_238_949_821.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6.2-01 费用申请单流程</div>


#### 2.6.3 功能清单

下表所列为完成费用申请主业务流程所涉及的功能节点，相关的初始准备设置（如审批流、报销标准、组织架构及人员角色权限等）不含在内，可参见第3章初始准备的内容。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">企业绩效管理</td><td rowspan="2">全面预算管理</td><td style='text-align: center; word-wrap: break-word;'>预算编制-预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算监控-控制方案</td></tr><tr><td rowspan="6">财务会计</td><td rowspan="6">费用管理</td><td style='text-align: center; word-wrap: break-word;'>初始设置-费用申请控制规则设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用申请单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用申请单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差旅费借款单/会议费借款单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差旅费报销单/差旅费报销单/交通费报销单/通讯费报销单/礼品费报销单/招待费报销单/会议费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>初始设置-期初余额</td></tr></table>

#### 2.6.4 产品解决方案

## 系统的解决方案思路：

为保证报销流程的正常使用，审批流程、代理权限、借款控制规则、合计平台设置等应提前设置好（本场景方案中不单独说明）。

● 申请人在借款/报销前先填写费用申请，经各级审批后生效。

若费用承担跨部门，须由费用承担部门负责人先确认后再传递至下一环节审批。

经最终审批生效的费用申请单可供控制规则所指定的借款单/报销单调用，并控制费用。

● 报销单引用了费用申请金额将回写费用申请单，费用申请单耗尽余额或到期后关闭，需重新进行费用申请。

● 费用申请单可单独控制业务类单据，也可受预算约束后控制业务单据。

## 解决方案步骤：

1. 设定费用控制规则：

【财务会计】→【费用管理】→【初始设置】→【费用申请控制规则设置】节点中，按财务组织定义控制规则，确定费用申请单的控制维度和控制对象。可设置集团级控制规则，也可按组织设置控制规则。集团与组织控制规则同时存在时，按组织控制规则进行控制。

● 控制维度：指可控制的维度层面组合，不为空：

可设置包括申请部门、费用承担部门、费用申请单明细项（包含成本中心、收支项目、项目、项目任务、客户、供应商、自定义项等），控制维度的成员取值于建模中的业务单元、部门、基础数据等节点中的已设置对象。

可以按费用申请单交易类型设置控制规则，每个费用申请单交易类型只能设置一个控制规则。

➢费用申请单、借款单、报销单默认维度对照关系如下表：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>费用申请单</td><td style='text-align: center; word-wrap: break-word;'>借款单</td><td style='text-align: center; word-wrap: break-word;'>报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>申请部门（表头）</td><td style='text-align: center; word-wrap: break-word;'>费用承担部门（表头）</td><td style='text-align: center; word-wrap: break-word;'>费用承担部门（表头）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用承担部门（表头）</td><td style='text-align: center; word-wrap: break-word;'>费用承担部门（表头）</td><td style='text-align: center; word-wrap: break-word;'>费用承担部门（表头）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>成本中心（表体）</td><td style='text-align: center; word-wrap: break-word;'>成本中心（表头）</td><td style='text-align: center; word-wrap: break-word;'>成本中心（表头）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收支项目（表体）</td><td style='text-align: center; word-wrap: break-word;'>收支项目（表体）</td><td style='text-align: center; word-wrap: break-word;'>收支项目（表体）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目（表体）</td><td style='text-align: center; word-wrap: break-word;'>项目（表体）</td><td style='text-align: center; word-wrap: break-word;'>项目（表体）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目任务（表体）</td><td style='text-align: center; word-wrap: break-word;'>项目任务（表体）</td><td style='text-align: center; word-wrap: break-word;'>项目任务（表体）</td></tr></table>

➢费用申请单若关联了报销业务单据，则必须关闭该申请单后才能新增控制维度。

➢费用申请单控制借款单、报销单时，调用的是费用申请单主组织的控制规则。

➢设有多个控制维度时，可设置各控制维度间是否可调剂，调剂规则为：

✓ 勾选了“可调剂”时，则该控制维度不作严格控制，即当第一条金额有余额时，该余额可调剂给下一条，当第一条金额不足时，也可调剂使用下一条的金额，直至最后一条可用余额不够时，才严格控制不予通过。

✓ 不勾选“可调剂”时，则按对应的控制维度严格控制。

✓ 当费用申请单在表头中勾选了“可调剂”，则费用申请单所控制的业务单据金额超出申请金额时，可按控制维度中设置为可调制的维度进行调剂。

✓ 当费用申请单在表头中未勾选 “可调剂”，则费用申请单控制的单据金额超出申请金额时，无论控制维度中是否设置有可调剂的维度，都不能在当前费用申请单的控制维度之间进行调剂。

✓ 费用申请单表头的“可调剂”字段在默认模板中设置为不显示，默认为勾选状态，实际业务中有严格控制要求时，可在实施中调整该模板的显示及取值。

● 控制对象：可控制对象包括借款单和各类报销单，支持到交易类型。

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_769_1085_1143.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.6.4-01 费用申请控制规则定义</div>


2. 填制、审批费用申请单：

【财务会计】→【费用管理】→【费用申请】→【费用申请单录入】→【费用申请单】\【费用申请单管理】节点中，按财务组织新增费用申请单，经提交、审批（【费用申请单管理】节点）等环节后使之生效：

☑ 费用申请单一张申请单可填写多个费用承担单位和费用承担部门，占用多个组织/部门的预算。

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_153_1086_734.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-02 费用申请单填写多个费用承担单位和费用承担部门</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_109_793_1084_1193.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-03 费用申请单占用多个费用承担单位和费用承担部门预算</div>


费用申请单一张申请单可填写多个利润中心和成本中心，如图 2.6.4-02，生成多个利润中心的责任凭证。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>责任核算账簿</td><td style='text-align: center; word-wrap: break-word;'>责任凭证类别</td><td style='text-align: center; word-wrap: break-word;'>凭证号</td><td style='text-align: center; word-wrap: break-word;'>制单日期</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团总公司-基准账簿</td><td style='text-align: center; word-wrap: break-word;'>责任凭证</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2014-01-17</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>无锡宏远工厂-基准账簿</td><td style='text-align: center; word-wrap: break-word;'>责任凭证</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2014-01-17</td></tr></table>

<div style="text-align: center;">图 2.6.4-04 费用申请单生成多个利润中心责任凭证</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_151_195_1125_464.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-05 费用申请单生成的责任凭证</div>


● 费用申请单的执行数和余额：已生效的费用申请单被报销单调用时，由报销单回写执行数，系统自动计算出当前申请单的余额。

☑ 费用申请单提供关闭功能：

当报销单执行完成自动关闭（余额为0）时自动关闭，报销单反生效则自动重启费用申请单。

余额不为 0 且未到期时，可由用户手工执行〖关闭〗，关闭后不再提供给借款单或报销单进行参照。

✓ 有执行的单据未生效时，费用申请单可关闭，执行单据在生效时系统提示“费用申请单 XXX 已关闭”。

✓ 已关闭的费用申请单，执行的单据不可反生效，由系统提示“费用申请单 XXX 已经关闭”后返回。

➢ 超期自动关闭：

✓ 系统日期等于原填写的自动关闭日期时，自动关闭已审批通过的整张费用申请单。

✓ 到期自动关闭时，关闭人取“系统用户”。

● 费用申请单可受预算控制（具体实现方式可参见《NCV6.33 产品手册-全面预算》），若受预算控制，则：

➢ 生效时回写预算执行数，关闭时释放所占用且未执行的预算。

关闭后可重启，重启检查预算情况，预算有余额则重新占用预算，无预算余额则不能重启。

➢ 费用申请单关联了预算时可执行〖联查-联查预算〗查看预算的占用、执行情况。

● 费用申请单若被报销单引用，则可点击【联查-联查单据】查阅当前申请单的后续执行情况，追溯到具体的报销单。

● 费用申请单支持审批流配置，可按审批流规范进行【提交-提交/收回】、【审批-审批/取消审批】等操作，使费用申请单通过审批生效。

<div style="text-align: center;"><img src="imgs/img_in_image_box_106_107_1089_612.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.6.4-06 费用申请单</div>


3. 填制、审批借款单/报销单：

【财务会计】→【费用管理】→【单据录入】→【会议费借款单】或【财务会计】→【费用管理】→【单据录入】→【单据管理】节点中，参照费用申请单新增报销单，例如会议费借款单或会议费报销单：

新增受费用控制规则约束的借款单或报销单时，可参照选择到已生效的费用申请单，在所选费用申请单的可用金额范围内，形成借款单或报销单，如图2.6.4-03、图2.6.4-04所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_106_896_1085_1303.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.6.4-07 参照费用申请单形成借款单-1</div>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="13">费用申请单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务组织</td><td style='text-align: center; word-wrap: break-word;'>交易类型</td><td style='text-align: center; word-wrap: break-word;'>单据日期</td><td style='text-align: center; word-wrap: break-word;'>单据编号</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>金额</td><td style='text-align: center; word-wrap: break-word;'>执行数</td><td style='text-align: center; word-wrap: break-word;'>余额</td><td style='text-align: center; word-wrap: break-word;'>事由</td><td style='text-align: center; word-wrap: break-word;'>申请部门</td><td style='text-align: center; word-wrap: break-word;'>申请人</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>无锡宏远工厂</td><td style='text-align: center; word-wrap: break-word;'>费用申请单</td><td style='text-align: center; word-wrap: break-word;'>2013-08-21</td><td style='text-align: center; word-wrap: break-word;'>261X201308210002</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>20,000.00</td><td style='text-align: center; word-wrap: break-word;'>0.00</td><td style='text-align: center; word-wrap: break-word;'>20,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>行政部</td><td style='text-align: center; word-wrap: break-word;'>马超</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>无锡宏远工厂</td><td style='text-align: center; word-wrap: break-word;'>费用申请单</td><td style='text-align: center; word-wrap: break-word;'>2013-08-02</td><td style='text-align: center; word-wrap: break-word;'>261X201308210001</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>20,000.00</td><td style='text-align: center; word-wrap: break-word;'>0.00</td><td style='text-align: center; word-wrap: break-word;'>20,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>行政部</td><td style='text-align: center; word-wrap: break-word;'>马超</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>无锡宏远工厂</td><td style='text-align: center; word-wrap: break-word;'>费用申请单</td><td style='text-align: center; word-wrap: break-word;'>2013-08-01</td><td style='text-align: center; word-wrap: break-word;'>261X201308300005</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>20,000.00</td><td style='text-align: center; word-wrap: break-word;'>16,700.00</td><td style='text-align: center; word-wrap: break-word;'>3,300.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>行政部</td><td style='text-align: center; word-wrap: break-word;'>马超</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.6.4-08 参照费用申请单形成借款单-2</div>


新增借款单/报销单时，可参照的费用控制单需满足如下条件：

✓ 只能对照本组织的申请单。

✓ 业务单据类型在费用控制单所对应控制规则的控制对象内。

✓ 查询出的是报销人自己的或有代理权限人员的费用申请单。

✓ 对应财务组织的费用控制单已生效、余额大于 0 且未关闭。

➢参照费用申请单生成的借款单，按借款单表体行受费用申请单表体行控制。

参照费用申请单生成的报销单，可维护报销单表体行，但控制维度的项目不能超出费用申请单的维度项目范围。

➢参照费用申请单生成的借款单/报销单，遵照如下规则：

✓ 携带费用申请单号进行关联，此时报销单和费用申请单均可通过【联查-联查单据】来查询到对应的上下游单据。

✓ 参照表体填写多个费用承担单位、费用承担部门的费用申请单生成的报销单，生成带分摊的报销单，如图 2.6.4-09 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_154_1085_730.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-09 参照分摊的费用申请单生成分摊的报销单</div>


✓ 受费用申请单控制，单据审批时检查报销单的金额不能超出所选费用申请单的可用余额，否则系统提示“单据金额超过申请的费用余额，请修改金额或重新申请”，如图 2.6.4-10 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_889_1088_1370.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.6.4-10 引用费用申请单的业务单据不得超出费用申请单余额</div>


✓ 【动态建模平台】→【流程管理】→【交易类型设置】节点中，在费用申请单交易类型上“允许报销百分比”为120%时，报销单的金额可以超出申请单20%。允许超出的百分比可设置，

设置后，按申请单上的最大允许报销金额控制报销单。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>交易类型管理</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.6.4-11 费用申请单交易类型上设置允许报销百分比</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_109_717_1083_1294.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-12 费用申请单上计算出最大允许报销金额</div>


✓ 根据【建模平台】→【基础数据】→【参数】→【业务参数设置-组织】节点中参数“ER11 费用申请单控制环节”的取值，将执行情况回写到费用申请单冲抵余额，如图2.6.4-13--2.6.4-16所示为报销单保存即回写的数据示例。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_162_1086_224.jpg" alt="Image" width="82%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>系统选择</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>组名称</td><td style='text-align: center; word-wrap: break-word;'>参数代码</td><td style='text-align: center; word-wrap: break-word;'>参数名称</td><td style='text-align: center; word-wrap: break-word;'>参数值</td><td style='text-align: center; word-wrap: break-word;'>控制下级</td><td style='text-align: center; word-wrap: break-word;'>取值范围</td><td style='text-align: center; word-wrap: break-word;'>注释</td><td style='text-align: center; word-wrap: break-word;'>最后</td></tr><tr><td rowspan="4">公共参数动态企业建模Web应用平台集成平台</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER11</td><td style='text-align: center; word-wrap: break-word;'>费用申请单控制环节</td><td style='text-align: center; word-wrap: break-word;'>保存</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>I, 保存, 审批 (生效)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER12</td><td style='text-align: center; word-wrap: break-word;'>总账关账是否检查本...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER9</td><td style='text-align: center; word-wrap: break-word;'>截止到本月单据全部生效 不检查</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>I, 不检查, 检查但不控制...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>zyada</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER4</td><td style='text-align: center; word-wrap: break-word;'>财务核报答差范围</td><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>zyada</td></tr><tr><td rowspan="3">应用管理平台企业绩效管理财务基础档案及规则</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ERS</td><td style='text-align: center; word-wrap: break-word;'>还款期限 (单位: 天)</td><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>zyada</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ERS</td><td style='text-align: center; word-wrap: break-word;'>是否允许冲销其他人...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>zyada</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER7</td><td style='text-align: center; word-wrap: break-word;'>是否必须冲销款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>zyada</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账应收管理应付管理费用管理固定资产存货核算税务管理费用预查</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER7</td><td style='text-align: center; word-wrap: break-word;'>费用申请单控制环节</td><td style='text-align: center; word-wrap: break-word;'>保存</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>ER7</td><td style='text-align: center; word-wrap: break-word;'>费用申请单控制环节</td><td style='text-align: center; word-wrap: break-word;'>保存</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.6.4-13 费用申请单控制环节参数配置</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_634_1083_1039.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-14 费用申请单联查单据</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_107_1099_1085_1445.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.6.4-15 费用申请单联查报销单</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_104_156_1085_506.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.6.4-16 费用申请单联查报销单</div>


注意：为方便结算支付，借款/报销单在提交审批前必须选定单位账户或个人账户，且该账户应通过期初复核。

## ● 借款单、报销单可设置是否必须的申请

➢【动态建模平台】→【流程管理】→【交易类型设置】节点中，在借款单、报销单交易类型上勾选“必须申请”，填写借款单、报销单只能通过参照申请单生成。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_810_1082_1261.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-17 差旅费报销单交易类型上勾选“必须申请”</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_157_1084_757.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.6.4-18 勾选 “必须申请” 的报销单只能参照申请单生成</div>


### 2.7 费用分摊与结转

#### 2.7.1 业务描述

● 费用管理涉及的费用分摊与结转业务常见于：

多部门为同一任务出差，回来后由某一部门发起的出差费用报销，应分摊到出差的各部门，由各部门负责人会签完成审批，各部门按应承担的费用进行预算控制。

➢ 总部统一支付的费用（如办公楼租金、物业管理费、坐席费、交易卫星通讯费等），需按各使用部门（或单位）占用面积进行计算和分摊。

集中支付模式下，总部为分支机构垫付费用后，需要摊销到各考核机构。

采购部门统一采购，各业务部门按需进行领用模式下，需定期按各部门领用情况将低值易耗品的费用核算到各业务部门。

● 从具体业务实现过程要求来看，费用的分摊与结转可分为分摊与待摊：

分摊：需多个部门分摊费用的业务报销单据（如物业管理费、水电费、低值易耗品、代垫费用等），

由某个部门统一的业务员统一报销，各部门负责人同时确认，各部门分别进行预算控制，生成一张或各单位的多张核算凭证。

✓ 业务员报销时若已明确各部门、各单位应该承担的费用金额，则直接在报销单上进行分摊。

✓ 业务员报销时不清楚如何分摊，则在报销后由财务人员根据业务部门提供的分摊表进行分摊（费用结转）。

待摊：业务人员报销时不清楚要否分期摊销，由财务核算人员指定如何摊销，其常见业务包括：

✓ 低值易耗品摊销。

✓ 预付保险费。

✓ 一次性购买印花税票和一次性购买印花税税额较大需分摊的数额。

✓ 经营租赁的预付租金、预报刊杂志费等。

✓ 固定资产修理费用。

● 已执行摊销可以取消，修改后可重新摊销。

#### 2.7.2 业务流程

〈流程名称〉

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_260_1075_1074.jpg" alt="Image" width="81%" /></div>


#### 2.7.3 功能清单

下表所列为完成费用分摊与结转业务场景流程所涉及的主要功能节点，相关的初始准备设置（如审批流、报销标准、组织架构及人员角色权限等）及期末处理、账表查询暂不包含，可参见第 3 章初始准备的内容。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">企业绩效管理</td><td rowspan="2">全面预算</td><td style='text-align: center; word-wrap: break-word;'>预算编制-预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算监控-控制方案</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">费用管理</td><td style='text-align: center; word-wrap: break-word;'>初始设置-分摊规则设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>初始设置-分摊结转单据对应设置-集团/组织</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="4"></td><td rowspan="4"></td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单/会议费借款单/差旅费报销单/交通费报销单/通讯费报销单/礼品费报销单/招待费报销单/会议费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用核算-费用结转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用核算-待摊费用摊销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>现金管理</td><td style='text-align: center; word-wrap: break-word;'>初始设置-期初余额</td></tr></table>

#### 2.7.4 产品解决方案

## 解决方案思路：

● 报销业务开始前定义好分摊规则，以便业务员报销时调用。

若费用结转单存在多种交易类型，则应设置费用结转单据和业务单据的对应关系，以方便业务单据和结转单据间的数据对应。

● 业务员申请报销时，若确知要否分摊和分摊对象、要否分期摊销，则可直接指定执行快速分摊，此时由系统自动据业务申请单推式生成费用结转单；若不清楚分摊、摊销事项，则由费用会计后续处理。

● 费用会计在审批业务报销单时，应判定是否分期摊销：

若需分期则先修改待摊标志及摊销期后再完成审批。

若不需分期，则事后根据已生效的业务报销单进行费用结转。

无论是费用结转还是跨期摊销，均回写业务报销单，释放其原占预算。

## 解决方案步骤：

### 1. 定义分摊规则

【财务会计】→【费用管理】→【初始设置】→【分摊规则设置-集团】/【分摊规则设置-组织】节点中，选择财务组织（若集团级定义则不选）后定义分摊规则。

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_150_1084_606.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.7.4-01 费用分摊规则定义</div>


## ☑ 分摊对象：

➢ 集团级节点参照到的分摊对象值为对应的集团级档案；组织级节点参照到的分摊对值为集团+组织级档。

分摊对象可多选，所选分摊对象的顺序与分摊规则列的顺序一致。

可选分摊对象由各产品模块的元数据供选择，系统默认的选择项包括：承担单位、承担部门、利润中心、成本中心、收支项目、项目、项目任务、核算要素、客户、供应商等。

分摊方式：可选择平均分摊、按比例分摊、按金额分摊，系统默认按比例分摊。平均分摊时只需列示分摊对象值；按比例分摊时各分摊对象的比例之和必须为 100%；按金额分摊则需列示各分摊对象值所分摊的金额。

### 2. 定义分摊结转单据对应设置

● 若设有多个费用结转单的交易类型时，则需在【财务会计】→【费用管理】→【初始设置】→【分摊结转单据对应设置-集团】/【分摊结转单据对应设置-组织】节点中提前设置好新增结转单的对应设置，否则：

系统将按预置的默认对应设置进行分摊结转。

若系统预置的分摊对应设置记录被删除，则系统将提示“该报销单交易类型未设置对应的费用结转交易类型”。

若集团和组织对同一业务类型的报销单所设置的结转单对应类型不一致时，各财务组织在结转时以组织设置的为准，如图 2.7.4-02 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>交易类型管理</td><td style='text-align: center; word-wrap: break-word;'>分摊结转单据对应设置-组织</td><td style='text-align: center; word-wrap: break-word;'>会议费报销单</td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'>☑</td></tr><tr><td colspan="5">新增 修改 删除 刷新</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务组织①） 无锡宏远工厂</td><td colspan="4">Q</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>来源交易类型</td><td style='text-align: center; word-wrap: break-word;'>目标交易类型</td><td style='text-align: center; word-wrap: break-word;'>所属组织</td><td style='text-align: center; word-wrap: break-word;'>所属集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1 交通费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2 差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3 会议费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4 礼品费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5 招待费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6 通讯费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7 会议费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单_def1</td><td style='text-align: center; word-wrap: break-word;'>无锡宏远工厂</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_757_1045_1160.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">2.7.4-02 分摊结转单据对应设置</div>


### 3. 报销时分摊费用

## 1 ）直接执行快速分摊：

【财务会计】→【费用管理】→【单据录入】→【差旅费报销单】/【交通费报销单】/【通讯费报销单】/【礼品费报销单】/【招待费报销单】/【会议费报销单】节点或【财务会计】→【费用管理】→【单据管理】节点中，直接执行分摊：

● 报销单录入时，点击【快速分摊】直接选择分摊规则进行分摊,分摊完成后报销单自动增加列示“费用分摊明细”页签，并打上分摊标志,如图2.7.4-03、2.7.4-04所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_111_151_1086_607.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.7.4-03 业务报销单直接分摊 1</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_109_677_1082_1178.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.7.4-04 业务报销单直接分摊 2</div>


● 报销单在执行快速分摊保存后，在【财务会计】→【费用管理】→【费用核算】→【费用结算】节点可查到该单据，并标示来源方式为“报销单生成”，如图 2.7.4-05、图 2.7.4-06 所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>单据管理</td><td style='text-align: center; word-wrap: break-word;'>费用结转</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.7.4-05 业务报销单直接分摊 3</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_109_710_1086_1210.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.7.4-06 业务报销单直接分摊 4</div>


## 2 ）事后结转实现分摊：

● 【财务会计】→【费用管理】→【费用核算】→【费用结转】节点中，点击【新增】，选择已签字生效的报销单进行确认：如图 2.7.4-07 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_149_1085_456.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.7.4-07 事后分摊-选择业务报销单</div>


● 选择报销单后，可选择【快速分摊】，也可手工增加各分摊行，选择分摊对象，调整分摊金额后保存：如图 2.7.4-08 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_603_1086_1128.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.7.4-08 事后分摊-费用结转操作</div>


新增结转单业务报销单时，系统默认查询条件中的“是否标记分摊”的默认取值为“是”，需清空或置为“否”。

● 选定待分摊的报销单后，系统自动将报销单的表头相关信息带入结转单表头，带入的信息不能修改，对应关系如下表所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>费用结转单（表头）</td><td style='text-align: center; word-wrap: break-word;'>报销单（表头）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销单单据编号</td><td style='text-align: center; word-wrap: break-word;'>单据编号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销金额</td><td style='text-align: center; word-wrap: break-word;'>合计金额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用承担单位</td><td style='text-align: center; word-wrap: break-word;'>费用承担单位</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>费用承担部门</td><td style='text-align: center; word-wrap: break-word;'>费用承担部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>成本中心</td><td style='text-align: center; word-wrap: break-word;'>成本中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>利润中心</td><td style='text-align: center; word-wrap: break-word;'>利润中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核算要素</td><td style='text-align: center; word-wrap: break-word;'>核算要素</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收支项目</td><td style='text-align: center; word-wrap: break-word;'>收支项目</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户</td><td style='text-align: center; word-wrap: break-word;'>客户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>供应商</td><td style='text-align: center; word-wrap: break-word;'>供应商</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销人单位</td><td style='text-align: center; word-wrap: break-word;'>报销人单位</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销人部门</td><td style='text-align: center; word-wrap: break-word;'>报销人部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销人</td><td style='text-align: center; word-wrap: break-word;'>报销人</td></tr></table>

● 可由财务人员手工增行录入分摊数据，按费用承担单位、费用承担部门、收支项目进行分摊。

● 已保存费用结转单的确认：

不支持审批流，节点中提供【审批-审批/取消审批】按钮，用于录入费用结转单以外的其他人员（如财务经理）来检查录入的费用结转单是否正确。

审批通过后传会计平台，按预置好的凭证转换模板，生成表体各费用承担单位的总账凭证和利润中心的责任凭证。

审批后的费用结转单不允许修改，要修改须先取消审批；取消审批时相应地删除原生成的凭证。

跨单位结转不支持转往来，只支持生成多单位的凭证。

● 费用结转时，按结转后的费用承担单位、费用承担部门(成本中心)进行预算占用，同时需释放报销时占用的预算。

☑ 约束规则

只能已生效报销单进行关联；

只能查询出当前费用承担单位的报销单进行费用结转；

一张费用结转单只允许关联一张报销单，一张报销单也只能被一张费用结转单关联；

已经结转的报销单不能反生效，一张报销单不能多次结转，一张报销单必须全额结转。

费用结转时释放原报销时所占预算，按费用结转后的结转信息占用预算；若报销与费用结转在不同会计期间，则报销单释放报销会计期间的预算，费用结转单占用费用结转所在会计期间的预算。

➢ 费用结转单不受预算控制，只回写预算执行数。

### 4. 分期摊销

1）【财务会计】→【费用管理】→【单据录入】→【差旅费报销单】/【交通费报销单】/【通讯费报销单】/【礼品费报销单】/【招待费报销单】/【会议费报销单】节点或【财务会计】→【费用管理】→【单据管理】节点中，填制报销单。

2）【财务会计】→【费用管理】→【单据管理】节点或主界面的【常用功能】→【工作任务】中选择待审

批的报销单(若当前操作员处在审批环节)，打开对应单据修改报销单的待摊属性，如图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_205_1086_625.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.7.4-09 事后待摊-待摊及摊销期确认</div>


3）【财务会计】→【费用管理】→【费用核算】→【待摊费用摊销】节点中，点击【刷新】，则系统自动弹出待摊销的业务单据，选中行记录后点击【摊销】即完成当前期间的分摊，如图 2.7.4-010 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_778_1085_959.jpg" alt="Image" width="82%" /></div>


#### 图 2.7.4-010 待摊费用摊销

## ☑ 分期摊销实现规则：

开始摊销的会计期间默认为当前会计期间，可修改为当前期以后的会计期间；会计期间取报销单位对应业务单元的会计期间，跨单位分摊时要求各单位会计期间方案一致；

在各类业务报销单中可在单据填写或财务审批环节设定“摊销”属性，并进而指定摊销期；

同一会计期间的摊销采用覆盖式摊销；

➢ 标示为“待摊”时释放预算，每会计期摊销时占用预算，回写预算执行数；

不支持同一张报销单既做事后结转，又做跨期摊销；

开始摊销会计期间起，在摊销期内，各会计期间都必须按序摊销，但已经分摊的报销单可在执行分期摊销后向后修改摊销期间。

● 已执行摊销的取消办法：

➢ 【待摊费用摊销】节点，增加按钮【取消摊销】按钮；支持取消最后一次已执行的摊销，允许从当前会计期依次向前取消摊销，可通过业务日期切换会计期间。

➢ 已生成摊销凭证的，需删除摊销凭证。如已生成正式凭证，需手工删除凭证后再取消摊销执；会计期间已关账的，允许取消摊销；会计期间已结账的，不允许取消摊销，取消摊销后，已回写的预算数和摊销情况恢复为摊销前的状态。

### 2.8 委托结算中心付款

#### 2.8.1 业务描述

企业成员单位在无权对外支付或没有对外银行账户的情况下，可委托结算中心，通过结算中心进行付款。借款单、报销单支持生成委托付款书，委托结算中心支付。

#### 2.8.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_111_821_898_1475.jpg" alt="Image" width="66%" /></div>

#### 2.8.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">动态建模平台</td><td rowspan="3">流程管理</td><td style='text-align: center; word-wrap: break-word;'>审批流定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务流定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工作流定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>差旅费借款单</td></tr><tr><td rowspan="2">资金管理</td><td style='text-align: center; word-wrap: break-word;'>账户管理</td><td style='text-align: center; word-wrap: break-word;'>内部账户办理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资金管理</td><td style='text-align: center; word-wrap: break-word;'>委托结算-委托付款</td></tr></table>

#### 2.8.4 产品解决方案

## ☑ 初始准备

1. 按企业的委托付款书的业务审批流程，在【动态建模平台】→【流程管理】→【流程设计】→【审批流定义】节点定义委托付款书的审批流。

2. 在【动态建模平台】→【流程管理】→【流程设计】→【工作流定义】定义委托付款书的工作流。

3. 在【动态建模平台】→【流程管理】→【流程设计】→【业务流定义】节点定义借款单、报销单到委托付款书的业务流。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">动作驱动配置</td></tr></table>

## ☑ 委托付款步骤

1. 【财务会计】→【费用管理】→【单据录入】→【差旅费借款单】/【差旅费报销单】，单据录入完成审批后，在联查中查看结算信息。

1）借款单、报销单上支付单位的银行账户需选择其在结算中心开设的内部账户，收款方员工或供应商/客户（供应商、客户需为外部客户）收款账户需为外部账户。供应商/客户收款账户也是在结算中心开户的内部账户时，不支持委托付款。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>签获费报销单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

2.【资金管理】→【现金管理】→【结算】节点，可将已签字的借款单、报销单委托结算中心进行支付。

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_512_1023_678.jpg" alt="Image" width="72%" /></div>


3.【资金管理】→【资金管理】→【委托结算业务】→【委托付款】经办，审批，委托付款完成。

4.【资金管理】→【资金管理】→【资金结算】→【资金组织业务回单】，委托付款回单生成。

### 2.9 费用预提

#### 2.9.1 业务描述

企业按规定预先提取但尚未实际支付的各项费用。就是企业还没支付，但应该要支付的，要记入负债。中国新会计准则已废除该科目，原属于预提费用的业务现应计入“其他应付款”科目。预提费用的特点是受益、预提在前，支付在后。如银行借款的利息费用、预提的固定资产修理费用、租金和保险费等。

#### 2.9.2 业务流程


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</td></tr></table>

流程图说明：

1. 业务员或财务人员录入预提单进行费用预提。

2. 财务会计、财务总监审批预提单。

3. 报销人或财务人员录入报销单并核销预提，通常企业的预提费用都是谁预提，谁报销并核销预提。

4. 出纳人员进行支付。

#### 2.9.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>开发配置</td><td style='text-align: center; word-wrap: break-word;'>交易管理-单据类型管理-费用管理-费用预提单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计平台</td><td style='text-align: center; word-wrap: break-word;'>通用平台-分类定义-费用管理-预提费用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计平台</td><td style='text-align: center; word-wrap: break-word;'>通用平台-转换模板-费用管理-费用预提单</td></tr><tr><td rowspan="3">财务会计</td><td rowspan="3">费用管理</td><td style='text-align: center; word-wrap: break-word;'>费用预提单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用预提单管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用预提单查询</td></tr></table>

#### 2.9.4 产品解决方案

### 1. 制单人填写费用预提单

报销人登录 NC 系统，进入【财务会计】→【费用预提】→【费用预提单录入】→【费用预提单】，新增费用预提单。

### 2. 上级业务经理审批费用预提单

上级业务经理登录 NC 系统，可以在【消息中心】→【已收到消息】→【工作任务】中看到待审批的任务，可以双击该消息进入单据管理界面，还可以直接进入【财务会计】→【费用预提】→【费用预提单管理】中审批该单据，审批人在单据管理节点可以查询、审批自己有权限审批的报销单据，还可以修改单据信息；同时，还可以联查审批情况。

### 3. 财务经理审核费用预提单

财务经理登录 NC 系统，同样可以在【消息中心】→【已收到消息】→【工作任务】中看到待审批的任务，双击该消息进入费用预提单管理界面可以修改单据，然后审批该单据。如图 2.1-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_760_1059_1105.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1-1 费用预提单</div>


4. 在费用预提单界面可上传和查看影像，可查看网上报账中上传的影像。

<div style="text-align: center;"><img src="imgs/img_in_image_box_184_1221_949_1392.jpg" alt="Image" width="64%" /></div>


### 5. 费用预提单支持红冲。

查询出已审批通过的、仍有余额的预提单，点击【红冲】按钮，保存单据，生成一张红冲的预提单。允许修改红冲金额，实施多次红冲。

<div style="text-align: center;"><img src="imgs/img_in_image_box_182_160_1051_938.jpg" alt="Image" width="72%" /></div>


### 6. 报销单可以核销预提单

填写报销单时，可以点击【核销预提】按钮，核销已生效的预提单。报销单预提单需要全额核销，在单据保存之前核销。核销之后在报销单和预提单中都有显示核销明细。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>费用预提单</td><td colspan="11">差旅费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>冲借款</td><td style='text-align: center; word-wrap: break-word;'>核销预提</td><td style='text-align: center; word-wrap: break-word;'>保存</td><td style='text-align: center; word-wrap: break-word;'>保存提交</td><td style='text-align: center; word-wrap: break-word;'>暂存</td><td style='text-align: center; word-wrap: break-word;'>取消</td><td style='text-align: center; word-wrap: break-word;'>快速分摊</td><td style='text-align: center; word-wrap: break-word;'>附件管理</td><td style='text-align: center; word-wrap: break-word;'>预算执行情况</td><td style='text-align: center; word-wrap: break-word;'>影像</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;返回</td><td style='text-align: center; word-wrap: break-word;'>核销预提</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务组织</td><td style='text-align: center; word-wrap: break-word;'>T查询</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="2">交易类本币汇支付原币金</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>单据编号</td><td style='text-align: center; word-wrap: break-word;'>交易类型</td><td style='text-align: center; word-wrap: break-word;'>单据日期</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>经办人</td><td style='text-align: center; word-wrap: break-word;'>预提金额</td><td style='text-align: center; word-wrap: break-word;'>预提余额</td><td style='text-align: center; word-wrap: break-word;'>核销金额</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>262X2014021</td><td style='text-align: center; word-wrap: break-word;'>费用预提单</td><td style='text-align: center; word-wrap: break-word;'>2014-02-11</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>zouzht</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用申请</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报销凭证核支付原币位</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交通费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>费用承担单位</td><td style='text-align: center; word-wrap: break-word;'>费用承担部门</td><td style='text-align: center; word-wrap: break-word;'>收支项目</td><td style='text-align: center; word-wrap: break-word;'>客户</td><td style='text-align: center; word-wrap: break-word;'>供应商</td><td style='text-align: center; word-wrap: break-word;'>预提金额</td><td style='text-align: center; word-wrap: break-word;'>预提余额</td><td style='text-align: center; word-wrap: break-word;'>核销金额</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>天惠电子股份</td><td style='text-align: center; word-wrap: break-word;'>财务预算部</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

### 2.10 报销费用调整

#### 2.10.1 业务描述

在企业的报销业务中，有时报销业务已经完成支付，并生成凭证。但财务发现该单据填写的预算项目错误，导致占用了其他费用项目的费用，需要调整。或者收支项目填写错误，生成的凭证错误，需要从业务发起一张单据生成凭证来修改凭证的错误。费用调整单则是用于财务来处理这类业务的单据。费用调整单是一张可以生成凭证、占用预算、填写正负数，但不传结算的单据。

#### 2.10.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_610_957_984.jpg" alt="Image" width="71%" /></div>


#### 2.10.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="5">动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-控制规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>流程管理</td><td style='text-align: center; word-wrap: break-word;'>交易类型管理-费用管理-主报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户化配置</td><td style='text-align: center; word-wrap: break-word;'>模板管理-模板设置-费用管理-报销单管理-费用调整单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户化配置</td><td style='text-align: center; word-wrap: break-word;'>模板管理-模板设置-费用管理-初始设置-分摊结转单据对应设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计平台</td><td style='text-align: center; word-wrap: break-word;'>通用平台-转换模板-费用管理-费用调整单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>单据录入-费用调整单</td></tr></table>

#### 2.10.4 产品解决方案

## ☑ 初始设置

1. 由于费用调整单是借用的报销单的表头和费用结转单的表体，预算控制时，需要同时选择费用调整单和费用调整结转单对应交易类型。

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_349_1028_684.jpg" alt="Image" width="73%" /></div>


2. 【交易类型管理】-【主报销单】中配置增加费用调整单交易类型，需将“报销类型”选为“费用调整”。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>安全搜索界面</td><td style='text-align: center; word-wrap: break-word;'>控制规则-组织</td><td style='text-align: center; word-wrap: break-word;'>模板设置-业务单元</td><td style='text-align: center; word-wrap: break-word;'>交易类型管理</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

3. 在【客户化配置】-【模板设置中】，配置费用调整单模板。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>安全搜索界面</td><td style='text-align: center; word-wrap: break-word;'>控制规则-组织</td><td style='text-align: center; word-wrap: break-word;'>模板设置-业务单元</td><td style='text-align: center; word-wrap: break-word;'>交易类型管理</td><td style='text-align: center; word-wrap: break-word;'>控制规则-集团</td><td style='text-align: center; word-wrap: break-word;'>模板设置-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>增</td><td style='text-align: center; word-wrap: break-word;'>修改</td><td style='text-align: center; word-wrap: break-word;'>复制</td><td style='text-align: center; word-wrap: break-word;'>测试</td><td style='text-align: center; word-wrap: break-word;'>设置默认模板</td><td style='text-align: center; word-wrap: break-word;'>导入导出</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="8">2011 费用管理
201100 初始设置
201107 费用预提
201110 费用申请
201120 报销管理
20112000 期初单据
20112002 单据录入
2011200201 差旅费借款单
2011200202 会议费借款单
2011200203 差旅费报销单
2011200204 交通费报销单
2011200205 通讯费报销单
2011200206 礼品费报销单
2011200207 招待费报销单
2011200208 会议费报销单
2011200209 还款单
2011200211 广告费报销单
2011200212 广告费报销单
2011200213 办公费报销单
2011200214 租赁费报销单
2011200215 招待费借款单
2011200216 办公费报销单
2011200240 费用调单单</td></tr></table>

在【模板设置】节点的费用管理【费用调整单】交易类型下复制根节点模板，点修改进行模板设置。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">NC</td></tr></table>

在模板上显示需要的字段即可。注意：自定新增费用调整单交易类型时，不要使用报销单业务页签字段。只显示分摊页签字段。表头“分摊”字段默认为勾选。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">NC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>模板设置-集团</td><td style='text-align: center; word-wrap: break-word;'>分摊结转单据对应设置-集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>新增</td><td style='text-align: center; word-wrap: break-word;'>删除</td><td style='text-align: center; word-wrap: break-word;'>保存</td><td style='text-align: center; word-wrap: break-word;'>取消</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>来源交易类型</td><td style='text-align: center; word-wrap: break-word;'>目标交易类</td><td style='text-align: center; word-wrap: break-word;'>交易类型编码</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>交通费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>通讯费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>费用调整单</td><td style='text-align: center; word-wrap: break-word;'>265a</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>招待费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>会议费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>礼品费报销单</td><td style='text-align: center; word-wrap: break-word;'>费用结转单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

注意：自定义了费用调整单交易类型时，需要在【分摊结算单据对应设置】中将调整单交易类型对应到 “265a 费用调整结转单交易类型”。

4. 在【会计平台】-【转换模板】中配置凭证模板。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>安全搜索界面</td><td style='text-align: center; word-wrap: break-word;'>控制规则-组织</td><td style='text-align: center; word-wrap: break-word;'>模板设置-集团</td><td style='text-align: center; word-wrap: break-word;'>转换模板-集团</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

☑ 费用调整单录入

1. 在【费用管理】--【单据录入】--【费用调整单】节点增加费用调整单。费用调整单金额可录入正数、负数，也允许合计金额为零，只支持手工新增，费用调整单不传结算。

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_228_1032_666.jpg" alt="Image" width="72%" /></div>


### 2.11 期末处理

#### 2.11.1 业务描述

会计期末，财务会计进行账务处理前，停止当期报销业务的进行，给总账输出确定的数据。

#### 2.11.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_335_1084_890_1215.jpg" alt="Image" width="46%" /></div>


#### 2.11.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>关账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>批量关账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>结账</td></tr></table>

#### 2.11.4 产品解决方案

## ☑ 关账

【财务会计】→【费用管理】→【期末处理】→【关联】节点中，选择财务组织，点击【关联】，则系统对所选账务组织对应会计期执行关联，如图2.8.4-01所示。关联后，不能再录入已关联期间的借款单、报销单。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_440_1037_837.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.7.4-011 关账</div>


【财务会计】→【费用管理】→【期末处理】→【批量关账】节点中，可选择同一会计期间方案下的多个财务组织，对同一会计期间批量关账。如图 2.8.4-02 所示

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_994_1019_1369.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.8.4-02 批量关账</div>


## ☑ 结账

【财务会计】→【费用管理】→【期末处理】→【关联】节点中，选择财务组织，点击【结账】，则系统对所选账务组织对应会计期间执行结账。选择多个财务组织，可进行多财务组织的批量结账如图

2.8.4-03 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_153_208_1018_440.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.8.4-03 批量结账</div>


➢ 关账后，结账前，可对借款单、报销单进行审批、可以操作费用结转、待摊费用摊销。

只能对已关闭期初的财务组织执行结账。

➢ 每期有未摊销的费用时，不能结账。

结账后，已结账会计期间不能做任何业务操作。

## 第三章 初始准备

### 3.1 参数

## ERY 预算控制组织类型

参数值说明：

集团级参数。下拉选择，可选项包括：费用承担单位；借款报销单位、借款报销人单位、支付单位。参数用途：

用于设定报销受预算控制时，按哪类组织来执行预算控制：

费用承担单位：按费用承担单位控制预算。

借款报销单位：按借款报销单位控制预算。

借款报销人单位：按借款报销人所属单位控制预算。

支付单位：按支付单位控制预算。

## ER1 审批流起点人

参数值说明：

集团级参数。下拉选择，可选项包括：录入人、借款报销人；默认为借款报销人。

## 参数用途：

确定单据的审批流按哪类角色开始。

录入人：当选择"录入人"时，取录入人为制单人的审批流。

借款\报销人：当选择"借款\报销人"时，借款单取借款人（借款人对应的操作员）为审批流的制单人；

报销单取报销人（报销人对应的操作员）为审批流的制单人。

## ER2 是否生成往来单据

参数值说明：

集团级参数。下拉选择，可选项包括："是"或"否"；默认为否。

参数用途：

选择是：当报销单位与费用承担单位不在同一单位时，则生成一张报销单位的应收单和费用承担单位的一张应付单；选择否：不生成往来单据。

## ER8 报销标准适用规则

参数值说明：

集团级参数。下拉选择，可选项包括："报销人单位、费用承担单位、报销单位"；默认为"报销单位"。参数用途：

共享服务中心模式下跨单位选用哪个单位的报销标准来执行报销。

## ER11 费用申请单控制环节

参数值说明：

组织级参数。下拉选择，可选项包括：保存、审批（生效）；默认为“保存”。参数用途：

用来确定执行费用申请单控制的环节。

保存：被控制单据保存时回写执行数，进行控制；

审批（生效）：单据审批或生效后回写执行数，进行控制。

## ER12 总账关账是否检查本系统结账状态

参数值说明：

组织级参数，用于定义总账关账前要否检查费用管理是否已结账，勾选方式。

参数用途：

勾选：总账关账检查业务系统结账状态时要检查费用管理是否已结账；

不勾选：总账关账检查业务系统结账状态时不检查费用管理是否结账，只检查除费用管理外的其他系统。

## ER4 财务核报容差范围

参数值说明：

数值型参数，手工录入。

参数用途：

用于设置报销单上报销金额与核准金额的最大允许差额。

## ER5 还款期限（单位：天）

参数值说明：

数值型参数，手工录入。

参数用途：

设置后，录入借款单，会根据该参数的参数值自动算出最迟还款日，用于借款控制以及还款预警。

## ER6 是否允许冲销其他人的借款

参数值说明：

逻辑型参数，可选值为："是，否"。默认为"是"。

参数用途：

确定报销时可以冲销其他人的借款。

是----则在执行冲借款动作时，借款人与报销人可以不为同一人。

否----则系统校验在冲借款时借款人与报销人必须为同一人。

## ER7 是否必须冲借款

参数值说明：

逻辑型参数，可选值为："是，否"。默认为"否"。

参数用途：

用于报销单据保存时按此参数取值校验，根据该参数取值判断是否保存单据。

是----则在报销单据保存时校验报销人是否有未冲销完的借款，若有则单据不能保存，必须执行冲借款

操作后才可保存。

否----不进行控制。

## ER9 截止到本月单据全部生效

参数值说明：

组织级参数，用于约束报销业务单据在月末是否要全部生成凭证，可选值包括“不检查；检查但不控制；检查并且控制”，默认为“不检查”。

参数用途：

用于约束报销业务单据在月末是否要全部生成凭证。

不检查----月末不检查报销业务单据是否已生效；

检查但不控制——月末检查所有报销业务单据是否已生效，但不强制约束。

检查并且控制——月末检查所有报销业务单据是否已效，若有未生成凭证的单据则强制要求生效。

### 3.2 用户关联人员

费用管理所涉及的用户必须先关联身份，如图 3.2-1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_174_895_1059_1100.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 3.2-1 用户关联人员</div>


这样当用户进行费用管理的业务时，其对应的报销人单位、报销人部门、报销人信息自动显示在单据中，如图 3.2-2 所示，否则报销人单位、报销人部门、报销人信息为空，不能手工编辑。

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_106_1063_581.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 3.2-2 报销人相关信息显示</div>


### 3.3 审批流设置

费用管理支持审批流，费用管理的不同业务单据可以根据企业需求灵活配置各个环节的审批流程，审批流的详细配置参见《流程管理手册》。

例如，应用场景中的员工直接报销和跨组织报销2个场景的报销审批流可以配置如图3.3-1所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_196_934_1062_1283.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.3-1 差旅费报销单审批流</div>


1. 员工直接报销审批流执行分支 $ ^{①} $，分支条件表达式的配置如图 3.3-2 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_233_153_1045_486.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 3.3-2 分支①的条件表达式配置</div>


2. 跨组织报销审批流执行分支②，分支条件表达式的配置如图 3.3-3 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_231_597_1029_933.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 3.3-3 分支②的条件表达式配置</div>


3. 图 3.1-1 的审批流配置中，可以看到上级经理和费用承担部门负责人都关联了同一个角色：组织主管，但是上级经理的限定模式为同组织，如图 3.3-4 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_489_1097_790_1215.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 3.3-4 上级经理的限定模式</div>


4. 费用承担部门负责人的限定模式为：费用部门负责人，如图 3.3-5 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_490_1336_786_1453.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">图 3.3-5 费用承担部门负责人的限定模式</div>

### 3.4 交易类型管理

在单据类型基础上，提供不同的交易类型，满足企业针对不同类型借款、报销的业务需求。系统预置了差旅费借款单、会议费借款单、差旅费报销单、交通费报销单、会议费报销单、通讯费报销单、招待费报销单、礼品费报销单、还款单九个交易类型。

同时支持自定义交易类型，配置交易类型对应的单据模板，可将交易类型发布成独立的节点，在发布的节点中，对发布的交易类型进行业务操作。针对具体交易类型，可设置是否需要手工签字确认、是否 CA 身份认证、在有借款的情况下进行报销是否提示冲借款，是否加载常用单据。

在【企业建模平台】→【流程管理】→【交易类型管理】节点，可以增加一个住宿费报销单，发布到一个【财务会计】→【费用管理】→【单据录入】节点下，然后将该节点的功能权限分配给用户，则用户登录后就可以在【财务会计】→【费用管理】→【单据录入】下看到【住宿费报销单】节点。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_699_1086_1206.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 3.4-1 交易类型管理</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_154_1087_582.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_109_596_1086_1132.jpg" alt="Image" width="82%" /></div>


🎉 🎉 🎉 🎉

## 按交易类型定义费用管理单据的编码规则

## 1、 定义编码规则

编码规则管理，支持按单据类型设置编码规则，不同交易类型采用不同的编码规则，实现方法：【企业建模平台】→【客户化配置】→【编码规则】→【other】借款单据，报销单据。

## 2、 引用编辑规则

## 3、 按引用编码规则生成单据编号

【企业建模平台】→【流程管理】→【流程定义】→【交易类型管理】→【费用管理】主借款单，主报销单。

4、单据类型中“是否签字确认”的取值会影响报销单生效时的处理，当该属性被勾选时，表示需要出纳签字确认，此时报销单可置空本方银行账户、现金账户，由出纳在结算时补充填写；若未勾选，则必须在审核前提供上述两个账户之一，否则系统提示“结算信息表体中本方银行账户、现金账户、票据号（商业汇票）不能同时为空，签字操作失败”，一旦输入，则结算时不能修改。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>是否封存</td><td style='text-align: center; word-wrap: break-word;'>是否传言平台</td><td style='text-align: center; word-wrap: break-word;'>编码规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>264X-Cxx-77</td><td style='text-align: center; word-wrap: break-word;'>广告费报销单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2643</td><td style='text-align: center; word-wrap: break-word;'>通讯费报销单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>264c</td><td style='text-align: center; word-wrap: break-word;'>报销转固单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>264a</td><td style='text-align: center; word-wrap: break-word;'>费用调整单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2645</td><td style='text-align: center; word-wrap: break-word;'>招待费报销单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2641</td><td style='text-align: center; word-wrap: break-word;'>差旅费报销单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2646</td><td style='text-align: center; word-wrap: break-word;'>会议费报销单</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2644</td><td style='text-align: center; word-wrap: break-word;'>礼品费报销单</td><td style='text-align: center; word-wrap: break-word;'>选择编辑规则</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✗</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2647</td><td style='text-align: center; word-wrap: break-word;'>还款单</td><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>显示效果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2642</td><td style='text-align: center; word-wrap: break-word;'>交通费报销单</td><td style='text-align: center; word-wrap: break-word;'>bx</td><td style='text-align: center; word-wrap: break-word;'>主报销单</td><td style='text-align: center; word-wrap: break-word;'>264XyyyMMdd0001</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>默认币种</td><td style='text-align: center; word-wrap: break-word;'>☑ 手工签字</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>备注</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐身份认证</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>是否提示:中借款</td><td style='text-align: center; word-wrap: break-word;'>是否加载常用单据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>结算</td></tr></table>

V6.5 在【企业建模平台】→【流程管理】→【交易类型管理】→【费用管理】主报销单和主借款单节点，增加参数手工签字和手工结算，用来控制是否需要人工控制签字和结算环节的操作。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_132_514_239_692.jpg" alt="Image" width="8%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_257_510_1076_686.jpg" alt="Image" width="68%" /></div>


### 3.5 报销类型和费用类设置

费用类型和报销类型是报销标准、单据项目的基础数据，为企业细化费用管理提供便利。费用类型和报销类型相互结合，清晰、完整地描述费用的类别、用途。

【财务会计】→【费用管理】→【初始设置】→【费用类型】用于确定报销费用类型，系统预置住宿费、交通费、出差补贴、差旅其他费用、日常通讯费、出差通讯费6种费用类型，分别占用001、002、003、004、005、006编码，如图3.5-1所示，用户可新增/修改费用类型。供用户设置报销标准时参照引用。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td><td style='text-align: center; word-wrap: break-word;'>停用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>001</td><td style='text-align: center; word-wrap: break-word;'>住宿费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>002</td><td style='text-align: center; word-wrap: break-word;'>交通费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>003</td><td style='text-align: center; word-wrap: break-word;'>出差补贴</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>004</td><td style='text-align: center; word-wrap: break-word;'>差旅其他费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>005</td><td style='text-align: center; word-wrap: break-word;'>日常通讯费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>006</td><td style='text-align: center; word-wrap: break-word;'>出差通讯费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☐</td></tr></table>

<div style="text-align: center;">图 3.5-1 费用类型</div>


【财务会计】→【费用管理】→【初始设置】→【报销类型】用于定义报销类型，例如新增2个报销类型为“培训”和“出差”，如图3.5-2所示，在常用单据设置和报销标准设置中可以参照引用。

<div style="text-align: center;"><img src="imgs/img_in_image_box_265_153_925_268.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">图 3.5-2 报销类型</div>


### 3.6 常用单据设置

常用单据将报销人定期报销，每次报销内容、项目类似的单据固化，在进行报销时只需修改少量信息即可提交，减少报销人工作量，提高报销效率。

系统同时支持集团设置全集团可用的常用单据和业务单元设置本组织可用的常用单据，每个交易类型可设置一个常用单据。集团和业务单元都设置有常用单据时，优先加载业务单元的常用单据。

注意：首先需要在交易类型中勾选“是否加载常用单据”后，如图 3.6-1 所示，对应的交易类型录入节点才会自动加载最新设置的常用单据。

单据管理类节点（单据管理、费用申请单管理、费用预提单管理）列表界面可设置显示金额合计，可在模板设置中配置。打印清单时按一次先预览，按两次打印。

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_825_1069_1228.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 3.6-1 交易类型设置</div>

### 3.7 报销标准设置

#### 3.7.1 报销标准设置

报销标准设置用于将各业务单元的标准条款化地录入系统，是单据显示报销标准、并按报销标准进行控制设置的基础数据。支持按业务单元、按交易类型设置报销标准。通过修改后台配置文件，可以按费用类型、报销类型、部门、人员、币种……等多维度组合设置报销标准。在报销单据中支持按报销人单位、报销单位、费用承担单位显示相应的报销标准。

### 1. 报销标准设置

● 【财务会计】→【费用管理】→【初始设置】→【报销标准设置】，此界面用来设置业务单元中报销标准交易类型单据的报销标准。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_682_1042_1102.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 3.7-1 报销标准设置</div>


● 报销标准维度配置。此界面用来配置报销标准设置界面的显示字段，必须选择一个核心控制字段，以便按其设置控制方式。

报销标准交易类型

- 2631 差旅费借款单

- 2632 会议费借款单

- 263X-Cxx-77 礼品费借款单

- 263X-Cxx-78 招待费借款单

- 2641 差旅费报销单

- 2642 交通费报销单

- 2643 通讯费报销单

- 2644 礼品费报销单

- 2645 招待费报销单

- 2646 会议费报销单

- 2647 还款单

- 264X-Cxx-77 广告费报销单

- 264X-Cxx-78 办公费报销单

- 264X-Cxx-79 租赁费报销单

- 264c 报销转固单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="7">报销标准</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>费用类型</td><td style='text-align: center; word-wrap: break-word;'>报销类型</td><td style='text-align: center; word-wrap: break-word;'>部门</td><td style='text-align: center; word-wrap: break-word;'>职位</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>金额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td colspan="4">报销标准配置</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>100.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保存</td><td style='text-align: center; word-wrap: break-word;'>快速复制</td><td style='text-align: center; word-wrap: break-word;'>取消</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>✗</td></tr><tr><td colspan="5">报销标准维度</td><td style='text-align: center; word-wrap: break-word;'>不</td><td style='text-align: center; word-wrap: break-word;'>☑</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>显示名称</td><td style='text-align: center; word-wrap: break-word;'>数据类型</td><td style='text-align: center; word-wrap: break-word;'>参照类型</td><td style='text-align: center; word-wrap: break-word;'>单据对应项</td><td style='text-align: center; word-wrap: break-word;'>单据显示项</td><td style='text-align: center; word-wrap: break-word;'>核心控制项</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>费用类型</td><td style='text-align: center; word-wrap: break-word;'>费用类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>报销类型</td><td style='text-align: center; word-wrap: break-word;'>报销类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>借款单业务行...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>☑</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>部门</td><td style='text-align: center; word-wrap: break-word;'>组织_部门</td><td style='text-align: center; word-wrap: break-word;'>部门</td><td style='text-align: center; word-wrap: break-word;'>原借款人部门</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>职位</td><td style='text-align: center; word-wrap: break-word;'>字符串</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>金额</td><td style='text-align: center; word-wrap: break-word;'>金额</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>备注</td><td style='text-align: center; word-wrap: break-word;'>字符串</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 3.7-2 报销标准设置</div>


● 报销标准控制设置。设置报销标准在报销单的显示字段、控制的金额字段及控制方式。控制模式可选不控制，提示或控制。控制金额与标准值之间如果需要经简单计算后比较，可以通过标准编辑公式实现。

<div style="text-align: center;"><img src="imgs/img_in_image_box_199_330_1066_569.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.7-3 报销标准设置</div>


### 2. 报销单模板设置

【动态建模平台】→【客户化配置】→【模板管理】→【模板设置】，此界面用来配置在报销单界面使用的单据模板，在报销单业务行中增加自定义字段，例如，“控制金额”，此字段为报销标准控制设置中的显示项，用来显示预设的控制金额。在显示属性中修改显示名称例如“控制金额”，卡片是否显示选择是，高级属性类型设置中，数值类型选择“数值 UFDouble”。保存模板。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_850_1059_1396.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.7-4 报销模板设置</div>


### 3. 报销单界面显示标准金额和标准控制效果

【财务会计】→【费用管理】→【单据录入】→【交通费报销单】，配置好报销标准和单据模板后，在报销单业务行录入金额后如果超标则系统会有提示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_256_1044_528.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 3.7-4 报销单界面</div>


### 3.8 借款控制设置

用于控制公司内的部门或业务员借款，是针对借款单进行控制的。

借款控制规则支持在集团和业务单元分别设置。进行控制时，集团控制规则和业务单元控制规则都要执行，系统从第一个不符合的规则开始提示、控制。

1. 控制类型：分为提示、控制。提示：在不符合控制要求时，进行提示，允许保存、审批单据；控制：在不符合控制要求时，系统不允许保存、审批单据。

2. 控制方式：允许借款总额/允许借款单张数/允许最长借款天数：先在该选项前打勾选择后，再录入相关数值。

1）允许借款总额：对所选择的控制对象要求借款的合计总额不能超过所设置的金额，一旦超过，按对应的控制类型（提示、控制）进行相应处理，在借款单据保存、审批时执行该控制规则。

2）允许借款单张数：对所选择的控制对象要求录入的借款单数量不能超过所设置的张数，超过时，按对应的控制类型（提示、控制）进行相应处理，在借款单据保存、审批时执行该控制规则。

3）允许借款天数时：针对对所选择的控制对象，要求在所设置的天数之前提示还款，还款日期为单据审批/生效日期加上设置的借款天数后对应的日期，超过还款日期时，按对应的控制类型（提示、控制）进行相应处理，在借款单据保存、审批时执行该控制规则。

4）控制到期未报销：针对所选择的控制对象，在到期（最迟还款日）未报销时按对应的控制类型（提示、控制）进行相应处理，在借款单据审批时执行该控制规则。

5) 最迟还款日由组织级参数[ER5-还款期限]控制，如图 3.8-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_286_208_1072_402.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 3.8-1 参数[ER5-还款期限]</div>


3. 交易类型：参照交易类型档案中单据类型为借款单的单据类型。

4. 结算方式：为空表示控制所有结算方式。

步骤 1：设置借款控制规则，如图 3.8-2 所示，如果选择了按集团本币控制，则表示借款单据的 “集团借款本币金额” 字段不能超过 “允许借款总额”，否则会进行超标准提示。注意：“集团借款本币金额” 字段在借款单据模板中默认不显示，如果要按照 “集团本币控制”，需要在模板设置中配置该字段的相关属性。

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_699_1064_1177.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 3.8-2 借款控制规则设置</div>


步骤 2：当借款人录入一张币种为 “人民币”，结算方式为 “现金”，总金额为 “5001” 的差旅费借款单，保存时，系统在左下角提示如图 3.8-3 所示，并不允许保存。

<div style="text-align: center;"><img src="imgs/img_in_image_box_398_159_839_361.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">图 3.8-3 控制型借款规则</div>


如果控制方式为提示，则保存时，系统会弹出提示框，如图 3.8-4 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_369_472_874_755.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图 3.8-4 提示型借款规则</div>


### 3.9 费用预算控制

进入【动态建模平台】→【计划平台】→【控制策略－全局】→【控制策略－全局】，可以设置费用管理系统中借款单/报销单保存、删除、审批、取消审批时执行数和预占数的维护规则。系统预置的规则设置如图3.9-1所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_1117_1047_1438.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 3.9-1 控制策略设置</div>


● 借款单保存时，预占数增加；

● 借款单删除时，预占数减少；

● 借款单审批后，执行数增加；

● 借款单反审批后，执行数减少；

● 借款单审批通过后，执行数增加；

● 借款单审批通过后，执行数增加；

● 借款单冲借款生效后，执行数减少；

● 借款单冲借款反生效后，执行数增加；

● 报销单保存时，预占数增加；

● 报销单删除时，预占数减少；

● 报销单审批后，执行数增加；

● 报销单反审批后，执行数减少。

借款单冲借款生效后，执行数减少，该控制规则表明当进行报销冲借款业务时，借款单所占预算释放。例如我们已经对收支项目为通讯费，交易类型为差旅费借款单和差旅费报销单都进行了预算控制。

1. 录入通讯费借款单，借通讯费 3000 元，执行数减少 3000 元，预算余额为 2000 元，如图 3.9-2 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_854_1027_958.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.9-2 录入借款单后的执行数</div>


2. 报销时，冲借款 1500 元，如图 3.9-3 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_1056_1050_1165.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.9-3 报销冲借款</div>


3. 报销充值款后，通讯费的预算执行数释放了 1500 元，预算余额增加到 3500 元，如图 3.9-4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_1260_1029_1362.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.9-4 报销冲借款后，执行数释放</div>


当编制了预算、资金计划，并设置了相应的控制策略，启用了控制方案时，在录入、审批借款单时，将按设置的控制方案进行预算控制、资金计划控制。控制系统支持刚性控制、预警型控制和柔性控制。

## 1 ) 刚性控制

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_205_1048_535.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.9-5 刚性控制</div>


## 2 ) 柔性控制

<div style="text-align: center;"><img src="imgs/img_in_image_box_301_637_890_1030.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 3.9-6 柔性控制</div>


## 3 ) 预警型控制

<div style="text-align: center;"><img src="imgs/img_in_image_box_299_1132_892_1532.jpg" alt="Image" width="49%" /></div>

<div style="text-align: center;">图 3.9-7 预警型控制</div>


### 3.10 期初单据

期初单据处理系统启用前未冲销完的借款单业务。期初单据保存后即为已生效状态。期初单据不传会计平台生成凭证。录入期初单据时，借款人字段参照不受只能参照自己以及代理人的控制。查询期初单据时，可以查到所有在期初中录入的借款单。期初单据不受借款控制、预算控制。

1. 只能录入单据日期在费用管理产品启用期间之前的单据。

2. 期初单据保存即审核。

3. 期初余额通常由财务人员录入。

### 3.11 查询对象注册

在【财务会计】→【费用管理】→【初始设置】→【查询对象注册】节点，支持将单据上的任何业务字段（包括自定义字段）注册为账表的查询对象。

1. 【查询对象注册】是“管理类”功能，有管理类功能权限的人员才有权限操作该节点。

2. 可将对应单据上的任何业务字段，包括自定义项注册为账表的查询对象。

3. 在【查询对象注册】中注册为查询对象后，在账表初始化时，可将注册的查询对象作为对应账表类型账表初始化时的查询对象并发布成节点。

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_981_1037_1222.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.11-1 查询对象注册</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_183_159_1048_599.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 3.11-2 账表初始化</div>


## 附录

## 附录 1：费用管理查询报表

### 1. 查询

费用管理支持对借款余额、借款明细、费用明细、费用汇总进行账表查询。通过账表初始化设置对应的查询对象。常用查询条件有查询方式：按日期、按月份，币种，财务组织、单据状态。支持按具体查询对象的值进行查询。支持设置是否包含下级。

1）借款明细查询，可查询所选财务组织对应查询对象的借款明细、借款单的还款明细情况及合计的借款余额。借款余额查询和借款明细查询的信息可相互联查。

2）借款余额查询，可查询所选财务组织对应查询对象在所查询时间范围内的借款、还款及查询截止时间借款余额情况。其中期初指查询开始时间查询对象的借款余额。

3) 费用明细查询，可查询所选财务组织对应查询对象的报销费用明细。

4）费用汇总查询，可查询所选查询组织在所查询的时间范围内的费用汇总金额。费用明细查询和费用汇总查询的信息可相互联查。

5）费用汇总表提供查询对象的费用汇总，费用报销人、各级领导及管理人员查询统计费用发生的汇

总情况。

6）借款账龄查询提供按账龄方案查询指定财务组织的借款记录，包含汇总数据和明细记录，查询到的记录可联查单据和凭证，并可执行穿透操作。

### 2. 账表初始化

设置借款、报销的相关账表查询、报表的格式、内容，发布成节点。费用管理支持将借款余额表、借款明细表、费用明细表、费用汇总表、借款账龄分析按查询对象及查询对象的组合发布成节点。查询对象支持借款人/报销人、借款人/报销人部门、费用承担部门、费用承担单位、项目、收支项目、结算方式。账页格式支持金额式和外币金额式，显示名称支持名称、编码、编码+名称。

### 3. 借款账龄分析

费用管理提供借款账龄分析表，通过账表初始化设置对应的查询对象，显示查询对象的借款账龄分布情况。借款账龄分析表提供“按账龄”对查询对象的借款账龄进行分析，支持按最迟还款日、单据日期、审批日期、生效日期四种分析日期的借款账龄分析。

## 附录 2：跨组织生成凭证的配置及分析

### 1. 入账规则及凭证模板的配置

## 1 ) 入账规则

a) 报销单位账簿

b) 费用单位账簿

c) 借款单位账簿

这里可以不使用公式，入账会自动过滤同组织的情况，对于不跨组织的单据也不会生成重复的凭证，在模板上处理分录的情况

## 2 ) 凭证模板

a) 费用科目 iif(目的组织==费用承担单位,报销金额,0) 借: 费用

iif(getcurrentbusiunit()==$fydwbm@,$er_finitem.ybje@,0)

b) 现金、银行存款 iif(目的组织==报销单位,支付金额,0) 贷：现金/银行存款 iif(getcurrentbusiunit()==$pk_org@,$er_finitem.zfybje@,0)

c) 现金、银行存款 iif(目的组织==报销单位,还款金额,0) 借：现金/银行存款 iif(getcurrentbusiunit()==$pk_org@,$er_finitem.hkybje@,0)

d) 冲其他应收款 iif(目的组织==借款单位,冲借款金额,0) 贷：其他应收款

iif(getcurrentbusiunit()==$er_bxcontrast.pk_org@,$er_bxcontrast.ybje@,0) ---挂人员档案的辅助核算（取借款报销人）

e) 内部往来（费用单位-报销单位） iif(目的组织==费用单位&&目的组织<>报销单位,支付金额,0)

贷：内部应付—报销单位

iif(getcurrentbusiunit()==$fydwbm@&&getcurrentbusiunit()<>$pk_org@,$er_finitem.zfybje@,0)--

-挂客商的辅助核算（取报销单位）

f) 内部往来(报销单位-费用单位) iif(目的组织==报销单位&&目的组织<>费用单位,支付金额,0)

借：内部应收-费用单位

iif(getcurrentbusiunit()==$pk_org]&amp;&amp;getcurrentbusiunit()&gt;&gt;Sfydwbm@$,$er_finitem.zfybje@,0)--

-挂客商的辅助核算（费用单位）

g) 内部往来（费用单位-借款单位） iif(目的组织==费用单位&&目的组织<>借款单位,冲销明细.

费用原币金额,0) 贷：内部应付-借款单位

iif(getcurrentbusiunit()==$fydwbm@&&getcurrentbusiunit()<>$er_bxcontrast.pk_org@,$er_bxcontrast.fyybje@,0)---挂客商的辅助核算（借款单位）

h) 内部往来（借款单位-费用单位） iif(目的组织==借款单位&&目的组织<>费用单位,冲销明细.

费用原币金额,0) 借：内部应收-费用单位

iif(getcurrentbusiunit()==$er_bxcontrast.pk_org@&&getcurrentbusiunit()<>$fydwbm@,$er_bxcontrast.fyybje@,0)---挂客商的辅助核算（费用单位）

i) 内部往来（借款单位-报销单位） iif(目的组织==借款单位&&目的组织<>报销单位,冲销明细.

还款原币金额,0) 借：内部应收-报销单位

iif(getcurrentbusiunit()==$er_bxcontrast.pk_org@&&getcurrentbusiunit()<>$pk_org@,$er_bxcontr

ast.cjkybje@-$er_bxcontrast.fyybje@,0)---挂客商的辅助核算（报销单位）

j) 内部往来（报销单位-借款单位） iif(目的组织==报销单位&&目的组织<>借款单位,冲销明细.

还款原币金额,0) 贷：内部应付-借款单位

iif(getcurrentbusiunit()==$pk_org]&&getcurrentbusiunit()&gt;&gt;$er_bxcontrast.pk_org@,$er_bxcontrast.cjkybje@-$er_bxcontrast.fyybje@,0)---挂客商的辅助核算（借款单位）

## 3 ) 客商辅助核算的配置公式

客户：getcolvalue("bd_customer","pk_customer","pk_financeorg",$pk_org@)

供应商：getcolvalue("bd_supplier","pk_supplier","pk_financeorg",$pk_org@)


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>生成目标</td><td style='text-align: center; word-wrap: break-word;'>总账凭证</td><td style='text-align: center; word-wrap: break-word;'>Q</td><td style='text-align: center; word-wrap: break-word;'>账簿_账簿类型</td><td style='text-align: center; word-wrap: break-word;'>基准账簿</td><td style='text-align: center; word-wrap: break-word;'>Q</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>影响因素</td><td style='text-align: center; word-wrap: break-word;'>对照表</td><td style='text-align: center; word-wrap: break-word;'>科目关联信息默认值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ERM01</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>ERM02</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>过渡科目</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>库存现金-人民币</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>ERM03</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>费用科目</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>销售费用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>ERM04</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>内部应收</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>内部应收账款</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>ERM05</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>内部应付</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>内部应付账款</td></tr></table>

借方：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">会计科目</td></tr></table>

贷方：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">会计科目</td><td style='text-align: center; word-wrap: break-word;'>原币贷发生额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>[ERM03 费用科目]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>[ERM01 其他应收款]</td><td style='text-align: center; word-wrap: break-word;'>if[getcurrentbusiunit(=报销单冲销对照行冲借款单位,&amp;报销单冲销对照行原币金额,0)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>[ERM02 过账科目]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>[ERM02 过账科目]</td><td style='text-align: center; word-wrap: break-word;'>if[getcurrentbusiunit(=报销单位,&amp;报销单财务行,支付金额,0)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>[ERM05 内部应付]</td><td style='text-align: center; word-wrap: break-word;'>if[getcurrentbusiunit(=&amp;费用承担单位&amp;&amp;getcurrentbusiunit(=&amp;报销单位,&amp;报销单财务行,支付金额,0)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>[ERM04 内部应收]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>[ERM05 内部应付]</td><td style='text-align: center; word-wrap: break-word;'>if[getcurrentbusiunit(==&amp;费用承担单位&amp;&amp;getcurrentbusiunit(=&amp;报销单冲销对照行冲借款单位,&amp;报销单冲销对照行,费用原币金额,0)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>[ERM04 内部应收]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>[ERM04 内部应收]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>[ERM05 内部应付]</td><td style='text-align: center; word-wrap: break-word;'>if[getcurrentbusiunit(==&amp;报销单位&amp;&amp;getcurrentbusiunit(=&amp;报销单冲销对照行冲借款单位,&amp;报销单冲销对照行,冲销原币金额,&amp;报销单冲销对照行,费用原币金额,0)</td></tr></table>

## 跨单位报销及冲借款的几种典型应用场景：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>借款单位</td><td style='text-align: center; word-wrap: break-word;'>报销单位</td><td style='text-align: center; word-wrap: break-word;'>费用承担单位</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>A</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>A</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>A</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td></tr></table>

借款时借款单生成凭证只有一种：借：其他应收款—张三

贷：现金/银行存款

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外系统生成凭证</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外系统生成凭证</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

以下是报销单上的各种凭证分析：

## 借款单位 A

报销单位 B

费用承担单位 C

1. 张三在 A 借款 1000，在 B 公司报销 800 冲借款 1000（还款 200），费用由 C 承担

A 公司生成凭证：借：内部应收款—B 200

内部应收款—C 800

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

附：结算单生成凭证：借：现金/银行存款 1000

贷：内部应收款—B 200

内部应收款—C 800

B 公司生成凭证：借：现金/银行存款 200

贷：内部应付款—A 200

核算账簿 广州市裕丰控股股份有

<div style="text-align: center;">凭证类别 记账凭证</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

附：结算单生成凭证：借：内部应付款—A 200

贷：现金/银行存款 200

C 公司生成凭证：借：费用 800

贷：内部应付款—A 800

核算账簿 广州市番禺裕丰钢铁有...

制单日期 2011-12-12

<div style="text-align: center;">凭证类别 记账凭证</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>800.00</td></tr></table>

附：结算单生成凭证：借：内部应付款—A 800

贷：现金/银行存款 800

张三在 A 借款 1000，在 B 报销 1200 冲借款 1000（支付 200），费用由 C 承担

A 公司生成凭证：借：内部应收款—C 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...

制单日期 2011-12-12

凭证类别 记账凭证


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款\内部应收账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

B 公司生成凭证：借：内部应收款—C 200

贷：现金/银行存款 200

核算账簿 广州市裕丰控股股份有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

C 公司生成凭证：借：费用 1200

贷：内部应付款—B 200

内部应付款—C 1000

<div style="text-align: center;">制单日期 2011-12-12</div>


<div style="text-align: center;">凭证类别 记账凭证</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

2. 张三在 A 公司借款 1000，在 B 报销 1000 冲借款 1000（无还款为支付），费用由 C 承担

A 公司生成凭证：借：内部应收款—C 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...

制单日期 2011-12-12

<div style="text-align: center;">凭证类别 记账凭证</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收账款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司不生成凭证

C 公司生成凭证：借：费用 1000

贷：内部应付款—A 1000

核算账簿 广州市番禺裕丰钢铁有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用\销售费用-</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

## 借款单位 A

报销单位 A

费用承担单位 B

张三在 A 公司借款 1000，在 A 公司报销 800 冲借款 1000（还款 200），费用由 B 承担

A 公司生成凭证：借：现金/银行存款 200

内部应收款—B 800

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：费用 800

贷：内部应付款—A 800

核算账簿 广州市番禺裕丰钢铁有...

制单日期 2011-12-12 凭证类别 记账凭证


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>800.00</td></tr></table>

1. 张三在 A 公司借款 1000，在 A 报销 1200 冲借款 1000（支付 200），费用由 B 公司承担

A 公司生成凭证：借：内部应收款—B 1200

贷：其他应收款—张三 1000

现金/银行存款 200

核算账簿 广州市裕丰企业集团有..


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：费用 1200

贷：内部应付款—A 1200

核算账簿 广州市番禺裕丰钢铁有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

2. 张三在 A 公司借款 1000，在 A 报销 1000 冲借款 1000（无还款无支付），费用由 B 承担

A 公司生成凭证：借：内部应收款—B 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="8">广州市裕丰企业集团有限公司-基准账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：费用 1000

贷：内部应付款—A 1000

核算账簿 广州市番禺裕丰钢铁有

<div style="text-align: center;">凭证类别 记账凭证</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

## 借款单位 A

报销单位 B

## 费用承担单位 A

1. 张三在 A 借款 1000，在 B 公司报销 800 冲借款 1000（还款 200），费用由 A 公司承担

A 公司生成凭证：借：费用 800

内部应收款—B 200

贷:其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：财务部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：现金/银行存款 200

贷：内部应付款—A 200

核算账簿 广州市裕丰控股股份有


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr></table>

2. 张三在 A 借款 1000，在 B 公司报销 1200 冲借款 1000（支付 200），费用由 A 承担

A 公司生成凭证：借：费用 1200

贷：其他应收款—张三 1000

内部应付款—B 200

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：财务部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr></table>

B 公司生成凭证：借：内部应收款—A 200

贷：现金/银行存款 200

核算账簿 广州市裕丰控股股份有


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

3. 张三在 A 借款 1000，在 B 报销 1000 冲借款 1000（无支付无还款），费用由 A 承担

A 公司生成凭证：借：费用 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...

凭证类别 记账凭证


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用/销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：财务部】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

B 公司不生成凭证

## 借款单位 A

报销单位 A

费用承担单位 A

1. 张三在 A 公司借款 1000，A 公司报销 800 冲借款 1000（还款 200），费用由 A 自己承担

A 公司生成凭证：借：费用 800

现金/银行存款 200

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...

制单日期 2011-12-12 凭证类别 记账凭证


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用/销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：销售部】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

2. 张三在 A 借款 1000，A 公司报销 1000 冲借款 1000（无还款无支付），费用有 A 承担

A 公司生成凭证：借：费用 1000

贷：其他应收款 1000

核算账簿 广州市裕丰企业集团有...

<div style="text-align: center;">凭证类别 记账凭证</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用/销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：销售部】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

3. 张三在 A 借款 1000，A 公司报销 1200 冲借款 1000（支付 200），费用由 A 承担

A 公司生成凭证：借：费用 1200

贷：其他应收款—张三 1000

现金/银行存款 200

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td colspan="2">销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：销售部】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td colspan="2">其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td colspan="2">库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr></table>

## 借款单位 A

报销单位 B

## 费用承担单位 B

1. 张三在 A 借款 1000，在 B 公司报销 800 冲借款 1000（还款 200），费用由 B 公司承担

A 公司生成凭证：借：内部应收款—B 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：现金/银行存款 200

费用 800

贷：内部应付款—A 1000

核算账簿 广州市裕丰控股股份有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td rowspan="2">销售费用销售费用-库存现金</td><td rowspan="2">【部门：采购部】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>800.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>800.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr></table>

2. 张三在 A 借款 1000，在 B 公司报销 1200 冲借款 1000（支付 200），费用由 B 公司承担

A 公司生成凭证：借：内部应收款—B 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：费用 1200

贷：内部应付款 1000

现金/银行存款 200

核算账簿 广州市裕丰控股股份有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-</td><td style='text-align: center; word-wrap: break-word;'>【部门：采购部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'>1,200.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>200.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>200.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

3. 张三在 A 公司借款 1000，在 B 公司报销 1000 冲借款 1000(无还款无支付)，费用由 B 承担

A 公司生成凭证：借：内部应收款—B 1000

贷：其他应收款—张三 1000

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰控股股份有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'>【人员档案：s01】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

B 公司生成凭证：借：费用 1000

贷：内部应付款—A 1000

核算账簿 广州市裕丰控股股份有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用\销售费用-</td><td style='text-align: center; word-wrap: break-word;'>【部门：采购部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>应付账款\内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

无借款 报销单位 A

费用承担单位 B

1. 张三在 A 公司报销 1000（支付 1000），费用由 B 公司承担

A 公司生成凭证：借：内部应收款—B 1000

贷：现金/银行存款 1000

核算账簿 广州市裕丰企业集团有...


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>应收账款内部应收</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市番禺裕丰钢铁有限公司】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

B 公司生成凭证：借：费用 1000

贷：内部应付款—A 1000

核算账簿 广州市番禺裕丰钢铁有...

制单日期 2011-12-12


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币(借方)</td><td style='text-align: center; word-wrap: break-word;'>组织本币(贷方)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'>【部门：营业部】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>应付账款内部应付账款</td><td style='text-align: center; word-wrap: break-word;'>【客商：广州市裕丰企业集团有限公司】</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

无借款 报销单位 A

费用承担单位 A

1. 张三在 A 公司报销 1000（支付 1000），费用由 A 公司承担

A 公司生成凭证：借：费用 1000

贷：现金/银行存款 1000

核算账簿 广州市裕丰企业集团有...

制单日期 2011-12-12


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币（借方）</td><td style='text-align: center; word-wrap: break-word;'>组织本币（贷方）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>销售费用\销售费用-差旅费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>【部门：销售部】</td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>库存现金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CNY</td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1,000.00</td></tr></table>

容易出问题的点：

1. 冲借款后无还款无支付的报销单生成临时凭证，反审后重新审核就重复生成临时凭证

2. 借款单生成凭证，重算后就自动删除了

3. 不生成结算信息的单据要注意，比较容易被忽略

### 2. 由收付来核算往来

## 1 ）在 A 借款，由 B 承担，在 B 报销

录入借款单，借款主体为 A，费用承担主体为 B

借：个人往来-张三

贷：现金

报销时录入一张报销单，费用承担公司为 B、报销公司为 B.，冲完借款后，转往来，生成一张 B 的应付单，A 的应收单

## B 的凭证

报销单生成 B 的凭证

借：费用

贷：中转

应付单生成 B 的凭证

借：中转

贷：内部往来-A公司

## A 的凭证

应收单凭证

借：内部往来-B 公司

贷：个人往来-张三（应收单上没有借款人信息，所以这个辅助核算取不到，可以考虑将报销单对应的借款单记录中的部分字段传递过去，比如借款人对应应收单上的业务员）

以上的前提是业务员张三为 A 公司的业务员

如果张三是非 A 公司的人，是 B 公司的人，上面的借“个人往来”是找不到张三的，因此不能如此做凭

证，下面列举应走的凭证（单据上借款人公司=费用承担公司）：

录入借款单，借款公司为 A，费用承担公司为 B。

借款单生成凭证

A 公司凭证

借：应收一个人借款（张三）

贷：内部往来一（客商：A）

报销时录入一张报销单，费用承担公司为 B、报销公司为 B. 转往来，生成一张 B 的应付单，一张 A 的应收单

## B 公司

报销单凭证

借：费用

贷：中转

应付单凭证

借：中转

贷：应收一个人借款 张三

A 公司

应收单凭证

(不需要生成凭证)

### 2. 在 A 借款，由 B 承担，在 A 报销

录入借款单，借款主体为 A，费用承担主体为 B

借：个人往来-张三

贷：现金

报销时录入一张报销单，费用承担公司为 B、报销公司为 A.，冲完借款后，转往来，生成一张 B 的应付单，A 的应收单

## B 的凭证

报销单生成 B 的凭证(报销单是否均生成费用承担公司的凭证？)

借：费用

贷：中转

应付单生成 B 的凭证

借：中转

贷：内部往来-A公司

## A 的凭证

应收单凭证

借：内部往来-B 公司

贷：个人往来-张三（应收单上没有借款人信息，所以这个辅助核算取不到，可以考虑将报销单对应的借款单记录中的部分字段传递过去，比如借款人对应应收单上的业务员）

### 3. 在 A 借款，由 B 承担，在 C 报销

## 1 ）借款 1000，报销 800 的情况

录入借款单，借款主体为 A，费用承担主体为 B

借款单生成凭证

借：应收_个人 1000

贷：现金 1000

方案一（这种方案目前不支持）：C无法对A还款

报销时录入一张报销单 800，费用承担公司为 B、报销公司为 C.，报销金额为 800，还款金额为 200，冲借款金额为 1000，转往来，生成一张 B 的应付单 800，A 的应收单 800，A 对 C 的应收单 200

方案二：分两个步骤

步骤 1：报销时录入一张报销单 800，费用承担公司为 B、报销公司为 C.，报销金额为 800，冲借款金额为 800，转往来，生成一张 B 的应付单 800，A 的应收单 800

## B 的凭证

报销单凭证

借：费用 800

贷：中转 800

应付单凭证

借：中转 800

贷：内部往来-A 公司 800

## A 的凭证

借：内部往来-B 公司 800

贷：应收_个人 800

步骤 2

张三到 A 公司还款 200（在哪里借款在哪里还的原则），录入还款单，报销金额为 0，冲借款金额为 200，转往来，生成一张 B 的应付单 200，A 的应收单 200

## B 的凭证

## 报销单凭证

报销单凭证

借：费用 200

贷：中转 200

应付单凭证

借：中转 200

A 的凭证

贷：内部往来-A 公司 200

借：内部往来-B 公司 200

贷：应收_个人 200

## 2 ) 借款 1000，报销 1200 的情况

录入借款单，借款主体为 A，费用承担主体为 B。借款金额 1000，

借款单生成 A 的凭证

借：应收一个人借款 1000

贷：现金 1000

报销时录入一张报销单，报销金额为 1200，费用承担公司为 B、报销公司为 C.，冲借款金额为 1000，支付金额为 200，转往来，生成一张 B 的应付单 1200，A 的应收单 1000，C 的应收单 200。

## B 的凭证

报销单生成 B 的凭证

借：费用 1200

贷：中转 1200

应付单凭证

借：中转 1200

贷：内部往来-A 公司 1000

内部往来-B 公司 200

## A 的凭证

应收单凭证

借：应收账款-B 公司 1000

贷：应收一个人借款 1000

## C 的凭证

应收单凭证

借：应收账款-B 公司 200

贷：现金 200

## 3 ) 无借款，在 B 报销，由 A 承担费用

报销时录入一张报销单，费用承担公司为 A，报销公司为 B，报销金额为 1000，转往来，生成一张 B 的应收单 1000，A 的应付单 1000。

## A 的凭证

报销单凭证

借：费用 1000

贷：中转 1000

应付单凭证

借：中转 1000

贷：内部往来（客商：杭州）1000

## B 的凭证

报销单凭证

借：中转 1000

贷：现金 1000

应收单凭证

借：内部往来（客商：宁波）1000

贷：中转 1000

## 4 ) 在 A 借款，在 B 报销，A 承担费用

## a) 借款 1000，报销 800 的情况

录入借款单，借款主体为 A，费用承担主体为 A。借款金额 1000

借款单生成凭证

借：应收-个人 1000

贷：现金 1000

报销时录入一张报销单，费用承担公司为 A、报销公司为 B，报销金额为 800，冲借款 1000, 还款金额 200，转往来，生成一张 B 的应付单 200，A 的应收单 200

## A 的凭证

报销单凭证

借：费用 800

贷：应收-个人 800

应收单凭证

借：内部往来（客商：杭州）200

贷：应收-个人 200

## B 的凭证

应付单凭证

借：现金 200

贷：内部往来 200

## b) 借款 1000，报销 1200 的情况

录入借款单，借款主体为 A，费用承担主体为 A。借款金额 1000

借款单生成凭证

借：应收-个人 1000

贷：现金 1000

报销时录入一张报销单，费用承担公司为 A、报销付款公司为 B.，报销金额为 1200，冲借款金额为 1000，支付金额为 200，转往来，生成一张 B 的应收单 200，A 的应付单 200

## A 的凭证

报销单凭证

借：费用 1200

贷：应收-个人 1000

中转 200

应付单凭证

借：中转 200

贷：内部往来-B 公司 200

## B 的凭证

应收单凭证

借：内部往来-A 公司 200

贷：现金 200

## 5 ) 多张借款单对应一张报销单

以 A1A2BC 为例，即在 A1 和 A2 分别借款，费用承担在 B，报销在 C

张三录入借款单 1，借款公司为 A1，费用承担公司为 B，借款金额为 1000。

借款单生成凭证

借：个人往来-张三 1000

贷：现金 1000

录入借款单 2，借款公司为 A2，费用承担公司为 B，借款金额为 2000。

借款单生成凭证

借：个人往来-张三 2000

贷：现金 2000

报销分两种情况，一是报销金额〉3000，一是报销金额 $ <3000 $

情况一：

报销时录入一张报销单，费用承担公司为 B、报销公司为 C.，报销金额为 4000，冲销 A 公司借款 1000，冲销 A2 公司借款 2000，支付金额 1000，转往来，生成四张往来单据，分别为 B 公司的应付单（三条表体行，供应商分别为 A1、A2 和 C）和 A1、A2 公司的应收单、C 公司的应收单。

## B 公司

报销单凭证

借：费用 4000

贷：中转 4000

应付单凭证

借：中转 4000

贷：内部往来-A1 1000

内部往来-A2 2000

内部往来-C 1000

## A1 公司

应收单凭证

借：内部往来—B 公司 1000

贷：个人往来-张三 1000

## A2 公司

应收单凭证

借：内部往来—B 公司 2000

贷：个人往来-张三 2000

## C 公司

应收单凭证

借：内部往来—B 公司 1000

贷：现金 1000

## 情况二

报销时录入一张报销单，费用承担公司为 B、报销公司为 C，报销金额为 2500，A1 公司借款 1000，冲销 A2 公司借款 2000，还款金额 500（还款给 C、C 应还给 A2 500）。转往来，共生成五张单据，分别为 B 的一张应付单（两条表体行，客商分别为 A1 和 A2），A1、A2 各一张对 B 的应收单、A2 对 C 的一张应收单、C 对 A2 的一张应付单

## B 公司

报销单凭证

借：费用 2500

贷：中转 2500

应付单凭证

借：中转

贷：内部往来-A1 1000

内部往来-A2 1500

## A1 公司

应收单凭证

借：内部往来—B 公司 1000

贷：个人往来-张三 1000

## A2 公司

应收单 1 凭证

借：内部往来—B 公司 1500

贷：个人往来-张三 1500

应收单 2 凭证

借：内部往来—C 公司 500

贷：个人往来-张三 500

## C 公司

应付单凭证

借：现金 500

贷：内部往来-A2 500

## 附录 3：报销单据多表体打印设置

【动态建模平台】→【客户化配置】→【模板管理】→【模板设置】，可在费用管理，报销单管理，单据录入中，输出模板，自定义变量，具体步骤如下：

1. 打印输出模板修改，因为多页签均属于业务页签的范畴，所以多页签中配置时不可以再用元数据，而是统一使用自定义变量，公式格式如下：“单据模板页签 Code.字段名称”单据模板页签 Code 可以在单据模板中查看到，截图如下：

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_150_1000_683.jpg" alt="Image" width="70%" /></div>


### 2. 修改自定义变量：

配置示例：交通费页签为：交通费页签 arap_bxbusitem.amount，其他页签：other.amount

对于想去档案的名称为：交通费页签为：arap_bxbusitem.szxmid.name，

其他页签：other.szxmid.name。

<div style="text-align: center;"><img src="imgs/img_in_image_box_174_841_1005_1244.jpg" alt="Image" width="69%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>元数据变量</td><td style='text-align: center; word-wrap: break-word;'>数据源变量</td><td style='text-align: center; word-wrap: break-word;'>自定义变量</td><td style='text-align: center; word-wrap: break-word;'>系统变量</td></tr><tr><td colspan="2">变量名</td><td colspan="2">表达式</td></tr><tr><td colspan="2">到达日期</td><td style='text-align: center; word-wrap: break-word;'>lift(dateformat(arap_bxbusitem.defitem2, ...</td><td style='text-align: center; word-wrap: break-word;'>if(dateformat(日期, &quot;yyy-MM-dd HH:mm:</td></tr><tr><td colspan="2">打印日期</td><td style='text-align: center; word-wrap: break-word;'>lift(dateformat(arap_bxbusitem.defitem1, ...</td><td style='text-align: center; word-wrap: break-word;'>if(dateformat(arap_bxbusitem.defitem1, ...</td></tr><tr><td colspan="2">出发日期</td><td style='text-align: center; word-wrap: break-word;'>getcolvalue(md_enumvalue, name, value, ...</td><td style='text-align: center; word-wrap: break-word;'>arap_bxbusitem.amount</td></tr><tr><td colspan="2">交通工具</td><td style='text-align: center; word-wrap: break-word;'>arap_bxbusitem.szmid.name</td><td style='text-align: center; word-wrap: break-word;'>arap_bxbusitem.szmid.name</td></tr><tr><td colspan="2">交通费金额</td><td style='text-align: center; word-wrap: break-word;'>other.szmid.name</td><td style='text-align: center; word-wrap: break-word;'>other.szmid.name</td></tr><tr><td colspan="2">交通费-收支项目</td><td style='text-align: center; word-wrap: break-word;'>other.amount</td><td style='text-align: center; word-wrap: break-word;'>other.amount</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td colspan="2">差旅费报销单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>单笔编号</td><td style='text-align: center; word-wrap: break-word;'>单笔编号</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>单笔日期</td><td style='text-align: center; word-wrap: break-word;'>单笔日期</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>报销人部门</td><td style='text-align: center; word-wrap: break-word;'>报销人部门、报销人项目、报销人项目、报销人项目、报销人项目、</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_171_157_1009_584.jpg" alt="Image" width="70%" /></div>


预制的自定义变量中使用到元数据的都需要进行修改，将之前的 er_busitem 替换为 单据模板页签 code。

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_693_1000_1074.jpg" alt="Image" width="69%" /></div>


预览打印界面

# 差旅费报销单

# ∏

担筒人箍门，财务部

费用承租部门：财务部

很简金额：$50.00


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>校友项目</td><td style='text-align: center; word-wrap: break-word;'>交通费金额</td><td style='text-align: center; word-wrap: break-word;'>到达日期</td><td style='text-align: center; word-wrap: break-word;'>出发日期</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

单位：费用A公司

<div style="text-align: center;"><img src="imgs/img_in_image_box_491_442_698_594.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform
