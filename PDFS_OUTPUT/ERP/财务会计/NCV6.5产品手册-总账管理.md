# NCV6.5产品手册-总账管理

产品手册- V6.5

总账管理

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权  
  
名词解释 ..... 5  
第一章 概述 ..... 6  
1.1 产品概述 ..... 6  
1.2 产品价值 ..... 7  
第二章 应用场景 ..... 8  
2.1 会计科目管控 ..... 8  
2.1.1 业务描述 ..... 8  
2.1.2 业务流程 ..... 11  
2.1.3 功能清单 ..... 12  
2.1.4 产品解决方案 ..... 12  
2.2 总账日常核算（凭证管理） ..... 18  
2.2.1 业务描述 ..... 19  
2.2.2 业务流程 ..... 21  
2.2.3 功能模型 ..... 22  
2.2.4 产品解决方案 ..... 22  
2.3 多账簿管理 ..... 26  
2.3.1 跨国集团 ..... 28  
2.3.2 跨行业集团 ..... 36  
2.3.3 内外两套账（内外报告分离） ..... 38  
2.3.4 多责任中心（财税分离） ..... 40  
2.3.5 外币分账制 ..... 42  
2.4 二级核算 ..... 44  
2.4.1 业务描述 ..... 44  
2.4.2 业务流程 ..... 45  
2.4.3 功能清单 ..... 45  
2.4.4 产品解决方案 ..... 46  
2.5 内部交易核算 ..... 49  
2.5.1 业务描述 ..... 49  
2.5.2 业务流程 ..... 50  
2.5.3 功能清单 ..... 53  
2.5.4 产品解决方案 ..... 53  
2.6 现金流量分析 ..... 63  
2.6.1 业务描述 ..... 63  
2.6.2 业务流程 ..... 63  
2.6.3 功能清单 ..... 63  
2.6.4 产品解决方案 ..... 64  
2.7 往来核销 ..... 67  
2.7.1 业务描述 ..... 67  
2.7.2 业务流程 ..... 68  
2.7.3 功能清单 ..... 68

2.7.4 产品解决方案 ..... 69  
2.8 期末处理 ..... 71  
2.8.1 业务描述 ..... 71  
2.8.2 业务流程 ..... 72  
2.8.3 功能清单 ..... 72  
2.8.4 产品解决方案 ..... 73  
2.9 业务单元多版本 ..... 80  
2.9.1 业务描述 ..... 80  
2.9.2 业务流程 ..... 81  
2.9.3 功能清单 ..... 81  
2.9.4 产品解决方案 ..... 82  
第三章 初始准备 ..... 83  
3.1 管控模式 ..... 83  
3.2 企业建模平台 ..... 83  
3.2.1 多组织管理 ..... 83  
3.2.2 基础数据维护 ..... 86  
3.3 财务管理 ..... 88  
3.3.1 财务会计基本档案 ..... 88  
3.3.2 总账 ..... 89  
第四章 操作指南 ..... 92  
附录 附录 1：控制点 ..... 93  
附录 2：查询报表 ..... 95  
附录 3：总账转账、报表函数名应用英文缩写变更 ..... 101  
附录 4：本文参见其他手册清单 ..... 104

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供业务需求与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关本模块的主要业务场景、流程、以及对应的业务功能的介绍；第三部分是初始准备设置；第四部分是关于本模块功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录中对一些可能需要对照查询的关键点进行了补充说明，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《产品手册-组织管理》-----深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助----针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《产品手册-流程管理》----提供关于交易类型、流程设计工具的应用指导。

4. 《产品手册-基础数据》——可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

## 名词解释

周期性凭证Recurring Entry: 源自SAP、Oracle等国外软件中的概念，指在一定有效期范围内，按一定周期反复做的业务，例如待摊费用、预提费用、折旧费用等。

内部交易协同 Internal transaction collaboration: 指的是根据协同业务设置的内部各成员单位之间的科目对应关系，由一方单位的凭证自动生成另一方单位凭证的"协同凭证"功能。

协同凭证 collaboration voucher: 集团各核算主体完成内部交易、内部往来业务时，与一笔内部交易、内部往来业务相关的两张或多张凭证，即协同凭证。协同凭证可以为合并报表系统确定内部交易业务提供数据基础。

## 第一章 概述

### 1.1 产品概述

总账作为财务会计系统的核心，除了满足企业日常基本财务核算工作中常用的凭证管理、往来核销管理、汇兑损益处理、自定义转账、期末处理、常用账簿查询等业务要求外，同时提供有现金流量分析及查询、账簿间财务折算、各财务组织间的内部交易对账与内部交易协同等特殊业务功能。总账系统使用时以财务核算账簿为主组织，因此可按不同账簿分别灵活设置其业务流程。

总账产品在组织管理和基础数据基本搭建完毕的基础上，可直接填制凭证，也可由财务核算的其他系统（存货核算、资产核算、费用预算、应收/付管理、报销管理等）经会计平台向总账传递凭证；无论是会计平台传递，还是总账直接形成的凭证均可提供给企业报表及合并报表调用；同时总账凭证也可受费用预算或全面预算的管控。产品功能架构如下图所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="6">财务领域产品架构</td></tr><tr><td colspan="2">层次（领域）</td><td colspan="3">模块</td><td style='text-align: center; word-wrap: break-word;'>集成（第三方接口）</td></tr><tr><td colspan="2">企业绩效管理</td><td style='text-align: center; word-wrap: break-word;'>全面预算财务分析</td><td style='text-align: center; word-wrap: break-word;'>企业报表分析报表</td><td style='text-align: center; word-wrap: break-word;'>合并报表合并账簿</td><td rowspan="2">数据交换管理</td></tr><tr><td colspan="2">战略工具</td><td colspan="2">商业分析平台</td><td style='text-align: center; word-wrap: break-word;'>财务分析</td></tr><tr><td colspan="2">财务领域</td><td style='text-align: center; word-wrap: break-word;'>总账固定资产</td><td style='text-align: center; word-wrap: break-word;'>应收管理存货核算</td><td style='text-align: center; word-wrap: break-word;'>应付管理税务管理</td><td style='text-align: center; word-wrap: break-word;'>数据交换管理</td></tr><tr><td colspan="2">UAP平台</td><td style='text-align: center; word-wrap: break-word;'>报表平台</td><td style='text-align: center; word-wrap: break-word;'>分析平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>银行账户现金流量项目</td></tr><tr><td colspan="2">标准化</td><td style='text-align: center; word-wrap: break-word;'>会计科目币种</td><td style='text-align: center; word-wrap: break-word;'>收支项目外币汇率</td><td style='text-align: center; word-wrap: break-word;'>会计期间凭证类别</td><td style='text-align: center; word-wrap: break-word;'>银行账户现金流量项目</td></tr></table>

<div style="text-align: center;">图 1.1-01 产品功能架构图</div>

### 1.2 产品价值

1\. 同一财务组织可按不同报告要求建立多个核算账簿，各核算账簿的会计科目、本位币、会计期间可以不相同，以满足境外上市、境外设立分支机构集团企业核算要求。

2. 提供两种二级核算单位核算模式：同一法人公司下各自独立经营的业务单元，可统一在公司的核算账簿中核算，用业务单元来区隔数据；也可以按业务单元分别建立各自的核算账簿独立核算。

3. 总账支持财务组织多版本，通过设定财务组织版本的有效期来实现与基础数据的有效性进行对应，满足企业在跨年度、跨公司场景下组织机构变动与科目体系变动后对于历史数据的保存和查询使用。

4. 日常凭证处理可通过参数配置方式，满足多种处理流程，如：制单——审核——记账；制单——记账；制单——出纳签字——审核——记账；制单——审核——出纳签字——记账。凭证可挂接原始单据附件。

5. 总账支持多币种与多主币：

1）多币种：同一科目核算多个币种、不同科目核算不同币种。

2）支持多主币：每笔业务最多可记录四种货币金额。

a）原币金额：交易发生货币金额；

b) 组织本币：每个财务组织自己的核算本位币金额；

c) 集团本币：记录满足集团报告要求的集团本位币金额；

d）全局本币：满足全局（跨所有集团）报告要求的全局本位币金额。

6. 灵活快捷的内部交易处理：

1）内部交易对账：内部交易双方自动对账，自动生成对账报告。

2）内部交易协同：内部交易双方凭证自动协同生成。

7. 月末处理：

1) 各种类型转账凭证自动生成：通过灵活的公式配置，按科目+辅助核算进行结转、分摊、归集；自动结转汇兑损益。

2）对账：月末可以进行总账与固定资产、资金结算、应收、应付、存货对账。

3) 关账：为了保证本月日常业务已完成，可以进行各种月末处理工作，需对当月日常业务进行关账。以保证月末处理的正确性。总账部分科目可进行提前关账，提前关账后，成本系统才能依据提前关账的

科目进行月末处理。新增批量关账功能，并支持在总账本期关账后，上游系统单据自动生成下期凭证的模式。

4) 结账：当月所有业务全部完成，可进行结账。支持跟企业报表进行月度一致性检查，确保账表数据相符，并可控制总账的反结账。

8. 现金流量分析与查询：可在录入业务凭证时直接记入现金流量项目，也可在事后按规则自动分析生成现金流量项目数据。并根据现金流量分析的结果，按照指定的查询条件查询一定日期范围内各现金流量表项的数据分配情况

9. 分布式应用：对于大型集团企业，可按板块子集团分别部署多个 NC 系统并实现管控政策的下发，子集团板块 NC 系统的本机政策、基础档案与业务数据可以按照预定要求定期上传和同步。

## 第二章 应用场景

### 2.1 会计科目管控

#### 2.1.1 业务描述

会计科目管控指的是会计科目的分级使用管理，体现集团会计政策管控的要求，随集团组织机构设置的不同而形成相应的管理形态。

多集团的各组织机构形式如 2.1-1 图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_112_1109_1083_1365.jpg" alt="Image" width="81%" /></div>


多集团组织机构示意图

<div style="text-align: center;">图 2.1-1 多集团组织机构图</div>


根据组织机构图，会计科目的多级管控如图 2.1-2 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_176_1082_957.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.1-2 科目多级管控业务模型</div>


## 说明：

● 从母集团开始建立会计科目，形成科目表并逐级下发，构成科目表树。

● 各级科目表在上级科目表下发科目的基础上，可自建科目，也可对继承自上级科目表的科目细化（如追加下级明细或末级科目）。

● 各财务组织（集团总部、子集团、公司等）通过引用不同的科目表来实现各自的核算要求；有时会跨级引用，例如子公司直接选用集团总部制定的科目表。

● 科目表的制定者和使用者可能相同，也可能不同。

● 科目表设置的层级不同将形成不同级次的管控模式（统一管控、二级管控、多级管控）：

➢ 统一管控模式：母集团统一设置一或多个科目表（多个科目表时可以分级）供下级单位使用，通常科目表的设计者不是使用者，多用于集权度高的集团企业。

➢ 二级管控模式：各子集团可按自身的管理需求，制定科目表并下发给本集团所属各级财务组织，多用于按子集团运作为主的多元产业集团。

➢ 多级管控模式：分子公司在子集团下发科目表的基础上细化科目表，分别形成本单位的科目表进行使用，有时也提供给下级单位或其他平级单位；科目的使用者是制定者的情况居多。

● 会计核算要求一致的财务组织间，即便不处在一个组织机构层级上，也能共享同一套科目表。

● 上级科目表预留的科目，下级科目表自建时不能占用。

● 上级科目表中科目变动时，如插入中间级科目、增加末级科目，对下级科目表造成影响应可控。

● 组织机构变动时，若不改核算政策，科目表可不变；若调整核算政策则重新引用科目表。

#### 2.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_262_990_1296.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">图 2.1-3 科目多级管控业务流程</div>


## 说明：

● 母集团集中创建科目体系，每一科目体系自动携带一套根科目表；

● 母集团集中创建、维护根科目表。

● 新创建的科目表默认携带一套科目控制规则，该规则可修改，也可新增控制规则。

● 每套科目控制规则下可挂一至多个下级科目表，下级科目表同时受上级科目表及所对应的科目控制规则约束；如此逐层建立形成科目表树形结构。

● 按科目表进行版本化管理，调整科目或形成新的版本，并按版本指定其生效日期。

● 母集团、各子集团及财务组织均可以选择科目控制规则创建各自的科目表，但最终必然按科目体系形成一套统一的科目表树。

● 每个科目表即是一套会计科目，无论是母集团、子集团、财务组织，其所设置的下级科目表可在继承上纫科目表科目的基础上自建或细化科目。

● 根据组织层级，母集团只能选用母集团所设的各级科目表；子集团可选用母集团及本子集团所设的科目表；财务组织可选用母集团、本子集团或本组织所设置的科目表。

#### 2.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="6">企业建模</td><td rowspan="5">基础数据</td><td style='text-align: center; word-wrap: break-word;'>科目体系</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目-全局</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目-财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目表版本对比</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>财务核算账簿</td></tr></table>

#### 2.1.4 产品解决方案

● 【科目体系设置】节点确定科目编码规则及科目类型。每建立一个科目体系自动生成该体系的根科目表，由全局级科目表开始往下逐级应用。

科目体系设置时，可指定科目属性控制策略，系统预置 15 项受控属性，支持 5 个自定义属性的控制策略设置，控制策略按不同属性可分别选择 “不控制、严格控制、部分控制” 等属性项，如图 2.1-4 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_180_170_1014_841.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.1-4 科目属性策略设置</div>


## ● 多科目表分级设置：

全局级、集团级、财务组织级的会计科目节点中，均可按层级设置多个科目表，但下级科目表的科目控制级次不能超出上级科目表的控制级次。控制级次的次序为：不控制->控制到1级->控制到2级->...控制到末级；

例如：图 2.1-5 的示例中 1 到 3 级科目表的控制级次已确定，则对 “y 全局四级” 表来说：

1、本表的科目级次规则只能设为“控制到末级”；

2、只能在“y 全局三级”表分给的末级科目基础上增加下级科目，但“y 全局三级”自建且未分配的科目不受影响：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>科目表</td><td style='text-align: center; word-wrap: break-word;'>所属上级科目表</td><td style='text-align: center; word-wrap: break-word;'>科目控制级次</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基层医疗卫生机构基准科目表</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>不控制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>y全局二级</td><td style='text-align: center; word-wrap: break-word;'>基层医疗卫生机构基准科目表</td><td style='text-align: center; word-wrap: break-word;'>控制到2级</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>y全局三级</td><td style='text-align: center; word-wrap: break-word;'>y全局二级</td><td style='text-align: center; word-wrap: break-word;'>控制到末级</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>y全局四级</td><td style='text-align: center; word-wrap: break-word;'>y全局三级</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_131_363_1062_803.jpg" alt="Image" width="78%" /></div>


资料目表的控制频次为末级，则当前科目表的控制频次必须为末级！

<div style="text-align: center;">图 2.1-5 科目表控制规则示例</div>


☑ 科目控制规则----确定各级科目表的管理颗粒度：

每个科目表配置一或多个科目控制规则，科目表创建时自动携带一个默认规则，用户可修改该默认规则或直接增、减科目控制规则，除根科目表外，任何一个科目表要对应于上级科目表的某个科目控制规则并受其约束。如图 2.1-6 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_1010_1103_1402.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2.1-6 科目表控制规则查询界面示意</div>


上级科目表可以将本表的全部或部分科目共享给下级科目表，部分共享时，若上级科目表新增末级科目，需在科目控制规则中增补新增加的科目，新增科目才会被共享到下级科

目表中；上级科目表中已经存在但是没有分配给下级科目表的，下级科目表可增加重复的科目，如图图 2.1-7 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_250_1086_918.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.1-7 科目表科目共享与分配界面示意</div>


科目控制规则可选择全部或指定部分财务组织进行细化，若指定部分组织则只有被指定的财务组织可创建该科目控制规则所属科目表的下级科目表。

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_170_1086_836.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.1-8 科目表控制规则中可细化组织界面示意</div>


各级科目表对继承自上级科目表的科目，可增补其辅助属性，或添加下级明细科目，可增加的下级明细科目受当前科目表的科目控制级次制约。

科目控制规则中取消某会计科目的分配时，该科目必须未被所有下级科目表引用。

科目控制规则中增补或取消共享某会计科目时，基于该规则产生的所有下级科目表都同步追加或者删除该会计科目。

■ 预留科目控制：预留科目指当前科目表为将来可能增加的科目预先指定好一个编码范围，用以限制该规则对应科目表的所有下级科目表不得增加编码在预留范围内的科目。

预留规则仅作用于受该规则约束的下级科目表，创建该规则的当前表及与当前表平级的其他科目表不受影响。

系统提供三类预留类方式：A、指定的科目编码，例如：1125；B、科目编码区间，例如：1015-1018，表示从1015到1018的科目都将预留；C、科目编码宏代换，例如：假定科目编码规则为4/2/2，则11239*表示1123的二级科目中以9打头的被预留，1123**则表示1123的二、三级科目全被预留。

预留规则设置时，不能指定当前表的所有下级科目表已存在的科目。

预留规则随科目表被下级科目表逐级继承，下级科目表继承上级表的预留规则后不能修改，但可增补属于自己的预留规则。

当前科目表的所有下级科目表创建有了编码在预留范围内的科目，则上级科目表不能再设置科目编码预留规则。

◆ 科目表与财务核算账簿间的引用关系可在科目表设置时统一分配，也可在财务核算账簿启用时选择，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_329_1043_1432.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.1-9 科目表与核算账簿的引用关系界面示意</div>

◆ 科目控制规则、科目表反映集团核算的多级管控要求，不受组织结构变动的影响；组织机构调整后，若核算要求有变则换用科目表，未变则不变化。

◆ 说明：针对实际业务中子集团或者某个公司直接独立建立科目表的业务，NCV6.33 产品仍采取自根科目表开始设置的科目控制方案，再在该基础上自由创建科目，以保证科目有明确归属的科目体系，清晰化科目结构与层次。

◆ 科目表的版本化管理：

■ 科目表版本化用于定格之前使用的科目表以及科目，以便查询历史业务数据；

■ 科目表的不同版本按照生效日期区分，新版本的生效日期要大于之前版本的，且必须晚于当前服务器时间；

■ 科目表产生了新版本后，该科目表的所有下级科目表都同步产生一个新版本，用于承载上级科目表对于会计科目的变动

■ 科目表对已下发科目进行修改，或插入中间级科目时，必须先版本化，再作相应处理，以便修改同步到下级科目表中：

☑ 一个科目表的多个版本不改变其所依赖的科目控制方案；

■ 核算账簿财务组织在指定科目表时，需要同时指定科目表的有效期间（按照账簿的会计期间方案设置），同一核算账簿的科目有效期需要连续。

■ 科目表新版本只有当前表及所有下级表的新版本未被业务引用，才允许删除，删除执行时所有下级科目表同步删除，沿用被删版本之前最近的版本。

### 2.2 总账日常核算（凭证管理）

财务核算记录日常发生的经济业务，经济业务在财务核算中体现为会计凭证，因此会计凭证管理是财务核算的核心内容。NCV6.33 产品中会计凭证来源包括手工直接录入、各类业务单据通过会计平台生成总账凭证、通过接口从外部系统导入。总账的凭证管理主要包括凭证保存、出纳签字、凭证审核、凭证记账、凭证冲销和凭证打印等业务操作，同时，还支持调整期凭证录入与管理、协同凭证生成、凭证即时折算、现金流量即时分析、联查预算、联查序时账等协作性业务。

#### 2.2.1 业务描述

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_249_1036_808.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.2-1 总账凭证管理业务</div>


说明：

重要业务处理基本在填制凭证环节就可完成。

◆ 会计角色业务处理：

■ 根据原始凭单录入凭证，录入过程中可暂存，录完后保存凭证；

■ 查询已存凭证是否经会计主管/出纳审核通过，未通过则修改；

◆ 财务主管业务处理：

■ 打印要存档的会计凭证。

☑ 根据凭证发生业务，进行凭证审核；

☑ 对有错凭证标错，退回会计；

对审核通过的凭证汇总、记账，准备出报表。

☑ 出纳人员业务处理：

审核有现金类科目的凭证；

☑ 记录涉及现金类科目的结算信息；

☑ 执行现金结算。

快速形成分摊凭证：既可按核算对象在同一会计期间快速分摊，也可将同一笔核算业务在多个期间进行分摊：

按核算对象在同一会计期间快速分摊；

■ 同一笔核算业务在多个期间进行分摊。

在凭证分录上记录业务日期，反映分录所核算业务的实际发生日期：

☑ 参照核销：

在总账中处理应收账款核销业务，收款凭证中核销号参照应收账款的核销号生成；

在总账中处理预收账款核销业务，应收账款凭证中核销号参照预收款的核销号生成；

总账凭证复制后凭证以制单日期的汇率为准。

凭证批量导入后的制单人为导入操作人，避免凭证制单人和导入操作人不一致，规范制单操作行为。

凭证中辅助核算项可以跨组织选择人员档案，实际业务中，不启用前端业务模块时，可在总账中解决跨组织或部门人员费用报销。

#### 2.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_137_281_1051_1252.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2.2-2 不同参数管控下的凭证管理流程</div>


说明：

凭证管理核心业务可分为制单、审核、签字和记账几个环节。

凭证管理各类业务操作可通过参数化配置设成不同的次序，如：

■ 制单-->审核-->签字-->记账

制单-->签字-->审核-->记账

■ 制单-->记账

■ 制单 -->审核 -->记账

■ 制单->签字->记账

除核心业务外，凭证管理功能还包括凭证样式的定制，凭证定制指凭证表体各栏目的显示风格及行高设置，支持按制单、签字、审核、查询、记账、冲销等业务环节将定制的凭证式样分配给不同账簿中的相关操作用户。

凭证从制单开始，直至记账、冲销各环节均支持各种状态下的即时查询。

#### 2.2.3 功能模型


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>初始设置-分摊规则\n凭证管理-定制\n凭证管理-制单\n凭证管理-签字\n凭证管理-审核\n凭证管理-记账\n凭证管理-查询\n凭证管理-冲销\n凭证管理-凭证整理\n周期凭证-周期凭证定义\n周期凭证-周期凭证执行\n往来核销-核销对象设置</td></tr></table>

#### 2.2.4 产品解决方案

在业务单元级参数中执行总账参数设置组合可实现不同的业务场景：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL130</td><td style='text-align: center; word-wrap: break-word;'>本期关联，上游系统单据是否生成下...</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL001</td><td style='text-align: center; word-wrap: break-word;'>是否需要出纳签字</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL003</td><td style='text-align: center; word-wrap: break-word;'>凭证审核后才能记账</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL030</td><td style='text-align: center; word-wrap: break-word;'>是否允许反结账</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL032</td><td style='text-align: center; word-wrap: break-word;'>结账检查损益结平</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL036</td><td style='text-align: center; word-wrap: break-word;'>制单后是否立即打印</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>GL039</td><td style='text-align: center; word-wrap: break-word;'>凭证是否自动补号</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>☐</td><td style='text-align: center; word-wrap: break-word;'>是否</td></tr></table>

<div style="text-align: center;">图 2.2-3 总账凭证管理流程参数界面示意</div>

■ 制单-->审核-->签字-->记账：GI001 是否需出纳签字---设为“是”；GI003 凭证审核后才能记账---设为“是”；GI091 凭证流程控制方案---设为“先审核后签字”。

制单-->签字-->审核-->记账：GI001是合需出纳签字---设为“是”；GI003凭证审核后才能记账---设为“是”；GI091凭证流程控制方案---设为“先签字后审核”。

■ 制单-->记账：GI001 是否需出纳签字---设为“否”；GI003 凭证审核后才能记账---设为“否”。

■ 制单 -->审核 -->记账：GI001 是否需出纳签字---设为“否”；GI003 凭证审核后才能记账---设为“是”。

制单->签字-->记账：GI001 是否需出纳签字---设为“是”；GI003 凭证审核后才能记账---设为“否”。

凭证审核过程中可标错，标错后由原填制人修改至正确后，凭证审核人需先取消标错内容才能进行审核。

审核人不能审核自己填制的凭证，不能取消他人已审核的凭证；已记账凭证不能取消审核；只能对未审核凭证标错，作废凭证不能标错。

凭证签字时注意参数 “GL088 签字日期生成规则”，若取值为 “系统日期” 时，则不能跨月签字。

凭证一经签字就不能再被修改、删除，只有取消签字后才可修改或删除；取消签字只能由原签字人本人执行。

◆ 未审核且未签字的凭证允许【作废】，作废后的凭证要实现物理删除还应执行凭证的【删除】操作，删除的凭证若非最后一个凭证，所形成的空号通过【凭证整理】节点进行清理。

☑『凭证整理』用于清理凭证的断号、错号，一旦整理会重排凭证号，因此凭证整理务必慎用，且应在凭证正式打印前完成。

☑ 已记账的错误凭证需通过『冲销』节点进行红冲或蓝冲形成新的凭证，再做相应的后续凭证处理。

红冲：指对原凭证生成方向相同金额为负数的凭证；

蓝冲：指对原凭证生成方向相反金额相同的凭证。

☑『制单』节点中凭证填制完毕，保存时易受到各项参数的约束，例如：

■ GL050 凭证原币为 0 是否允许保存；

GL051凭证原币合计不平是否允许保存；

■ GL053 凭证数量为 0 是否允许保存；

■ GL054 凭证是否序时控制；

■ GL055 余额方向控制方式；

■ GL089 保存凭证时是否检查现金流量；

■ GL094 制单是否逐分录对科目的余额进行控制；

■ GL098 保存凭证时是否即时核销；

■ GL096 保存凭证时是否立即检查附单据数；

■ GL107 现金流量是否校验原币金额；

■ GL109 是否支持提前关账，若置为是，则：

✓ 增加凭证时检查凭证制单日期对应的会计期间是否已提前关账；

✓ 若未提前关账，则可保存；

✓ 若已提前关账，则该张凭证只要有一条分录是提前关账的会计科目，整张凭证即不能保存；

■ GL116 是否校验集团本币借贷平衡；

■ GL118 是否校验全局本币借贷平衡。

记账节点中对已审核、已签字的凭证进行过账处理，但需受到各项参数的约束，例如：

■ GL003凭证审核后才能记账；

■ GL066 上月未结账本月是否能记账；

凭证记账前需检查是否已期初建账，只有已期初建账的账簿才能记账，期初建账时支持期初余额按 Excel 格式导入导出。

凭证管理同时具备的协作性功能：

☑ 凭证填制中根据参数 “GL085 外部导入凭证是否允许删除” 的设置可删除外部导入的凭证；

■ 填制凭证时支持即时分析现金流量、核销往来款（GL096 保存凭证时是否即时核销）、协同生成凭证、进行凭证折算（GL095 是否立即生成折算凭证）；

■ 出纳对凭证签字时可补充现金类科目的部分辅助信息

☑ 凭证管理同时支持的便利性功能：

■ 整张凭证的联查：如联查单据、联查原始凭单、汇总显示、联查来源凭证、联查目的凭证、联查现金流量、联查预算等；

☑ 凭证空号查询、凭证查询结果中科目编码与名称的转换、

☑ 凭证中指定分录的联查：如联查余额、联查辅助信息、文档管理等；

凭证及分录的复制、粘贴操作。

已填制凭证的批量处理：如批量签字、批审、批量快速记账等。

## ☑ 快速形成分摊凭证：

按核算对象在同一会计期间快速分摊；

➢ 【财务会计】→【总账】→【初始设置】→【分摊规则】节点中定义分摊规则：

✓ 设置时分摊对象可多选；按分摊对象的取值组合构成表体的各个分摊行；

✓ 分摊方式：若设为平均分摊方式，则表体中不提供“比例”的显示及输入；若设为手工设置方式，则列示“比例”由用户交互输入，输入完后系统自动检查各分摊对象之和是否100%，为否，则报错不予保存。

➢【财务会计】→【总账】→【凭证管理】→【制单】节点中实现快速分摊：

✓ 凭证填制完后，若有满足分摊规则的分录行，则可选择该行后点击【分录-快速分摊】；

✓ 在弹出的窗口中选择分摊规则并确定，则当前分录按分摊规则分解为多行不同辅助核算值的记录。

■ 同一笔核算业务在多个期间进行分摊。

➢ 【财务会计】→【总账】→【周期凭证】→【周期凭证定义】节点中定义周期凭证：

✓ 设置时注意定义起始期间和周期，起始期间决定从何时开始可形成分摊凭证，周期则指定该业务要在各期间分摊的次数；

✓ 分摊的周期类型：若设为按比例，则“比例”栏目可录值，各期比例的总和应等于100%；若设为按金额，则只有“金额”栏目可录值；若设为平均分摊方式，则表体中不提供“比例”的显示及输入；若设为手工设置方式，则列示“比例”由用户交互输入，输入完后系统自动检查各分摊对象之和是否100%，若否，则报错不予保存。

➢【财务会计】→【总账】→【凭证管理】→【制单】节点中录入待分摊凭证，

实现周期性快速分摊----如下两种方式中任选其一可完成分摊凭证的快速生成：

✓ 【财务会计】→【总账】→【凭证管理】→【制单】中点击【常用凭证-周期凭证】，在弹出窗口中选择已定义的周期凭证规则（可选“包含未记账凭证”）后点击【确定】，保存生成的凭证；

✓ 【财务会计】→【总账】→【周期凭证】→【周期凭证生成】中指定会计期间（可选“包含未记账凭证”），选择已定义的周期凭证规则后点击【生成凭证】，并保存生成的凭证。

✓ 无论是【制单】中点击【常用凭证-周期凭证】还是【周期凭证生成】中点击【生成凭证】，所形成的分摊凭证均最终由【制单】节点实现分摊凭证的确认及保存，并回写至【周期凭证定义】，将状态改为“已执行”，此时可点击【联查凭证】查看摊销明细。

☑ 凭证分录上记录业务日期反映分录所核算的业务的实际发生日期：

【财务会计】→【总账】→【凭证管理】→【定制】节点中，可增加“业务日期”字段项并分配给指定账簿、指定操作用户（或操作角色）；

【财务会计】→【总账】→【凭证管理】→【制单】节点中即可按新分配的凭证样式显示“业务日期”，新增第一条分录业务日期默认为制单日期（即登录系统时指定的当前业务日期，若未指定，取服务器系统日期），可修改，但不能晚于制单日期；

若分录中辅助核算的涉及到核销信息，则核销信息默认取该分录的业务日期，可修改，改后回写分录中的原业务日期；

若该分录涉及到结算信息，则结算信息中的票据日期默认取自业务日期，可修改；

➢ 【财务会计】→【总账】→【账簿查询】→【序时账】/【三栏明细账】/【辅助明细账】各节点中，查询条件中增加显示业务日期，查询结果列示可提供业务日期的展示。

☑ 参照核销的实现办法：

【财务会计】→【总账】→【往来核销】→【核销对象设置】中配置会计科目核销的规则，可选是否严格控制辅助核算，若非严格控制则参照会计科目所有未核销的分录，若严格控制则只参照有辅助核算项的未核销分录；

【财务会计】→【总账】→【凭证管理】→【制单】录入应收账款凭证，在分录-辅助信息中录入核销号，完成并保存凭证。新建收款凭证，在行中录入核销的科目后，点击参照核销，在弹出的界面中选择要核销的应收分录行，点击确定之后，收款凭证中需要核销的会计科目行会参照应收账款凭证行生成金额和相反的借贷方向，且可以修改。应收的核销号会带到收款的辅助信息中，完成凭证后保存即核销。核销完成之后，凭证不可以再修改。

【财务会计】→【总账】→【凭证管理】→【制单】录入预收款凭证，在分录-辅助信息中录入核销号，完成并保存凭证。新建收入凭证，在行中录入核销的科目后，点击参照核销，在弹出的界面中选择要核销的预收分录行，点击确定之后，应收凭证中需要核销的会计科目行会参照预收账款凭证行生成金额和相反的借贷方向，且可以修改。预收的核销号会带到应收的辅助信息中，完成凭证后保存即核销。核销完成之后，凭证不可以再修改。

总账凭证复制后汇率的取数以凭证复制后的制单日期的汇率为准。例如，原凭证制单日期是1日，凭证复制后的制单日期是9日，那么复制后的凭证取9日的汇率作为核算汇率。

总账凭证为增量导入，导入后凭证的制单人以操作人为准。

◆ 总账凭证中辅助核算项中的人员档案可以跨组织和部门选择人员。设置部门和人员的交叉效验规则后，在制单时，会计科目的辅助核算项，可以根据人员自动带出部门，人员档案，可以跨组织和部门选择。

在基础数据会计信息会计科目中增加科目的辅助核算项人员档案，启用之后在总账凭证行中可以使用人员档案辅助核算项。

### 2.3 多账簿管理

多账簿起源于集团企业中的财务组织需要对财务账簿按多规则进行反映和统计，核心在于账簿分离，如图 2.3-1 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_269_1029_920_1484.jpg" alt="Image" width="54%" /></div>

<div style="text-align: center;">图 2.3-1 多账簿业务模型</div>


根据组织机构和财务考核要求的不同，多账簿应用通常可分为跨国集团（境外分支机构、境外上市）应用、跨行业集团、内部管理和对外报告两套账、多责任中心、外币分账制等模式，其中尤以跨国集团应用最为典型。

各应用模式按分账标准、分账层次、所使用的科目、核算流程、权限控制、凭证记录方式等方面各有其要求，详见下表：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分析项目</td><td style='text-align: center; word-wrap: break-word;'>跨国集团</td><td style='text-align: center; word-wrap: break-word;'>跨行业集团</td><td style='text-align: center; word-wrap: break-word;'>内外两套账</td><td style='text-align: center; word-wrap: break-word;'>多责任中心</td><td style='text-align: center; word-wrap: break-word;'>外币分账制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分账标准</td><td style='text-align: center; word-wrap: break-word;'>按会计制度分账</td><td style='text-align: center; word-wrap: break-word;'>按行业分账</td><td style='text-align: center; word-wrap: break-word;'>按管理要求分账</td><td style='text-align: center; word-wrap: break-word;'>按责任中心分账</td><td style='text-align: center; word-wrap: break-word;'>按币种分账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分账层次</td><td style='text-align: center; word-wrap: break-word;'>集团/公司</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>公司</td><td style='text-align: center; word-wrap: break-word;'>公司</td><td style='text-align: center; word-wrap: break-word;'>公司</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目</td><td style='text-align: center; word-wrap: break-word;'>不同国家会计科目不一致</td><td style='text-align: center; word-wrap: break-word;'>不同行业账的科目通常不一致</td><td style='text-align: center; word-wrap: break-word;'>内、外账的科目通常不一致</td><td style='text-align: center; word-wrap: break-word;'>各责任中心共享一套</td><td style='text-align: center; word-wrap: break-word;'>各币种账共享一套</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>流程参数</td><td style='text-align: center; word-wrap: break-word;'>不同公司不同国家账参数不同</td><td style='text-align: center; word-wrap: break-word;'>不同公司不同行业账的参数不同</td><td style='text-align: center; word-wrap: break-word;'>同一公司内账、外账的参数可能不一致</td><td style='text-align: center; word-wrap: break-word;'>同一公司参数可能不一致</td><td style='text-align: center; word-wrap: break-word;'>同一公司一套参数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>权限</td><td style='text-align: center; word-wrap: break-word;'>不同公司不同国家账的权限不同</td><td style='text-align: center; word-wrap: break-word;'>各行业的公司不同，按公司赋权</td><td style='text-align: center; word-wrap: break-word;'>内、外账的具体功能权限、数据权限不一致</td><td style='text-align: center; word-wrap: break-word;'>权限可能不一致</td><td style='text-align: center; word-wrap: break-word;'>权限一致</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证记录</td><td style='text-align: center; word-wrap: break-word;'>同一笔业务按不同会计制度生成不同凭证</td><td style='text-align: center; word-wrap: break-word;'>按业务直接形成各自行业凭证</td><td style='text-align: center; word-wrap: break-word;'>业务数据形成内、外账各自的凭证</td><td style='text-align: center; word-wrap: break-word;'>业务数据按责任中心形成凭证</td><td style='text-align: center; word-wrap: break-word;'>业务数据生成不同币种的凭证</td></tr></table>

<div style="text-align: center;">表 2.3-1 多账薄应用模式比较</div>

#### 2.3.1 跨国集团

##### 2.3.1.1 业务描述

A境外上市模式：

<div style="text-align: center;"><img src="imgs/img_in_image_box_112_380_1081_1048.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.3.1-1 跨国集团多账簿业务</div>


## 说明：

☑ 跨国集团的集团总部和分、子公司均是独立的法人主体。

跨国集团按组织结构模式通常分为如下三种（后两种也可合并为境外设立分支机构），但其实质是集团内各财务组织要遵循多个不同的会计准则或制度进行会计核算，为此需按会计准则分账：

☑ 国内集团企业海外多地上市

■ 国内企业在海外设立分支机构

■ 国外企业在国内设立分支机构

既可按集团，也可按公司进行分账，境外上市模式要求集团和各子公司都要同时分设境内账和上市所在地账；境外设分支机构模式则只需境外公司分设境内账和境外账；

分账后各账簿间的权限要求不同；

通常情况下对应于不同会计准则的核算账簿，其会计科目、期间、币种会有所不同，核算流程也可能不一致；

同一笔会计业务按不同会计准则分别形成各个账簿间的会计凭证。

##### 2.3.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_133_420_1054_1253.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.3.1-2 多账簿总体应用流程</div>


说明：

应用准备环节中，建立责任核算账簿主要用于内外两套账的业务模式，该模式下，责任核算账簿建立后的应用由管理会计领域说明，本章节不赘述。

凭证协同方式应用于跨行业集团、多责任中心业务模式，该模式下通过协同方式在多个账簿间传递凭证。

◆跨财务组织间的不同币种账簿直接协同。例如 A 公司 A1 账簿设人民币为记账本币，B 公司 B1 账簿设美元为记账本币，B2 账簿设人民币为记账本币，则只能 A1 和 B2 协同，B2 折算给 B1。

##### 2.3.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="10">建模平台</td><td rowspan="2">组织管理</td><td style='text-align: center; word-wrap: break-word;'>账簿类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务核算账簿</td></tr><tr><td rowspan="4">基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目</td></tr><tr><td rowspan="4">会计平台</td><td style='text-align: center; word-wrap: break-word;'>入账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>转换模板</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据生成</td></tr><tr><td rowspan="5">财务会计</td><td rowspan="5">总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-记账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折算规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证折算</td></tr></table>

##### 2.3.1.4 产品解决方案

多账簿的应用需先定义会计期间、币种、科目体系、会计科目等基础档案项备用，可分别进入如下节点进行设置，相关操作可参见《基础数据手册》相关章节：

☑ 【企业建模平台】→【基础数据】→【公共信息】→【会计期间】

☑ 【企业建模平台】→【基础数据】→【公共信息】→【币种】

☑ 【企业建模平台】→【基础数据】→【会计信息】→【科目体系】

☑ 【企业建模平台】→【基础数据】→【会计信息】→【会计科目-全局/集团/财务组织】

☑ 进入【企业建模平台】→【组织管理】→【组织结构定义】--【账簿类型】中定义账簿类型，以确定用于各核算账簿的会计期间方案、科目体系和本位币(如下图所示)。

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_171_1042_430.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.3.1-3 账簿类型设置</div>


在业务单元已建好财务组织的基础上，在【企业建模平台】-【组织管理】-【组织结构定义】-【财务核算账簿】中定义各组织的账簿，注意勾选“允许折算”以便后续执行折算处理。套用不同会计准则的账簿在此处需要选择适用的科目表。(如下图所示)。

<div style="text-align: center;"><img src="imgs/img_in_image_box_178_605_1012_965.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.3.1-4 核算账簿设置</div>


同一笔业务同时在多个账簿间记录是多账簿业务处理的重点和难点，系统提供了多种方式，如图2.3.1-5所示：

账簿间直接折算，直接折算又细分为即时折算和批量折算两种模式；

☑ 会计平台生成凭证（相关内容可查阅《会计平台》手册内容）；

各组织间凭证协同（凭证协同的处理见本书 2.4 内部交易核算的相关内容）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_111_167_1080_1024.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.3.1-5 多账簿的凭证传递方式</div>


◆ 账簿间凭证折算无论是填制凭证时直接折算，还是记账后的批量折算，均要提前设置好折算规则，折算规则设置流程如图 2.3.1-6 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_390_174_849_680.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">图 2.3.1-6 折算规则设置流程</div>


■ 折算规则参数：指定当前规则所应满足的条件，以及折算凭证的生成方式，应注意：

指定规则对应的来源账、目的账，每个来源账对同一目的账簿只能设置一套折算规则，但每套折算规则下可设置多个明细规则，并指定默认的明细规则；

若折算后的金额不平，应指定是将差额写入指定的补差科目还是提示后不予生成，设为“不生成”时需在目的账簿中手工输入凭证；

若制单人/出纳/审核人/记账人非空，则生成目的账簿凭证时，折算凭证的相关操作员取指定操作人员，为空则按源账簿凭证的相关操作员形成；

若勾选“实时折算”，则可作为在【制单】中执行【即时折算】时可供选择的规则，未勾选则不提供参选。如图 2.3.1-7 所示

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_159_1028_1215.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.3.1-7 实时折算规则设置与制单间关系界面示意</div>


折算生成凭证自动记账：对源账簿已记账凭证执行批量折算时，生成的折算凭证将自动在目的账簿记账。

关联完整账簿/差异账簿：只能在同一财务组织间选择差异账簿方式，且差异账簿只能被选择一次。

折算规则明细设置，此时即为设定一对来源账簿和目的账簿间的多个明细折算规则：

➢ 币种折算方式：

默认规则：勾选后在【财务会计】→【总账】→【凭证管理】→【制单】节点执行【即时折算】，或在【财务会计】→【总账】→【财务折算】→【凭证折算】节点执行【折算】时，该规则将被自动选入。

“科目对照”组中“无对应科目处理方式”若选择提示且不生成时，需在目的账簿中视需要手工输入凭证。

☑ 直接折算：指填制凭证时直接折算，需要注意：

■ 业务单元级参数 “G1095 是否立即生成折算凭证” 设为 “是” 时，凭证保存前将弹出凭证折算规则选择窗口供用户选择，也可不选当前规则，而在以后进入 “制单” 节点选该凭证执行即时折算；

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_468_1077_967.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.3.1-8 不直接折算界面示意</div>


G1095 参数设为否时，涉及到要折算的凭证也可在填制凭证时，保存前可手工触发即时折算，或执行批量折算处理；

凭证立即折算成功后，可在制单中按不同核算账簿联查当前凭证的来源凭证或目的凭证。

☑ 支持不同本位币的账簿间期间初余额折算。

☑ 批量折算：凭证记账后才可参与批量折算。

协同生成凭证的凭证传递方式参见 2.4 内部交易核算章节；会计平台生成凭证的传递方式参见会计平台手册。

凭证审核、记账的业务操作参见产品在线帮助。

#### 2.3.2 跨行业集团

##### 2.3.2.1 业务描述

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_366_987_629.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 2.3.2-1 跨行业集团的多账簿业务</div>


说明：

☑ 跨行业集团的集团总部及其下属工业子集团、旅游业子集团、商业子集团都是独立的法人主体。

企业集团的成员企业往往覆盖多个行业，成员企业间业务并不相关，为满足不同行业会计报告的要求，需分别设账。

集团内的成员企业间关系分为两类：

■ 成员间可能存在内部交易，集团需要在财务层面上统一协调与控制各投资对象，以财务预算为前提，以资金管理为手段，以会计核算为基础，集中监控或考评子公司的财务；

成员间没有任何关系，上层集团一般采用汇总报表和合并报表的方式来监控、评价下层各企业(或集团)。

集团统一设置会计期间，分行业设置会计科目和对应账簿体系，按业务直接形成各自行业凭证。

◆ 账簿体系为满足合并报表的需要，可以对集团内部的经济业务进行特别的标记，形成内部业务的明细账簿，内部经济业务包括：

☑ 集团内部的股权投资；

☑ 内部收益与内部应收、应付股利；

☑ 内部债权债务；

☑ 内部存货、固定资产、无形资产；

相关损益结转与利润分配。

##### 2.3.2.2 业务流程

◆ 同 2.3.1 节的业务流程说明，若存在内部交易业务，则日常业务处理时应进行凭证协同处理。

##### 2.3.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="11">建模平台</td><td rowspan="3">组织管理</td><td style='text-align: center; word-wrap: break-word;'>账簿类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务核算账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>责任核算账簿</td></tr><tr><td rowspan="4">基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目</td></tr><tr><td rowspan="4">会计平台</td><td style='text-align: center; word-wrap: break-word;'>入账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>转换模板</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据生成</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>凭证管理-记账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>折算规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>凭证折算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>公有协同设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>公有协同中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>公有协同确认</td></tr></table>

##### 2.3.2.4 产品解决方案

☑ 应用操作基本和 2.3 节的产品解决方案相同。

跨行业集团因涉及科目不同，折算规则中务必注意源账簿和目的账簿的科目对应关系。

☑ 内部交易的功能处理要点参见 2.5 内部交易核算章节的内容。

#### 2.3.3 内外两套账(内外报告分离)

##### 2.3.3.1 业务描述

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_355_1004_550.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 2.3.3-1</div>


说明：

◆ 集团总部从考核角度出发，对各子公司的收入、成本、费用进行划分，这种划分可能与会计制度对这些会计要素的规定不完全相同。

需要分别按会计制度规定（财务核算账，也称外账）和企业内部管理规定（管理会计账，也称内账）分别处理同一原始业务，形成内、外账各自的凭证和账簿记录，据此分别形成对外财务报表和内部管理报表。

企业集团存在多级法人结构，从集团总部到公司的每个法人企业均按管理要求分设内、外账簿：

☑ 内、外账在会计期间和记账本位币上没有区别；

☑ 内、外账的科目通常在科目核算体系或科目明细程度上会有所不同；

■ 大部分业务同时在内、外两个账簿中记账，且记账科目与金额相同；少量业务在这两套账中记账的科目、金额有区别；还有少量业务只在对内的账簿中记账。

##### 2.3.3.2 业务流程

需要同时建立财务核算账簿和责任核算账簿。

◆ 管理会计单独运用（内账），详见管理会计手册。

◆ 内、外账之间通过会计平台相互传递凭证，详见会计平台手册中相关内容。

##### 2.3.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">建模平台</td><td rowspan="3">组织管理</td><td style='text-align: center; word-wrap: break-word;'>账簿类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务核算账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>责任核算账簿</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="8"></td><td rowspan="4">基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目</td></tr><tr><td rowspan="4">会计平台</td><td style='text-align: center; word-wrap: break-word;'>入账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>转换模板</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据生成</td></tr><tr><td rowspan="8">财务会计</td><td rowspan="8">总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折算规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证折算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公有协同设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公有协同中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公有协同确认</td></tr></table>

##### 2.3.3.4 产品解决方案

在【企业建模平台】→【组织管理】→【组织结构定义】→【账簿类型】中建立责任核算账簿类型；

在【企业建模平台】→【组织管理】→【组织结构定义】→【责任核算账簿】中建立责任核算账簿；

☑ 外部账的操作与总账日常核算场景中的相同；

☑ 内部账凭证的形成方式有两种：

在【管理会计】→【责任会计】中执行相关处理，详细解决方案可查阅《责任会计》手册相关部分；

通过【企业建模平台】→【会计平台】→【单据生成】中由业务单据生成。

#### 2.3.4 多责任中心(财税分离)

##### 2.3.4.1 业务描述

模式A：多责任中心----事业部非法人，单独核算但不对外报送报表

<div style="text-align: center;"><img src="imgs/img_in_image_box_153_411_928_827.jpg" alt="Image" width="65%" /></div>


模式B: 财税分离----分公司非法人但报税

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_944_1041_1377.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.3.4-1</div>


说明：

企业整体是一个法人单位，下属可能有独立核算的分公司或事业部。

◆ 下属单位不具有独立的法人资格，但在地域上比较分散，实行独立核算或被授予内部法人的地位

◆ 下属单位是否独立核算都不具有真实法人地位，但因地域原因，某些业务需向分公司所在地交税，因此需向当地税务部门提供交税业务按会计制度规定口径的税务报告。

各下属单位独立核算时，所用的会计科目、会计期间、币种相同，但核算流程与计量规则上可能存在差别，且各责任中心间发生的内部业务，需要协同记账。

公司对外业务需在公司级账簿中反映，形成对外财务报告，并按责任关系同时记录到某责任中心的账上。

##### 2.3.4.2 业务流程

同 2.3.1 节的业务流程。

##### 2.3.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="11">建模平台</td><td rowspan="3">组织管理</td><td style='text-align: center; word-wrap: break-word;'>账簿类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务核算账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>责任核算账簿</td></tr><tr><td rowspan="4">基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目</td></tr><tr><td rowspan="4">会计平台</td><td style='text-align: center; word-wrap: break-word;'>入账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>转换模板</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据生成</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td></tr><tr><td rowspan="7"></td><td rowspan="7"></td><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-记账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折算规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证折算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公有协同设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公有协同中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公有协同确认</td></tr></table>

##### 2.3.4.4 产品解决方案

☑ 有几个责任主体便建立几个财务组织。

☑ 应用操作基本和 2.3 节的产品解决方案相同。

☑ 跨行业集团因涉及科目不同，折算规则中需注意源账簿和目的账簿间的科目对应关系。

☑ 内部交易协同的功能处理要点参见 2.5 内部交易核算章节的内容。

#### 2.3.5 外币分账制

##### 2.3.5.1 业务描述

<div style="text-align: center;"><img src="imgs/img_in_image_box_294_632_897_1113.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.3.5-1 外币分账制业务描述</div>


说明：

按财务部规定，有外汇业务的金融企业(包括银行、保险公司、证券公司、信托投资公司、期货公司、基金管理公司、租赁公司、财务公司等)，可以自主选择采用外汇分账制或外币统账制核算方法，目前国内的证券公司和商业银行及企业财务公司对外汇业务普遍采用外汇分账制进行核算。

外汇分账制下，各种外币业务均以原币填制记账凭证、登记账簿、编制报表，涉及不同货币的业务则通过设置一个过渡科目(如"货币兑换"或"外汇买卖"科目)处理，各种货币之间的兑换及账务之间的联系均通过该过渡科目。

◆ 会计期末，各外币账户及上述过渡科目的余额均按国家规定的会计期末汇率折算为记账本位币，"货币兑换"或"外汇买卖"科目中由于汇率变动所产生的余额则转为汇兑损益并计入当期损益。

◆ 实际业务上一般仅对美元、港币等大币种单独建账核算，对于一些小币种（如泰国铢）则不单设账簿，而是作为外币录入到某一大币种账中。

◆ 为此，金融企业除了人民币账簿外，还需要为各主要外汇大币种设置不同的账簿进行核算并编制会计报表，所有账簿必须按照金融企业会计制度进行核算；这些不同的账簿不分主从，相互独立。

##### 2.3.5.2 业务流程

常规处理同 2.3.1 节的业务流程。

外币分账制可通过在同一财务组织的不同核算账簿中设不同记账本位币实现，也可同一账簿分别取用全局、集团、组织本位，NCV6.3 起建议采用前一种方式。

##### 2.3.5.3 功能模型


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="10">建模平台</td><td rowspan="2">组织管理</td><td style='text-align: center; word-wrap: break-word;'>账簿类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务核算账簿</td></tr><tr><td rowspan="4">基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目</td></tr><tr><td rowspan="4">会计平台</td><td style='text-align: center; word-wrap: break-word;'>入账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>转换模板</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>单据生成</td></tr><tr><td rowspan="5">财务会计</td><td rowspan="5">总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-记账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折算规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证折算</td></tr></table>

##### 2.3.5.4 产品解决方案

☑ 略。

### 2.4 二级核算

#### 2.4.1 业务描述

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_380_1074_873.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.4-1 二级核算业务</div>


☑ 二级核算单位不独立建账：

■ 同一法人公司下，存在非法人的二级核算单位；

■ 二级核算单位各有其独立的经营业务，独立建立业务组织；但不单独建账，所有业务合并在法人公司核算账簿中核算；

要求在同一核算账簿下，可按二级核算单位细分出总账数据，各自出具报表。

法人公司下部分子公司的核算政策和法人公司完全一致，且其业务集中、核算简单，也可能出于集约化考虑，通过二级核算单位进行核算。

☑ 二级核算单位独立建账：

■ 同一法人公司下，存在非法人的二级核算单位，这些单位有独立的经营业务；

☑ 二级核算单位在总账中独立建账簿进行核算，独立填报本业务组织的报表；

■ 部分业务可能需在上级公司的核算账中核算，同一笔业务同时在两个核算账簿中反应。

#### 2.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_241_256_950_903.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 2.4-2 二级核算业务流程</div>


#### 2.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td rowspan="9">财务会计</td><td rowspan="9">总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-签字</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-审核</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-记账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-冲销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-凭证整理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量表-科目关系设置</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="19"></td><td rowspan="19"></td><td rowspan="19"></td><td style='text-align: center; word-wrap: break-word;'>现金流量表-业务规则设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量表-现金流量分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量表-现金流量查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量表-现金流量分析表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-科目余额表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-三栏式总账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-三栏式明细账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-辅助余额表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-辅助明细账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-科目汇总表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-摘要汇总表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-多栏账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-日报表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿查询-资金日报表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义转账-自定义转账执行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-核销处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-往来账龄分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-核销余额表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-核销情况查询</td></tr></table>

#### 2.4.4 产品解决方案

二级核算单位独立建账时，按各自公司建立账簿，其相关核算和一般核算相同，本解决方案着眼于二级核算单位不独立建账模式下的应用。

☑ 【企业建模平台】→【组织管理】→【组织结构定义】→【业务单元】节点中设定所需业务组织，详细操作请参阅产品帮助。

☑ 【企业建模平台】→【基础数据】→【公共信息】/【会计信息】下的各节点录入所需基础档案，详细操作请参阅产品帮助。

☑ 【企业建模平台】→【基础数据】→【参数】→【业务参数设置-组织】节点中，针对特定的业务单元设置 “GL120 是否支持二级核算单位”，设为 “是”，则：

■ 总账产品中【期初余额】、【凭证管理】中提供可选择的业务单元，通过区分不同业务单元来录入不同二级核算单位的期初余额、当期发生金额；

■ 业务单元的选择范围为本业务单元及下级单位；

☑ 如果系统判断该组织账簿中没有数据，则支持设置 “GL120 是否支持二级核算单位” 更为“否”。

☑ 【企业建模平台】→【基础数据】→【参数】→【业务参数设置-组织】节点中，针对特定的业务单元设置 “GL121 是否按业务单元进行平衡检查”，设为 “是”，则：

【财务会计】→【总账】→【期初余额】节点中按业务单元分别录入各科目期初余额并进行试算平衡校验(如图2.4-3所示，其他节点界面类同);

<div style="text-align: center;"><img src="imgs/img_in_image_box_173_363_1021_823.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.4-3 二级核算单元不独立建账，分别核算的期初余额界面示例</div>


【财务会计】→【总账】→【凭证管理】下的各节点均提供按业务单元查询、处理方式，其中【制单】节点中在凭证保存时将按业务单元进行会计平衡关系校验；

该参数受 GL120 约束，并约束 GL122。

☑ 【企业建模平台】→【基础数据】→【参数】→【业务参数设置-组织】节点中，针对特定的业务单元设置“GL122 现金流量是否支持二级核算单位”，设为“是”，则：

【财务会计】→【总账】→【现金流量表】→【科目关系设置】/【业务规则设置】节点中，可选择业务单元进行设置；

【财务会计】→【总账】→【现金流量表】→【现金流量分析】/【现金流量查询】/【现金流量分析表】各节点中分别按业务单元进行现金流量的分析及查询；

该参数受 GL120、GL121 约束。

☑ 【总账】→【账簿查询】中【科目余额表】、【三栏式总账】、【三栏式明细账】、【辅助余额表】、【辅助明细表】、【科目汇总表】、【摘要汇总表】、【多栏账查询】、【日报表】、【资金日报表】支持按业务单元查询。

总账各类业务函数中，提供按二级业务单元取数(函数中最末一个参数设定为二级业务单元的编码)，取数公式设置及结果、取数后的联查追溯如图2.4-4---2.4.6所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_176_1084_649.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.4-4 按二级核算单元取数示例</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_747_1085_1283.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.4-5 按二级核算单元取数追溯示例 1</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_112_175_1088_388.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.4-6 按二级核算单元取数追溯示例 2</div>


### 2.5 内部交易核算

#### 2.5.1 业务描述

☑ 集团内部交易业务通常可区分为六大类：

■ 日常业务类：主要是集团内相关单位之间销售商品、劳务形成各方之间的存货、产品、固定资产、无形资产和在建工程等；

■ 资金往来类：集团内上下级单位资金之间的划拨、平级单位之间的借款和应付、付款；

☑ 资产划拨类:除资金之外的资产(如固定资产、物资等)的划拨;

税收类: 下级单位向母公司划入应交税款，由母公司合并缴纳；

利润类：下级单位将成本利润上划给上级单位；

☑ 投资类：集团内各单位间追加投资和确认投资收益。

◆ 集团内单位之间存在内部交易业务时，要在交易的各方间进行核算并对账；

集团对外提供合并报表前，需在合并范围内完成单位间对账，对符后确定抵消数据；总账结账前也要完成集团内对账，对符后方可结账，总账的对账结果可提供给合并报表使用。

◆ 集团内部交易中，若两个财务组织间主账簿的币种不同，可按主账簿进行对账，这种对账仅为及时核对检查对账双方记账的及时、准确，不进行合并。

☑ 总额对账查询支持按照主账簿对账规则查询，并可选择会计期间方案。

☑ 内部交易公有协同规则支持引用按主账簿对账的内部交易对账规则。

☑ 内部交易对账节点打印功能完善。

◆ 协同已确认消息发送协同人。

#### 2.5.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_173_274_1015_1114.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.5-1 内部交易对账实现</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_144_192_1044_1522.jpg" alt="Image" width="75%" /></div>

<div style="text-align: center;">图 2.5-2 集团对账流程</div>


说明：

双方单位分别记录内部交易业务，记录的方式分为三种方式：A、业务发生时直接进行单据协同，经确认后形成凭证，此时两方凭证自动对符；B、业务发生时不进行协同处理，由总账核算时进行凭证协同，形成的协同凭证自动对符；C、其他来源（如往来双方各自手工录入）的内部交易凭证，按对账规则手工对账。

◆ 业务主动方（内部交易单位 A）对账，形成对账报告，内部协同形成的凭证自动对符；

◆ 业务被动方（内部交易单位 B）确认对账报告；

◆ 集团基于对账结果查询内部交易，进行抵销，完成合并。

## 内部交易协同流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_562_1075_1325.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.5-3 内部交易协同流程</div>


说明：

☑ 自动协同流程：录入本方凭证——生成对方协同凭证——修改、确认对方凭证——协同双方记账。

☑ 手工协同流程：录入本方凭证——选择待协同凭证——对方确认协同凭证——协同双方记账。

◆ 协同接受方在确认协同凭证时补充凭证的对应分录信息后生成本方凭证，并将“已确认”状态回传发起方的协同凭证。

#### 2.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="6">财务会计</td><td style='text-align: center; word-wrap: break-word;'>基础档案及规则</td><td style='text-align: center; word-wrap: break-word;'>内部交易对账规则-全局内部交易对账规则-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账-内部交易协同</td><td style='text-align: center; word-wrap: break-word;'>公有协同设置-全局公有协同设置-集团公有协同中心公有协同确认公有协同查询</td></tr><tr><td rowspan="4">总账-内部交易对账</td><td style='text-align: center; word-wrap: break-word;'>期初初始化明细对账汇总对账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对账报告生成对账报告确认总额对账查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对账报告审核-全局对账报告审核-集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对账结果查询</td></tr></table>

#### 2.5.4 产品解决方案

将内部交易凭证按形成来源可分为三类，分别处理：

一是其他来源的内部交易凭证，指由交易各方各自直接录入的内部交易凭证，或直接录入的内部交易单据生成的凭证，这类凭证要定期执行核对；

二是内部交易各方通过协同生成的内部交易单据，所形成的凭证，这类凭证自动对待；

三是内部交易各方一方填制凭证，通过协同生成的另一方凭证，这类凭证也自动对符。

先通过协同然后将数据过渡到对账，再由对账数据生成合并报表的抵销凭证。

◆ 【财务会计】→【基础档案及规则】→【内部交易对账规则-全局】/【内部交易对账规则-集团】中设置对账规则：

■ 对账内容可针对“数量/原币/组织本币/集团本币/全局本币”任意选择组合，但至少必须选择一项；是否启用受集团参数、全局参数控制。

☑ “按主账簿对账”：

✓ 勾选则“账簿类型”的选项默认为空，不可修改；

✓ 勾选后“生成抵销分录”项默认置为“不生成抵销分录”，且不可修改；

✓ 表体中本方科目、对方科目，若未选择按账簿类型，则需手工输入科目。

☑ 本方科目/对方科目：

✓ 从当前定义节点所对应级次（全局或集团）的科目表中选取；

✓ 非末级科目和末级科目均可选，但不能重复选择有相互包含关系的科目；

✓ 可设置多行相同方向的科目。

■ 辅助核算：可指定多个类型，每个类型可指定多个档案；但只能即集团参照集团级档案，全局参照全局级档案。

■ 设置好的内部对账规则可供公有协同规则设置时选用，公有协同规则选用了内部对账规则后，其所生成的凭证将自动对符。

集团定义时若涉及全局已定义的科目对，则另一方会计科目必须也在全局定义的、同一内部交易对账规则中另一方的科目对账范围内，对账时优先按照集团级内部交易对账规则执行。

■ 未结转下年的内部交易规则，在下一年将不能执行对账，也不能生成对账报告。

注意：对账规则一旦启用则只能停用，不能删除。

全局节点定义的对账规则，全局、集团均可使用，由全局维护；集团节点定义的对账规则，只能是该集团下的所有财务账簿可用，集团维护。

在【财务会计】→【总账】→【内部交易对账】→【期初初始化】节点录入内部交易对账前的期初余额和期初未对符的数据：

■ 若所选择的“内部交易对账规则”是“按主账簿对账”，则仅参照出用户有权限的主账簿，“是否已对符”项由系统自动置为“未对符”且不可修改；

■ 录入 “财务核算账簿”、“年度”、“内部交易对账规则”、“科目”等必输项后，系统自动检查对应账簿上年有否参与对账的记录：

✓ 若有，则期初初始化数据不可编辑；

✓ 若无，则可录入的凭证数据是“账簿启用日期、对账规则启用日期、当前会计年第一天”三者间最晚日期前的凭证；

☑ 起始日期取所选内部交易对账规则的启用日期。

■ 未进行期初初始化也可以执行对账操作，视同默认的启用日期规则；若生成了正式生成对账报告，则不允许编辑期初，也不能修改相关财务核算账簿的启用日期。

■ 按 “一个核算账簿+内部交易对账规则（等于辅助核算）+一个末级科目（含本对方科目）” 控制已对符数据；“客商辅助核算+币种”也应唯一，保存时校验。

■ 录入期初发生额必须勾选“是否已对符”，此时表体提供“凭证类别、凭证号、分录序号”供录入；若录入期初余额则不勾选“是否已对符”。

■ 科目为所选对账规则上指定的科目(如图 2.5-4 所示)，若交易对账规则上设置的是非末级科目，录入期初始化数据时需按末级科目录入。

<div style="text-align: center;"><img src="imgs/img_in_image_box_139_327_1053_922.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_145_982_1057_1432.jpg" alt="Image" width="76%" /></div>


### 2.5 -4 内部对账规则的科目控制与初始对账关系界面示例

☑ 结转下年与取消结转处理：

✓ 可按年顺序把当前年度的内部交易对账规则结转至下年。

✓ 结转后下一年的启用日期为下年的年初日期

✓ 若内部交易对账规则设置的取数规则为余额，则把已对符余额（已对符余额=期初余额+当年的所有已对符发生数）和结转时仍未对符的发生数据结转至下年，作为下年的期初未达和期初对符余额数据。

✓ 已结转后内部交易对账规则不能再参与以前年度的期初初始化，只能初始化当年数据。

✓ 未结转下年的内部交易规则，在下一年应不能执行对账，也不能生成对账报告。

✓ 若最近一个年度已执行对账，则不能取消结转；若属第一年启用，则不允许取消结转；只能从后往前逐年取消结转

在【财务会计】→【总账】→【内部交易协同】→【公有协同设置-全局】/【公有协同设置-集团】节点设置协同规则，如图 2.5-5 所示，设置中应注意：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>制单</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td><td style='text-align: center; word-wrap: break-word;'>内部交易对账规则-集团</td><td style='text-align: center; word-wrap: break-word;'>公有协同设置-集团</td><td style='text-align: center; word-wrap: break-word;'>期初初始化</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>协同业务编码</td><td style='text-align: center; word-wrap: break-word;'>01</td><td style='text-align: center; word-wrap: break-word;'>协同业务名称</td><td style='text-align: center; word-wrap: break-word;'>日常销售往来类</td><td style='text-align: center; word-wrap: break-word;'>启用日期</td><td style='text-align: center; word-wrap: break-word;'>2011-02-01</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>发送方式</td><td style='text-align: center; word-wrap: break-word;'>自动</td><td style='text-align: center; word-wrap: break-word;'>内部交易对账规则</td><td style='text-align: center; word-wrap: break-word;'>备注</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>所属集团</td><td style='text-align: center; word-wrap: break-word;'>新世纪纸业集团</td><td style='text-align: center; word-wrap: break-word;'>启用状态</td><td style='text-align: center; word-wrap: break-word;'>已启用</td><td style='text-align: center; word-wrap: break-word;'>处理方式</td><td style='text-align: center; word-wrap: break-word;'>双向</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>除障_除障类型</td><td style='text-align: center; word-wrap: break-word;'>中国大陆报告除障</td><td colspan="4">自动生成抵销凭证</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本方科目</td><td style='text-align: center; word-wrap: break-word;'>对方科目</td><td colspan="4"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>关联公司往来</td><td style='text-align: center; word-wrap: break-word;'>关联公司往来</td><td colspan="3"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>银行承兑汇票</td><td style='text-align: center; word-wrap: break-word;'>银行承兑汇票</td><td colspan="3"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>商业承兑汇票</td><td style='text-align: center; word-wrap: break-word;'>商业承兑汇票</td><td colspan="3"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>内部存款</td><td style='text-align: center; word-wrap: break-word;'>内部单位存款</td><td colspan="3"></td></tr></table>

<div style="text-align: center;">图 2.5-5 公有协同设置界面示意</div>


■ 处理方式设为双向时，必须在客户和供应商档案中互设对应的客户和供应商，并指定“是否协同”为“是”，否则涉及内部交易的凭证不参与协同（如图 2.5-6 所示）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_132_168_1047_1235.jpg" alt="Image" width="76%" /></div>


### 2.5 -6 内部客商设置界面示例

设置协同时可引用对应组织级别的内部交易对账规则，实现与内部对账的关联：

✓ 引用对账规则时协同规则的启用日期和对账规则启用日期一致；

✓ 若有部分单位不启用协同，则将该单位在内部客商中的“参与协同”属性项置为“否”。

集团对账规则允许设置为一对多和多对多，而协同凭证因其特殊性只能引用对账规则为一对一或多对一的规则。

☑ 设置协同规则时可指定角色或用户进行消息通知的提醒式处理。

■ 发送方式的 “自动” 和 “手动” 取值决定了涉及内部交易的凭证是自动生成协同，还是人为触发凭证协同的生成。

协同发起方可通过参数 “GL106 公有协同主体账簿” 来控制：当选择了某一账簿，则其他账簿不能发送协同，也不能查询出未协同凭证，结帐时也不关注协同凭证处理情况；若置空，则所有账簿均可以发送协同。

协同的账簿类型：自动携带所引用内部交易对账规则中指定的账簿，可修改；未引用内部交易对账规则时，必须指定账簿类型（否则指定不了本、对方科目）。

■ 利用业务单元级参数‘GL109 折算生成的凭证是否参与公有协同’”，选择是，则折算生成的凭证也可以作为公有协同发送给接受方，可满足不同单位间跨币种协同的应用。

### ◆ 有关内部交易协同流程（图 2.4-3）操作包括：

协同规则设置并启用后，若遇有协同业务发生，则协同发起方在【财务会计】→【总账】→【凭证管理】→【制单】中填制凭证并保存；

■ 发起方的凭证若有分录满足协同规则的设定条件，且对应的内部客商档案已设立时，该凭证可执行协同，协同分自动和手动两种方式；

✓ 当协同规则的发送方式为“自动”时，则向凭证中有关协同业务主分录中所指定的内部客商自动发起协同，等待接受方单位确认，可在【财务会计】→【总账】→【内部交易协同】→【公有协同中心】中查询到已协同凭证；

✓ 若协同规则发送方式为手动，则保存当前凭证后，在【财务会计】→【总账】→【内部交易协同】→【公有协同中心】中执行【协同生成】；

协同凭证的接受方在【财务会计】→【总账】→【内部交易协同】→【公有协同确认】中查询出“未确认”的协同凭证，执行【本方修改】，补充对应分录后完成确认。

协同凭证的接受方可选多笔协同业务合并生成一张协同凭证，但不能对同一协同凭证中的分录行进行合并

■ 协同发起方可在【财务会计】→【总账】→【内部交易协同】→【公有协同中心】查看已确认后的协同凭证，执行【对方浏览】。

■ 制定协同规则的母/子集团可在【财务会计】→【总账】→【内部交易协同】→【公有协同查询】中随时过滤查询某发起方或某接受方相关的协同凭证。

## 协同凭证各状态的控制：

✓ 未发送状态下，可以判定是否需要协同；

✓ 接受方未确认时，发起方可以取消协同，接受方协同确认处自动取消；若接受方已确认，则不允许发起方取消协同；

✓ 已取消的协同凭证可再次进行协同生成。

☑ 已发起协同的凭证按如下规则控制：

✓ 若接受方未确认，则发送方可在【财务会计】→【总账】→【凭证管理】→【制单】中执行删除、作废、修改等操作，接受方自动同步处理；

✓ 若接受方已确认，则发送方不能直接进行凭证删除、作废，需接受方取消协同才可执行；涉及协同的主分录其关键信息项币种、客商、金额、科目不能修改；

✓ 接受方通过协同方式生成的凭证不允许删除、作废,不能修改涉及协同分录上的币种、客商、金额等关键信息，科目修改则控制为只能将非末级改为当前协同科目的末级。

✓ 三方协同：对于协同分录以及协同分录拆分出的分录，均不可再次发起协同；对于非协同分录，则只要满足协同条件，则可再次发起协同。

例如：集团有 A、B、C 三家公司，B 为结算中心，C 销售产品给 A，发起协同给 B，由 B 拨付款，并向 A 发起协同，A 据到货情况确认协同入账，则可按如下流程处理：

C 公司发起的协同凭证为：

借：其他应收款--B公司

贷：主营业务收入

B 公司确认的协同凭证为:

借：其他应收款--A公司

贷：其他应付款--C公司

B 公司可针对 “借：其他应收款-A 公司” 分录对 A 公司再次发起协同。

A 公司收到并处理的协同凭证为：

借：存货

## 贷：其他应付款--B公司

◆ 对账结果提供给【战略管理】→【合并报表】→【对账与抵销】→【自动生成抵销分录】中执行【生成抵销分录】。

◆ 参数 “GL101，协同凭证对方未确认，本方应不允许提前关账/关账”，启用时发起方关账检查报告有接受方未确认协同，发起方不允许“提前关账/关账”，不启用则不控制。

◆ 参数 “GL104，协同接受方有未确认协同业务，本方应不允许提前关账/关账”，启用时协同接受方关账检查报告有来自发起方的未确认协同，接受方不允许“提前关账/关账”，不启用则不控制。

☑ 内部交易对账因涉及双方的业务控制，要遵循严格的操作流程，以明细对账为例，基本顺序如下：

■ 主对账方在【财务会计】→【总账】→【内部交易对账】→【明细对账】节点执行【手动勾对】或【自动勾对】操作，完成对账；除期初已对符记录外，对账号批次号由系统自动写入；

■ 对账双方任一方未关账则不能正式生成对账报告，对账完成后对账双方各自在【财务会计】→【总账】→【期末处理】→【关账】节点执行【关账】；

主对账方在【财务会计】→【总账】→【内部交易对账】→【明细对账】节点执行【生成对账报告】操作：

✓ 正式对账报告一个月只能正式生成一次，已正式生成的对账期间数据不能进行反勾对操作；

✓ 正式生成后，再进行内部交易对账时，双方的对账期间只能记录在已正式生成的下一会计期间，或取消正式生成后再重新正式生成；

✓ 若选择的对账规则为“按主账簿对账”时，不能生成对报告。

■ 被对账方在主对账方生成正式对账报告后，在【财务会计】→【总账】→【内部交易对账】→【总额对账查询】节点中执行【确认】操作；

母、子集团在【财务会计】→【总账】→【内部交易对账】→【对账报告审核-全局/集团】（母集团进全局级节点，子集团进集团级节点）中执行“审核”操作，至此一个对账规则的对账流程完成。

从对账报告生成起，母/子集团即可在【财务会计】→【总账】→【内部交易对账】→【总额对账查询】节点查询对账结果，可查询状态分为“生成、正式生成、已确认、已审核”，分别对应“生成对账报告、正式生成对账报告、确认对账报告、审核对账报告”等操作。

■ 系统提供集团级参数 “GL125 关联检查内部交易对账是否完成”，如果为是，则关账前当月数据必须全部勾对，若为否，则关账不检查内部交易对账情况。

汇总对账的业务操作过程与明细对账基本相同，但多提供了“对账方式”供选择（如图所示），表现在：

<div style="text-align: center;"><img src="imgs/img_in_image_box_232_178_960_714.jpg" alt="Image" width="61%" /></div>


2.5-7 汇总对账查询界面示例

■ 对账方式选择的借贷对账，则查询结果只显示本方借方和对方贷方；

如果对账方式选择净发生，则借贷方不显示，只显示净发生列的数据；

☑ 净发生=科目余额方向发生数-另一方向发生数；

一次汇总对账形成统一的批次号，后勾对的必须在先勾对的批次号范围内勾对；

■ 本方科目为借方余额时，差额=本方借方-对方贷方或=本方净发生-对方净发生；本方科目为贷方余额时，差额=本方贷方-对方借方或=本方净发生-对方净发生。

■ 如果对账规则中对账金额性质选择为“余额”，则：

✓ 校验期末对符余额是否相等，如果不相等，则不能生成对账报告，此时可在日志中查询错误记录；

✓ 对已对符数据只显示为正数，按制单日期取当月的期末余额=本年期初余额+截止至本期的科目方向的已对符累计发生数-截止至本期的科目对方方向的已对符累计发生数；

✓ 对未对符数据，本对方数据的方向为科目的方向，数值也显示为显示方向的数值，按制单日期取截止至当前期间期末所有的未对符数据的净发生（即这一时点的未对符余额）；

如果对账规则中对账金额性质选择为“发生额”，则：

✓ 对于已对符数据，按制单日期取当月的净发生数，本对方数据的方向为科目的方向，发生额为未对符科目方向发生数-该科目对方方向发生数；

✓ 对于未对符数据，本对方数据的方向为科目的方向，发生额为未对符科目方向当期（按制单日期为准）发生数-该科目对方方向当期（按制单日期为准）发生数（即当期净发生额）。

■ 无论发生额还是余额，均按已对符和未对符的合计计算差额：

✓ 如果双方的科目方向相反，取本对方已对符和未对符的合计数据相减的绝对值；

✓ 如果双方的科目方向相同，取本对方科目相加的绝对值。

若启用了合并对账模块，则对账完成后，对账记录传递到【战略管理】→【合并账簿】→【调整与抵销】→【抵销凭证录入】，形成“总账对账”来源方式的抵销凭证。

内部交易对账完成与否可能影响到总账模块的关账，按集团级参数 GL125 “关账检查内部交易是否完成” 进行约束。

◆ 【财务会计】→【总账】→【内部交易对账】→【对账结果查询】节点中，可按自然日期范围查询对账结果，包括双方的已对符发生额、未对账发生额，及联查明细数据。

☑ 总额对账查询按照主账簿对账规则：

在基础档案及规则中，定义内部交易对账规则，启用按主账簿对账，对账内容选原币和组织本币，对账金额选余额或发生额，本方科目，对方科目，辅助核算项等。

■ 按照所选会计期间方案的会计期间，转换为各核算账簿的会计期间进行数据汇总查询。

例如：香港公司-香港账簿和大陆工厂-大陆账簿之间进行对账，会计期间对应关系如下表


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>香港公司-香港账簿（香港会计期间方案）</td><td style='text-align: center; word-wrap: break-word;'>大陆工厂-大陆账簿（大陆会计期间方案）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>201401</td><td style='text-align: center; word-wrap: break-word;'>201404</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>201402</td><td style='text-align: center; word-wrap: break-word;'>201405</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>……</td><td style='text-align: center; word-wrap: break-word;'>……</td></tr></table>

在内部交易协同-公有协同设置中，可以选择内部交易对账规则，在内部交易对账规则中启用按主账簿对账，则内部交易协同可以在不同类型的账簿中发生。例如，协同的发起方和确认方的账簿类型可以不同，账簿中的币种，会计期间方案可以不同。

☑ 内部交易对账节点打印功能完善

☑ 对账结果查询支持打印未对符明细和已对符明细；

汇总对账结果，支持打印。

协同凭证的发起方在做协同凭证后，向接收方发送消息。

### 2.6 现金流量分析

#### 2.6.1 业务描述

☑ 作为会计三大报表之一的现金流量表，依据收付实现制编制。

在会计期末，可以依据资产负债表、利润表来编制现金流量表，但该方法和日常核算脱节，不能明晰的查看现金流量项目整个的来源，也不能提供现金流量项目细化管理。

在日常核算中需要记录业务发生时涉及的现金流量，同时还要实时查询某一段时间内企业现金流量的状况，为财务管理和分析提供支撑。

对于一些凭证形式固定、较单一简单的业务，提供按科目汇总方式进行快速便捷的分析。

☑ 对现金流量明细的查询可以查询到具体的凭证号和科目及金额。

允许对非现金类凭证进行现金流量分析。

#### 2.6.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_261_816_927_1246.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">2.6-1 现金流量分析流程</div>


#### 2.6.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>现金流量项目-全局/集团/财务组织</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="7">财务会计</td><td rowspan="7">总账</td><td style='text-align: center; word-wrap: break-word;'>科目关系设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务规则设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量快速分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量分析表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量明细查询</td></tr></table>

#### 2.6.4 产品解决方案

◆ 日常业务核算中在填制凭证时即将现金流量信息进行记录；可在填制凭证时及时进行分析，也可在凭证填制完毕后分析。

通过指定现金流量项目或科目（科目对）之间的关系来快速分析凭证对应的现金流量。

☑ 支持按不同时间段查询现金流量项目的金额。

在【财务会计】→【总账】→【现金流量表】→【科目关系设置】节点可建立现金流量项目和科目之间的关联，用于后续现金流量分析过程中的自动分析。

在【财务会计】→【总账】→【现金流量表】→【业务规则设置】节点可预定义凭证分录结构与现金流量表项间的对应关系，后续可据此对应关系，自动生成现金流量分录。

在【财务会计】→【总账】→【凭证管理】→【制单】节点点击【凭证-现金流量分析】对当前凭证进行即时分析：

■ 点【载入】将未进行分析的非现金类分录批量增加到表体，只有设置了科目对应关系，才能载入分录。

点【分析】则根据科目关系设置对整张凭证进行自动分析，分析结果展现到表体行，产品默认对多借多贷凭证的分析方式默认为“空”，可指定分析方式；现金流量表项保存在非现金类科目上。

■ 选多个表体行点【归集】组，可以将多行分录合并到一个指定的现金流量项上，此时可输入主表表项与附表表项。

在【财务会计】→【总账】→【现金流量表】→【现金流量快速分析】节点点击【查询】，可对业务简单、凭证形式较固定的凭证方便地快速展开分析：

查询结果默认按现金类分类/非现金分类显示，可右击鼠标快速调用批量操作，这些批量操作项包括：按科目展开、按辅助核算展开、按现金流量项目展开、收回展开项目、联查凭证、指定现金流量项、取消现金流量项：

按科目展开——选定非末级科目行，可按科目逐级展开现金；

按辅助核算展开----按最明细的档案值显示，不考虑逐级显示的功能，辅助核算值当期发生数为 0 则不显示；

指定现金流量项目----提供三种快速指定现金流量的方式：

✓ 自动分析：按科目与现金流量项目对应关系迅速指定现金流量；

✓ 手动分析：选定行记录进行指定，在弹出的现金流量档案表中人为指定现金流量的主、附表项；

现金流量分析：对可操作行联查现金流量分析节点的结果，可进行单张凭证和多张凭证的快速分析。

取消现金流量----取消现金流量分析的结果，注意该操作仅能对本节点指定的项目执行，

经由【制单】或【现金流量分析】节点完成现金流量分析的凭证分录不能取消；但【制单】或【现金流量分析】节点可撤消本节点指定的现金流量分析项。

在【财务会计】→【总账】→【现金流量表】→【现金流量分析】节点批量选择凭证进行分析(如图所示)，该节点中注意事项如下：

先查询出指定期间内的凭证，准备执行分析，查询时可按已指定/未指定/全部，包含未记账/只包含现金凭证/包含零现金发生凭证，及凭证号范围、制单人、科目编码、对方科目、辅助项等组合查询所需凭证（如图2.6-2现金流量分析查询界面示意）；

<div style="text-align: center;"><img src="imgs/img_in_image_box_204_796_988_1461.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 2.6-2 现金流量分析查询界面示意</div>

查询出凭证后，可按 “自动分析/单张分析”、“归集”、“添加表项/编辑表项/删除表项” 等分析方式执行现金流量分析操作，“归集”、“添加表项/编辑表项/删除表项”为手工指定方式：

✓ 自动分析：按照科目关系或业务规则分析满足查询条件的一批凭证；

✓ 单张分析：按照科目关系或业务规则分析某一特定凭证；

✓ 添加表项/编辑表项：由用户按照业务需要手工将分录指定到现金流量表项中，也可称为手工指定方式；

✓ 删除表项：手工将已分析的表项删除，为回卷性操作。

☑ “自动分析”与“单张分析”均可在【制单】节点已执行【现金流量分析】的基础上重新分析（图2.6-3所示），重分析后的结果在【制单】节点将按新结果显示；

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_564_1041_981.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.6-3 现金流量分析自动/单张分析方式界面示意</div>


☑ “自动分析”与“单张分析”的分析方式既可选“按对方科目”，也可用“按业务规则”进行，但按业务规则时必须完全满足业务规则所定义的各项条件；

当前分析结果可设置为分析规则予以保存，尤其对于多借多贷的凭证较为方便；

■ 多借多贷凭证的分析方式既可按照事先设定的业务规则分析，也可指定分配方式后按对应科目设置规则进行自动分析；

☑ 手工指定时添加到表项中的金额不能超过凭证分录的实际金额；

关于节点中的操作可参阅产品中的在线帮助。

◆ 现金流量分析完成后，即可在【财务会计】→【总账】→【现金流量表】→【现金流量查询】和【财务会计】→【总账】→【现金流量表】→【现金流量分析表】中查看现金流量情况：

【现金流量查询】支持联查明细、联查现金流量，并可执行错误分析，若存在指定到现金流量表项中的金额与分录金额不一致的项目，则通过【错误分析】钮可显示该分录的日期、凭证号、摘要、科目、借方、贷方和分配金额等内容，方便用户修改现金流量分析结果；

☑ 【现金流量查询】支持按多个账簿联查现金流量分析情况；

【现金流量查询】和【现金流量分析表】均支持按未记账凭证、币种、起止期间段等条件组合的查询，且返回币种可选“组织本币、集团本币、全局本币”之一；

☑ 【现金流量分析表】支持按查询对象及查询范围作分组小计。

## 相关参数控制：

■ GL089 保存凭证时是否检查现金流量：若置为 “检查主表信息” 或 “主附表信息”，则凭证保存前必须完成现金流量即时分析；若置为 “不检查”，则可在【凭证-现金流量分析】中批量事后分析。

■ GL107 现金流量是否校验原币余额：设为“是”则保存凭证和结帐时检查原币和本币，为“否”则只检查本币。

■ GL108 关联时是否检查现金流量：若设为 “是” 遇有错误分析的现金流量则不允许关联，关联后不允许再修改现金流量分析；若设为 “否” 则关联时不检查，关联后仍然可修改现金流量分析。

■ GL122 现金流量是否支持二级核算单位: 设为“是”则可按二级核算单位分析现金流量, 为“否”则只能按主核算单位分析现金流量。

## ☑ 现金流量明细查询：

■ 增加一个功能节点 “现金流量明细查询”，在查询现金流量表项的同时可以查询对应的凭证号，摘要，会计科目，辅助核算项，金额。在查询条件中可以选择账簿，期间，主附表，表项，币种等分类查询。通过凭证联查，可以查询现金流量表项对应的来源凭证。

非现金类凭证可以支持现金流量主表分析：

在基础数据-业务组织参数-组织-财务-总账中，保存凭证时是否检查现金流量，可选主表信息/附表信息/不检查。

在录入非现金类凭证时，做凭证-现金流量分析，会计科目选择主表表项或附表表项，保存时若现金流量借贷方之和不为零，则系统会提示“现金流量金额分析错误”。

### 2.7 往来核销

#### 2.7.1 业务描述

往来核销是针对还款业务建立其与借款业务之间的勾兑关系，反映企业实际借款、还款的情况，主要解决总账科目在往来凭证层面的往来核销处理。

事先明确哪些往来业务要进行核销，按何种规则（口径）核销。

需核销的往来业务若存在期初未达账项，应先行核对正确。

☑ 支持针对银行存款未达账项的核销。

☑ 日常核销处理时应可单独及时核销，也可事后查询与调整核销情况，支持核销账龄分析。

◆ 集团企业需能支持：单一企业的往来账分析；跨单位往来账分析；包含多单位的往来账分析。

在往来业务中，对非末级科目之间的核销增加参数控制，避免错误发生。

往来核销支持按业务单元查询和分别各自核销。账龄分析语义模型定义中支持按业务单元查询。

往来核销在同一账簿下有多个二级核算单位的，支持按多个业务单元查询往来账龄分析。

#### 2.7.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_298_488_888_1020.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">2.7-1 通用往来核销业务流程</div>


#### 2.7.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="6">财务会计</td><td rowspan="6">总账</td><td style='text-align: center; word-wrap: break-word;'>往来核销-核销对象设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-期初未达录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-核销处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-往来账龄分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-核销余额表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>往来核销-核销情况查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>业务组织参数-组织-财务-总账-是否允</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>许跨末级科目核销（默认“否”）</td></tr></table>

#### 2.7.4 产品解决方案

在【财务会计】→【总账】→【往来核销】→【核销对象设置】节点设置拟核销的科目、辅助项，并确定要否严格控制及核销号是否必录：

一旦设有辅助核算，则根据“是否严格控制”检查，必须按该核算项同一取值的借、贷双方核销（例如设了按人员核销，则张三的借款只能由张三本人还款时核销）。

若科目已经启用则不能修改核销对象，也不能取消启用，需将已核销的记录全部反核销后取消启用，再进行修改。

往来核销下的所有功能与操作，只能在当前集团下执行。

☑ 在【财务会计】→【总账】→【往来核销】→【期初未达录入】节点，执行操作时应注意：

■ 若存在满足核算对象的科目期初，则无论核算是否严格控制，均应在核算对象启用前录入或导入该往来科目的期初并保持平衡，否则核算对象无法启用；

☑ 核算对象一旦启用则不能再行修改往来未达期初；

核销对象设置与期初未达录入为互斥性操作，同一账簿下不能同时登录使用。

即时核销---在【财务会计】→【总账】→【凭证管理】→【制单】中执行：

■ 录入凭证的科目符合【核销对象设置】中定义的科目时，在凭证保存后点击【分录-即时核销】，即可完成往来核销操作；

即时核销完成后可在【核销余额表】、【往来账龄分析】、【核销情况查询】中查询；

☑ 已完成即时核销的凭证要取消核销，只能通过【往来核销处理】执行【反核销】操作。

☑ 批量核销---在【财务会计】→【总账】→【往来核销】→【往来核销处理】节点中执行：

已录入的凭证若有科目符合【核销对象设置】中的定义且当时未核销时，可在此处查询出并执行【核销】或【自动核销】，完成往来核销操作，具体操作可参阅产品帮助；

完成核销的凭证可在【核销余额表】、【往来账龄分析】、【核销情况查询】中查询；

☑ 已完成批量核销的凭证可通过【历史查询】后执行【反核销】处理。

核销处理页面提供金额排序的功能，点击表头的原币栏，即可按照金额大小排序。

往来核销仅限于在当前集团下操作和查询。

◆ 【财务会计】→【总账】→【往来核销】→【核销情况查询】：

提供按单个账簿、指定单个往来核算对象的查询；

支持指定核算类型、起止日期范围、分析方式、币种、分析方向、是否包含未记账、是否包含已两清等条件组合的查询。

◆ 【财务会计】→【总账】→【往来核销】→【核销余额表】：

提供按单个账簿，可指定多个往来核算对象的余额查询，并按预定义的账龄区间方案提供账龄；

支持指定起止日期范围、核销范围、分析日期、币种、分析方向、是否包含未记账、是否包含已两清等条件组合的查询。

◆ 【财务会计】→【总账】→【往来核销】→【往来账龄分析】：

提供指定账龄区间、多个往来核算对象，多个科目，按一到多个账簿的账龄分析；

当勾选了“坏账估算”的〖是否显示〗时，应继续设置所选账龄区间各区间段的坏账比率，NCV6.33产品将按所设条件执行坏账设置（如图2.7-2所示）：

<div style="text-align: center;"><img src="imgs/img_in_image_box_163_403_1059_993.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图2.7-2 往来账龄分析界面示例</div>


■ 账龄分析结果支持按汇总或明细方式列示

支持指定起止日期范围、核销范围、分析日期、币种、分析方向、是否包含未记账、是执行收款账龄分析还是按坏账估算的方式等各条件组合的查询。

账龄分析查询时只能在坏账估算和收款账龄分析两者中选一种方式执行。

往来核销末级核销科目控制

在基础数据-业务参数设置-组织中，增加“是否允许跨末级科目核销”控制参数，参数值为“是或否”，用来控制对非末级科目核销的控制。

在总账-往来核销-核销处理中做核销。

## ☑ 往来核销区分业务单元

在总账-往来核销-核销处理中，支持按照业务单元查询凭证，并且按照业务单元来核销凭证。

在语义模型-设计-业务数据-总账-科目账龄分析语义提供者-可预制查询条件界面，可按照二级核算单位过滤账龄分析数据。

往来核算单位的核算账簿下启用了二级核算单位的，在往来账龄分析查询界面核算账簿下显示业务单元选项，支持区分多个业务单元查询往来账龄分析。

### 2.8 期末处理

#### 2.8.1 业务描述

总账的期末处理包括（提前）关账、关账、(汇兑)损益类结转、结账等项，期末处理涉及和多个业务模块的互动操作，流程化控制方案可按需设定。

◆ 汇兑损益处理：

■ 企业进行外币业务交易时，由于不同外币兑换、汇率变动折合为记账本位币而形成的收益或损失，在会计期末必须准确反映。

■ 要求可预置汇兑损益规则，期末自动处理因汇率变动等原因产生的汇兑损益，形成记账凭证。

集团内存在多主币，应支持多主币的汇兑损益结转，结转时可调整各本币的汇率，并据此计算差值，形成汇兑损益凭证。

汇兑损益结转凭证的制单日期。

自定义结转：会计期末，企业需要完成费用的归集和分摊，以及相应科目的结转业务。

需要灵活地定义转账规则、取数，完成转账凭证的预设置；

■ 可按科目、辅助核算项目结转发生额、余额等数值。

☑ 可按重分类凭证取数。

若一个法人核算账簿下，有多个业务单元且财务核算分开，需要分业务单元执行结转规则。

## ☑ 关联与结账：

会计期末出于出具报表需要，需及时对本会计期间进行结账处理；

企业若有多个业务系统运行，各自处理进度不一，为确保结账过程中业务系统不再产生本期间的凭证，需对财务系统进行关账处理；

■ 关账时有部分后期处理的业务系统产生本会计期间的新凭证，为此应对关账细分，前期完成的核算科目进行提前关账，如期间费用类科目；后期处理的科目如汇兑损益类科目；

根据企业内控要求，应保持同一会计期内分类明细账与总账数据的一致与完整，为此需控制：除损益结转和汇兑损益的凭证外，关账后当前会计期不能再增加会计凭证，上游业务系统单据将自动生成下期凭证；

会计期临结束时，需对账务数据进行试算平衡、结账等处理，当一切都处理完毕后，对当前期间打上结束标志，并将当前期余额转入下期。

☑ 总账关账时可以出具关账检查报告。

☑ 总账和业务系统对账：

同时应用财务核算专项模块（应收/应付、存货核算、固定资产核算）和总账模块下，总账核算人员与各专项模块核算管理人员需进行明细账与总账的定期或不定期核对。

当业务数据与总账核算数据因各自分隔而对不上账时，需要有对账工具来分析差异原因。

■ 总与业务系统的对账平时也可不定期进行，建议在总账关账前务必执行，以免关账后对账不平时引起核算数据的不必要回卷操作（如反关账）。

会计年度起始期间不同，因此报表取数期间不同，需要转换对照会计期间。例如，2015/1/1 至 2015/12/31，可以是一个会计年度，2015/4/1 至 2016/3/31 也可以作为一个会计年度。

#### 2.8.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_251_566_937_1190.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">2.8-1 总账期末处理流程</div>


#### 2.8.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计科目-全局/集团/财务组织</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">总账</td><td style='text-align: center; word-wrap: break-word;'>汇兑损益定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>汇兑损益结转</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="10"></td><td rowspan="10"></td><td style='text-align: center; word-wrap: break-word;'>自定义结转分类定义-集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义转账定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义结转方案档案定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义结转方案定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>期末处理-试算平衡</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>期末处理-关联</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>期末处理-批量关联</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>期末处理-结账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对账设置-集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对账执行</td></tr></table>

#### 2.8.4 产品解决方案

期末处理通常需要较严格的操作顺序，一般情况下按如下步骤操作(详细操作说明请参阅产品帮助中相关节点说明):

◆ 【企业建模】→【基础数据】→【会计信息】→【会计科目-全局】/【会计科目-集团】/【会计科目-财务组织】：

☑ 选定科目表中拟提前关账科目进行修改，勾选“提前关账”属性；

注意：科目被使用或共享后不能再改动该属性，为此需在财务初始化时全面考虑后提前设置。

不能再改动该属性，为此需在财务初始化时全面考虑后提前设置。

◆ 【财务会计】→【总账】→【期末处理】→【试算平衡】选择核算账簿、指定期间、币种后，点击【刷新】查看试算平衡。

◆ 【财务会计】→【总账】→【自定义转账】→【自定义转账分类定义-集团】/【自定义转账分类定义-组织】：

■ 非必设，只是当单位转账业务多，查看转账定义与进行转账执行时不易迅速找到时，可在此对转账凭证设置分类，方便转账执行时，按分类查找并执行转账业务；

■ 集团级设置的默认为公用；组织级设置的可指定为公用，则此时该账簿下、所有有操作权限的操作员可用；也可按角色或操作员指定使用人，此时则只有被指定的操作员（角色）可管理该转账凭证类别。

◆ 【财务会计】→【总账】→【自定义转账】→【自定义转账定义】：

■ 用于设置转入科目、转出科目、金额及数量公式等转账凭证内容，可指定凭证中的多条分录按序结转；

☑ 已设置的转账凭证可移动到其他分类，可复制到本集团的其他核算账簿；

■ 自定义转账定义时，可选择“重分类”转账属性，以便涉及债权债务的报表业务数据处理，要注意的是，定义重分类属性的转账凭证时，只能取余额类函数,如下图所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_246_1087_537.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.8-2 自定义转账定义示例</div>


转账公式中若涉及多笔借贷方，可用 CE 函数获取凭证借贷平衡差额：

✓ CE 函数在计算借贷平衡差额时，可以根据其所在的位置进行计算；

✓ 若一张凭证有多笔结转业务，每笔结转业务都需计算平衡时，可根据结转分录的位置，确定 CE 函数的计算方向。

例一：向下计算平衡差额，转账凭证定义如下

借：管理费用 CE（向下计算）

贷：应付工资 FS()

应付福利费 FS()

说明：计算 CE（）函数所在分录之下的分录的借贷差额。该凭证贷方有多条分录，将其合计数据转入到上面的借方分录中。

例二：向上计算平衡差额，转账凭证定义如下：

借：主营业务收入－存货 A    FS(，，, 存货 A, 贷)*T%

主营业务收入－存货 B    FS(，，, 存货 B, 贷)*T%

贷：主营业务税金及附加－消费税    CE（向上计算）

说明：计算 CE（）函数所在分录之上的分录的借贷差额。该凭证借方有多条分录，将其合计数据转入到下面的贷方分录中。

例三：多次计算差额，转账凭证定义如下：

借：主营业务收入—存货 A    FS(., , 存货 A, 贷)*T%

主营业务收入—存货 B    FS(., , 存货 B, 贷)*T%

贷：主营业务税金及附加—消费税    CE（向上计算）

借：主营业务收入—存货 A  FS(.,, 存货 A, 贷)*T%*0.07

主营业务收入—存货 B  FS(.,, 存货 B, 贷)*T%*0.07

贷：主营业务税金及附加—城建税 CE（向上计算）

借：主营业务收入—存货 A    FS(.,, 存货 A, 贷)*T%*0.015

主营业务收入—存货 B    FS(.,, 存货 B, 贷)*T%*0.015

贷：主营业务税金及附加—教育费附加 CE（向上计算）

说明：多次计算 CE（）函数所在分录之上的分录的借贷差额，每次计算的是上一次 CE 函数与本 CE 函数之间的借贷差额

✓ 当自定义分录的方向选空时，金额公式只能与 CE（）函数搭配使用，选其他金额公式将不能保存。设为选空且与 CE（）函数搭配使用时，生成凭证时 CE（）函数分录方向自动选择使金额为正的方向。

◆ 【财务会计】→【总账】→【自定义转账】→【自定义结转方案档案定义】/【自定义结转方案定义】：

当用户不希望与产品交互转账操作，而是由系统全自动完成转账时，可在此预定义结转方案的各个步骤，以及每个步骤包含的所有结转凭证及次序；

【自定义结转方案档案定义】用于预设结转方案的编号、名称、说明，供【自定义结转方案定义】调用；

☑ 【自定义结转方案定义】只可用于单个核算账簿，其详细操作可参阅产品相关节点的帮助说明。

◆ 【财务会计】→【总账】→【自定义转账】→【自定义转账执行】：

【自定义转账执行】属核算账簿级运用，可按【自定义转账定义】中的预定义设置批量自动生成转账凭证，也可按预定义的转账方案执行自动转账；

批量结转可选择多个自定义转账规则对指定的多个核算账簿执行结转；

■ 自定义转账定义与执行的操作支持“前台/后台生成凭证”及“含未记账凭证”，其操作过程如图 2.8-3 所示，


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td colspan="2">自定义转账定义</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_128_1086_705.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">2.8-3 自定义转账执行界面示例</div>


批量结转与按转账方案结转互斥，即勾选了转账方案则不能执行批量结转，如图 2.8-4 所示；

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_812_1087_1006.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.8-4 自定义转账执行界面示例</div>


关于自定义转账几个项目的说明：

✓ 【自定义转账定义】中的“转账时间”决定了选择当前转账业务发生的期间，可选值为“年/季/月”，是转账数据来源的依据。例如，转账定义中设置了“年初余额”公式，则在执行转账时，当“年度”选择“2011”时，则生成的转账凭证数据为2011年的年初余额，当“年度”选择“2012”年时，则生成的转账凭证数据为2002年的年初余额；

✓ 【自定义转账定义】中的“转账频度”决定了同一笔转账业务在同一会计期内可结转的次数，达到最大次数则不执行结转并给出提示；

✓ 【自定义转账定义】中的“前台/后台生成凭证”用于控制用户是否希望在执行转账时查看生成转账凭证的内容，若用户希望在转账生成时不显示凭证界面，直接执行选择的转账定义，则可选"后台生成凭证"，将生成的转账凭证自动保存到未记账凭证库中。

同一法人核算账簿下，二级核算单位分开财务核算的，可以在总账自定义转帐定义，分开业务单元执行转账规则，二级核算单位生成的结转凭证是分隔的。

## ◆ 【财务会计】→【总账】→【期末处理】→【关账】：

■ 期间费用类科目转账完成后，进入本节点，点击【提前关账】/【关账】，完成对期间费用类科目的关账，被“提前关账/关账”的科目只能增加下一会计期的凭证。

■ 提前关账需在科目表中预设相关科目的“提前关账”属性。

■ 提前关账受业务单元级参数 “GL112 是否支持提前关账” 约束，若设为是，则提前关账时应检查：

✓ 所有含有提前关账属性的会计科目的凭证均已记账；

✓ 已提前关账的，含有提前关账属性的会计科目的凭证不允许反记账；

✓ 不含提前关账属性科目的凭证，其增删改不受提前关账控制；

（提前）关账受业务单元级参数“GL108 提前关账时是否检查现金流量”约束，详见本文中“2.5现金流量分析”中参数控制说明部分。

■ 提前关账受业务单元级参数 “GL034 关联检查业务系统是否结账的核算账簿” 约束，若选定了账簿，则该账簿关联前应先检查应收/应付、存货核算、固定资产等业务系统是否已先结账。

☑ （提前）关账受业务单元级参数 “GL084 不允许有未生成凭证的实时凭证的（提前）关账检查期间” 约束，若设为 “每月” 时，则（提前）关账前应将会计平台中各业务系统生成的临时凭证生成账簿中的实时凭证。

☑ （提前）关账受业务单元级参数“GL101协同凭证对方未确认，本方应不允许（提前）关账、记账、不控制）”约束，若设为“不允许（提前）关账”则应待被协同单位确认协同凭证后再执行（提前）关账。

■ 关账受业务单元级参数 “GL033 检查凭证断号的环节” 约束，若该参数设为 “关账” 时，则凭证库中凭证发生断号不能关账，应先在【凭证整理】节点处理后再行关账。

■ 关账受集团级参数“GL125 关账检查内部交易是否完成”约束，若置为是，则应先完成内部交易，否则不能关账。

■ 关账受业务单元级参数 “GL020 是否允许反关账” 约束。

■ 关账不校验本期间是否进行提前关账，如没有提前关账，则自动进行提前关账。

若存在未确认协同的凭证不能关联，应先对未确认凭证进行处理。

■ 关账时将检查所有非来源于损益结转和汇兑损益的凭证，要求这些凭证均已记账。

■ 关账后非来源于损益结转和汇兑损益的的凭证不能反记账。

■ 关联不要求按会计期间顺序执行，只要未结账，任何一个会计期间均可以设为关联，但已结账的会计期间不允许取消关联。

☑ 【财务会计】→【总账】→【期末处理】→【批量关账】：

会计期间方案的参照范围为登陆用户有权限的所有业务单元的会计期间方案，及其财务核算账簿(主账簿、报告账簿)关联的账簿类型的会计期间方案。默认为空。

选择指定的会计期间，但不能包括调整期。当会计期间方案选中后默认显示当前会计期间。

根据选定的方案、期间和账簿可以查询返回符合条件的核算账簿及其关账状态。

■ 用户可选择多个账簿进行批量关账、反批量关账、批量提前关账、反批量提前关账等操作。如用户选择了不符合按钮可操作状态范围内的数据，给出错误提示。

■ 批量关账操作过程需要满足相关的校验，例如：关账时是否检查凭证断号、检查业务系统是否结账等。

■ 关账过程中如果某个核算账簿校验不通过则该账簿无法关账，其他账簿仍能批量关账成功。未进行关账的核算账簿将统一进行提示。

☑ 系统支持不校验连续期间的关账，即对当前期进行关账时，以前期可以没有关账。

■ 通过参数 “GL034 关联检查业务系统是否结账的核算账簿”，参照当前业务单元所有已启用的核算账簿。单选。当参数值为空时，业务系统是否结账不影响该业务单元所有核算账簿的关联动作。否则选定核算账簿关联时，校验同一业务单元(BU)参与校验的业务系统是否结账，如果没有结账，则控制总账的该核算账簿不能关联。该核算账簿已关联，同一业务单元（BU）的业务系统不允许反结账操作。关联检查的接口模式由业务系统注册。

■ 涉及跟上下游系统的处理关系时，上游系统独立预置接口参数：下游系统（总账）关账是否检查本系统结账，参数值：是/否，如果选择“是”，则总账应检查的上游系统是否已结账，如果没有结账，则不允许下游系统（总账）关账。下游系统（总账）已经关账的，不允许上游系统取消结账，如果参数值选择“否”，则上游模块结账与否与总账关账没有关系。

■ 进行总账批量关账操作时，各业务系统反馈的错误信息（例如是否已结账）会集中显示在状态栏，方便进行查看处理。

## ◆ 【财务会计】→【总账】→【汇兑损益】→【汇兑损益结转】：

在【财务会计】→【总账】→【汇兑损益】→【汇兑损益定义】中按核算账簿预先指定汇兑损益类结转凭证的转出、转入科目及币种，已定义的转账凭证可在本集团内的各核算账簿间复制。

企业存在外币业务，发生了汇兑损益时，可在关联后结账前，进入该节点执行汇兑损益的结转处理。

汇兑损益的结转与自定义转账生成的操作基本相同，只是汇兑损益结转只能选定核算账簿执行，不能批量结转。

汇兑损益结转凭证的制单日期为当前会计期的最后一天。

## ☑ 【财务会计】→【总账】→【期末处理】→【结账】：

保持手工核算的操作习惯，月末进行，结帐时给出月末工作报告。

■ 结账按向导式操作，在结账向导中逐项点击【下一步】，系统自动核对账簿、出具月度工作报告后完成结账，若有下列情形，结账无条件中止：

✓ 上月未结账；

✓ 还有未记账凭证；

✓ 总账和明细账未对平；

✓ 试算平衡未通过；

结账受下列参数约束：

✓ 业务单元级参数 “GL030 是否允许反结账”；

✓ 业务单元级参数 “GL032 结账检查损益结平”，若置为否，则损益不平也可通过结账；

✓ 业务单元级参数 “GL033 检查凭证断号的环节”，若设为结账则有断号凭证则中止结账；

结账过程中工作报告出具的内容包括：

✓ 业务单元级参数 “GL084 不允许有未生成凭证的实时凭证的（提前）关账检查期间”，若设为不检查，则不仅关账时不查，结账时也可不检查而直接结账通过。

✓ 本月未记账凭证数（共多少张，哪些凭证）；

✓ 本月损益类(或收入、支出类)未结转为零的一级科目（哪些科目）；

✓ 本月账面试算平衡结果（同试算平衡）

✓ 本月账账核对结果（XX账与XX账是否平衡）；

✓ 本月工作量(共计多少张凭证、多少条分录，各凭证类别分别多张凭证、多少条分录，其中断号凭证多少张、分别是哪些断号）；

✓ 本月若有需执行但还未执行的期末结转（分按自定义结转、汇兑损益结转列出）；

✓ 动态会计平台中未生成凭证的单据；

✓ 本月其他相关系统是否已进行月末处理（哪些系统未结账）。

支持同时选取多个核算账簿集中结账。

☑ 【重建余额表】操作：可更正部分异常数据对账账平衡的影响，用于重新构造余额数据。对于月末结账时，提示总账与明细账不符的情况，可以使用此功能。支持多会计期间和多账簿的选择。

在年度结转时，若下年已有期初余额数据，系统仍允许强制进行年度结转，但结转后，会覆盖下年期初余额的数据，务必慎重执行。

总账关账检查报告。总账关账时系统默认提供关账检查报告，但不支持修改或自定义月结检查项。

☑ 期末处理相关参数汇总：

✓ GL020 是否允许反关账

✓ GL030 是否允许反结账

✓ GL032 结账检查损益结平

✓ GL033 检查凭证断号的环节（凭证打印、关账、结账、不检查）

✓ GL034 关联检查业务系统是否结账的核算账簿

✓ GL084 不允许有未生成凭证的实时凭证的（提前）关账检查期间

✓ GL101 协同凭证对方未确认，本方应不允许（（提前）关账、记账、不控制）

✓ GL108 提前关账时是否检查现金流量

✓ GL112 是否支持提前关账

✓ GL125 关联检查内部交易是否完成

☑ 对于因会计年度不同，报表取数期间的解决方法：

财务核算账簿的会计期间与报表任务的会计期间的对应关系如下：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>报表的会计期间方案</td><td style='text-align: center; word-wrap: break-word;'>对应财务核算账簿会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2014年1月</td><td style='text-align: center; word-wrap: break-word;'>2014年4月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2014年2月</td><td style='text-align: center; word-wrap: break-word;'>2014年5月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>……</td><td style='text-align: center; word-wrap: break-word;'>……</td></tr></table>

### 2.9 业务单元多版本

#### 2.9.1 业务描述

企业在实际业务中对于 ERP 基础档案调整会是一项经常性工作，尤其对于跨公司、跨年度存储和处理数据的 ERP 系统，诸如组织机构、部门和科目的调整等更加频繁。业务单元的变动包括组织的编码、名称和属性的变化、组织机构的停用或启用等，以及组织机构的调整引起组织结构的变化，例如级次的调整、隶属关系的调整，下级单位的调整等，分别对应了组织的版本化和组织体系的版本化。

NC 系统采取设定有效期的方式来处理业务单元的多版本问题，实现业务单元多版本下业务处理参照并显示正确的编码和名称，以及单据和账簿查询显示正确的编码和名称。

通过设置有效期来确定基础数据在某一阶段是否有效：

■ 如果有效则可以在符合数据权限的前提下，对该基础数据涉及的业务数据进行处理。

如果无效则诸如录入业务数据的业务就不能处理，但查询可以在符合数据权限的前提下进行跨越当前有效期数据档案的有关业务处理。

☑ 判断业务单元变动影响是否需要版本化：

在基础数据管理界面直接修改业务单元的属性，但并不构成对财务组织结构的调整时，只在基础数据档案中保留修改的痕迹，不必建立新版本。

■ 对财务组织进行结构性调整，需要终止原组织版本，新建财务组织的同时须确保新财务组织的有关属性必须与原来保持一致。

#### 2.9.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_169_258_1045_839.jpg" alt="Image" width="73%" /></div>


#### 2.9.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td></tr><tr><td rowspan="11">财务会计</td><td rowspan="11">总账</td><td style='text-align: center; word-wrap: break-word;'>凭证管理-制单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-签字</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-审核</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-记账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证管理-冲销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账表查询-科目余额表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账表查询-三栏式总账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账表查询-三栏式明细账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账表查询-辅助余额表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账表查询-辅助明细账</td></tr></table>

#### 2.9.4 产品解决方案

◆ 业务单元多版本定义，【企业建模】→【组织管理】→【业务单元】：

☑ 根据实际业务发生调整业务单元信息。

通过【多版本】操作设定版本名称及生效日期，完成业务单元版本定义。

【财务会计】→【总账】→【凭证管理】→【制单】/【签字】/【审核】/【记账】/【查询】/【冲销】：

查询条件的参照按查询日期范围的截止日期对应版本，如果没有截止日期，则为最新版本。

修改了查询日期后，再打开参照，则重新刷新参照内容，不打开参照，则不重新刷新。

新增修改凭证及凭证查询后的显示：按照制单日期对应的版本显示，打开的参照也是根据制单日期对应的版本显示。

☑ 冲销凭证按冲销生成制单日期对应版本显示。

◆ 【财务会计】→【总账】→【账表查询】→【科目余额表】/【三栏式总账】/【三栏式明细账】/【辅助余额表】/【辅助明细账】：

查询条件的参照按查询日期范围的截止日期对应版本，如果没有截止日期，则为最新版本。

修改了查询日期后，再打开参照，则重新刷新参照内容，不打开参照，则不重新刷新。

☑ 查询结果显示:

✓ 汇总：按查询日期范围的截止日期对应版本显示。

✓ 明细：根据所在凭证的制单日期对应的版本显示。

✓ 联查凭证：根据凭证制单日期对应的版本显示。如果按照组织单元出合计数据，则忽略多版本问题，一个组织单元一行数据；组织编码名称等按照该时段内截止日期对应版本显示。

■ 涉及跨期间的账表查询时，查询结果的小计按照查询条件的截止日期所对应的版本显示。

以组织单元为条件统计查询业务数据时，默认在界面上不选择版本信息，按照选中组织单元所有版本下产生的业务数据进行统计查询。

◆ 支持报表数据项目、语义模型从总账直接取数：

## 第三章 初始准备

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_296_1085_869.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3-1 总账模块初始准备</div>


### 3.1 管控模式

管控模式中，关于凭证类别、收支项目、现金流量项目的设定决定了企业建模平台中可使用的节点是全局、集团还是业务组织级，详见《系统管理手册》相关章节部分。

### 3.2 企业建模平台

#### 3.2.1 多组织管理

通过设置财务组织、账簿类型、财务核算账簿等相关业务组织，实现财务组织的多账簿管理以及财务组织的二级核算。

组织建立在系统中包括业务单元、账簿类型、财务核算账簿，具体操作应用请参见《多组织管理手册》。

##### 3.2.1.1 组织管理-组织结构定义

### 1. 业务单元

对企业中的业务职能进行了划分，是企业中特定业务职能（业务及政策）的载体，是为了完成特定业务职能而划分的具有相应功能权限的单位。比如：财务业务单元完成财务核算的功能；销售业务单元完成销售业务的功能等；

### 2. 核算账簿

总账管理的主组织是核算账簿，由带有财务属性的业务单元（通常称为财务组织）按账簿类型创建，常规的核算账簿通常带有公司属性，也可以是公司下带有财务属性的二级业务单元。

核算账簿必须归属某一账簿类型，一个账簿类型确定了币种、期间和科目体系，财务组织建有多个核算账簿时，必有一主账簿和一至多个报告账簿；每个核算账簿可选择自用的科目表。

账簿启用后，如果账簿内没有数据，则支持修改启用期间。

##### 3.2.1.2 功能节点与主组织对照表


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>路径</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td><td style='text-align: center; word-wrap: break-word;'>NC6x 主组织</td></tr><tr><td rowspan="11">企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td rowspan="3">公共信息</td><td style='text-align: center; word-wrap: break-word;'>会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>外币汇率</td></tr><tr><td rowspan="7">会计信息</td><td style='text-align: center; word-wrap: break-word;'>会计辅助核算项目</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证类别-全局/集团/核算账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目体系</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会计科目-全局/集团/财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>现金流量项目-全局/集团/财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收支项目-全局/集团/财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内部交易对账规则-全局/集团</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="5">则</td><td style='text-align: center; word-wrap: break-word;'>常用摘要-全局/集团/组织</td><td style='text-align: center; word-wrap: break-word;'>全局/集团/财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账龄区间设置-集团/组织</td><td style='text-align: center; word-wrap: break-word;'>集团/财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>凭证类别约束规则</td><td style='text-align: center; word-wrap: break-word;'>核算账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基础档案对照</td><td style='text-align: center; word-wrap: break-word;'>集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交叉校验规则</td><td style='text-align: center; word-wrap: break-word;'>财务组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>期初余额</td><td style='text-align: center; word-wrap: break-word;'>核算账簿、二级财务组织</td></tr></table>

参数设置中即有全局级参数，也有集团及财务组织（产品实现时选业务单元，系统给出带有财务属性的业务单元供选）级的参数，各自按对应作用区域起作用。

会计期间、币种、外币汇率、会计辅助核算项目、科目体系均在全局级设置并在全局区域起作用；会计科目默认提供全局、集团、财务组织三级节点，可通过参数配置调整可处理节点。

凭证类别、现金流量项目、收支项目根据管控参数的设定而提供相应的操作节点；

内部交易对账规则系统默认提供全局、集团两级节点；账龄区间设置系统默认提供集团、组织两级节点处理。

其他的基础数据档案均依赖于核算账簿起作用。

期初余额录入必须的主组织是核算账簿，根据是否进行二级核算而可能会有二级财务核算组织作为辅财务组织。

基础数据维护在系统中包括参数设置，公共信息、会计信息和财务核算基本档案的具体操作应用请参见《基础数据手册》。

##### 3.2.1.3 跨组织部门、人员参照

1\. 相关单据调整(包括：应收单、应付单、收款单、付款单、期初应收/应付/收款/付款、未确认应收、暂估应付、期初暂估应付单)

1) 应收单/收款单/期初应收/期初收款/未确认应收/应付单/付款单/期初应付/期初付款/暂估应付/期初暂估应付单据的销售组织、销售部门、销售人员、采购组织、采购部门、采购人员变更为业务组织、业务部门、业务人员；

2) 业务组织的参照为业务单元，业务单元的参照范围为根据主组织(财务组织)的财务核算委托关系的所有业务单元；

3) 业务部门的参照范围：业务组织下所有部门，并且包含业务员的来源所属组织的部门，如：A 组

织和 B 组织无财务核算委托关系，但 A 组织的人员在 B 组织做事，业务发生在 B 组织，所以在做部门参照时同样可以参照到 A 组织的部门；

4) 业务人员的参照范围：业务员的参照范围同业务部门的参照范围；

5) 自制单据时，业务组织默认等于财务组织；

6) 单据默认显示业务组织、业务部门、业务人员，单据模板的部门、人员默认不显示。

2. 转移并账、核销、汇兑损益、坏账处理、单据协同、账表查询等功能涉及业务组织、部门、人员的参照都做相应的调整。

#### 3.2.2 基础数据维护

基础数据维护在系统中包括参数设置，供应商信息和结算信息中相关基本档案，具体操作应用参见“V6基础数据手册”。

##### 3.2.1.3 基础设置

### 1. 参数设置

全局级参数动态建模-基础数据中，BD401“科目的维护方式”可选择“总部统一制定、集团统一制定、各单位自行维护”，注意该参数决定了系统管理中会计科目可维护的节点，且一旦设定即不能修改，务必慎重选择。

注意：该参数自 NCV6.3 起取消。

##### 3.2.1.4 公共信息

### 1. 会计期间

会计期间也称会计分期，是指将企业川流不息的经营活动划分为若干个相等的区间，在连续反映的基础上，分期进行会计核算和编制会计报表，定期反映企业某一期间的经营活动和成果。提供了灵活的方式来定义会计期间，企业可以根据需要将特定的会计年度和期间定义为一个会计期间方案。

### 2. 币种

币种档案用于维护全局范围内用到的币种，支持在全局、集团两级设定不启用本位币、基于原币计算、基于本币计算等可选化的参数配置方式。

### 3. 外币汇率

外币汇率方案用于定义一种汇率制度和规则，在一个外币汇率方案下，一对“源币种—目的币种”之间只能设置一组汇率；在建立财务组织、核算账簿、报表折算规则时需要关联外币汇率方案。

##### 3.2.1.5 会计信息

### 1. 会计辅助核算项

辅助核算是在科目核算的基础上的进一步细化，也是从另一个角度对企业的财务业务进行分析，辅助核算与会计科目的组合使用，能全面反映企业的经济业务，也可使账务处理更加灵活；会计辅助核算项目用于定义财务核算可参照的辅助核算项目档案，预置大部分基础档案作为辅助核算项，同时支持用户自定义。

### 2. 凭证类别

凭证类别是指定会计凭证的分类方式，凭证设置分类能满足企业的内控管理，也方便了财务人员根据分类快速及时地查询到凭证。常见的凭证分类方式有：一、记账凭证；二、收款凭证、付款凭证、转账凭证；三、现金凭证、银行凭证、转账凭证；四、现金收款凭证、现金付款凭证、银行收款凭证、银行付款凭证、转账凭证。

预置有全局级的“会计凭证”类别，用户可以根据企业自身的核算需要和业务量的多寡补充设置不同的凭证类别。根据管控模式设置的不同，凭证类别档案可分为“凭证类别-全局、凭证类别-集团和凭证类别-核算账簿”三个节点，分别用来定义全局级、集团级和核算账簿级的凭证类别档案。

凭证类别与凭证类别约束规则同时作用于各财务核算账簿。

### 3. 科目体系

科目体系作为针对会计科目按编码规则、科目类型组划分出的科目方案，在全局范围内默认按科目体系编码唯一。预置有“基准科目体系”，允许客户自维护。

### 4. 会计科目

会计科目依托于科目表存在，会计科目表依托于科目体系独立设置，再和各财务核算账簿关联，形成核算账簿对科目表的对应映射关系，可使财务核算既灵活多样又不失其管控特性。

科目表中各科目的属性设置将影响到财务核算的各个环节。

财务核算账簿在启用后，如果账簿没有数据，则支持修改科目表。

### 5. 现金流量项目

按管控模式设置的不同，现金流量项目可分为“全局、集团和财务组织”三个节点，分别用来定义全局级、集团级和财务组织级的现金流量项目档案，默认现金流量项目档案编码为唯一性规则对象，并预置新会计制度下的一般企业现金流量项目供客户使用。

### 6. 收支项目

收支项目作为会计科目影响因素之一，用于做不同业务时的参照取值，对收支项目的管控模式多样；依据管控模式的不同，收支项目可分为“全局、集团和财务组织”三个节点进行反映；同样地，默认收支项目档案编码为唯一性规则对象。

### 3.3 财务管理

#### 3.3.1 财务会计基本档案

### 1. 内部交易对账规则

内部交易对账规则用于确定全局或集团中参与对账的对账内容、科目范围，甚至包括辅助核算。设置时由“对账关系设置方”组织负责“科目对应关系设置”，本单位对账科目为“本方科目”列表中列示的科目，对方单位的科目为在“对方科目”列表中列示的科目，对账科目范围为本级科目及其下级明细科目。

### 2. 常用摘要

用于预设完全相同或大部分相同的业务摘要，供填制凭证、单据时调用，以便提高业务处理效率账龄区间设置；日常凭证处理时也可即时将当前摘要保存为常用摘要。

### 3. 账龄区间设置

用于设置往来账款的时间长度，供总账、应收管理、应付管理三个模块使用，v60 提供集团、组织两级节点分别维护所在区域范围内的账龄区间档案。

### 4. 凭证类别约束规则

核算账簿级节点，用于规范某凭证类别可记录的业务；一个核算账簿里的一个凭证类别只能被一个约束规则使用。

例如：凭证类别分为收款、付款、转账三类时，可指定收款凭证借方必有现金、银行存款、内部存款等科目，则凭证填制或生成时若借方科目无上述三科目之一的，将不能使用收款凭证。

### 5. 基础档案对照

用于建立在两个不同财务组织间除会计科目外的，其他基本档案间的对照关系，以解决同一集团下因业务、管理的需要，各财务组织之间发生横向业务联系（例如内部交易发生，责任中心考核等）时因基础档案不同而无法确定责任主体的问题。

基础档案对照节点的主组织为集团，定义档案时档案的参照范围为所选组织的组织级档案，来源组织与目的组织也只能参照到当前集团下的业务单元。

### 6. 交叉校验规则

当不同的档案之间原有的固定对应关系（比如某个业务员负责具体某类存货的销售等）在基本档案里无法建立联系时，可通过交叉校验规则来明确这种关系，以减少在录入凭证的辅助核算、录入单据不同字段时的差错，减轻录入凭证单据的工作量。交叉校验规则的主组织是业务单元。

#### 3.3.2 总账

##### 3.3.2.1 基础设置

### 1. 期初余额

用户在开始启用总账系统时，要将各账户的余额录入到总账系统中，作为开始录入日常业务之前的准备。期初余额即用于录入各科目启用日期前的余额和累计发生额，有辅助核算的科目可按辅助项录入期初，有外币及数量核算的科目可以录入其外币、数量的期初。

期初余额的主组织为核算账簿，若存在二级核算，可按二级核算的业务单元分别录入各科目的期初；期初数据录入完毕后，需分析检测试算平衡。

在总账模块启用后每一年的年初，可以在此对当年的年初余额进行调整。

支持用户在导出期初余额的输入格式后，在 EXCEL 中进行编辑操作，方便地填完期初余额后，再以 EXCEL 的形式导入到总账中，导入后自动进行检查，检查项包括：根据辅助项输入控制规则检查辅助项合法性；试算平衡检查；交叉校验规则检查；若遇断电或导入中途出错等异常，可根据错误提示重新执行导入。

同一核算主体不同币种的账簿之间，期初余额可进行折算。异币种账簿之间期初折算的规则差异主要体现在不同币种采用相应汇率进行折算上。

折算规则按如下逻辑处理：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>折算\n方式\n目的方</td><td style='text-align: center; word-wrap: break-word;'>原币对本币</td><td style='text-align: center; word-wrap: break-word;'>本币对本币（完全）</td><td style='text-align: center; word-wrap: break-word;'>本币对本币（不完全）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>组织本币</td><td style='text-align: center; word-wrap: break-word;'>根据原币折算汇率取值详见以下说明</td><td style='text-align: center; word-wrap: break-word;'>根据本币折算汇率取值详见以下说明</td><td style='text-align: center; word-wrap: break-word;'>1）对于来源方业务原币币种与目的方组织本币币种不同的情况：根据本币折算汇率取值详见说明2）对于来源方业务原币币种与目的方组织本币币种相同的情况：目的方组织本币金额取来源方原币金额</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>集团本币</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>全局本币</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td><td style='text-align: center; word-wrap: break-word;'>与来源方相等</td></tr></table>

当折算规则中币种折算方式为“原币对本币”时，汇率取值规则为：汇率取期初建账的日期的前一天做为基准日期去取汇率；

当折算规则中币种折算方式为“本币对本币（完全）”时，汇率取值规则如下：

对于未在 “科目折算汇率” 进行汇率定义的科目，汇率取期初建账的日期的前一天做为基准日期去取汇率；

若 “科目折算汇率” 进行了相应定义，各科目按照所定义的汇率进行折算：

✓ 日汇率：汇率取期初建账的日期的前一天做为基准日期去取汇率；

✓ 即时汇率：按用户折算时输入的折算汇率进行折算；

✓ 期间汇率：按期初建账的日期的上一期间的期间汇率来折算；

✓ 固定汇率：按用户在折算规则中所输入的固定折算汇率进行折算。

当折算规则中币种折算方式为“本币对本币（不完全）”时，

对于未在 “科目折算汇率” 进行汇率定义的科目，汇率取期初建账的日期的前一天做为基准日期去取汇率；

若 “科目折算汇率” 进行了相应定义，各科目按照所定义的汇率进行折算：

✓ 日汇率：汇率取期初建账的日期的前一天做为基准日期去取汇率

✓ 即时汇率：按用户折算时输入的折算汇率进行折算

✓ 期间汇率：按期初建账的日期的上一期间的期间汇率来折算

✓ 固定汇率：与现有产品规则相同，按用户在折算规则中所输入的固定折算汇率进行折算。

■ 例外：若来源方业务原币币种与目的方组织本币币种相同，目的方组织本币金额直接取来源方原币金额，而不按照来源方组织本币金额进行换算，如下表所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源方账簿</td><td style='text-align: center; word-wrap: break-word;'>目的方账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>组织本位币：人民币</td><td style='text-align: center; word-wrap: break-word;'>组织本位币：美元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">1 货币资金期初余额：</td></tr><tr><td colspan="2">科目 币种 原币 组织本币 集团本币 全局本币</td></tr><tr><td colspan="2">货币资金 美元 1000 6000 7000 7000</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="6">按照“本币对本币（完全）“折算方式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币</td><td style='text-align: center; word-wrap: break-word;'>集团本币</td><td style='text-align: center; word-wrap: break-word;'>全局本币</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>货币资金</td><td style='text-align: center; word-wrap: break-word;'>美元</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>1200</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>7000</td></tr><tr><td colspan="6">按照“本币对本币（不完全）“折算方式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币</td><td style='text-align: center; word-wrap: break-word;'>组织本币</td><td style='text-align: center; word-wrap: break-word;'>集团本币</td><td style='text-align: center; word-wrap: break-word;'>全局本币</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>货币资金</td><td style='text-align: center; word-wrap: break-word;'>美元</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>1000</td><td style='text-align: center; word-wrap: break-word;'>7000</td><td style='text-align: center; word-wrap: break-word;'>7000</td></tr></table>

☑ V6.5 版对期初余额的功能做了如下优化：

➢ 期初 Excel 导入时增加增量导入方式，路径：【财务会计】→【总账】→【初始设置】→【期初余额】→【导入导出】;

➢ 期初余额录入界面，默认币种改为组织本币；

➢ 期初余额，选择某个科目进入辅助界面，导入导出支持按照档案编码导入导出。

### 2. 各功能组合的预定义

各功能组合的预定义如，可在初始化时预定义，也可在该模块组合正式运用前定义，这些预定义在第二章各场景中已有涉及，详细操作可参阅产品帮助的相关节点说明：

凭证管理中的“定制”（定义凭证模板）；

现金流量表中的“科目关系设置”、“业务规则设置”；

财务折算中的“折算规则”

往来核销中的“核销对象设置”、“期初未达录入”；

内部交易对账中的“对账初始化”（内部交易对账规则由财务会计的基础档案及规则中设定）；

公有协同设置中的“公有协同设置”；

汇兑损益中的“汇兑损益定义”；

自定义转账中的“自定义结转分类定义、自定义转账定义、自定义转账方案档案定义、自定义转账方案定义”；

账簿查询中的“多栏账定义”；

总账与业务系统对账中的“对账设置”。

## 第四章 操作指南

本手册具体详细操作应用，请登录 NC 系统参见相关产品帮助。

## 附录

## 附录 1：控制点

### 1. 约束条件


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>功能点</td><td style='text-align: center; word-wrap: break-word;'>规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应用系统管理</td><td style='text-align: center; word-wrap: break-word;'>管控模式</td><td style='text-align: center; word-wrap: break-word;'>客户/供应商若设为集团级以下，则不能执行跨集团对账及跨集团合并账簿业务。</td></tr><tr><td rowspan="5">建模平台</td><td style='text-align: center; word-wrap: break-word;'>科目体系</td><td style='text-align: center; word-wrap: break-word;'>按科目体系形成科目表树。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>核算账簿</td><td style='text-align: center; word-wrap: break-word;'>核算账簿一经启用不能删除，停用后不能重启用。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目体系</td><td style='text-align: center; word-wrap: break-word;'>每新增一个科目体系，自动创建该科目体系下的全局根科目表，根科目表携带默认的科目控制规则，要删除新增的科目体系应先删除根科目表。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目表-全局/集团/财务组织</td><td style='text-align: center; word-wrap: break-word;'>无论哪一级科目表，只要被引用过不能删除，增加下级或插入中间级时，将同时检查上级及下级科目表的科目情况；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户-集团/供应商-集团</td><td style='text-align: center; word-wrap: break-word;'>设了内部客商后，要将该内部客商的“是否协同”勾选上，才能进行公有协同。</td></tr></table>

### 2. 单据参数

总账产品中的流程控制参数如下表所示，详细应用内容可参阅《基础数据手册》中总账模块相关章节。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>模块</td><td style='text-align: center; word-wrap: break-word;'>所属组织与范围</td><td style='text-align: center; word-wrap: break-word;'>代码</td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>相关参数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公共参数</td><td style='text-align: center; word-wrap: break-word;'>全局</td><td style='text-align: center; word-wrap: break-word;'>NC002</td><td style='text-align: center; word-wrap: break-word;'>全局本位币计算方式：不启用全局本位币；基于原币计算；基于组织本位币计算</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公共参数</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>NC001</td><td style='text-align: center; word-wrap: break-word;'>集团本位币计算方式：不启用集团本位币；基于原币计算；基于组织本位币计算</td><td style='text-align: center; word-wrap: break-word;'>NC002</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>建模平台</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>ORG003</td><td style='text-align: center; word-wrap: break-word;'>财务组织是否自动启用</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>建模平台</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>BD001</td><td style='text-align: center; word-wrap: break-word;'>外币交易折本汇率模式：买入卖出价，中间价</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>建模平台</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>FIP003</td><td style='text-align: center; word-wrap: break-word;'>如目标系统关账则单据自动进下一期间</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>GL097</td><td style='text-align: center; word-wrap: break-word;'>凭证号是否允许修改</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>GL125</td><td style='text-align: center; word-wrap: break-word;'>关账检查内部交易对账是否完成</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>GLS01</td><td style='text-align: center; word-wrap: break-word;'>查询账簿期间最大值</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>GLS02</td><td style='text-align: center; word-wrap: break-word;'>是否允许设置查询包含未记账凭证</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>GLS05</td><td style='text-align: center; word-wrap: break-word;'>预算查询总账发生数据查询方式自动转换</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL001</td><td style='text-align: center; word-wrap: break-word;'>是否需要出纳签字</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL003</td><td style='text-align: center; word-wrap: break-word;'>凭证审核后才能记账</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL091</td><td style='text-align: center; word-wrap: break-word;'>凭证流程控制方案</td><td style='text-align: center; word-wrap: break-word;'>GL001GL003</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL009</td><td style='text-align: center; word-wrap: break-word;'>是否允许反记账</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL011</td><td style='text-align: center; word-wrap: break-word;'>账簿表头科目显示模式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL020</td><td style='text-align: center; word-wrap: break-word;'>是否允许反关账</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL021</td><td style='text-align: center; word-wrap: break-word;'>对方科目显示模式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL030</td><td style='text-align: center; word-wrap: break-word;'>是否允许反结账</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL032</td><td style='text-align: center; word-wrap: break-word;'>结账检查损益结平</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL033</td><td style='text-align: center; word-wrap: break-word;'>检查凭证断号的环节（凭证打印、关账、结账、不检查）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL034</td><td style='text-align: center; word-wrap: break-word;'>关账检查业务系统是否结账的核算账簿</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL036</td><td style='text-align: center; word-wrap: break-word;'>制单后是否立即打印</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL039</td><td style='text-align: center; word-wrap: break-word;'>凭证是否立即补号</td><td style='text-align: center; word-wrap: break-word;'>GL033</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL040</td><td style='text-align: center; word-wrap: break-word;'>凭证起始编号</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL050</td><td style='text-align: center; word-wrap: break-word;'>凭证原币为0是否允许保存</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL051</td><td style='text-align: center; word-wrap: break-word;'>凭证原币合计不平是否允许保存</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL053</td><td style='text-align: center; word-wrap: break-word;'>凭证数量为0是否允许保存</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL054</td><td style='text-align: center; word-wrap: break-word;'>凭证是否序时控制</td><td style='text-align: center; word-wrap: break-word;'>GL040GL036</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL055</td><td style='text-align: center; word-wrap: break-word;'>余额方向控制方式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL066</td><td style='text-align: center; word-wrap: break-word;'>上月未结账本月能否记账</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL080</td><td style='text-align: center; word-wrap: break-word;'>核销日期</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL081</td><td style='text-align: center; word-wrap: break-word;'>核销顺序</td><td style='text-align: center; word-wrap: break-word;'>GL080</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL084</td><td style='text-align: center; word-wrap: break-word;'>不允许有未生成凭证的实时凭证的（提前）关账检查期间</td><td style='text-align: center; word-wrap: break-word;'>GL112</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL085</td><td style='text-align: center; word-wrap: break-word;'>外部导入凭证是否允许删除</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL088</td><td style='text-align: center; word-wrap: break-word;'>签字日期生成规则</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL089</td><td style='text-align: center; word-wrap: break-word;'>保存凭证时是否检查现金流量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL091</td><td style='text-align: center; word-wrap: break-word;'>凭证流程控制方案</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL092</td><td style='text-align: center; word-wrap: break-word;'>辅助核算是否带默认值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL093</td><td style='text-align: center; word-wrap: break-word;'>辅助项为空是否显示</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL094</td><td style='text-align: center; word-wrap: break-word;'>制单是否逐分录对科目的余额进行控制</td><td style='text-align: center; word-wrap: break-word;'>GL055</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL095</td><td style='text-align: center; word-wrap: break-word;'>是否立即生成折算凭证</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL096</td><td style='text-align: center; word-wrap: break-word;'>保存凭证时是否检查附单据数</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL097</td><td style='text-align: center; word-wrap: break-word;'>凭证号是否允许修改</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL098</td><td style='text-align: center; word-wrap: break-word;'>凭证保存时是否即时核销</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL101</td><td style='text-align: center; word-wrap: break-word;'>协同凭证对方未确认，本方应不允许：（提前）关账、记账、不控制</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>GL112</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL104</td><td style='text-align: center; word-wrap: break-word;'>协同接受方有未确认的协同业务应不允许</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL106</td><td style='text-align: center; word-wrap: break-word;'>公有协同核算账簿</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL107</td><td style='text-align: center; word-wrap: break-word;'>现金流量是否校验原币金额</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL108</td><td style='text-align: center; word-wrap: break-word;'>（提前）关账时是否检查现金流量</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL109</td><td style='text-align: center; word-wrap: break-word;'>折算生成的凭证是否参与公有协同</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL110</td><td style='text-align: center; word-wrap: break-word;'>是否需要人工确认被协同凭证</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL112</td><td style='text-align: center; word-wrap: break-word;'>是否支持（提前）关账</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL116</td><td style='text-align: center; word-wrap: break-word;'>是否校验集团借贷平衡</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL118</td><td style='text-align: center; word-wrap: break-word;'>是否校验全局借贷平衡</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL120</td><td style='text-align: center; word-wrap: break-word;'>是否支持二级核算单位</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL121</td><td style='text-align: center; word-wrap: break-word;'>是否按二级单元进行平衡检查</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>GL120</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL122</td><td style='text-align: center; word-wrap: break-word;'>现金流量表是否支持二级核算单位</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>GL120</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL130</td><td style='text-align: center; word-wrap: break-word;'>本期关账，上游系统是否生成下期凭证</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>GL134</td><td style='text-align: center; word-wrap: break-word;'>是否允许跨末级科目核销</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 附录 2：查询报表

### 1. 科目表版本对比

◆ 可以按科目体系查询会计科目表树的构成及各科目表所引用的核算账簿。

☑ 可以查询各科目表的版本。

### 2. 组织关账

◆ 可以按业务单元查看各产品模块在各个会计期间的提前关账、关账、结账状态。

### 3. 平台日志

◆ 可以按目的组织、生成目标（指总账凭证或责任会计凭证）、核算账簿等条件组合查询各业务模块生成凭证的情况。

### 4. 总账账簿查询

◆ 科目余额表：查询条件窗口如图附录 2-1:

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_172_1083_774.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图附录 2-1 总账科目余额表查询条件窗口界面示意</div>


■ 可统计查询、输出各级科目在指定起始会计期内的期初余额、本期发生额、累计发生额和余额等，支持多账账簿查询及合并。

查询时可包括未记账凭证、错误凭证。

■ 多个核算账簿查询时可按各主体分别列示，也可多主体合并列示。

查询支持按不同币种过滤，并可指定返回币种（注意与 NC001、NC002 的设置有关）。

三栏式总账：提供按借、贷、余三栏账格式反映指定科目的各会计期经济业务发生的汇总情况，以及全年业务的累计发生情况数据。查询条件设置与科目余额表类同。

三栏式明细账：用于查询各指定科目的日常明细发生情况。除科目余额表提供的查询条件外，还支持查询方式的分页设置，如图附录 2-2 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_1109_1059_1459.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图附录 2-2 总账三栏式明细账查询条件窗口界面示意</div>

科目汇总表：用于查询指定期间范围、指定科目范围内的凭证，并将查询结果按科目分别汇总，常用于替代凭证汇总表。查询条件设置与科目余额表类同。

摘要汇总表：用于查询指定的单个账簿下某个科目的凭证汇总表，这类汇总表要求凭证填制时摘要具备一定的规律。查询条件支持起止期间段、余额范围、可含未记账凭证和错误凭证；支持返回币种的选择。

◆ 序时账：提供单个核算账簿下按各种查询条件定义、查询出所需要的明细业务数据，并生成序时账。查询条件如图附录2-3所示，序时账查询支持数量、结算方式、结算号、票据日期等自定义条件。

<div style="text-align: center;"><img src="imgs/img_in_image_box_199_389_1035_1177.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图附录 2-3 总账序时账查询条件窗口界面示意</div>


多栏账：多栏账的查询需先进行多样账定义，之后按多栏账的定义执行按科目、辅助条件的组合查询，不同多栏账的格式、取数原则、查询条件随业务核算要求的不同而各不相同，例如：管理费用多栏账可按部门分析，也可按明细科目分析，或者按项目分析。查询条件如图附录2-4所示：

多栏账定义：

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_239_1036_730.jpg" alt="Image" width="72%" /></div>


多栏账查询定义：

<div style="text-align: center;"><img src="imgs/img_in_image_box_154_836_1028_1207.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图附录 2-4 总账多栏账查询界面示意</div>


☑ 辅助余额表：用于根据查询条件的设置按科目、辅助项进行分组汇总查询并打印输出各期间的余额、发生额。支持按多个账簿查询；可将指定范围的各类查询对象分别设置为表头、表体形成查询的二维表；支持多账簿下的显示、排序方式；因查询分组可能涉及的内容较大，产品中支持对辅助余额表的即时查询和异步查询两种方式。

☑ 辅助明细账：用于根据查询条件的设置按科目、辅助项分组查询各科目的明细辅助记录。支持按多个账簿查询；可将指定范围的各类查询对象分别设置为表头、表体形成查询的二维表；支持查询结果的排序方式设定。

◆ 日报表：可查询多个账簿下指定的某个科目在指定期间内的发生额及余额情况，生成日报表。

◆ 日记账：用于查询单个账簿下指定范围的多个科目在指定期间内，按业务发生的先后顺序逐日逐笔登记并按日结余的明细账簿，常用于（但不限于）现金、银行存款类账。

资金日报表：查询资金类科目在指定期间段内各日的发生额及余额情况，生成资金日报表。支持多账簿查询、含未记账及错误凭证、返回币种可控等查询条件项。

现金日记账：用于查询单个核算账簿下，指定日期起止范围的现金类科目的日记账。支持含未记账及错误凭证、返回币种可控等查询条件项。

银行日记账：用于查询单个核算账簿下，指定日期起止范围的银行存款类科目的日记账。支持含未记账及错误凭证、返回币种可控等查询条件项。

### 5. 总账管理报表

☑ 辅助属性余额表：功能同辅助余额查询表，但查询对象较辅助余额表多提供有“供应商档案属性、客商档案属性、人员档案属性、物料档案属性、项目档案属性、客户档案属性”等作为查询补充。如图附录2-5所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_569_1040_1313.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图附录 2-5 总账辅助属性余额表查询界面示意</div>


◆ 多主体科目余额表：功能与科目余额表基本相同，增加了按主体账簿的级次展开查询的功能。

科目辅助余额表：用于对单个账簿的余额表查询，其特点是带有辅助核算的科目会将每一个辅助核算组合作为一个明细科目形成查询结果的返回记录。

多维分析表：用于按科目辅助核算、对方科目、科目自由项、凭证类别、制单/出纳/审核/记账人等操作员、金额范围、摘要等条件的组合对当期凭证汇总查询，如图附录2-6所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_127_185_1088_894.jpg" alt="Image" width="80%" /></div>


保存方案 删除方案

<div style="text-align: center;">图附录 2-6 总账多维分析表查询条件窗口界面示意</div>


### 6. 总账账表查询功能比较：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>查询账表</td><td style='text-align: center; word-wrap: break-word;'>跨年查询</td><td style='text-align: center; word-wrap: break-word;'>提供明细联查</td><td style='text-align: center; word-wrap: break-word;'>跨年联查明细</td><td style='text-align: center; word-wrap: break-word;'>联查凭证</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目余额表</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'>---</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>三栏式总账</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'>不支持</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>日报表</td><td style='text-align: center; word-wrap: break-word;'>不支持</td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'>跨年查询时，在指定时间范围内分别以科目汇总累计，不支持按年显示科目值。联查明细时支持跨年，此时按年+月+日排序</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>科目汇总表</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'>跨年查询时，在指定时间范围内分别以科目汇总累计，不支持按年显示科目值。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>摘要汇总表</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>三栏式明细账</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>日记账</td><td style='text-align: center; word-wrap: break-word;'>不支持</td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>序时账</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>多栏账</td><td style='text-align: center; word-wrap: break-word;'>支持</td><td style='text-align: center; word-wrap: break-word;'>不提供</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>提供</td><td style='text-align: center; word-wrap: break-word;'>跨年查询时，表体按年+月+日排序，无“年”一列。</td></tr></table>
