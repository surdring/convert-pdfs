# NCV6.5产品手册-收付款合同

产品手册- V6.5

收付款合同

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权  
  
第一章 概述 ..... 4  
1.1 产品概述 ..... 4  
1.2 产品价值 ..... 6  
第二章 应用场景 ..... 7  
2.1 收付款合同立账 ..... 7  
2.1.1 业务描述 ..... 7  
2.1.2 业务流程 ..... 8  
2.1.3 功能清单 ..... 8  
2.1.4 产品解决方案 ..... 9  
2.2 收付款计划的执行 ..... 14  
2.2.1 业务描述 ..... 14  
2.2.2 业务流程 ..... 15  
2.2.3 功能清单 ..... 15  
2.2.4 产品解决方案 ..... 16  
2.3 关联付款合同进行费用报销 ..... 17  
2.3.1 业务描述 ..... 17  
2.3.2 业务流程 ..... 18  
2.3.3 功能清单 ..... 18  
2.3.4 产品解决方案 ..... 18  
第三章 初始准备 ..... 19  
3.1 业务系统初始化 ..... 19  
3.1.1 管控模式 ..... 19  
3.1.2 业务初始化 ..... 19  
3.2 动态建模平台 ..... 19  
3.2.1 权限管理 ..... 19  
3.2.2 基础数据 ..... 19  
3.2.3 流程管理 ..... 20  
3.2.4 客户化配置 ..... 20  
第四章 操作指南 ..... 20  
附录  
附录 1：本文参见其他手册清单 ..... 21

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供业务需求与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关本模块的主要业务场景、流程、以及对应的业务功能的介绍；第三部分是初始准备设置；第四部分是关于本模块功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录中对一些可能需要对照查询的关键点进行了补充说明，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《产品手册-组织管理》-----深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助----针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《产品手册-流程管理》----提供关于交易类型、流程设计工具的应用指导。

4. 《产品手册-基础数据》——可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

5. 《产品手册-应收管理》-----提供关于应收管理相关业务的应用指导。

6. 《产品手册-应付管理》----提供关于应付管理相关业务的应用指导。

7. 《产品手册-费用管理》——提供关于费用管理相关业务的应用指导。

## 第一章 概述

### 1.1 产品概述

企业的经济往来，主要是通过合同形式进行的，一个企业的经营成败和合同及合同管理有密切关系。NC 收付款合同为企业提供了基于信息化技术的合同管理功能，其支持企业对以自身为当事人的合同依法进行录入登记、审批、履行、变更、冻结、终止以及审查、监督、控制等一系列活动。其中录入登记、审批、履行、变更、冻结、终止是收付款合同管理的内容；审查、监督、控制是收付款合同管理的手段。

收付款合同的执行过程包括合同起草、合同审批、合同生效、合同履行、合同冻结/解冻、合同变更、合同终止及查询统计环节，具体执行过程如下图 1.1-1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_640_1002_969.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 1.1-1 NC 收付款合同执行过程</div>


NC 收付款合同对合同的执行全过程提供了很好的支持，其产品功能架构如下图 1.1-2 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_171_1011_843.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 1.1-2 NC 收付款合同产品功能架构图</div>


收付款合同与应收管理、应付管理、费用管理模块之间存在接口，基于收款合同可以进行应收与收款业务处理，基于付款合同可以进行应付、付款及费用管理的业务处理。收付款合同与其他模块的主要接口如下图 1.1-3 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_212_171_976_669.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 1.1-3 NC 收付款合同集成接口图</div>


### 1.2 产品价值

1. 收付款合同的签订支持审批流，通过制度化的流程审批降低了合同风险和办公成本，提高了合同签订效率。

2. 在收付款合同立账时支持通过参照收付款协议自动生成收付款计划，根据收付款计划可按时进行收付款，同时为资金计划提供了参考依据。

3. 支持超合同金额的收款和付款控制，降低收付款风险。

4. 收付款合同与应收管理、应付管理和费用管理业务均可进行集成，通过收付款合同可以获得合同准确及时的执行情况，降低合同履约执行相关风险。

5\. 实现集团公司及其成员企业从合同的录入登记、审批、履约管理、监控执行、统计查询等全生命周期的自动化作业模式，实现了企业合同的规范化管理目标。

## 第二章 应用场景

### 2.1 收付款合同立账

#### 2.1.1 业务描述

企业的业务部门与客户或供应商经过协商、谈判并达成一致后拟定收款或付款合同，合同在按照企业合同审批通过后正式生效，同时合同进入收付款计划的履行状态。当企业与合同中指定的客户或供应商发生应收或应付业务时，财务部参照合同进行应收或应付账款的确认，合同执行人可根据相应收付款计划进行收款或付款。收付款合同立账场景如下图 2.1-1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_164_689_1013_1344.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.1-1 收付款合同立账场景图</div>

#### 2.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_252_1086_641.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.1-2 收付款合同立账业务流程</div>


说明：

● 收付款合同支持审批流。

● 收付款合同审批生效后进入合同履行状态。

● 应收应付管理可结合收付款合同确认应收应付，确认的应收应付金额会更新到收付款合同的累计开票金额信息。

● 应收应付管理通过对收付款合同拉单来进行应收应付立账时，应收应付业务会自动关联收付款合同的收付款计划，合同执行人可根据该收付款计划执行相应的收付款业务操作。

#### 2.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td rowspan="2">收款协议-集团收款协议-业务单元付款协议-集团付款协议-业务单元收付款类型合同条款定义-集团合同条款定义-业务单元交易类型管理审批流定义-集团审批流定义-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>流程管理</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="3"></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>业务流定义</td></tr><tr><td rowspan="2">客户化配置</td><td style='text-align: center; word-wrap: break-word;'>模板设置-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模板设置-业务单元</td></tr><tr><td rowspan="8">财务会计</td><td rowspan="4">收付款合同</td><td style='text-align: center; word-wrap: break-word;'>收款合同维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款合同台账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款合同维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款合同台账</td></tr><tr><td rowspan="2">应收管理</td><td style='text-align: center; word-wrap: break-word;'>应收单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收单管理</td></tr><tr><td rowspan="2">应付管理</td><td style='text-align: center; word-wrap: break-word;'>应付单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应付单管理</td></tr></table>

#### 2.1.4 产品解决方案

1. 在【收款合同维护】和【付款合同维护】节点可以进行收付款合同的维护，包括合同录入、合同审批、合同生效、合同冻结/解冻、合同变更和合同终止等基本操作。

## 1 ）合同录入

合同录入界面包括合同基本、合同条款、合同大事记、变更历史、执行过程和收/付款计划几个页签，用户可以对合同基本、合同条款、合同大事记和收/付款计划进行维护，变更历史和执行过程两个页签分别用来记录合同的变更历史和反映合同的执行状态，供用户参考用，不能直接维护。

下图 2.1-3 为收款合同录入界面，付款合同录入界面与其类似。

<div style="text-align: center;"><img src="imgs/img_in_image_box_134_991_1113_1350.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.1-3 收款合同录入界面</div>


## a) 合同基本信息

## ● 收款合同基本信息

收款合同基本信息的关键数据如下表 2.1-1 所示：

<div style="text-align: center;">表 2.1-1 收款合同关键数据</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>字段名称</td><td style='text-align: center; word-wrap: break-word;'>字段解释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务组织</td><td style='text-align: center; word-wrap: break-word;'>合同的主组织。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合同编码</td><td style='text-align: center; word-wrap: break-word;'>用户可以手工输入合同编码，也可以由系统按照统一的编码规则进行生成。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合同类型</td><td style='text-align: center; word-wrap: break-word;'>交易类型，用户可以在【交易类型管理】节点进行自定义，通过合同类型用户可以为不同类型的合同定义不同的审批流。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款协议</td><td style='text-align: center; word-wrap: break-word;'>用户可以在【收款协议-集团】或【收款协议-业务单元】节点进行自定义，如指定收款协议，合同将参照该协议自动生成收款计划</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计开票金额</td><td style='text-align: center; word-wrap: break-word;'>收款合同与应收单集成应用时应收单金额的回写数，或者付款合同与应收单/报销单集成应用时下游单据金额的回写数。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计收款金额</td><td style='text-align: center; word-wrap: break-word;'>收款合同与收款单接口集成应用时收款单金额的回写数，其中累计收款金额=收款金额+预收款金额。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计预收款金额</td><td style='text-align: center; word-wrap: break-word;'>收款合同与收款单集成应用时预收款金额的回写数。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>超合同收款限额（%）</td><td style='text-align: center; word-wrap: break-word;'>表示允许超合同收款金额所占合同金额的比例，字段为“空”或“0”时表示该合同不允许超合同收款。</td></tr></table>

● 付款合同基本信息

付款合同基本信息的关键数据如下表 2.1-2 所示：

<div style="text-align: center;">表 2.1-2 付款合同关键数据</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>字段名称</td><td style='text-align: center; word-wrap: break-word;'>字段解释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务组织</td><td style='text-align: center; word-wrap: break-word;'>合同的主组织。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合同编码</td><td style='text-align: center; word-wrap: break-word;'>用户可以手工输入合同编码，也可以由系统按照统一的编码规则进行生成。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合同类型</td><td style='text-align: center; word-wrap: break-word;'>交易类型，用户可以在【交易类型管理】节点进行自定义，通过合同类型用户可以为不同类型的合同定义不同的单据模板和审批流。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款协议\n<img src="imgs/img_in_image_box_277_1043_377_1146.jpg" alt="Image"" /></td><td style='text-align: center; word-wrap: break-word;'>用户可以在【付款协议-集团】或【付款协议-业务单元】节点进行自定义，如指定付款协议，合同将参照该协议自动生成付款计划。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计开票金额</td><td style='text-align: center; word-wrap: break-word;'>付款合同与应付单或报销单集成应用时下游单据金额的回写数。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计付款金额</td><td style='text-align: center; word-wrap: break-word;'>付款合同与付款单、报销单或借款单集成应用时下游单据金额的回写数，其中累计付款金额=付款金额+预付款金额。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计预付款金额</td><td style='text-align: center; word-wrap: break-word;'>付款合同与付款单或借款单集成应用时下游单据金额的回写数。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>超合同付款限额（%）</td><td style='text-align: center; word-wrap: break-word;'>表示允许超合同付款金额所占合同金额的比例，字段为“空”或“0”时表示该合同不允许超合同付款。</td></tr></table>

● 用户可以选择以物料或项目等任何维度进行合同的录入

默认情况下，收付款合同模板只显示了项目维度，用户可以通过自定义收付款合同的单据模板来显示出物料维度的相关字段信息，如物料编码、物料名称等信息。

## ● 合同基本信息执行 NC 统一的 VAT 计税模型

## b) 合同条款

● 合同条款使用系统已定义的合同条款档案

● 引用系统定义的合同条款后，合同条款内容、其他信息、备注允许修改

● 一个合同可以引用多个合同条款，也可以不引用合同条款

## c) 收/付款计划

## ● 收付款计划的内容

收付款计划的内容包括收付款期、计划比例、起效依据、起算日期、账期天数、计划到期日、计划金额、结算金额、是否为预收/付款、是否为质保金和收付款类型，其能够结构化合同签订双方约定的收付款计划。

## ● 收/付款计划的功能

根据合同表头维护的收/付款协议，系统自动对合同金额进行拆分生成收/付款计划，当合同未维护具体收/付款协议时，系统会自动拆分生成一行比例为100%的收/付款计划行；

系统拆分形成的收/付款计划允许再进行手工维护，维护后收/付款计划行的比例合计必须等于100%，收/付款计划的金额总和需等于合同总金额；

收付款类型为必输项，拆分形成收/付款计划后，需要用户手工维护收/付款计划行的收付款类型；

一个合同的收/付款计划最多只能有一个计划行为质保金业务。

## ● 根据收/付款计划进行预警

● 关于收/付款协议自动拆分生成收/付款计划相关算法请参照附录 1

收/付款合同支持根据收/付款计划进行预警，预警功能的具体实现请参考 NC 系统平台的预警平台相关资料。

预警设置中，组织单元参照财务组织，按照设置的财务组织，根据收付款协议进行账期拆分后，对有实际到期日的收/付款协议行，如果实际到期日-当前日期<=预警提前天数则对相关记录进行预警；对于没有实际到期日的收/付款协议，如果计划到期日-当前日期<=预警提前天，则对相关记录进行预警。

## 2 ）合同审批

收款和付款合同的审批均支持审批流，用户为不同的合同类型定义不同的审批流。

对于设置了审批流的合同，合同提交后将进入到审批流环节，对于未设置审批流的合同，合同不需要进行提交，有合同维护权限的用户都可以直接进行合同审批。

## 3 ) 合同生效

合同审批完成后，合同的承办人（或其他有权限的用户）可以点击‘合同生效’按钮进行合同生效，合同生效后合同自动进入合同履行状态，下游系统可以根据合同进行合同的履行，如：资金的收付、债权债务的确认等。

对于已经生效的合同不允许取消审批。

合同生效后，允许对合同进行冻结、解冻和变更。

如果生效的合同已经发生了后续业务，则不允许合同取消生效。

## 4 ) 合同冻结/解冻

合同生效后，在合同履行过程中允许对合同执行冻结或解冻操作。

合同冻结后，已根据合同发生的后续业务也被冻结，后续业务不能继续履行，控制要求如下：

a) 合同被冻结后，不允许参照该合同进行拉单等操作；

b）根据合同生成的下游单据不能再发生后续业务，进行中的业务会被中止，如：付款单已签字但未进行支付，此时合同已被冻结，则该业务单据不能再继续进行支付。

合同冻结后，可以对合同进行解冻操作，解冻后，上下游业务可以正常进行。

## 5 ) 合同变更

合同生效后，允许合同进行变更操作。

合同变更允许修改除合同编码、合同名称以外的所有信息。

合同变更金额约束：合同变更后，金额应该小于等于合同累计收付款金额-超合同收/付款限额(\%)*合同变更金额。

合同变更会记录合同变更前的历史内容，能够根据合同版本进行查询变更历史记录。

6) 合同终止

合同生效后，允许合同进行终止操作。

合同终止后，不影响后续业务的逻辑处理。

合同终止时，若终止日期与合同计划终止日期不同，则需要录入终止原因。

2. 在【应收单录入】和【应付单录入】节点可以通过对收/付款合同拉单进行应收/应付的立账，即参照收/付款合同进行应收/应付账款的确认。

1）收/付款合同与应收/应付单接口的控制规则

收/付款合同与应收/应付单接口方式采用流程配置，仅支持拉单模式，用户需要在【业务流定义】节点创建业务流来实现通过收/付款合同拉单生成应收/应付单。

<div style="text-align: center;"><img src="imgs/img_in_image_box_209_165_933_740.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">图 2.1-4 收款合同拉单立账</div>


<div style="text-align: center;">图 2.1-5 付款合同拉单立账</div>


对收/付款合同拉单生成的应收应付单只支持同币种业务。

应收/应付单对收/付款合同进行拉单时会拉取合同基本信息，收/付款协议由收/付款合同的收/付款计划携带，应收/应付单不需再做拆分；

应收/应付单保存或删除后回写合同表体的‘累计开票金额’，且仅回写原币金额；

## 2 ) 业务逻辑

应收/应付单的合计数不能超出合同金额数。

应收/应付单信用到期日的拆分

a) 全额拉单

● 应收/应付单会将每行的金额根据合同的收/付款协议进行拆分，保证应收/应付单行所对应的账期与合同所对应的账期一致；

● 应收/应付单所有行所对应的同账期的合计数必须要与合同所对应的账期金额一致。

b) 部分拉单

● 首先将部分拉单总金额按最终余额或最近余额法方式分配到各个账期，分配原则是先分配先清；

总金额分配完成后，会确定本次拉单的具体账期数及各账期的金额；

● 根据已确定的账期，将各行的金额按比例拆分到各个账期中。

### 2.2 收付款计划的执行

#### 2.2.1 业务描述

收付款计划的场景，根据合同的资金计划进行收付款。

### 1. 根据合同的资金计划进行收付款

企业与客户或供应商签订的收/付款合同进入合同履行状态后，财务部可参照合同的相应收付款计划进行收款或付款处理，该应用场景如下图 2.2-1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_547_1010_1074.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.2-1 收付款计划执行场景图</div>

#### 2.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_119_250_1068_735.jpg" alt="Image" width="79%" /></div>


<div style="text-align: center;">图 2.2-3 收付款计划执行业务流程</div>


说明：

● 合同执行人根据合同的收付款计划进行收付款，收付款业务处理会同时更新收付款合同的累计收款金额信息。

● 关联同一合同的应收/付单与收/付款单生效后会自动核销。

#### 2.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="8">财务会计</td><td rowspan="4">收付款合同</td><td style='text-align: center; word-wrap: break-word;'>收款合同维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款合同台账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款合同维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款合同台账</td></tr><tr><td rowspan="2">收款管理</td><td style='text-align: center; word-wrap: break-word;'>收款单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款单管理</td></tr><tr><td rowspan="2">付款管理</td><td style='text-align: center; word-wrap: break-word;'>付款单录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款单管理</td></tr></table>

#### 2.2.4 产品解决方案

### 1. 收/付款合同资金计划的执行

不同于收/付款合同与应收/应付单接口的流程配置方式（拉单），收/付款合同与收/付款单的接口方式为关联方式。

在进行收/付款结算业务处理时，有以下两种处理方式：

1）选中收/付款合同的‘收款计划’或‘付款计划’页签后，直接点击‘收款’或‘付款’按钮，系统会弹出收款单或付款单的编辑页面

下图 2.2-4 为选择收款合同的收款计划直接执行收款的界面

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_532_1073_812.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.2-4 关联合同执行收款计划方式一</div>


通过该方式进行收款或付款时，收/付款合同中选择的收/付款计划行与收款单的表体行一一对应，收/付款单保存后回写收/付款合同的收/付款计划的结算金额。

2）在收款单或付款单操作界面，通过参照选择收/付款合同编码进行合同与收/付款单之间的关联下图2.2-5为通过在收款单录入界面录入合同编码来执行相应收款计划的界面

<div style="text-align: center;"><img src="imgs/img_in_image_box_174_1031_1070_1359.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.2-5 关联合同执行收款计划方式二</div>


通过该方式进行收款或付款时，以收/付款单表体为主，收/付款单表体行按合同号的合计数必须小于或等于收/付款合同的未结算收/付款计划的合计数。

收/付款合同资金计划的执行时会受到超合同收/付款金额的控制，及合同的累计收/付款金额不能超过合同金额+合同金额*超合同收/付款限额(%)。

### 2. 收/付款业务的核销处理

与同一合同相关联的应收/应付单与收/付款单生效后会自动核销。

### 2.3 关联付款合同进行费用报销

#### 2.3.1 业务描述

企业供应商经过协商、谈判签订付款合同，合同允许供应商基于合同进行费用报销，如参照合同进行借款或报销业务。当参照付款合同进行借款业务时，借款金额会统计到合同的累计预付款金额；当参照付款合同进行报销业务时，报销单的报销金额会统计到合同的累计开票金额，相应的报销支付金额会统计到合同的累计支付金额。关联付款合同进行费用报销的场景如下图 2.3-1 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_177_705_1025_1218.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.3-1 关联付款合同进行费用报销</div>

#### 2.3.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_143_253_1044_704.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.3-2 关联付款合同进行费用报销业务流程</div>


说明：

● 报销单或借款单维护时主动关联已生效未完成的付款合同。

● 报销单或借款单关联付款合同后，借款单金额回写到合同的累计预付款金额，报销单的报销金额回写到合同的累计开票金额，相应的报销支付金额回写到合同的累计支付金额。

● 报销单或借款单关联付款合同时可以关联多张合同。

#### 2.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">财务会计</td><td rowspan="2">收付款合同</td><td style='text-align: center; word-wrap: break-word;'>付款合同维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款合同台账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>费用管理</td><td style='text-align: center; word-wrap: break-word;'>单据录入</td></tr></table>

#### 2.3.4 产品解决方案

1. 在费用报销单或借款单的录入界面，可以参照选择付款合同编码，进行合同与报销单或借款单之间的关联

编辑报销单关联付款合同时，以报销单表体为主，报销单表体行按合同号的合计数必须小于或等于付款合同的未结算付款计划的合计数。

### 2. 单据联查

支持报销单和借款单联查付款合同，联查付款合同的执行情况。

支持付款合同联查报销单和借款单。

## 第三章 初始准备

### 3.1 业务系统初始化

#### 3.1.1 管控模式

管控模式中，关于合同条款、收款时点、收款协议、付款时点、付款协议、物料、项目的设定决定了企业建模平台中可使用的节点是全局、集团还是业务组织级，详见《系统管理手册》相关章节部分。

#### 3.1.2 业务初始化

在业务初始化节点选择相应集团，然后选择‘收付款合同’模块进行业务初始化。

### 3.2 动态建模平台

#### 3.2.1 权限管理

维护收付款合同操作相关的职责、角色并分配给相关用户。

#### 3.2.2 基础数据


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="5">动态建模平台</td><td rowspan="5">基础数据</td><td style='text-align: center; word-wrap: break-word;'>收款协议-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收款协议-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款协议-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>付款协议-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收付款类型</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>合同条款定义-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合同条款定义-业务单元</td></tr></table>

#### 3.2.3 流程管理

收款和付款合同的审批均支持审批流，用户为不同的合同类型定义不同的审批流。

收/付款合同与应收/应付单接口方式采用流程配置，仅支持拉单模式，用户需要在【业务流定义】节点创建业务流来实现通过收/付款合同拉单生成应收/应付单。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="4">动态建模平台</td><td rowspan="4">流程管理</td><td style='text-align: center; word-wrap: break-word;'>交易类型管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>审批流定义-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>审批流定义-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务流定义</td></tr></table>

#### 3.2.4 客户化配置

默认情况下，收/付款合同没有把所有的字段显示出来，包括一些较为常用的字段，如收款合同中的“超合同收款限额(%)”、付款合同中的“超合同收款限额(%)”，如果用户需要使用这些字段，可以通过模板设置相关节点来进行修改。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">动态建模平台</td><td rowspan="2">客户化配置</td><td style='text-align: center; word-wrap: break-word;'>模板设置-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模板设置-业务单元</td></tr></table>

## 第四章 操作指南

该部分为关于本模块功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。

## 附录

## 附录 1：本文参见其他手册清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>手册名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-组织管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-流程管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-基础数据》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-应收管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-应付管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-费用管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_489_449_697_602.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform
