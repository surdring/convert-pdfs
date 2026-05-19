# NCV6.5产品手册-费用预算

产品手册- V6.5

## 费用预算

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权.....1  
  
名词解释.....5  
  
第一章 概述.....9  
  
1.1 产品概述.....9  
  
1.2 产品价值.....12  
  
第二章 应用场景.....15  
  
2.1 设置预算任务.....15  
  
业务描述.....15  
  
功能清单.....15  
  
产品解决方案.....15  
  
2.2 预算编制.....21  
  
2.2.1 预算编制流程.....21  
  
2.2.2 不同格式要求预算表的编制.....34  
  
2.2.3 固定频度和自定义期间预算.....50  
  
2.2.4 滚动预算的编制.....52  
  
2.3 预算调整.....67  
  
2.3.1 预算调整流程.....67  
  
2.3.2 预算调整业务.....77  
  
2.4 预算分析.....78  
  
2.4.1 基于任务的预算分析.....78  
  
2.4.2 自定义查询分析.....81  
  
第三章 初始准备.....82  
  
3.1 构建预算体系.....83  
  
3.1.1 单一集团预算组织体系构建.....83  
  
3.1.2 多集团预算组织体系构建.....86  
  
3.1.3 多个预算组织体系.....88  
  
3.1.4 分级管理预算体系.....89  
  
3.1.5 多套预算体系.....91  
  
3.2 管控模式.....92  
  
3.3 控制策略.....95  
  
3.4 预算档案.....96  
  
3.5 预算模型.....98  
  
3.5.1 维度管理.....98  
  
3.5.2 指标属性.....100  
  
3.5.3 应用模型.....101

3.5.4 数据集管理 ..... 103  
3.5.5 业务规则 ..... 103  
3.5.6 控制规则 ..... 106  
3.5.7 套表管理 ..... 121  
3.6 审批流 ..... 122  
3.7 规划维度、模型和套表 ..... 126  
3.7.1 规划应用模型和套表 ..... 126  
3.7.2 抽取维度 ..... 128  
3.7.3 自动汇总的注意事项 ..... 129  
3.8 设计 Excel 端套表 ..... 131  
3.8.1 套表设计基本功能 ..... 131  
附录 ..... 149  
附录 1：接口说明 ..... 149  
附录 2：EXCEL 客户端安装常见问题 ..... 153  
附录 3：本文参见其他手册清单 ..... 161

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供业务需求与产品功能相匹配的思路。

本手册包括四部分，第一部分是名词解释；第二部分是对产品及其价值的概要介绍；第三部分是对有关本模块的主要业务场景、流程、以及对应的业务功能的介绍；第四部分是初始准备设置，概要介绍了关于本模块功能点的重要初始化操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。。

此外，为了便于用户对整体内容加深理解应用，手册中附录了关于本产品的接口及一些常见问题，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《NCV6.5 产品手册-组织管理》——深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助----针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《NCV6.5 产品手册-流程管理》——提供关于交易类型、流程设计工具的应用指导。

4. 《NCV6.5 产品手册-基础数据》-----可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

## 名词解释

### 1. 指标

指标是指在营运管理的过程中，集团公司为内部成员单位、部门、个人等所设定的一些经营任务。

指标分为财务指标及非财务指标。财务指标即“硬指标”，包括：销售额、毛利额、各项营运费用、损耗、利息、净利、税金、库存天数等。非财务指标即“软指标”，包括：人员编制、员工满意度、人员流动率、来客数、客单价、顾客满意度等等。在 v61 产品中，指标置入维度管理中。

### 2. 维度

维度是指对指标进行多重解释的具体分类，一个指标可以按照多个维度进行解释。如，营运费用指标，可以用主体维度、时间维度、币种等维度进行解释。

维度的一个具体取值称为维度成员。如，业务方案维度，具体成员有：预算数、预测数、实际数等。

### 3. 维度组合

维度组合（也叫维度向量）是预算产品中特有的一种概念，预算样表中有行 / 列 / 表头维度交叉成员的组合称为维度组合（或维度向量）。

## 1 ) 数据描述方式

在 NC 预算系统里，虽然数据的展示形式也是一种表格，但是每个单元格都会有维度组合的属性。预算中使用维度组合而不是单元格坐标来描述数据，主要是考虑在表格应用时会存在一些缺陷，特别是不能进行数据的多维旋转、钻取等操作，而且基于单元格的应用，如果单元格发生变化往往需要重新定义取数公式，增加了维护工作量。因此在预算系统中使用多维的储存方式。如图 01 中的 B3 单元格，预算数据存储的时候将存储为：

（主体=集团，业务方案=预算数，年维度=2009，指标=手机通讯费，币种=本币，月=4月）的值。

<div style="text-align: center;"><img src="imgs/img_in_image_box_227_1170_973_1394.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 01：预算中的表单</div>


## 2 ) 如何快速知道单元格维度组合

那么如何才能快速的知道单元格的维度组合信息？如何根据维度组合快速定位到数据单元格？在预算里一个单元格的维度信息受三方面的维度作用：表头维度、行维度和列维度，多个维度交叉生成一个单元格的维度组合。我们看一个单元格的维度信息时如果知道行列及表头维度信息，通过多个维度成员组合就能知道一个单元格的维度信息，如图02所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_240_343_993_866.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 02: 单元格的维度组合属性</div>


在一个模型中，维度组合是唯一确定的。一个维度组合（维度向量）只能储存一个数据，因此维度向量相同的单元格，他们之间是数据共享的关系。也可以说，单元格和维度组合的关系是多对一的关系。

### 4. 应用模型

应用模型可以理解为预算系统用来储存数据的一个多维数据空间。应用模型中的预算维度相互交叉组合，最终确定数据在应用模型中的储存位置。

如下图示例的应用模型，包含三个预算维度 “产品名称”、“地区”、“时间”，通过交叉组合确定了各个预算数据的储存位置。

<div style="text-align: center;"><img src="imgs/img_in_image_box_393_172_841_500.jpg" alt="Image" width="37%" /></div>


在预算系统中的应用模型，可以包含6到20个维度。我们建立的应用模型中必须包含的维度有6个：“业务方案”、“版本”、“币种”、“主体”、“计划期间”、“指标”。一般情况下，模型中的维度数量在10个左右比较合适，完全可以满足客户的需求。应用模型中的维度越多，数据关系就越复杂，系统处理的效率也就越慢。后续章节中我们会讲到如何抽取维度，以提高系统运算效率。

应用模型的多维化，对于数据的汇总查询、切片查询等有很大益处。如下图所示，数据可以在“时间”“地区”维度上进行汇总查询：

<div style="text-align: center;"><img src="imgs/img_in_image_box_386_838_803_1126.jpg" alt="Image" width="35%" /></div>


也可以在“时间”“地区”的层面上进行切片查询：

<div style="text-align: center;"><img src="imgs/img_in_image_box_383_1219_833_1392.jpg" alt="Image" width="37%" /></div>

鉴于上述应用模型的数据储存、汇总和查询特性，我们要求“凡是具有相互联系的数据，尽量放在同一个模型当中”。用上述的图示举例来说，季度预算表、月度预算表以及年度预算表的数据就需要建立在同一个模型中。

### 5. 套表

套表，可以理解为一个 Excel 文件模板。

举例来讲，我们建立了一个套表《综合预算》，目前这个套表还不能进行填报，因为它只是一个模板，我们还没有赋予它具体的“主体”、“时间”等维度含义。

我们通过任务管理节点，选择“主体”、“时间”等维度生成任务，把《综合预算》套表赋予了“主体”、“时间”等维度的具体含义后，这个 Excel 文件模板就变成了可以填报的“Excel 文件”。这个“Excel 文件”被我们称为“预算任务”。

如下图，选择了时间、币种、主体等参数维后，启用任务，就可以生成可以编制的 EXCEL 文件：2012 年综合预算（西安公司）.xlsx...2012 年综合预算（中建七局）.xlsx 等。

<div style="text-align: center;"><img src="imgs/img_in_image_box_198_738_1034_1100.jpg" alt="Image" width="70%" /></div>


套表中可以设计多个 MDarea（多维数据区域）。MDarea（多维数据区域），是下图所示中双线的区域，绿色单元格是维度成员，黑色字体是用户的原有 EXCEL 表，空白的单元格就是上一章节中提到的应用模型中的多维数据。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>月</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指標</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td style='text-align: center; word-wrap: break-word;'>5月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1001</td><td style='text-align: center; word-wrap: break-word;'>庫存現金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1002</td><td style='text-align: center; word-wrap: break-word;'>銀行存款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1003</td><td style='text-align: center; word-wrap: break-word;'>存放中央銀行款項</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1011</td><td style='text-align: center; word-wrap: break-word;'>存放同業</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1012</td><td style='text-align: center; word-wrap: break-word;'>其他省幣資金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1021</td><td style='text-align: center; word-wrap: break-word;'>结算備付金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1031</td><td style='text-align: center; word-wrap: break-word;'>存出保證金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1101</td><td style='text-align: center; word-wrap: break-word;'>交易性金融資產</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA. global.0001.1111</td><td style='text-align: center; word-wrap: break-word;'>買入返售金融資產</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

一个 MDarea（多维数据区域）必须指定一个数据储存的来源，即关联一个应用模型。

一般来讲，在一个套表中，所有的 MDarea 尽量对应同一个模型。这样做，有利于编辑公式、数据汇总、分析查询等后续应用。

### 6. 预算体系

预算体系是指各预算组织需要编报什么预算，各预算项目之间的勾稽关系是什么。

### 7. 柔性预算控制

在实际业务中，企业行为会存在很多不确定性，有些突发事件虽会导致超预算，但也必须执行，在这种情况下，通常需要走特批流程。我们将这种在预算控制中对于实际发生会超预算，通过特批也可以允许业务进行的控制类型，称为柔性预算控制。

## 第一章 概述

### 1.1 产品概述

NC6.X 的费用预算产品，是在以前版本的基础上并结合众多项目的应用需求而改进，使产品应用更加完善。NC 费用预算产品能够满足企业集团管控的应用要求，提供了完善的企业费用预算体系解决方案，为企业提供了从预算目标下达、下级预算填报、预算数据上报和批复、数据多版本管理、预算调整、执行监控和预算多维分析等完整的预算管理解决方案。

费用预算主要用于满足企业对费用计划管理的要求，同时也可满足一些项目快速实施的要求。费用预算和全面预算产品共用一个数据平台，相较于全面预算产品，在功能上有所精简，并预置了一些费用计划模型。

费用预算主要适用于同时满足以下条件的用户：

1. 没有预算合并业务，或者有预算合并业务但比较简单，不需要使用预算系统进行预算合并业务处理；

2. 预算样表简单，也就是说其预算维度只能是系统预算的指标维度（预算主体、时间维度、币种、业务方案等）。如果超出预置指标维度，例如有按行业、项目、客户等其他维度管理预算的，则建议使用全面预算。

目前预算产品的解决方案分为四大块内容：

1. 预算体系创建平台：通过该平台搭建用户的多维预算体系，预算体系支持集团管控，既可以满足集中式管理型集团的应用要求，又可以实现各下属企业个性化预算体系的要求；

2. 预算填制的过程管理平台和预算填制的全流程支持：实现预算填制的过程管理，监控下级的预算填制过程；支持从集团预算目标下达、下级预算填报、预算数据上报、预算数据批复、数据汇总、预算数据调整等全过程的预算填制过程；支持预算几上几下的填报过程；

3. 预算的分析和执行监控平台：提供了执行监控功能，能够从业务数据获取执行数，对业务系统进行预算控制和预警；支持预算多维分析，可以按不同的角度进行数据分析，预置了差异分析、趋势分析和预算分析等分析方法；

4. 支持 Excel 客户端，通过 Excel 客户端，可完成预算表单设计、数据填制、预算分析等操作。

产品功能架构如图 1.1-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_160_1076_861.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 1.1-01 费用预算模块构成</div>


产品业务流程如图 1.1-02 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_167_1070_1076.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 1.1-02 预算业务流程</div>


### 1.2 产品价值

1. 支持单一集团和跨集团构建预算组织体系；

2. 预算组织和 UAP 多组织管理完全整合。

3. 支持业务单元、成本中心、部门作为预算组织；支持预算主体矩阵式汇总。

4. 支持多行业集团建立多套预算体系（包括编制、分析体系）：整个集团共用、子集团个性化、业务单元个性化的预算内容体系。

5. 支持直接映射使用 UAP 基础数据、自定义档案、业务单元、部门、成本中心等作为预算的维度和指标。

6. 预算系统的数据权限适配 UAP 数据权限模型。

7. 将预算流程相关的内容和后台多维模型区隔开来，流程设置到任务（多个表单+参数维），应用模型不再关联流程。

8. 后台多维模型优化，在提交数据时能支持按照维度成员的层级关系和后台业务规则自动更新相关联的数据。

9. 预算编制和财务系统中现金管理、应收应付、报销管理、总账等模块的高度集成，费用预算系统可取上述各模块的实际发生数，作为编制本期预算的参考；也可预算控制现金管理、应收应付、报销、总账系统；并且，预算取数和控制提供对现金管理、报销管理、应收应付等系统的预占用业务的支持。

### 10. 支持 EXCEL 客户端应用：

1) 支持在 EXCEL 客户端进行预算套表设计；

2) 支持在 EXCEL 客户端编制预算、提交数据、提交审批；

3) 支持在 EXCEL 客户端作相应的预算分析；

4) 支持在 EXCEL 客户端选择维度成员或者根据维度层级、维度属性自由查询预算数据；

5) 支持在 EXCEL 客户端执行后台业务规则。

11. 预算编制支持固定期间预算编制和滚动预算编制。滚动预算支持两种滚动方式：

1) 每期向后滚动一期，保持预算期间长度不变；

2) 预算期间不变，每期编制预算时会将已经结束期间的预算数替换为实际数。

12. 按照用于控制的数据是固定还是变动的区分，支持以下控制方式：

1) 固定控制：\支持按照固定的预算的确定的比例对实际业务进行控制；

2) 弹性控制：以收定支的控制模式，即按照当期的实际收入的一定比例来动态确定本期可开支的费用；

3) 对于需要编制而未上报的预算，支持设置零预算控制规则来对业务系统的实际业务进行控制。

13\. 按照超预算后实际业务的处理方式不同，支持以下控制方式：

1) 支持刚性控制：超过预算后不允许业务发生；

2) 支持柔性控制：当实际发生数超过预算额度或属于预算外项目时，支持由相应人员判断是否执行特殊审批流程，若启动特殊审批流程，则超预算的业务单据通过特殊审批后仍可以继续发生；

3) 支持预警性控制：在业务系统作业务单据或审批单据时，超过预算后系统只给出提示信息，业务仍可继续发生。

14. 支持根据不同的管理要求选择各种调整方式，可根据不同的调整方式走不同的流程：

1) 直接调整：调整审批的对象是整个计划表；

2) 调整单调整：调整审批的对象是调整单，支持根据不同的调整内容设置不同的审批流程，如只调整数据、追加项目等，支持用户自定义调整类型；

3) 调剂单调整：调整审批的对象是调剂单，调增和调减的合计数为 0，支持用户自定义调剂类型；

4) 支持对多主体的任务进行集中调整。

### 15 \. 预算分析：

1) 支持两种分析的应用：A、支持集团统一建立分析模板，各预算主体选择相关信息后进行数据展现；B、支持直接选择查询条件（具体成员和规则成员），刷新即可查询到预算及执行相关数据；

2) 预算分析和财务系统的高度集成：支持预算从现金管理、应收应付、报销管理、总账统取实际发生数进行分析，并可联查到业务系统的各种明细账、表，直至业务单据（凭证）；

3) 支持预算和 iufo 报表的双向取数，便于预算数和决算数据进行对比分析。

16. 支持预算编制阶段和调整阶段进行预算模拟测算：

1) 支持在编制预算前期根据不同的假设进行模拟测算，保存多个测算版本，最终选择一个合适的版本数据作为最后编制上报的数据；

2) 支持在预算调整前进行模拟测算，根据测算结果来申请作预算调整，审批同意后再作预算调整。

## 第二章 应用场景

### 2.1 设置预算任务

## 业务描述

在企业的预算管理过程中，预算样表的分配、预算数据的提交、审批等大多都是按照一套预算表，即一个 Excel 文件（book）为单位来组织。预算任务设置便是用来创建一个包含一套预算表的编制任务或者分析任务，并对任务指定年、月、业务方案、版本等参数，再将任务分配给编制主体，同时指定该任务的责任主体及可用预算样表。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务--任务管理-全局/集团/组织</td></tr></table>

## 产品解决方案

1. 在 NC 客户端创建预算任务，进行任务分配和任务管理，任务名称要求全局范围内唯一。

2. 任务管理支持三级管控：

【财务会计】-【费用预算】-【预算任务】-【任务管理-全局/集团/组织】节点中，下一级组织的节点可查看并再分配上一级组织的预算任务，也可新建本组织的任务并分配给该组织及其下级组织。例如：集团级可查看全局级的任务并分配，或创建本集团的自有任务；组织级可查看全局级及所属集团的任务并分配，或创建本组织的自有任务。任务管理以左树右表的方式展现，如图 2.1-01 所示为集团级的任务管理节点。

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_157_1074_576.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.1-01 任务管理-集团</div>


1) 任务必须关联套表，根据当前用户权限和模块启用情况，可选择不同的系统如全面预算，费用预算、采购计划、资金计划等，如图 2.1-02 所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">修改任务</td></tr></table>

<div style="text-align: center;">图 2.1-02 修改任务</div>

2) 任务可进行参数维实例化（指定业务方案、年、月、币种、版本等，如图 2.1-03 所示），并将任务分配给编制主体、指定该任务的责任主体，默认责任主体参照编制主体生成，各编制主体可选择不同的预算表单，如图 2.6-03 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_306_1111_1056.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.1-03 选择表单范围</div>


注意：在没有创建任务实例前，所有任务基础信息都可以改；创建任务实例后，只能修改选择编制主体和责任主体。同时，任务支持复制和删除的处理方式，可复制指定任务的编制主体、任务类型、可用系统等基础信息后对这些基础信息进行修改，修改后需要输入新的任务名称保存；删除任务则要求任务列表中所有实例化的任务均处于关闭状态。

3) 预算任务可以查看一个或多个预算任务的具体的状态（预算任务的状态分为：已启动、编制中、已提交、审批中、审批通过、审批不通过），只有已启动、编制中和审批不通过的任务可以提交数据，其他状态的任务不能提交数据，如图 2.1-04 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_162_1075_605.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.1-04 任务管理-全局</div>


关于预算任务各状态的说明如下：

a) 未启动：任务实例的初始虚拟状态；

b) 已启动：系统管理员操作“启动任务”图标按钮后，任务状态改为“已启动”；

c) 编制中：编制版本和直接调整版本的数据从 Excel 客户端 “提交数据” 后，任务实例的状态为 “编制中”；

d) 待调整：指启动了单据调整，待单据调整状态的任务；任务实例状态为“审批生效”和“待调整”的任务，可以启动直接调整（为保证自动汇总的一致性，勾选下级主体时启动调整时，会自动勾选其所有上级主体）；

e) 调整中：启动直接调整或单据调整后，任务状态改为“调整中”，此时可在 Excel 客户端下载该任务实例进行调整编辑；

f) 已提交：编制版本和直接调整版本的数据从 Excel 客户端 “提交审批” 后，任务实例的状态为 “已提交”；

g) 审批中：提交审批后和前一个审批人审批意见为审批通过，待下一个审批人审批的任务状态为“审批中”；

h) 审批通过：当所有审批人全部审批通过后任务状态为“审批通过”。

i) 审批不通过：当审批流程中，其中一个审批人进行了“不批准”或“驳回”的操作，任务状态为“审批不通过”。

4) 对预算任务可指定 UAP 审批流，并通过优先级来实现个别预算任务实例的特殊审批流程，预算任务管理处每增加一个任务，则 UAP 定义审批流的单据类型下将对应的增加一个交易类型(审批流定义

如图 2.1-06 所示，审批流设置详细操作参见《NCV6.3 产品手册-审批流》），在任务上绑定审批流时，只能参照该单据类型和本交易类型所对应的审批流，若参数维组合对应的审批流设置重复，则按优先级高（1 为最高）的执行。预算任务中指定审批流如图 2.1-05 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_302_1074_937.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.1-05 选择审批流</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>审批流定义</td><td colspan="2">任务管理-全局</td></tr></table>

<div style="text-align: center;">图 2.1-06 审批流定义</div>


5) 每个预算任务可指定计算规则、审核规则、折算规则、执行取数规则等，将相关业务规则指定到任

务上，其后可在 EXCEL 客户端执行相关操作（如规则运算、折算规则、审核规则、执行取数规则等，如图 2.1-08 所示）触发所选规则，或在【财务会计】-【费用预算】-【预算监控】-【预算执行】中执行“执行取数规则”触发所选的取数规则。如图 2.1-07 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_147_311_1113_973.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.1-07 计算规则</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_113_1045_1076_1301.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.1-08 预算编制</div>

### 2.2 预算编制

#### 2.2.1 预算编制流程

## 业务描述

➢ 预算编制流程上至少应包括预算的编报、审批环节，这两个环节完成之后的预算数据才是生效数据，其中预算审批应能结合本单位的审批流应用到财务、业务的事中控制，具体包括：

各业务单位预算管理人员负责录入预算数；

各业务单位将编制完成的预算报送上级单位审批；

☑ 各预算主管单位汇总、合并下级单位报上来的预算；

☐ 预算委员会审核批准的预算；

☑ 各预算管理单位将批准的预算下达到各预算执行单位，并按此监控各业务单位的预算执行情况。

➢ 预算编制方式：需要满足支持自上而下和自下而上两种方式：

♦ 自上而下：由集团预算编制委员会先制定出总的计划，然后逐层分解到各单位\部门，各单位\部门对计划进行相应的调整后，再进行汇总；

♦ 自下而上：由各单位\部门负责人先编制计划，然后汇总生成总的计划，集团预算编制委员会针对汇总计划进行调整后，再形成各单位的计划。

预算编制应能骤支持直接采用类似 Excel 既具方式的设计与填报，也能通过 NC 端选择任务、期间、主体后筛选任务进行填报。

预算表样应能满足固定表、浮动表（指行或列可变的表）等不同的格式要求。

预算编制应能支持滚动预算的处理，包括：

☐ 预算期间不断延伸的滚动预算；

☑ 预算期间固定的滚动预算。

预算期间设定上需要满足固定频度预算的编制和自定义期间预算编制。

预算编制过程中可以将编制的预算数据折算为另外一币种预算数据。

预算编制可以结合 UAP 的审批流应用。

## 业务流程

<div style="text-align: center;">编制任务流程&状态</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_115_290_1061_1384.jpg" alt="Image" width="79%" /></div>


<div style="text-align: center;">图 2.1.1.1-01 业务流程</div>

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="23">动态建模平台</td><td rowspan="4">组织管理</td><td style='text-align: center; word-wrap: break-word;'>业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>成本中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算组织体系-全局/集团</td></tr><tr><td rowspan="5">基础数据</td><td style='text-align: center; word-wrap: break-word;'>公共信息-会计期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公共信息-币种</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义项-自定义栏</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义项-自定义栏</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>流程管理</td><td style='text-align: center; word-wrap: break-word;'>流程设计-审批流定</td></tr><tr><td rowspan="11">计划平台</td><td style='text-align: center; word-wrap: break-word;'>系统设置-控制策略</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算档案-预算科</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算档案-业务方</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算档案-预算版本-全局/集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算档案-自定义计划期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-指标属性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-业务规则-全局/集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-控制规则-全局/集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理-全局/集团/组织</td></tr><tr><td rowspan="2">预算Excel端</td><td style='text-align: center; word-wrap: break-word;'>预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算分析</td></tr><tr><td rowspan="8">财务会计</td><td rowspan="8">费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-业务规则-全局/集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-控制规则-全局/集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理-全局/集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理-全局/集团/组织</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Excel功能-预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Excel功能-预算分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算编制-预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算编制-预算桌面</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td rowspan="2"></td><td style='text-align: center; word-wrap: break-word;'>预算编制-预算审批</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算编制-预算查阅</td></tr></table>

说明：

● 上表中基础数据包含从会计期间、币种到自定义项的所有基础档案，未全部罗列，实施中根据需要调用。

● 上表中红色的业务规则、控制规则及黄色的 Excel 功能，在建模平台和费用预算中均可点击进入，建议以动态建模平台的为准。

## 产品解决方案

### 1. 建立预算编制任务：

路径：【财务会计】-【费用预算】-【预算任务】-【任务管理-全局/集团/组织】

操作：输入任务名称，选择关联套表、选择需要编制该预算的单位。如图 2.2.1-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_577_1123_1051.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-01 任务管理-全局</div>


### 2. 启动预算任务：

第一步，选择任务参数维，如：业务方案（预算数）、年（本例为 2012 年）、原币（人民币）、版本（默认版本）；

第二步，选择编制主体，启动预算任务；

第三步，点【启动】按钮，对应任务实例的状态变为“已启动”。如图 2.2.1-02 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_159_1123_632.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-02 任务管理-全局</div>


### 3. 预算编制：

1) 方式 A：在 Excel 端【预算编制】页签中进行预算数据的填制：

● 在打开的 Excel 表中选择 “NC 计划预算” 页签，依次执行图 2.2.1-03 中所示操作，进入到 Excel 预算编制窗口；


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Book1 - Microsoft Excel</td></tr></table>

<div style="text-align: center;">图 2.2.1-03 NC 计划预算</div>


● 在 Excel 预算编制页签窗口中下载任务，选择编制中、已启动、调整中的任务，勾选后确定，如图 2.2.1-04 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_297_1122_916.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.1-04 下载任务</div>


● 在打开的预算表中选择对应的预算表页签，录入数据或执行相应的规则运算、取数规则后，点击【提交数据】，确认无误后点击【上报数据】，则预算编制即告完成。

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_154_1124_708.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.1-05 提交数据</div>


● 若当前预算任务未配置审批流，则预算任务状态自动变更为“已上报”，如图 2.2.1-06 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_816_1121_1291.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.1-06 任务管理-全局</div>


● 若当前预算任务配有审批流，则预算任务状态自动变更为“审批中”。

2) 方式 B: NC 客户端中编制预算:

● 路径：【财务会计】-【费用预算】-【预算编制】-【预算编制】/【预算桌面】

● 节点中选择 “已启动”、“编制中”、“调整中” 和 “审批不通过” 状态的任务,录入数据:

● 预算编制操作顺序为：选择预算任务->选择预算主体->点击【编制】->录入数据或点击【公式计算】、【公式审核】->点击【保存】，操作顺序如图 2.2.1-07 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_254_1123_804.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.1-07 预算编制操作</div>


● 浮动表的增行操作参见 2.2.2.2 中产品解决方案的第六步预算填制。

● 预算编制完毕，确认无误后，点击功能菜单钮中的【审批-上报】或快捷功能钮中的【上报】，将预算提报上级汇总或审批，如图 2.2.1-08 所示：

大型企业管理与电子商务平台

-回×

<div style="text-align: center;"><img src="imgs/img_in_image_box_145_157_1124_803.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-08 审批</div>


● 上报完成后，当前预算主体更新为红色的“已上报”状态，在预算任务管理节点则根据当前预算任务是否配有审批流而变更其任务状态，如图 2.2.1-09 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_150_1124_706.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-09 审批</div>


说明：【预算编制】或【预算桌面】节点的界面中，各主体的不同颜色标识当前任务的不同状态：

● 黑色：表示当前任务为“已启动”、“编制中”或“审批不通过”状态；

● 红色：表示当前任务为“已上报”状态；

● 蓝色：表示当前任务为“审批通过”状态；

● 黑色下划线：表示当前任务为“调整中”状态；

● 红色下划线：表示当前任务为调整流程的“已上报”状态；

● 蓝色下划线：表示当前任务为调整流程的“审批通过”状态；

4. 预算审批：

1) 路径：【财务会计】-【费用预算】-【预算编制】-【预算审批】/【预算桌面】（若经审批流审批则可通过 NC 常用功能的工作任务中触发，如图 2.2.1-10 所示）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_143_157_1125_731.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-10 功能导航</div>


2) 对已《提父审批》的任务进行《审批》（或根据预算任务的审批流配置情况逐级审批至通过），如图图 2.2.1-11 所示。审批通过的预算显示为蓝色，并支持联查审批意见，如 2.2.1-12 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_888_1124_1435.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-11 审批流处理情况</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_145_156_1122_709.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-12 审批流处理情况</div>


5. 如果审批通过，则任务正式生效，正式生效之后系统不支持再反操作修改；

6. 如果审批不通过，则将任务退回，可在 Excel 端“预算编制”页签或【预算编制】/【预算桌面】节点重新填制，填制完成后，再提交审批。

7. 预算组织体系中非末级的预算主体可对下级单位报送的预算进行汇总处理，如图 2.2.1-13 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_145_951_1122_1478.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-13 选择汇总单位</div>

8. 汇总后的数据经刷新后，可联查其本级及下级指标数据，如图 2.2.1-14 所示。

<div style="text-align: center;">预算桌面_2012年ys01_all_预算数人民币_默认版本（总经理室）</div>


-回×

<div style="text-align: center;"><img src="imgs/img_in_image_box_144_268_1123_886.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.2.1-14 查询所有下级</div>


- 差额汇总：点按钮【差额汇总】时，系统进行如下运算：差额主体数据=非末级主体数据-SUM（非末级主体的直接下级）数据。注意：只有预算组织体系成员中标记为差额组织的预算业务单元，才能在差额汇总的时候记录相应的差额数据；且浮动表不处理可变维上的差额。

#### 2.2.2 不同格式要求预算表的编制

预算表的不同格式主要通过预算表样设计的不同方式实现，其预算任务的制定及预算编制基本相同，因此本节着重描述不同预算样表的设计。

##### 2.2.2.1 固定表编制

## 业务描述

固定表是预算样表中最常见的样式，例如管理费用预算表、销售费用预算表、预计资产负债表、预计利润表、预计现金流量表等。

## 业务举例

现有一张管理费用预算表如表 2.2.2.1-01 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>N-1年1-9月实际数</td><td style='text-align: center; word-wrap: break-word;'>N-1年预算数</td><td style='text-align: center; word-wrap: break-word;'>合计</td><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td colspan="3">N年预算数</td></tr></table>

<div style="text-align: center;">表 2.2.2.1-01</div>


## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>会计信息-会计科目</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开发平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开发平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-业务规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-控制规则</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr></table>

## 产品解决方案

### 1. 建立指标

1) 此例中，使用会计科目档案作为预算指标，需要预置好会计科目管理费用的科目明细。

2) 使用会计科目档案作为预算指标，后期能对总账凭证进行预算控制，并且能够取到总账执行数进行预算执行情况分析。

3) 固定表设计的过程就是创建维度向量的过程，维度的组合最好能正确表达数据的业务含义。

4) 多个维度组合时，不同维度尽量分行/分列显示。

### 2. 建立维度

此例中，可以使用系统预置的指标维、计划期间维度、业务方案维度。

### 3. 建立应用模型

在【【动态建模平台】-【计划平台】-【模型设置】-【应用模型】节点建立应用模型(本例为 02 费用应用模型)，维度成员如图 2.2.2.1-02 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_342_1081_708.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.1-02 应用模型</div>


### 4. 表单设计&套表管理

1) 设计向导：确定应用模型、参数维和行/列维度

登陆 Excel 客户端，在【表单设计】页签下，通过“设计向导”选择应用模型，确定参数维、行/列维度等。

行维度：指标

列维度：年、月、业务方案

参数维：主体、年、版本、币种、业务方案

注意问题：

a) 使用“设计向导”生成样表后，还能修改行/列维度。点击【表单设计管理】按钮弹出界面中选中表头区域设置页签，可在此增删行/列维度。

b) 生成样表区域时支持两种方式：

● 新建样表，即从 0 开始设计样表，系统生成样表区域作为设计参考；

● 已有客户样表，指表单设计根据用户已有预算样表格式来设计，不自动生成行/列编码区。

在本示例中，均使用“已有客户样表”的方式。

## 2 ) 匹配行/列维度成员

a) 行表头直接匹配“指标”维度。匹配样表时，可使用以下两种方式匹配指标维度：

● 通过维度信息面板的填充功能匹配指标。

● 通过维度信息面板上的图标快速匹配行/列维度，功能同：右键——快速匹配行/列维度。

● 行表头匹配完成后，将得到结果如图 2.2.2.1-03 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>指标</td><td style='text-align: center; word-wrap: break-word;'>费用要素</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.660201</td><td style='text-align: center; word-wrap: break-word;'>办公费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020101</td><td style='text-align: center; word-wrap: break-word;'>业务费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020102</td><td style='text-align: center; word-wrap: break-word;'>邮电通讯费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010201</td><td style='text-align: center; word-wrap: break-word;'>水电费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010202</td><td style='text-align: center; word-wrap: break-word;'>折旧费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010203</td><td style='text-align: center; word-wrap: break-word;'>修理费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010204</td><td style='text-align: center; word-wrap: break-word;'>财产保险费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010205</td><td style='text-align: center; word-wrap: break-word;'>租赁费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010288</td><td style='text-align: center; word-wrap: break-word;'>燃料</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020103</td><td style='text-align: center; word-wrap: break-word;'>低值易耗品摊销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010301</td><td style='text-align: center; word-wrap: break-word;'>会议费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010302</td><td style='text-align: center; word-wrap: break-word;'>业务招待费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010303</td><td style='text-align: center; word-wrap: break-word;'>劳动保护费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010304</td><td style='text-align: center; word-wrap: break-word;'>资产摊销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010305</td><td style='text-align: center; word-wrap: break-word;'>营销费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010306</td><td style='text-align: center; word-wrap: break-word;'>运输费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010307</td><td style='text-align: center; word-wrap: break-word;'>广告费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602010388</td><td style='text-align: center; word-wrap: break-word;'>展览费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020104</td><td style='text-align: center; word-wrap: break-word;'>售后服务费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020105</td><td style='text-align: center; word-wrap: break-word;'>包装费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020106</td><td style='text-align: center; word-wrap: break-word;'>装卸费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020107</td><td style='text-align: center; word-wrap: break-word;'>委托代销手续费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020108</td><td style='text-align: center; word-wrap: break-word;'>仓储保管费用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66020109</td><td style='text-align: center; word-wrap: break-word;'>样品及产品损耗</td></tr><tr><td colspan="2">合计：</td></tr></table>

<div style="text-align: center;">图 2.2.2.1-03</div>


行维度上的“合计”使用 Excel 的 SUM 公式。

b) 列表头对应年、月和业务方案三个维度，其中 “月” 维度需要使用累计函数，“年” 维度需要使用滚动函数。最终设计完成后将得到样表如图 2.2.2.1-04（星号标注为方便描述而后加的）：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">2.</td></tr></table>

<div style="text-align: center;">图 2.2.2.1-04</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_328_698_384_730.jpg" alt="Image" width="4%" /></div>


● 在  $ \left\{\begin{array}{l}1 \\ \text{区域的列表头编码区单元格需设置滚动年 } N-1 \text{，如图 } 2.2.2.1-05 \text{ 所示: }\end{array}\right. $

<div style="text-align: center;"><img src="imgs/img_in_image_box_286_779_894_1185.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">图 2.2.2.1-05</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_322_1226_376_1261.jpg" alt="Image" width="4%" /></div>


● 在  $ \sum_{n=1}^{\infty}2\sum_{n=1}^{\infty} $ 区域的列表头编码区单元格需设置滚动年 N4，如图 2.2.2.1-06 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_296_152_896_556.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.2.2.1-06</div>


● 在  $ \begin{array}{c} \text{M} \\ \text{M} \end{array} $ 区域的列表头编码区单元格需设置累计函数 1-9 月，如图 2.2.2.1-07 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_318_601_378_685.jpg" alt="Image" width="5%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_253_692_944_1256.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">图 2.2.2.1-07</div>


● 其余的列表头匹配对应的维度成员即可。

注：本例中月维度编码区设置为空时，表示取1-12月的合计，如图2.2.2.1-08所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_317_164_871_299.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 2.2.2.1-08</div>


## 3 ) 提交套表并发布

〖提交套表〗：表单设计完成后，点此按钮提交套表到 NC 客户端的套表管理节点。注：需要先在套表管理节点新建分类文件夹。

套表提交后需要在【财务会计】-【费用预算】-【模型设置】-【套表管理】节点发布（如图 2.2.2.1-09 所示），然后才能在【财务会计】-【全面预算】-【预算任务】-【任务管理-全局/集团/组织】节点创建任务模板时参照到该套表。

<div style="text-align: center;"><img src="imgs/img_in_image_box_145_690_1120_1154.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.1-09</div>


5. 任务管理：建立并启动预算编制任务，详细操作参见 2.1。

6. 预算填制：参见 2.2.1 节内容。

##### 2.2.2.2 浮动表编制

## 业务描述

如果预算样表的某些维度成员集团进行在样表设计时不能确定，可以设置为浮动表，在各个单位编制时再自行添加维度成员。

## 业务示例

现有一张预算样表如图 2.2.2.2-01 所示。其中，期数是浮动维。

<div style="text-align: center;">三项成本结转表</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">编制单位：</td></tr></table>

<div style="text-align: center;">图 2.2.2.2-01</div>


## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>自定义项-自定义档案定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>基础数据</td><td style='text-align: center; word-wrap: break-word;'>自定义项-自定义档案维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr></table>

## 产品解决方案

### 1. 建立自定义档案并维护档案成员

在【企业建模平台】-【基础数据】-【自定义项】-【自定义档案定义】节点，新增自定义档案：统计维、项目期数两个维度。如图 2.2.2.2-02 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_1144_1076_1286.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.2.2-02</div>


在【企业建模平台】-【基础数据】-【自定义项】-【自定义档案维护-全局/集团/业务单元】节点，维护统计维和项目期数两个维度的档案成员。如图 2.2.2.2-03 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_106_1082_371.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-03</div>


### 2. 建立维度

在【动态建模平台】-【计划平台】-【模型设置】-【维度管理】节点新增维度：统计维和项目期数，分别与之前自定义的两个档案相对应。如图 2.2.2.2-04 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_541_1080_1013.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-04</div>


### 3. 建立应用模型

在【动态建模平台】-【计划平台】-【模型设置】-【应用模型】节点建立应用模型 01 项目预算，维度成员如图 2.2.2.2-05 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_155_1080_675.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-05</div>


### 4. 表单设计 & 套表管理

1) 设计向导：确定应用模型、参数维和行/列维度

登陆 Excel 客户端，在【表单设计】页签下，通过“设计向导”选择应用模型，确定参数维、行/列维度等。

行维度：指标、项目期数

列维度：统计维

参数维：主体、年、版本、原币、业务方案

注意问题：

a) 使用 “设计向导” 生成样表后，还能修改行/列维度。点击【表单设计管理】按钮弹出界面中选中表头区域设置页签，可在此增删行/列维度。

b) 生成样表区域时支持两种方式：

● 新建样表，即从 0 开始设计样表，系统生成样表区域作为设计参考；

● 已有客户样表，指表单设计根据用户已有预算样表格式来设计，不自动生成行/列编码区。

在本示例中，均使用“已有客户样表”的方式。

## 2 ) 匹配行/列维度成员

a) 行表头的“项目期数”维度需设置为浮动，指标维度为固定的三个成员：土地费用、前期费用和工程成本，操作顺序如下：

● 匹配行指标维度的三个成员：土地费用、前期费用和工程成本，如图 2.2.2.2-06 所示；

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_370_1123_1078.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-06</div>


选中“项目期数”维度文本所在单元格，对其进行“合并单元格”设置，之后点击“浮动设置-行浮动区”(或右击鼠标，点“生成业务区-行浮动区”)设置行浮动，如图2.2.2.2-07所示；

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_154_1124_513.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-07</div>


● 对项目期数所在的文本单元设置“浮动单元格类型-可变维”，维度指定为“项目期数”，如图 2.2.2.2-08 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_714_1123_1288.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-08</div>


● 同样地，对 “土地费用” 所在的文本单元设置 “浮动单元格类型-多维区域浮动”，维度指定为 “指标”，如图 2.2.2.2-09 所示；

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_151_1119_707.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-09</div>


b) 列表头直接匹配 “统计维” 维度。匹配样表时，可使用以下两种方式匹配指标维度：

● 通过维度信息面板的填充功能匹配指标。

● 通过维度信息面板上的图标快速匹配行/列维度，功能同：右键——快速匹配行/列维度。

“备注”列需通过 Excel Ribbon 区的生成业务区-备注说明区，或是鼠标右键：生成业务区-备注说明区来实现行备注区的设置。

c) 表头需设置任务属性函数。

● 表头的“编制单位”需设置如下属性函数，取任务的主体名称。如图 2.2.2.2-10 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_325_168_917_701.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 2.2.2.2-10</div>


● 表头的“预算年度”需设置如下属性函数，取任务的年。如图 2.2.2.2-11 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_306_830_912_1368.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.2.2.2-11</div>


最终设计完成后将得到样表如图 2.2.2.2-12 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目期数</td><td style='text-align: center; word-wrap: break-word;'>指标</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>统计维</td><td style='text-align: center; word-wrap: break-word;'>global.01</td><td style='text-align: center; word-wrap: break-word;'>global.02</td><td style='text-align: center; word-wrap: break-word;'>global.03</td><td style='text-align: center; word-wrap: break-word;'>global.04</td><td style='text-align: center; word-wrap: break-word;'>global.05</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目期数</td><td style='text-align: center; word-wrap: break-word;'>指标</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>总成本</td><td style='text-align: center; word-wrap: break-word;'>截止上年</td><td style='text-align: center; word-wrap: break-word;'>总未结转</td><td style='text-align: center; word-wrap: break-word;'>预计结转</td><td style='text-align: center; word-wrap: break-word;'>本年预算结转面积（₹2）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>global.xn</td><td style='text-align: center; word-wrap: break-word;'>TB.global</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>土地费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>global.xn</td><td style='text-align: center; word-wrap: break-word;'>TB.global</td><td style='text-align: center; word-wrap: break-word;'>Dim#xmqs</td><td style='text-align: center; word-wrap: break-word;'>前期费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>global.xn</td><td style='text-align: center; word-wrap: break-word;'>TB.global</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>工程成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.2.2.2-12</div>


## 1 ) 提交套表并发布

〖提交套表〗：表单设计完成后，点此按钮提交套表到 NC 客户端的套表管理节点。注：需要先在套表管理节点新建分类文件夹。

套表提交后需要在【动态建模平台】-【计划平台】-【模型设置】-【套表管理】节点发布，以便【任务管理】节点创建任务模板时参照到该套表。如图 2.2.2.2-13 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_148_680_1112_925.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.2.2-13</div>


1. 任务管理：进行预算编制任务的创建与启用，参见 3.1.1.4 中的第 1、2 步内容。

### 2. 预算填制：

1）在 Excel 客户端进行预算编制时，每次点击 “编辑浮动区-浮动增行”，则会自动弹出选择维度成员窗口，若勾选 “是否只新增空浮动区” 并指定浮动区数，则自动弹出新增的空行数；若不勾选 “是否只增空浮动区”，而是直接勾选指标值，则直接新增带有指标值的行数，新增时按三行（土地费用、前期费用、工程成本）的倍数增加，如图 2.2.2.2-14、图 2.2.2.2-15 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_155_1121_919.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-14</div>


<div style="text-align: center;">三项成本结转表</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>总成本</td><td style='text-align: center; word-wrap: break-word;'>截止上年</td><td style='text-align: center; word-wrap: break-word;'>总未结转</td><td style='text-align: center; word-wrap: break-word;'>预计结转</td><td style='text-align: center; word-wrap: break-word;'>本年预算结转面积（m2）</td></tr><tr><td rowspan="6">项目期数</td><td style='text-align: center; word-wrap: break-word;'>土地费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前期费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工程成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>土地费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前期费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工程成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">aa</td><td style='text-align: center; word-wrap: break-word;'>土地费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前期费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工程成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">bb</td><td style='text-align: center; word-wrap: break-word;'>土地费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>前期费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工程成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.2.2.2-15</div>


1）在 NC 客户端的【预算编制】节点中进行预算编制时，在编制时选中可变区后点击 ☐，同样

会自动弹出选择维度成员窗口，如图 2.2.2.2-16 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_146_204_1120_757.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.2.2-16</div>


#### 2.2.3 固定频度和自定义期间预算

## 业务描述

企业集团要求编制一套年度预算：

1. 自然年度编制预算，即年度的起始时间为1月1日，结束日期为12月31日；

2. 非自然年度编制预算，如年度的起始时间为4月1日，结束日期为下年度的3月31日；

3. 为了控制日常的业务要求各预算组织编制细化的月度（或季度、半年等）预算；

4. 支持编制三年或五年等其他长期计划。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开发平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开发平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>预算档案-自定义计划期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开发平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-表单设计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr></table>

## 产品解决方案

### 1. 设置计划期间

预算系统提供的时间维度分为两大类：标准计划期间和自定义计划期间。

1) 标准计划期间，如图 2.2.3-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_444_1075_1023.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.3-01</div>


标准时间维度系统预置维度如表 2.2.3-01 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>维度定义名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基准会计期间方案</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年半年季月旬</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年季月</td><td style='text-align: center; word-wrap: break-word;'>允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年月</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年双周</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年周</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自定义计划期间</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WBS</td><td style='text-align: center; word-wrap: break-word;'>不允许增加成员</td></tr></table>

<div style="text-align: center;">表 2.2.3-01</div>


a) 支持周维度应用，目前只支持自然周；每年的第一天就是第一周的第一天，第一周不一定是 7 天；

b) 对于年维度，系统允许增加、修改、删除维度成员，并且在增加一个新的年维度成员时，系统自动为其增加下级季度、月份成员。

2) 自定义计划期间：自定义计划期间支持增加起始结束时间没有规律的时间维，如图 2.2.3-02 所示；

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_431_1077_574.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.3-02</div>


增加自定义计划期间成员，如“项目阶段一”，其可以任意指定起始和结束日期，如起始日期 2008-3-1，结束日期为 2010-4-30。

### 2. 建立应用模型

在建立应用模型时，可以根据不同的预算编制频度和期间，选择自定义计划期间作为计划期间的汇总结构。

### 3. 表单设计&套表管理

在 Excel 端【表单设计】节点完成表单格式设计的工作。设计完成后提交到【财务会计】-【费用预算】-【模型设置】-【套表管理】节点，并【发布】。

### 4. 任务管理

在【财务会计】-【费用预算】-【预算任务】-【任务管理】节点完成创建预算任务并启动相关任务实例。

#### 2.2.4 滚动预算的编制

产品可以支持如下滚动预算的编制方式：

##### 2.2.4.1 预算期间不断延伸的滚动预算

## 业务描述

随着时间的推移和预算的执行，其预算时间不断延伸，预算内容不断补充，整个预算处于永续滚动状

态的一种预算方法。

## 业务举例

现举一例说明，预算按照季度滚动编制，在最近的预算编制期间需要细化到月度，如图 2.2.4.1-01 所示：

<div style="text-align: center;">2011年1季度</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_206_356_977_631.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 2.2.4.1-01</div>


## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr></table>

## 产品解决方案

### 1. 建立维度

在本例中，需要使用“年季月”结构的计划期间，“年维度”的成员需要手工增加，此例中在2012年2季度编制预算时，计划期间就会延续到2013年，所以需要在【动态建模平台】-【计划平台】-【模型设置】【维度管理】节点将“年维度”成员添加到2013年。如图2.2.4.1-02所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_156_1077_520.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.4.1-02</div>


### 2. 创建应用模型

在【动态建模平台】-【计划平台】-【模型设置】-【应用模型】节点创建应用模型，计划期间的汇总结构选择“年季月”。如图 2.2.4.1-03 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_105_746_1072_1043.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.4.1-03</div>


### 3. 表单设计&套表管理

1) 在 Excel 端【表单设计】页签，通过“设计向导”选择应用模型，确定参数维、行/列维度等。

a) 参数维：本例为按季度滚动，参数维需同时选择“年和季”，如图 2.2.4.1-04 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_156_1074_830.jpg" alt="Image" width="80%" /></div>


图 2.2.4.1-04

b) 行/列维度：列维度需选择“季和月”，如图 2.2.4.1-05 所示：

## 设计向导

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_166_1073_826.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.4.1-05</div>


2) 匹配行/列维度。

列维度需要插入滚动期间函数。

“季”对应的编码区，如图 2.2.4.1-06 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_998_893_1397.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.2.4.1-06</div>


“月”对应的编码区如图2.2.4.1-76所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_296_156_899_554.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.2.4.1-07</div>


设计完成后列表头得到如图 3.1.4.1-07 所示的格式：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N+1</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N+1</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N+3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N+1</td><td style='text-align: center; word-wrap: break-word;'>#QuARTER</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N+1</td><td style='text-align: center; word-wrap: break-word;'>#QuARTER</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N</td><td style='text-align: center; word-wrap: break-word;'>#Roll#=N+3</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.2.4.1-08</div>


## 3 ) 提交套表并发布

【提交套表】：表单设计完成后，点此按钮提交套表到 NC 客户端的套表管理节点。注：需要先在套表管理节点新建分类文件夹。

套表提交后需要在【财务会计】-【费用预算】-【模型设置】-【套表管理】节点发布，然后才能在任务管理节点创建任务模板时参照到该套表。

### 4. 任务管理

在【财务会计】-【费用预算】-【预算任务】-【任务管理-全局/集团/组织】节点完成创建预算任务，选择参数维成员组合实例化，此例中设置“季=2季度，年=2012年”时，则N季度实例化为2012年2季度，N+1季度实例化为2012年3季度，以此类推。

### 5. 预算编制

在 Excel 客户端【预算编制】页签，下载相关任务，即得到如图 2.2.4.1-09 所示显示效果。

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_155_1077_521.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.4.1-09</div>


##### 2.2.4.2 预算期间固定的滚动预算

## 业务描述

每个期间编制预算包括的期间是固定的，但是在预算编制前要求将本期间之前期间的预算数替换为执行数，并将预算数与执行数之间的差额按照某种规则分摊到本期及以后各期间。

## 业务举例

年度预算编制到月，每个月将之前期间数据替换为执行数，再滚动预测以后期间的预算。如图 2.2.4.2-01 所示：

<div style="text-align: center;">2011年1月</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td style='text-align: center; word-wrap: break-word;'>5月</td><td style='text-align: center; word-wrap: break-word;'>6月</td><td style='text-align: center; word-wrap: break-word;'>7月</td><td style='text-align: center; word-wrap: break-word;'>8月</td><td style='text-align: center; word-wrap: break-word;'>9月</td><td style='text-align: center; word-wrap: break-word;'>10月</td><td style='text-align: center; word-wrap: break-word;'>11月</td><td style='text-align: center; word-wrap: break-word;'>12月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算数</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td><td style='text-align: center; word-wrap: break-word;'>预算数1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>生产成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>制造费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">2011年2月</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td style='text-align: center; word-wrap: break-word;'>5月</td><td style='text-align: center; word-wrap: break-word;'>6月</td><td style='text-align: center; word-wrap: break-word;'>7月</td><td style='text-align: center; word-wrap: break-word;'>8月</td><td style='text-align: center; word-wrap: break-word;'>9月</td><td style='text-align: center; word-wrap: break-word;'>10月</td><td style='text-align: center; word-wrap: break-word;'>11月</td><td style='text-align: center; word-wrap: break-word;'>12月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>实际数</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td><td style='text-align: center; word-wrap: break-word;'>预算数2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>生产成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>制造费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.2.4.2-01</div>


## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr></table>

## 产品解决方案

### 1. 建立维度

在本例中，需要使用“年月”结构的计划期间，“年维度”的成员需要手工增加，可以在【动态建模平台】-【计划平台】-【模型设置】-【维度管理】节点将“年维度”成员添加到2013年。如图2.2.4.2-02所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_363_1076_723.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.2.4.2-02</div>


### 2. 创建应用模型

在【动态建模平台】-【计划平台】-【模型设置】-【应用模型】节点创建应用模型，计划期间的汇总结构选择“年月”。

### 3. 表单设计 & 套表管理

1) 在 Excel 端【表单设计】页签，通过“设计向导”选择应用模型，确定参数维、行/列维度等。

a) 参数维：本例为按月滚动，参数维需同时选择“年和月”，如图 2.2.4.2-03 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_150_1079_709.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.4.2-03</div>


b) 行/列维度：列维度需选择“月和业务方案”，如图 2.2.4.2-04 所示：

## 设计向导

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_814_1081_1375.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.4.2-04</div>


## 2 ) 匹配行/列维度

列维度需要插入滚动预测函数。

选中“业务方案”维度编码区，插入滚动预测函数，如图 2.2.4.2-05 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_296_203_900_601.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">2.2.4.2-05</div>


设计完成后列表头得到如 2.2.4.2-05 所示格式：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td style='text-align: center; word-wrap: break-word;'>5月</td><td style='text-align: center; word-wrap: break-word;'>6月</td><td style='text-align: center; word-wrap: break-word;'>7月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td><td style='text-align: center; word-wrap: break-word;'>#RollForecast#</td></tr></table>

3) 提交套表并发布：同前，略

### 4. 任务管理

在【财务会计】-【费用预算】-【模型设置】-【任务管理】节点完成创建预算任务，选择参数维成员组合实例化，此例中设置“月=2月，年=2012年”时，则1月对应的业务方案实例化为“实际数”，2-12月对应的业务方案实例化为“预算数”。

### 5. 预算编制

在 Excel 客户端【预算编制】页签，下载相关任务，即得到如图 2.2.4.2-07 显示效果。

<div style="text-align: center;"><img src="imgs/img_in_image_box_111_1158_1077_1425.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.4.2-07</div>


#### 2.2.5 资产负债表（双表头）

## 业务描述

资产负债表需要有两个行表头，在预算样表的设计上相对复杂。

# 资产负债表


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>资产</td><td style='text-align: center; word-wrap: break-word;'>期末余额</td><td style='text-align: center; word-wrap: break-word;'>年初余额</td><td style='text-align: center; word-wrap: break-word;'>负债和股东权益</td><td style='text-align: center; word-wrap: break-word;'>期末余额</td><td style='text-align: center; word-wrap: break-word;'>年初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>流动资产:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>流动负债:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>货币资金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>短期借款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>交易性金融资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>交品性金融负债</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收票据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付票据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收账款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付账款<img src="imgs/img_in_seal_box_742_597_837_743.jpg" alt="Image"" /></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预付款项</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>预收款项</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收利息</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付职工薪酬</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应收股利</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应交税费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付利息</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>存货</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付股利</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>一年内到期的非流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>其他应付款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他流<img src="imgs/img_in_seal_box_282_1053_411_1169.jpg" alt="Image"" /></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>一年内到期的非流动负债</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>流动资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>其他流动负债</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>非流动资产:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>流动负债合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>可供出售金融资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>非流动负债:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>持有至到期投资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>长期借款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>长期应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>应付债券</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>长期股权投资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>长期应付款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>投资性房地产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>专项应付款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>预计负债</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在建工程</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>递延所得税负债</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工程物资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>其他非流动负债</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固定资产清理</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>非流动负债合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>生产性生物资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>负债合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>油气资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>股东权益：</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>无形资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>实收资本（或股本）</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开发支出</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>资本公积</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商誉</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>减：库存股</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>长期待摊费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>盈余公积</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>递延所得税资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>未分配利润</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他非流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>股东权益合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>非流动资产合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产总计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>负债和股东权益总计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">表 2.2.5-01</div>


## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置-维度管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>预算档案—自定义计划期间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置--应用模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>预算excel端</td><td style='text-align: center; word-wrap: break-word;'>预算编制-&gt;NC计划预算--表单设计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>动态建模平台</td><td style='text-align: center; word-wrap: break-word;'>计划平台</td><td style='text-align: center; word-wrap: break-word;'>模型设置--套表管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务--任务管理-全局/集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算编制—预算编制-全局/集团/组织</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算编制—预算桌面-全局/集团/组织</td></tr></table>

## 产品解决方案

### 1 \. 设计向导：确定应用模型、参数维和行/列维度

资产负债表有两个行表头：资产类、负债和股东权益类，因为行/列表头编码区域必须连续，因此需要使用两次设计向导。

设计向导一：登陆 Excel 客户端，在【表单设计】页签下，通过“设计向导”选择应用模型，确定参数维、行/列维度等。

## 行维度：指标

## 列维度：统计维

（注：统计维应先在自定义档案中设置，本例中统计维的档案应包括期末余额和年初余额，并将“统计维”这个自定义档案加入到维度中，加后结果如图 2.2.5-01 所示。）

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_848_1123_1360.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.2.5-01</div>


参数维：主体、年、版本、原币、业务方案

## 注意问题：

1）使用 “设计向导” 生成样表后，还能修改行/列维度。点击【表单设计管理】按钮弹出界面中选中表头区域设置页签，可在此增删行/列维度。

2）生成样表区域时支持两种方式：

a）新建样表，即从0开始设计样表，系统生成样表区域作为设计参考；

b）已有客户样表，指表单设计根据用户已有预算样表格式来设计，不自动生成行/列编码区。

c）在本示例中，均使用“已有客户样表”的方式。

### 2. 匹配行/列维度成员

1）行表头直接匹配“指标”维度。匹配样表时，可使用以下两种方式匹配指标维度：

a）通过维度信息面板的填充功能匹配指标。

b) 通过维度信息面板上的图标快速匹配行/列维度，功能同：右键——快速匹配行/列维度。

行表头匹配完成后，将得到结果如图 2.2.5-02 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>资产</td><td style='text-align: center; word-wrap: break-word;'>期末余额</td><td style='text-align: center; word-wrap: break-word;'>年 末余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>流动资产：</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>货币资金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>交易性金融资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>应收票据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>应收账款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>预付款项</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>应收利息</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>应收股利</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.66</td><td style='text-align: center; word-wrap: break-word;'>存货</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>一年内到期的非流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>其他流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>流动资产合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>非流动资产：</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>可供出售金融资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>持有至到期投资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>长期应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>长期股权投资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>投资性房地产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>在建工程</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>工程物资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>固定资产清理</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>生产性生物资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>油气资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>无形资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>开发支出</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>商誉</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>长期待摊费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>递延所得税资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>其他非流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>非流动资产合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.6602</td><td style='text-align: center; word-wrap: break-word;'>资产总计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.2.5-02</div>

2）列表头直接匹配“统计维”维度，列表头匹配完成后，将得到结果如图2.2.5-03所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_468_222_763_294.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">图 2.2.5-03</div>


待完成设计向导一的匹配后，进行设计向导二，设计向导二的行/列维度和参数维等均与设计向导一相同，匹配方法也与设计向导一相同。

资产负债表设计完成后得到结果如图 2.2.5-04 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="6">资产负债表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>qmye</td><td style='text-align: center; word-wrap: break-word;'>ncye</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>qmye</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产</td><td style='text-align: center; word-wrap: break-word;'>期末余额</td><td style='text-align: center; word-wrap: break-word;'>年初余额</td><td style='text-align: center; word-wrap: break-word;'>负债和股东权益</td><td style='text-align: center; word-wrap: break-word;'>期末余额</td><td style='text-align: center; word-wrap: break-word;'>年初余额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>流动资产:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>流动负债:</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>货币资金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>短期借款</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>交易性金融资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>交易性金融负债</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应收票据</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应付票据</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应收账款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应付账款</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>预付款项</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>预收款项</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应收利息</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应付职工薪酬</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应收股利</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应交税费</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>其他应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应付利息</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>存货</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应付股利</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>一年内到期的非流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>其他应付款</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>其他流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>一年内到期的非流动负债</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>流动资产合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>其他流动负债</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>非流动资产:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>流动负债合计</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>可供出售金融资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>非流动负债:</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>持有至到期投资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>长期借款</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>长期应收款</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>应付债券</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>长期股权投资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>长期应付款</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>投资性房地产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>专项应付款</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>预计负债</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>在建工程</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>递延所得税负债</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>工程物资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>其他非流动负债</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>固定资产清理</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>非流动负债合计</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>生产性生物资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>负债合计</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>油气资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>股东权益:</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>无形资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>实收资本（或股本）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>开发支出</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>资本公积</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>商誉</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>减：库存股</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>长期待摊费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>盈余公积</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>递延所得税资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>未分配利润</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>其他非流动资产</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>股东权益合计</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>非流动资产合计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>资产总计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BA.0001.00001.</td><td style='text-align: center; word-wrap: break-word;'>负债和股东权益总计</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.2.5-04</div>


### 3. 提交套表并发布

### 2.3 预算调整

#### 2.3.1 预算调整流程

##### 2.3.1.1 直接调整流程

## 业务描述

● 预算生效后，由于某些原因需要修改预算数据，需直接在原预算表上修改预算数据。

● 预算直接调整后需要走审批的流程使数据生效。

● 预算调整可以结合 UAP 的审批流应用。

## 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_241_1035_1351.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 2.3.1.1-01</div>

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算审批</td></tr></table>

## 产品解决方案

1. 在【财务会计】-【费用预算】-【预算任务】-【任务管理】节点进启动直接调整，启动后任务状态变为“调整中”，如图 2.3.1.1-02 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_526_1079_1003.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.3.1.1-02</div>


2. 可以在 Excel 端的预算编制页签，下载调整任务，通过 Excel 录入数据后重新提交；也可以通过【财务会计】-【费用预算】-【预算调整】-【直接调整】节点选择待调整预算任务执行调整编制后提交。两种操作的方式均与预算编制相同。

3. Excel 端通过 “提交审批” 功能，【直接调整】通过 “上报” 将调整完的数据提交到审批人员处进行预算审批，如图 2.3.1.1-03 所示。

<div style="text-align: center;">预算桌面_2011年f01_预算数_人民币_默认版本_采购部_总成本_项目刚盘（无锚定运工）</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_108_154_1082_710.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.3.1.1-03</div>


1. 审批通过后调整完成，预算任务更新为“审批通过”状态，相关的变化情况可通过【财务会计】-【费用预算】-【预算编制】-【版本查询】节点查询各版本的调整变化情况，如图 2.3.1.1-04 所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>2011年01-预算数人民币,默认版本-采购部,总成本-项目期数(元模型选工厂)</td></tr></table>

<div style="text-align: center;">图 2.3.1.104</div>

##### 2.3.1.2 调整单调整流程

## 业务描述

调整单调整是指为满足对同一主体的多个计划（可以是不同应用模型生成的计划）同时调整，或对不同主体的多个计划（可以是不同应用模型生成的计划）进行调整。

## 业务流程

<div style="text-align: center;">单据调整任务流程&状态</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_111_505_1076_1480.jpg" alt="Image" width="81%" /></div>

<div style="text-align: center;">图 2.3.1.2-01</div>


## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算调整-局部调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算调整-调整单管理</td></tr></table>

## 产品解决方案

1. 在【财务会计】-【费用预算】-【预算任务】-【任务管理-全局/集团/组织】节点进启动单据调整，启动后任务状态变为“调整中”；

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_613_1081_1072.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.3.1.2-02</div>


2. 在【财务会计】-【费用预算】-【预算调整】-【局部调整】节点，点击【调整-局部调整/批量调整/多主体批量调整】，各步操作如图 2.3.1.2-03、图 2.3.1.2-4 所示，确定后完成调整，生成调整单。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>任务管理-全局</td><td style='text-align: center; word-wrap: break-word;'>局部调整</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

ALUE:3 STATUS3=0,STATUS2=20 DV=(原币=CNY人民币,部门=ALL ALL,主体=11.11-0105办公室,指标=BA.1001.nczy001.660203折旧费,业务方案=global.Budget预算数,计划期间=33月,版本=global.v0默认版本,统计错ALL ALL,项目期数=ALL ALL)

1zcfzb 2管理费用滚动预算 3部门收支项目浮动 4成本结转（快浮动）

<div style="text-align: center;">图 2.3.1.2-03</div>


## 扙畳諢甦

2012年ys01_all_预算数_人民


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>D</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>G</td><td style='text-align: center; word-wrap: break-word;'>H</td><td style='text-align: center; word-wrap: break-word;'>I</td><td style='text-align: center; word-wrap: break-word;'>J</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td colspan="7">任务函数</td><td colspan="3">年财务预算报表-管理费用</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>企业名称：</td><td colspan="9">任务函数</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td rowspan="2">费用要素</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>合计</td><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td style='text-align: center; word-wrap: break-word;'>5月</td><td style='text-align: center; word-wrap: break-word;'>6月</td><td style='text-align: center; word-wrap: break-word;'>7月</td><td style='text-align: center; word-wrap: break-word;'>8月</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>工资</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>福利费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>折旧费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>办公费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>差旅费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>8.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4.00</td><td style='text-align: center; word-wrap: break-word;'>4.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>业务招待费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>8.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4.00</td><td style='text-align: center; word-wrap: break-word;'>4.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>税金</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5.00</td><td style='text-align: center; word-wrap: break-word;'>5.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>其他管理费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>10.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>5.00</td><td style='text-align: center; word-wrap: break-word;'>5.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>水电费</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>12.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'>6.00</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.3.1.2-04</div>


3.【财务会计】-【费用预算】-【预算调整】-【调整单管理】节点中，可以点击【调整单查询】打开【调整单管理】节点，如图 2.3.1.2-05 所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>任务管理-全局</td><td style='text-align: center; word-wrap: break-word;'>局部调整</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.3.1.2-05</div>


4. 或者在【财务会计】-【费用预算】-【预算调整】-【调整单管理】节点直接查看调整单，对指定的调整单点击【提交】、【审批】使调整单生效，预算单据即告完成，审批通过后可在【局部调整】节点中联查“审批意见”，如图 2.3.1.2-06---图 2.3.1.2-08 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_104_725_1083_1011.jpg" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 2.3.1.2-06</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_167_1084_344.jpg" alt="Image" width="81%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>预算任务</td><td style='text-align: center; word-wrap: break-word;'>责任主体</td><td style='text-align: center; word-wrap: break-word;'>计划期间</td><td style='text-align: center; word-wrap: break-word;'>指标</td><td style='text-align: center; word-wrap: break-word;'>其他维度</td><td style='text-align: center; word-wrap: break-word;'>调整前数据</td><td style='text-align: center; word-wrap: break-word;'>调整数据</td><td style='text-align: center; word-wrap: break-word;'>调整后数据</td><td style='text-align: center; word-wrap: break-word;'>调整意见</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>ys01_all</td><td style='text-align: center; word-wrap: break-word;'>办公室</td><td style='text-align: center; word-wrap: break-word;'>3.3月</td><td style='text-align: center; word-wrap: break-word;'>BA1001.nczy001.660204 办公费</td><td style='text-align: center; word-wrap: break-word;'>ALL默认版本A..</td><td style='text-align: center; word-wrap: break-word;'>3.00</td><td style='text-align: center; word-wrap: break-word;'>1.50</td><td style='text-align: center; word-wrap: break-word;'>4.50</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>ys01_all</td><td style='text-align: center; word-wrap: break-word;'>办公室</td><td style='text-align: center; word-wrap: break-word;'>3.3月</td><td style='text-align: center; word-wrap: break-word;'>BA1001.nczy001.660205 差旅费</td><td style='text-align: center; word-wrap: break-word;'>ALL默认版本A..</td><td style='text-align: center; word-wrap: break-word;'>4.00</td><td style='text-align: center; word-wrap: break-word;'>1.50</td><td style='text-align: center; word-wrap: break-word;'>5.50</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>ys01_all</td><td style='text-align: center; word-wrap: break-word;'>办公室</td><td style='text-align: center; word-wrap: break-word;'>3.3月</td><td style='text-align: center; word-wrap: break-word;'>BA1001.nczy001.660206 业务招待费</td><td style='text-align: center; word-wrap: break-word;'>ALL默认版本A..</td><td style='text-align: center; word-wrap: break-word;'>4.00</td><td style='text-align: center; word-wrap: break-word;'>1.50</td><td style='text-align: center; word-wrap: break-word;'>5.50</td></tr></table>

<div style="text-align: center;">图 2.3.1.2-07</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_107_612_1081_969.jpg" alt="Image" width="81%" /></div>


1 zcfzh 2 管理费用滚动预算 3 部门收支项目浮动 4 成本结转（快浮动）

<div style="text-align: center;">图 2.3.1.2-08</div>


5. 调整单生效后，可在【财务会计】-【费用预算】-【预算编制】-【版本查询】节点查询单据调整情况，如图 2.3.1.2-09、2.3.1.2-10 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_151_1078_716.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.3.1.2-09</div>


## 2012 年ys01_all_数据数人民币_默认版本（办公室）


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>2管理费用滚动预算</td></tr></table>

<div style="text-align: center;">图 2.3.1.2-10</div>


6. 如果调整单要走审批流，可以在流程管理节点定义局部调整的审批流，并在预算任务中按调整阶段对已设好的审批流选用，详细操作请参见 3.6 节内容。

#### 2.3.2 预算调整业务

## 业务描述

预算调整主要是为了满足由于各种原因对已经正式生效的预算数据进行的调整，以及对调整数据的审批、查询分析。

各种预算调整的应用场景描述如下：

### 1. 年中定期预算调整：

由于预算编制时依据的假设发生变化，在年中要求根据最新掌握的情况对年初编制的预算进行调整。

1) 预算调整的发起人通常情况下和预算编制人相同；

2) 预算调整的审批流程和预算编制的审批流程相同；

3) 调整涉及的内容和编制的内容也基本相同。

### 2. 局部预算调整：

由于经营情况发生特殊变化，个别预算组织需要对部分预算项目进行调整，这种调整在预算执行期间可能会随时发生；这种调整的审批通常有别于预算编制的流程。

### 3. 总部集中预算调整：

由于集团整体经营环境发生重大变化，集团总部为了实现其年初确定的预算目标，会集中对相关预算组织的预算进行调整。如各公司的收入统一调增5%、费用调减3%等。

### 4. 预算组织内部不同预算指标的调剂：

将不同预算指标进行相互调剂，保证预算总额不变。如将管理费用中的交通费调增 20 万，而将招待费调减 20 万，保持总的费用额度不变。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 功能-预算编制</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算调整-局部调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算调整-预算调剂</td></tr></table>

## 产品解决方案

### 1. 年中定期预算调整：

在这种应用场景下，调整的数据范围大，需要对预算整表进行直接调整，一般通过产品 excel 客户端的【预算编制】节点实现。

【预算编制】节点支持计划数据的直接调整和直接调剂，调整的对象为整个计划，不走调整单审批。

### 2. 局部预算调整：

在这种应用场景下，一般通过产品的【财务会计】-【费用预算】-【预算调整】-【局部调整】节点实现。

【财务会计】-【费用预算】-【预算调整】-【局部调整】节点主要用于对计划数据进行局部的调整，调整过程系统自动生成计划调整单。

### 3. 总部集中预算调整：

在这种应用场景下，一般通过产品的【财务会计】-【费用预算】-【预算调整】-【局部调整】节点实现。

【财务会计】-【费用预算】-【预算调整】-【局部调整】节点主要用于对计划数据进行局部的调整，调整过程系统自动生成计划调整单。

例如：各公司的收入统一调增 5%、费用调减 3% 等，可以使用【调整-多主体批量调整】功能针对同个计划，根据批量调整规则同时调整多个预算组织的数据。

### 4. 预算组织内部不同预算指标的调剂：

在这种应用场景下，一般通过产品的【财务会计】-【费用预算】-【预算调整】-【预算调剂】节点实现。

【财务会计】-【费用预算】-【预算调整】-【预算调剂】指相同预算指标在不同主体之间的互相调剂，调剂不影响总的预算数，一张调剂单上的调整数总计=0；调剂过程系统自动生成计划调整单。

### 2.4 预算分析

#### 2.4.1 基于任务的预算分析

## 业务描述

1. 基于预算任务的分析方式，通过在集团统一定义分析套表、创建分析任务来进行预算分析

2. 适用于比较固定的预算分析模式

3. 通过分析任务完成数据获取和展现

4. 基于任务的分析通过 Excel 客户端来实现

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Excel</td><td style='text-align: center; word-wrap: break-word;'>表单设计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>模型设置-套表管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>预算任务-任务管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>费用预算</td><td style='text-align: center; word-wrap: break-word;'>Excel 客户端-预算分析</td></tr></table>

## 产品解决方案

1. 通过 Excel 端的表单设计功能，设计单独的分析套表：

1) 表单设计节点，设计分析用的套表，设计完后提交如图 2.4.1-01 所示套表。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_583_1000_1096.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 2.4.1-01</div>


2)【财务会计】-【费用预算】-【模型设置】-【套表管理-全局/集团/组织】节点发布套表

3)【财务会计】-【费用预算】-【预算任务】-【任务管理全局/集团/组织】节点，创建分析任务，并选择要分配的预算主体成员。如图2.4.1-02所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_176_999_768.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 2.4.1-02</div>


4)【财务会计】-【费用预算】-【预算任务】-【任务管理全局/集团/组织】节点启用任务

5) Excel 端的预算分析节点，下载分析任务获取分析数据，如图 2.4.1-03 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>开始</td><td style='text-align: center; word-wrap: break-word;'>插入</td><td style='text-align: center; word-wrap: break-word;'>页面布局</td><td style='text-align: center; word-wrap: break-word;'>公式</td><td style='text-align: center; word-wrap: break-word;'>数据</td><td style='text-align: center; word-wrap: break-word;'>审阅</td><td style='text-align: center; word-wrap: break-word;'>视图</td><td style='text-align: center; word-wrap: break-word;'>加载项</td><td style='text-align: center; word-wrap: break-word;'>Hyperion</td><td style='text-align: center; word-wrap: break-word;'>表单设计</td><td style='text-align: center; word-wrap: break-word;'>预算编制</td><td style='text-align: center; word-wrap: break-word;'>预算分析</td></tr><tr><td rowspan="4">刷新</td><td rowspan="4">下载任务</td><td style='text-align: center; word-wrap: break-word;'>设计</td><td style='text-align: center; word-wrap: break-word;'>表单设</td><td style='text-align: center; word-wrap: break-word;'>设置属性函数</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>任务信息面板</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>cdl</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>选项</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td rowspan="3">向导</td><td rowspan="3">计管理</td><td rowspan="3">☑</td><td rowspan="3">规则成员</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>维度信息面板</td><td style='text-align: center; word-wrap: break-word;'>✓</td><td style='text-align: center; word-wrap: break-word;'>当前集团</td><td style='text-align: center; word-wrap: break-word;'>大珠江系</td><td style='text-align: center; word-wrap: break-word;'>日志</td></tr><tr><td rowspan="2">单元格信息面板</td><td rowspan="2">✓</td><td rowspan="2">所选组织选择</td><td rowspan="2">✓</td><td style='text-align: center; word-wrap: break-word;'>i</td><td style='text-align: center; word-wrap: break-word;'>登录到</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>帮助</td><td style='text-align: center; word-wrap: break-word;'>NC系统</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>选择任务</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分析任务</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>预算任务</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>编制主体</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>预算任务</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>编制主体</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2012年10月分析任务_预算数_人民币_默认版本（大珠江集团）</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1 大珠江集团</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2012年10月分析任务_预算数_人民币_默认版本（控股集团）</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2 控股集团</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2012年10月分析任务_预算数_人民币_默认版本（投管集团）</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2 投管集团</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2012年10月分析任务_预算数_人民币_默认版本（股份集团）</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>2 股份集团</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.4.1-03</div>


#### 2.4.2 自定义查询分析

## 业务描述

1. 通过预算任务进行分析，相对格式比较固定，用户不能做灵活调整；

2. 通过预算分析节点的分析功能，可以让用户自由选择要分析的指标进行数据分析，灵活性较高

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Excel 客户端</td><td style='text-align: center; word-wrap: break-word;'>预算分析</td></tr></table>

## 产品解决方案

### 1. 预算分析节点设置分析表单

1) 选择“预算分析节点”的设计向导，创建分析用的表单（设计过程同表单设计，少了参数维指定）。所设计的表单如图 2.4.2-01 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>开始</td><td style='text-align: center; word-wrap: break-word;'>插入</td><td style='text-align: center; word-wrap: break-word;'>页面布局</td><td style='text-align: center; word-wrap: break-word;'>公式</td><td style='text-align: center; word-wrap: break-word;'>数据</td><td style='text-align: center; word-wrap: break-word;'>审阅</td><td style='text-align: center; word-wrap: break-word;'>视图</td><td style='text-align: center; word-wrap: break-word;'>加载项</td><td style='text-align: center; word-wrap: break-word;'>Hyperion</td><td style='text-align: center; word-wrap: break-word;'>表单设计</td><td style='text-align: center; word-wrap: break-word;'>预算编制</td><td style='text-align: center; word-wrap: break-word;'>预算分析</td></tr></table>

<div style="text-align: center;">图 2.4.2-01</div>


2. 指定分析参数维（分析表单中没有在行列维度上的维度都作为参数维），参数维指定后将显示分

析数据，可以随时修改分析参数维

1) 新创建的分析表单，选择参数维页签，指定其它一些参数维如预算主体、预算年度等，参数维指定完后即可显示分析数据，如图 2.4.2-02 所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>月</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1月</td><td style='text-align: center; word-wrap: break-word;'>2月</td><td style='text-align: center; word-wrap: break-word;'>3月</td><td style='text-align: center; word-wrap: break-word;'>4月</td><td style='text-align: center; word-wrap: break-word;'>5月</td><td style='text-align: center; word-wrap: break-word;'>6月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指标</td><td style='text-align: center; word-wrap: break-word;'>统计维</td><td style='text-align: center; word-wrap: break-word;'>付款级别</td><td style='text-align: center; word-wrap: break-word;'>项目名称</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>生产成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>制造费用</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>劳务成本</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>研发支出</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>工程施工</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>工程结算</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>机械作业</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RF.0001.5</td><td style='text-align: center; word-wrap: break-word;'>0001.02</td><td style='text-align: center; word-wrap: break-word;'>0001.01</td><td style='text-align: center; word-wrap: break-word;'>0001.100</td><td style='text-align: center; word-wrap: break-word;'>主营业务收入</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参数维...</td><td style='text-align: center; word-wrap: break-word;'>维度信...</td><td style='text-align: center; word-wrap: break-word;'>☑</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>维度</td><td style='text-align: center; word-wrap: break-word;'>维度成员</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>版本</td><td style='text-align: center; word-wrap: break-word;'>默认版本</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>业务方案</td><td style='text-align: center; word-wrap: break-word;'>预算数</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>主体</td><td style='text-align: center; word-wrap: break-word;'>珠投本部</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>年</td><td style='text-align: center; word-wrap: break-word;'>2012年</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>季</td><td style='text-align: center; word-wrap: break-word;'>1季</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.4.2-02</div>


## 第三章 初始准备

费用预算产品的初始准备包括动态组织管理、管控模式设定、控制策略、预算档案、预算模型设置、相关审批流等的配置，如图 3-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_131_1130_865.jpg" alt="Image" width="85%" /></div>


<div style="text-align: center;">图 3-01</div>


### 3.1 构建预算体系

#### 3.1.1 单一集团预算组织体系构建

## 业务描述

1\. 集团公司制定统一的预算体系、预算样表，下发给所有分子公司执行；

2. 集团公司对各分子公司最后定案的预算进行审批。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-成本中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-预算组织体系-全局/集团</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构视图-组织结构图</td></tr></table>

## 产品解决方案

### 1. 根据预算业务需要，建立业务单元、部门和成本中心

我们建议，把预算主体中的用来储存汇总数据的汇总主体，建成业务单元，方便后续使用；举例说明：

北京控股集团（行政结构）如图 3.1.1-01 所示：

bkcorp 北京控股集团有限责任公司

bk01 北京市燃气集团有限责任公司

bk0101 北京燃气第一分公司

bk0102 北京燃气第二分公司

bk02 北京燕京啤酒股份有限公司

bk03 北京首都高速公路发展有限公司

<div style="text-align: center;">图 3.1.1-01</div>


北京控股集团（根据预算业务建立业务单元）如图 3.1.1-02 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_1177_992_1407.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 3.1.1-02</div>


此例中，我们把行政结构中的公司 “北京控股集团有限责任公司”，根据预算业务需要建立了两个业务单元：一个是用来储存预算汇总数据的业务单元 “北京控股集团有限责任公司（汇总）”，一个是实体公司

“北京控股集团有限责任公司（榔）”。

### 2. 建立预算组织

预算组织用于描述企业集团的预算管理组织及执行组织，可以对应多种实体类型的组织，在 NC 产品中可以对应业务单元、部门或成本中心。

1) 在【企业建模平台】-【组织管理】-【组织结构定义】-【业务单元】节点建立业务单元，并勾选“预算”的属性；

2) 在【企业建模平台】-【组织管理】-【组织结构定义】-【部门】节点建立部门，并勾选“预算”的属性；

3) 在【企业建模平台】-【组织管理】-【组织结构定义】-【成本中心】节点成本中，并勾选“预算”的属性。

预算组织是费用预算的主组织，围绕费用预算展开的一系列业务活动均是基于预算组织的：

1) 预算套表通过指定到预算组织体系而对应到相应类型的预算组织上；

2) 预算组织将作为后续预算编制和描述的基础组织，基于预算组织进行预算（计划）的编制；

3) 基于预算组织建立业务控制规则，执行预算控制；

4) 基于预算组织体系进行预算的查询分析。

### 3. 建立预算组织体系

全集团建立一套预算组织体系，在【企业建模平台】-【组织管理】-【组织结构定义】-【预算组织体系-全局】节点建立一套预算组织体系。

预算组织间没有上下级关系，通过预算组织体系建立多棵预算组织树，体现预算组织间的上下级关系。预算系统根据这棵预算组织树，进行数据的自动汇总。

### 4. 预算组织体系查询

在 UAP 平台组织管理完成后，标识了预算组织属性的组织单元将构成企业组织整体结构树当中的一个分支。

在【企业建模平台】-【组织管理】-【组织结构视图】-【组织结构图-全局/集团】节点中，可以查询各种业务组织结构图，包括预算组织结构图，同时，通过【生成快照】功能，可以对预算组织结构的变动进行记录。

#### 3.1.2 多集团预算组织体系构建

## 业务描述

1. 集团母公司制定一套统一的预算体系，下发给所有子公司（内容主要为综合指标）；

2. 集团对各子公司最后定案的预算进行审批；

3. 各子集团根据行业特性分别制定适用于各行业的一套或几套预算体系，在子集团范围内执行；

4. 各子集团需要同时编制本集团和集团总部制定的预算体系。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-成本中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-预算组织体系</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构视图-组织结构图</td></tr></table>

## 产品解决方案

### 1. 建立预算组织

同 3.1.1 单一集团预算组织体系构建 章节。

### 2. 建立预算组织体系

集团总部在【企业建模平台】-【组织管理】-【组织结构定义】-【预算组织体系-全局】节点建立跨集团的预算组织体系；各子集团在【企业建模平台】-【组织管理】-【组织结构定义】-【预算组织体系-集团】节点建立各自的预算组织体系。

举例说明：

北京控股集团（行政结构）如图 3.1.2-01 所示：

bkcorp 北京控股集团有限责任公司

bk01 北京市燃气集团有限责任公司

bk0101 北京燃气第一分公司

bk0102 北京燃气第二分公司

bk02 北京燕京啤酒股份有限公司

bk03 北京首都高速公路发展有限公司

<div style="text-align: center;">图 3.1.2-01</div>


北燃集团（行政结构）如图 3.1.2-02 所示：

brcop 北京北燃实业有限公司  

001 企业管理部（部门）  

002 财务部（部门）  

003 行政部（部门）  

br001 北京液化石油气公司  

br002 北京市煤气工程公司  

br003 北京炼焦化学厂  

001 成本中心一（成本中心）  

002 成本中心二（成本中心）  

003 成本中心三（成本中心）

<div style="text-align: center;">图 3.1.2-02</div>


京泰集团（行政结构）如图 3.1.2-03 所示：

jtcop 京泰实业集团有限公司

jt01 北京华远地产有限公司

jt02 北京三元食品有限公司

图 3.1.2-03

构建成预算体系后如图 3.1.2-04 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_142_169_1019_902.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 3.1.2-04</div>


### 3. 预算组织体系查询

<div style="text-align: center;">同 3.1.1 单一集团预算组织体系构建 章节。</div>


#### 3.1.3 多个预算组织体系

## 业务描述

在企业集团中，根据内部管理的不同要求，会产生适应多种管理的组织结构，因此，预算的数据也需要按照不同的组织结构进行汇总、合并及分析。例如，按照行政关系和业务关系建立多个预算组织体系。

在预算组织管理时，产品支持构建多个预算组织体系（即预算组织树），满足上述预算管理要求。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-成本中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-预算组织体系</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构视图-组织结构图</td></tr></table>

## 产品解决方案

### 1. 建立预算组织

同 3.1.1 单一集团预算组织体系构建 章节。

### 2. 建立预算组织体系

在【企业建模平台】-【组织管理】-【组织结构定义】-【预算组织体系-全局】节点建立两个预算组织体系。

### 3. 预算组织体系查询

同 3.1.1 单一集团预算组织体系构建 章节

#### 3.1.4 分级管理预算体系

## 业务描述

分级管理预算体系分为集权管理和分级管理两种：

1. 集权管理：集团统一制定预算指标、预算维度、预算套表、业务规则，统一开展预算管理；

2. 分级管理：预算指标、预算维度、预算套表、业务规则等的分级制定，分别授权并进行数据隔离；子集团的预算体系中的有些数据和勾稽到集团总部的预算表中。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>权限管理</td><td style='text-align: center; word-wrap: break-word;'>职责管理-职责</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>权限管理</td><td style='text-align: center; word-wrap: break-word;'>角色管理-管理类角色</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>权限管理</td><td style='text-align: center; word-wrap: break-word;'>角色管理-业务类角色</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>权限管理</td><td style='text-align: center; word-wrap: break-word;'>授权管理-数据权限</td></tr></table>

## 产品解决方案

### 1. 预算产品功能权限的分配

使用集团管理员账号进入系统，在【企业建模平台】-【权限管理】-【职责管理】-【职责】节点分配产品的功能节点权限，例如：指标管理、维度管理、应用模型、编制表单等。

### 2. 预算组织权限的分配

使用集团管理员账号进入系统，在【企业建模平台】-【权限管理】-【角色管理】-【管理类角色】、【企业建模平台】-【权限管理】-【角色管理】-【业务类角色】节点分配预算组织的权限。如图 3.1.4-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_645_1043_1136.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 3.1.4-01</div>


### 3. 预算产品数据权限的分配

使用集团管理员账号进入系统，在【企业建模平台】-【权限管理】-【授权管理】-【数据权限】节点分配相关的数据权限。如图 3.1.4-02 所示

权限管理的具体介绍可参见《NCV6.3 产品手册-权限管理》。

<div style="text-align: center;"><img src="imgs/img_in_image_box_301_161_888_291.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_299_305_916_796.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">图 3.1.4-02</div>


#### 3.1.5 多套预算体系

## 业务描述

多套预算体系是指集团总部统一制定两套以上的预算体系（如国资委预算体系和企业内部预算体系），两套预算体系之间有数据勾稽关系。

## 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-业务单元</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-成本中心</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构定义-预算组织体系</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>企业建模平台</td><td style='text-align: center; word-wrap: break-word;'>组织管理</td><td style='text-align: center; word-wrap: break-word;'>组织结构视图-组织结构图</td></tr></table>

## 产品解决方案

### 1. 建立预算组织

同 3.1.1 单一集团预算组织体系构建 章节。

### 2. 建立预算组织体系

根据具体情况可建立一个或者多个预算组织体系。

### 3. 预算组织体系查询

同 3.1.1 单一集团预算组织体系构建 章节。

### 4. 预算编制内容体系搭建

下文所讲述的都是预算编制内容体系的搭建方法，请参见 3.4、3.5、3.7、3.8 相关章节。

### 3.2 管控模式

费用预算平台基础数据的管控模式包括两个部分：

1. 支持 UAP 统一的管控模式。

2. 需要支持特殊的管控模式。由于 UAP 统一的管控模式只能针对维度定义来设置，不能支持对维度成员设置，而多级集团应用时，需要对维度成员设置不同的管控模式；在预算系统上级组织需要对下级组织设置相应的基础数据管控方式（可见性范围）。

计划平台的基础数据仅在计划预算产品内使用，基础数据内容包括：指标、维度、时间维、应用模型、套表管理、业务规则、控制规则、控制策略。其中套表管理用于设计表单，主要在 Excel 端来设计。这些基础数据分别作为独立的功能节点，支持不同的管控模式。如图 3.2-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_162_1076_731.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3.2-01</div>


管控模式用于初始化时进行档案规则的配置，即针对每个档案根据最常规的应用方案，设置它的默认规则。用户可以在每个档案可支持的规则范围内进行调整。

一个档案只能在可选择的管控模式范围内选择某个在用的管控模式。按照 “管控模式” 的不同，档案将分为全局级、集团级、组织级的多个节点，再通过集团管理员完成功能授权后交由指定操作员使用。

1. 管理模式：定义节点可维护数据的最大范围。后续应用中系统将根据管理模式的不同，将档案分为全局级、集团级、组织级等多个节点。维护性范围控制如下表所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'>模式</td><td style='text-align: center; word-wrap: break-word;'>维护性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>全局</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可维护全局内的全部数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>全局+集团</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可维护从属于全局的数据；\n集团节点：可维护从属于本集团；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>全局+集团+组织</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可维护从属于全局的数据；\n集团节点：可维护从属于本集团的数据；\n组织节点：可维护从属于本组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>全局+组织</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可维护从属于全局的数据；\n组织节点：可维护从属于本组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>集团节点：可维护从属于本集团的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>集团+组织</td><td style='text-align: center; word-wrap: break-word;'>集团节点：可维护从属于本集团的数据；</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>组织节点：维护从属于本组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>组织</td><td style='text-align: center; word-wrap: break-word;'>组织节点：可维护从属于本组织的数据。</td></tr></table>

上表中，每个模式确定了后续可用的产品节点及各节点的维护范围。

例如：当管理模式为 “全局+集团+组织”，则对应档案会有全局、集团、业务单元三个功能节点，全局节点能维护从属于全局的数据，集团节点能维护从属于本集团的数据，业务单元节点可以维护从属于该业务单元的数据。

2. 可见性范围：决定用户可以查看、使用基础数据的最大范围。每个节点显示的内容受“可见性范围”的约束。可见性范围如下表所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'>模式</td><td style='text-align: center; word-wrap: break-word;'>默认查询范围</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>全局</td><td style='text-align: center; word-wrap: break-word;'>可见全局内的全部数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>全局+集团</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可见从属于全局的数据；\n集团节点：可见从属于全局+本集团+本集团所有组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>全局+集团+组织</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可见从属于全局的数据；\n集团节点：可见从属于全局+本集团的数据；\n组织节点：可见从属于全局+本集团+本组织增加的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>全局+组织</td><td style='text-align: center; word-wrap: break-word;'>全局节点：可见从属于全局的数据；\n组织节点：可见从属于全局+本组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>可见从属于本集团+本集团所有组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>集团+组织</td><td style='text-align: center; word-wrap: break-word;'>集团节点：可见从属于本集团的数据；\n组织节点：可见从属于本集团+本组织的数据；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>组织</td><td style='text-align: center; word-wrap: break-word;'>组织节点：可见从属于本组织的数据。</td></tr></table>

例如：当可见性范围为“全局+集团”时，表示全局节点可以看到从属于全局的数据，集团级节点可以看到从属于全局+本集团+本集团所有组织的数据；当可见性范围为“全局+集团+组织”时，表示全局节点可以看到从属于全局的数据，集团级节点可以看到从属于全局+本集团的数据，组织级节点可看到从属于全局+本集团+本组织的数据。

3. 唯一性范围：决定基础数据唯一性的范围。唯一性范围的控制如下表所示。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编码</td><td style='text-align: center; word-wrap: break-word;'>模式</td><td style='text-align: center; word-wrap: break-word;'>保存校验</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>全局</td><td style='text-align: center; word-wrap: break-word;'>数据在数据库范围内唯一；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>全局+集团</td><td style='text-align: center; word-wrap: break-word;'>从属于全局的数据不能与全局+所有集团的数据重复；从属于集团的数据不能与全局+本集团重复；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>全局+集团+组织</td><td style='text-align: center; word-wrap: break-word;'>从属于全局的数据不能与全局+所有集团+所有组织的数据重</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>复；从属于集团的数据不能与全局+本集团+本集团下所有组织；从属于组织的数据不能与全局+本集团+本组织重复；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>全局+组织</td><td style='text-align: center; word-wrap: break-word;'>从属于全局的的数据不能与全局+所有组织的数据重复；从属于组织的数据不能与全局+本组织重复；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>集团</td><td style='text-align: center; word-wrap: break-word;'>数据在本集团+所有组织范围内唯一；从属于集团的数据不能与本集团+所有组织重复；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>集团+组织</td><td style='text-align: center; word-wrap: break-word;'>从属于组织的数据不能与本集团+本组织重复；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>组织</td><td style='text-align: center; word-wrap: break-word;'>数据在本组织范围内唯一。</td></tr></table>

上表中示例：当唯一性范围为“全局+集团+组织”时，表示全局节点增加的数据不能与“全局+所有集团+所有组织”的数据重复，集团级节点增加的数据不能与“全局+本集团+本集团下的所有组织”的数据重复，组织级节点增加的数据不能与“全局+本集团+本组织”下的数据重复。

当管理模式、可见性范围、唯一性范围都设置为“全局+集团+组织”时，表示该档案有全局、集团、组织三个功能节点，其中全局节点可以查看、维护全局增加的数据，且全局节点增加的数据不能与“全局+所有集团+所有组织”的数据重复；集团节点可以查看“全局+本集团”的数据，可以维护“本集团”增加的数据，且增加的数据不能与“全局+本集团+本集团”的数据重复；组织级节点可以查看从属于“全局+本集团+本组织”的数据，且组织级节点增加的数据不能与“全局+本集团+本组织”下的数据重复。

### 3.3 控制策略

【动态建模平台】-【计划平台】-【系统设置】-【控制策略】节点是计划平台为各个产品模块提供的一个入口，各个使用预算平台做计划的模块，均可以在此注册。注册模块的单据，影响计划数的时点，对应单据的某个动作，可以是保存、审批，或者其他。

但是并非每个模块单据都使用了这个功能，例如采购计划就没有使用该节点，目前采购单据对采购计划的影响时点是固定在控制单据审批时，形成对采购计划的预占数和执行数。如图 3.3-01 所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_164_1078_605.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3.3-01</div>


### 3.4 预算档案

预算维度需要对应到档案，但预算特有的一些维度在 UAP 找不到对应的档案，为此 NC 系统在建模平台-计划平台中提供预算档案节点，用于预置预算特有维度所需的 UAP 档案。预算预置的档案包括预算科目、预算版本、业务方案和自定义计划期间。用户可在预置档案的基础上进行增补，增补后一旦被引用，则只能停用而不能删除。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_987_1080_1418.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.4-01</div>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>业务方案-全局</td></tr></table>

<div style="text-align: center;">图 3.4-02</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>业务方案-全局</td><td style='text-align: center; word-wrap: break-word;'>✗</td><td style='text-align: center; word-wrap: break-word;'>预算版本-全局</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>新增</td><td style='text-align: center; word-wrap: break-word;'>修改</td><td style='text-align: center; word-wrap: break-word;'>删除</td><td style='text-align: center; word-wrap: break-word;'>查询</td><td style='text-align: center; word-wrap: break-word;'>刷新</td><td style='text-align: center; word-wrap: break-word;'>过滤</td><td style='text-align: center; word-wrap: break-word;'>启用</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">☐</td><td rowspan="3">预算版本
• v0 默认版本
• v1 编制生效版本
• v2 单策调整（生效）版本
• v3（直接）调整生效版本1
• v4（直接）调整生效版本2
• v5（直接）调整生效版本3</td><td style='text-align: center; word-wrap: break-word;'>创建组织</td><td style='text-align: center; word-wrap: break-word;'>全局</td><td style='text-align: center; word-wrap: break-word;'>预算版本编码</td><td style='text-align: center; word-wrap: break-word;'>v2</td><td style='text-align: center; word-wrap: break-word;'>预算版本名称</td><td style='text-align: center; word-wrap: break-word;'>单据调整（生效）版本</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>版本阶段</td><td style='text-align: center; word-wrap: break-word;'>调整版本</td><td style='text-align: center; word-wrap: break-word;'>版本类型</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>启用状态</td><td style='text-align: center; word-wrap: break-word;'>已启用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'>预置</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>☑</td><td style='text-align: center; word-wrap: break-word;'>审计信息</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 3.4-03</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>业务方案-全局</td><td colspan="2">自定义计划期间</td></tr></table>

<div style="text-align: center;">图 3.4-04</div>

### 3.5 预算模型

预算模型设置是预算管理的重点，包括维度管理、指标属性定义、预算应用模型设定、业务规则和控制规则的预置，以及预算所需用到的表单等。

#### 3.5.1 维度管理

维度是对指标进行多重解释的具体分类，一个指标可以按照多个维度进行解释。维度设定后供预算模型建立时调用。

维度不仅从分类上管理着预算指标，同时，维度的层级结构确定了维度成员间的结构和汇总关系，一个预算样表实际包含着的就是预算表的格式信息和匹配的维度信息，因此，维度在预算建模中起着举足轻重的作用。

## 路径：

【动态建模平台】—【计划平台】—【模型设置】—【维度管理】

## 操作：

点击【新增】进入编辑状态，输入编码、名称，在子表中选择“关联档案表”页签，点击【增行】钮，在【类型】栏中选择“基础档案”或“自定义档案”，再在其后的栏目中根据所选类型选择对应的档案表，完毕后点击【保存】，即形成新增维度，如图3.5.1-01所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_992_1109_1338.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 3.5.1-01</div>


其中自定义档案应先在【动态建模平台】-【基础数据】-【自定义档案定义】节点新增档案，详细操作见《NCV6.3 产品手册-基础数据》文档基础档案中自定义项的相关说明。
