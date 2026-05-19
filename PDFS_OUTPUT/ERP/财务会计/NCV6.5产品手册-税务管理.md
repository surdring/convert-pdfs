# NCV6.5产品手册-税务管理

产品手册- V6.5

税务管理

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权 1  
  
名词解释 ..... 4  
第一章 概述 ..... 6  
1.1 产品概述 ..... 6  
1.2 产品价值 ..... 7  
第二章 应用场景 ..... 8  
2.1 独立核算，独立调整 ..... 8  
2.1.1 手工差异调整 ..... 8  
2.1.2 自动差异调整 ..... 11  
2.1.3 多税种统一调整 ..... 16  
2.1.4 自动生成固定资产折旧差异凭证 ..... 18  
2.1.5 递延所得税核算 ..... 19  
2.1.6 独立计提 ..... 25  
2.2 独立核算，委托调整 ..... 29  
2.2.1 手工差异调整 ..... 29  
2.2.2 自动差异调整 ..... 29  
2.2.3 多税种统一调整 ..... 30  
2.2.4 自动生成固定资产折旧差异凭证 ..... 30  
2.2.5 递延所得税核算 ..... 30  
2.2.6 统一计算、自动分配、统一计提 ..... 30  
第三章 初始准备 ..... 35  
3.1 企业建模平台 ..... 35  
3.1.1 基础数据维护 ..... 35  
3.2 财务会计 ..... 36  
3.2.1 税务管理—基础设置 ..... 36  
第四章 操作指南 ..... 36  
附录 37  
附录 4：本文参见其他手册清单 ..... 37

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供业务需求与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关本模块的主要业务场景、流程、以及对应的业务功能的介绍；第三部分是初始准备设置；第四部分是关于本模块功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录中对一些可能需要对照查询的关键点进行了补充说明，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《产品手册-组织管理》-----深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助----针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《产品手册-流程管理》----提供关于交易类型、流程设计工具的应用指导。

4. 《产品手册-基础数据》----可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

## 名词解释

## 税务会计

以纳税人为会计主体，以货币为主要计量单位，依据税收法规，运用会计基本理论和方法，对税务资金运动进行连续、系统、全面的核算与筹划。其会计主体是负有纳税义务的独立纳税人，包括法人和非法人。

## 税种

指一国税收体系中的具体税收种类，是基本的课税单元。根据征税对象的不同可将税收划分成不同的种别，税种的名称一般也以征税对象来命名。如对增值税课税的税种叫增值税；对资源课税的税种叫资源税。

## 税率

税额与课税对象之间的数量关系或比例关系，是指课税的尺度，主要表现为税额占课税对象的比例。一般分为定额税率、比例税率、累进税率。

## 企业所得税

对我国境内的企业和其他取得收入的组织的生产经营所得和其他所得所征收的一种税收，它是国家参与企业利润分配的重要手段。

## 递延所得税

指按照所得税准则规定，应予确认的递延所得税资产和递延所得税负债，在期末应有的金额相对于原已确认金额之间的差额，即递延所得税资产及递延所得税负债当期发生额的综合结果。

## 应纳税暂时性差异

指在确定未来收回资产或清偿负债期间的应纳税所得额时，将导致产生应税金额的暂时性差异。该差异在未来期间转回时，会增加转回期间的应纳税所得额，在应纳税暂时性差异产生当期，应当确认相关的递延所得税负债。

## 可抵扣暂时性差异

指在确定未来收回资产或清偿负债期间的应纳税所得额时，将导致产生可抵扣金额的暂时性差异。该差异在未来期间转回时，会减少转回期间的应纳税所得额，减少未来期间的应缴所得税。在可抵扣暂时性差异产生当期，应当确认相关的递延所得税资产。

## 永久性差异

指某一会计期间，由于会计制度和税法在计算收益、费用或损失时的口径不同，所产生的税前会计利润与应纳税所得额之间的差异。这种差异在本期发生，不会在以后各期转回。

## 应纳税所得额

企业所得税的计税依据，按照税法规定，应纳税所得额为企业每一个纳税年度的收入总额、减除不征税收入、免税收入、各项扣除以及允许弥补的以前年度亏损后的余额。

## 应纳税额

根据应纳税所得额和税率计算，是企业应该缴纳的实际税款金额。

## 汇算清缴

指所得税的纳税人以会计数据为基础，将财务会计处理与税收法律法规规定不一致的地方按照税收法律法规的规定进行纳税调整，将会计所得调整为应纳税所得，套用适用税率计算得出年度应纳税额，与年度内已预缴税额相比较后的差额，确定应补或应退税款，并在在税法规定的申报期内向税务机关提交会计决算报表和企业所得税年度纳税申报表以及税务机关要求报送的其他资料，经税务机关审核后，办理结清税款手续。企业所得税汇算清缴工作应以企业会计核算为基础，以税收法规为依据。

## 第一章 概述

### 1.1 产品概述

税务管理是为税务会计服务的，是进行税务筹划、税金核算和纳税申报的一种会计系统。它是财务会计与管理会计的自然延伸，是对以投资人为导向的财务会计按税法法律制度进行核算调整，形成税务账簿以及纳税申报表，并按税法规定缴纳税款的一种管理活动。

税务管理是按不同的税种，基于总账中的财务数据进行调整，从而形成税务数据。为了防止数据的重复，只将调整的部分计入税务账簿，而纳税申报表的数据是结合财务账簿和税务账簿共同作用形成的，并且通过税务管理计算形成的应交税款返回给总账作为财务数据进行记录，所以税务管理产品是依赖于总账产品的。税务管理是税务调整相关工作处理的平台，它由以下模块组成：税务核算、递延所得税、期末处理、税务报表、纳税申报、汇算清缴。

<div style="text-align: center;"><img src="imgs/img_in_image_box_106_777_978_1341.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 1.1-1 产品功能架构图</div>


NC 供应链提供集团采购供应、集团销售分销两大业务领域的解决方案，通过集团销售分销业务、政策

管理、业务流程规范、商务协同应用，帮助构建集团企业销售与分销业务经营管理平台，提升经营绩效、优化资源配置、满足客户需求、降低运营成本；集团销售分销解决方案包括销售管理、销售价格、销售信用、内部交易和运输管理五大模块。

### 1.2 产品价值

### 1. 支持对不同税种的日常税务核算

支持设置不同税种不同的差异调整项目，用于区别记录差异调整凭证；

➢ 支持按税收政策对总账凭证进行调整，形成差异调整凭证。

### 2. 支持自动生成差异凭证

支持使用直接调整规则，自动生成差异凭证；

支持使用按扣除标准调整规则，自动生成差异凭证；

支持使用广告费调整规则，自动生成差异凭证；

➢ 支持记录广告费调整明细，形成广告费辅助账；

支持通过固定资产系统，自动生成与固定资产相关的差异凭证。

### 3. 支持自动计算递延所得税

➢ 支持记录暂时性差异数据，作为递延所得税计算的数据基础；

支持自动计算递延所得税，并作为入账依据生成总账记账凭证。

### 4. 支持企业所得税多种纳税申报方式

➢ 支持总部统一缴纳企业所得税的情况，通过税款计提规则直接生成计提的税款；

支持总部统一调整核算、分子公司分别预缴的情况，通过设定税款分配规则，按计提规则生成各公司的税款；

支持将计提完成的结果作为入账依据，生成总账记账凭证。

### 5. 支持企业所得税汇算清缴工作

➢ 支持设置税款计提规则，并按规则生成汇算清缴的结果；

支持将汇算清缴的结果作为入账依据，生成总账记账凭证。

### 6. 支持生成税务报表

➢ 支持通过税务函数获取税务相关数据；

➢ 支持使用预置税务报表模板生成税务报表；

➢ 支持生成不同税种的税务报表。

## 第二章 应用场景

### 2.1 独立核算，独立调整

支持独立总账核算的法人公司，基于总账进行独立的各税种的财税差异调整；支持独立总账核算的下属分公司对企业所得税外的其他税种进行独立财税差异调整。

#### 2.1.1 手工差异调整

##### 2.1.1.1 业务描述

按照税收政策要求，针对总账数据进行财税差异调整；

不同税种的调整要求和方式不同，对一套总账数据要分税种分别进行调整；

差异调整的结果直接形成差异调整凭证，差异调整凭证可以有单边凭证的发生；

非年初启用的税务账簿需要维护年初数据，以保证数据的完整性；

➢ 要求实时查询差异凭证；

➢ 对差异凭证要求审核进行确认。

##### 2.1.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_274_240_914_756.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 2.1.1-1</div>


##### 2.1.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">财务会计</td><td rowspan="3">税务管理</td><td style='text-align: center; word-wrap: break-word;'>期初录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异凭证录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异凭证查询</td></tr></table>

##### 2.1.1.4 产品解决方案

### 1. 维护税务调整的期初数

当税务核算账簿在非年初期间启用时，在【期初录入】中录入账簿启用日期之前，税务账簿当期的差异调整分录；

依据税收政策分不同的税种调整财税差异，通过差异调整项来确定税种；

通过辅助信息查看差异调整项对应的税种以及差异属性信息；

对于委托核算的情况，使用调整财务核算账簿区分核算；

➢ 支持对【期初录入】数据的打印。

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_242_1030_565.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.1-2</div>


### 2. 手工录入差异凭证

依据税收政策分不同的税种调整财税差异，在【差异凭证录入】中形成差异凭证；

通过辅助信息查看差异调整项对应的税种以及差异属性信息；

当对企业所得税进行调整时，需要确认差异属性属于暂时性差异还是永久性差异，暂时性差异的调整分录用于计算递延所得税；

对于委托核算的情况，使用调整财务核算账簿区分核算；

通过〖审核〗对录入完毕的差异凭证确认差异调整；

在【差异凭证查询】中，支持对差异凭证的即时查询。

<div style="text-align: center;"><img src="imgs/img_in_image_box_155_1025_1034_1216.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.1-3</div>

## 注意：

➢【期初录入】只能录入税务核算账簿启用日期之前的调整记录；

➢【差异凭证录入】只能录入税务核算账簿启用日期之后的调整记录；

在【差异凭证录入】中，若差异调整项为暂时性差异，要求差异凭证必须借贷平衡；

当税务核算账簿关账后，不允许再进行【期初录入】和【差异凭证录入】。

#### 2.1.2 自动差异调整

##### 2.1.2.1 业务描述

在税收政策中，如工资薪金、业务招待费或广告费等，是有具体扣除标准或调整规则的；

在税务管理系统中，可以利用这些规则对总账凭证进行统一调整，一次生成差异凭证；

通过在系统中设置相应的调整规则，人为触发执行规则来实现财税差异的自动调整。

##### 2.1.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_933_1041_1442.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2-1</div>

##### 2.1.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="5">财务会计</td><td rowspan="5">税务管理</td><td style='text-align: center; word-wrap: break-word;'>差异凭证录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异凭证查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异调整规则设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异调整规则执行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>广告费辅助账</td></tr></table>

##### 2.1.2.4 产品解决方案

### 1. 直接调整

当需要调整的财务数据很多，并且这些数据有相同的调整科目时，适用直接调整规则；

在【差异调整规则设置】中设置直接调整属性的调整规则；

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_735_1039_1034.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.1.2-2</div>


在【差异调整规则执行】中对调整的税务核算账簿【执行】直接调整规则，调整某个期间的财务数据；

<div style="text-align: center;"><img src="imgs/img_in_image_box_365_145_825_515.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">图 2.1.2-3</div>


自动生成直接调整的差异凭证到【差异凭证录入】中，可根据需要对差异凭证维护和审核；

在【差异调整规则执行】中生成调整执行日志，并可通过日志联查差异凭证；

➢ 可在【差异凭证查询】中查询使用规则生成的差异凭证。

<div style="text-align: center;"><img src="imgs/img_in_image_box_157_726_1033_901.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.2-4</div>


### 2. 按扣除标准调整

➢ 本规则专门为调整企业所得税提供；

当需要调整的财务数据有两个扣除标准，按实际数据取其中最小时，适用按扣除标准调整规则；

如：企业发生的与生产经营活动有关的业务招待费支出，按照发生额的 60% 扣除，但最高不得超过当年销售（营业）收入的千分之五。

在【差异调整规则设置】中设置按扣除标准属性的调整规则以及扣除标准；

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_160_1032_598.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.2-5</div>


在【差异调整规则执行】中对调整的税务核算账簿【执行】按扣除标准规则，调整某个期间的财务数据；

<div style="text-align: center;"><img src="imgs/img_in_image_box_366_746_827_1117.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">图 2.1.2-6</div>


自动生成按扣除标准调整的差异凭证到【差异凭证录入】中，可根据需要对差异凭证维护和审核；

在【差异调整规则执行】中生成调整执行日志，并可通过日志联查差异凭证；

➢ 可在【差异凭证查询】中查询使用规则生成的差异凭证。

### 3. 广告费调整

➢ 本规则专门为调整企业所得税提供；

当需要调整财务数据中的广告费时，适用广告费调整规则；

在【差异调整规则设置】中设置广告费调整属性调整规则以及扣除标准；

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_152_1038_606.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.1.2-7</div>


在【广告费辅助账】中【导入】财务核算账簿中的广告费相关凭证记录；

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_703_1029_893.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.2-7</div>


在【差异调整规则执行】中对调整的税务核算账簿【执行】广告费调整规则，调整某个年度广告费相关的财务数据；

自动生成广告费调整的差异凭证到【差异凭证录入】中，可根据需要对差异凭证维护和审核；

在【差异调整规则执行】中生成调整执行日志，并可通过日志联查差异凭证；

➢ 可在【差异凭证查询】中查询使用规则生成的差异凭证。

同时，在【广告费辅助账】中生成广告费抵扣明细。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td colspan="3">差异调整规则设置-全局</td><td colspan="2">差异调整规则执行</td><td colspan="7">广告费辅助账</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>新增</td><td style='text-align: center; word-wrap: break-word;'>修改</td><td style='text-align: center; word-wrap: break-word;'>删除</td><td style='text-align: center; word-wrap: break-word;'>查询</td><td style='text-align: center; word-wrap: break-word;'>刷新</td><td style='text-align: center; word-wrap: break-word;'>导入</td><td colspan="8"></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>税务核算账簿</td><td colspan="3">集团总公司-基准账簿</td><td colspan="10">Q</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="2">1</td><td colspan="2">调整财务核算账簿</td><td style='text-align: center; word-wrap: break-word;'>制单日期</td><td style='text-align: center; word-wrap: break-word;'>年度</td><td style='text-align: center; word-wrap: break-word;'>期间</td><td style='text-align: center; word-wrap: break-word;'>凭证类别</td><td style='text-align: center; word-wrap: break-word;'>凭证号</td><td style='text-align: center; word-wrap: break-word;'>分录号</td><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>科目</td><td style='text-align: center; word-wrap: break-word;'>辅助核算</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>原币金额</td><td style='text-align: center; word-wrap: break-word;'>组织本币借方</td></tr><tr><td colspan="2">集团总公司-基...</td><td style='text-align: center; word-wrap: break-word;'>2012-10-25</td><td style='text-align: center; word-wrap: break-word;'>2012</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>记账凭证</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>广告费</td><td style='text-align: center; word-wrap: break-word;'>销售费用</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>350.0000</td><td style='text-align: center; word-wrap: break-word;'>350.0000</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="14">合计</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="14">4</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="14">广告费抵扣记录</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2012</td><td colspan="2">2012-10-26</td><td style='text-align: center; word-wrap: break-word;'>4</td><td colspan="9">350.0000</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 2.1.2-8</div>


## 注意：

➢【差异调整规则设置】中子表的差异调整项为暂时性差异时，平衡分录为必填项；

当规则属性为按扣除标准或广告费调整时，自动调整执行生成的差异凭证为 12 月 31 日的凭证；

当规则属性为广告费调整时，调整方式的调增或是调减由计算规则来确定，只有当广告费为调减时按调整方式来决定。

#### 2.1.3 多税种统一调整

##### 2.1.3.1 业务描述

不同税种的调整要求和方式不同，对一套总账数据要分税种分别进行调整；

在税务管理系统中，制作差异凭证时，可支持一次性调整涉及多个税种的财税差异。

##### 2.1.3.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_377_237_810_791.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图 2.1.3-1</div>


##### 2.1.3.2 业务流程


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>税务管理</td><td style='text-align: center; word-wrap: break-word;'>差异凭证录入</td></tr></table>

##### 2.1.3.4 产品解决方案

### 1. 多税种统一调整

当用户需要进行多个税种的差异调整时，可一次在一张差异凭证上录入多个税种的调整分录；

在【差异凭证录入】中【新增】一张凭证；

在凭证子表中【增行】用以增加调整分录，根据需要调整的税种选择差异调整项，通过右侧辅助信息栏可查看差异调整项对应的税种详情；

➢一张凭证上可增加多行调整分录，每条调整分录可以对应不同税种的差异调整项。

#### 2.1.4 自动生成固定资产折旧差异凭证

##### 2.1.4.1 业务描述

固定资产系统分为财务核算账簿和税务核算账簿，对于同一固定资产折旧卡片会记录财务和税务两条数据；

➢ 利用固定资产已有的财务和税务数据，自动生成财税差异调整凭证。

##### 2.1.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_198_594_1021_1230.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 2.1.4-9</div>


##### 2.1.4.2 业务流程


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>资产信息管理</td><td style='text-align: center; word-wrap: break-word;'>设备卡片</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="4">企业建模平台</td><td rowspan="4">会计平台</td><td style='text-align: center; word-wrap: break-word;'>平台设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>分类定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>入账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>转换模板</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">税务管理</td><td style='text-align: center; word-wrap: break-word;'>差异凭证录入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异凭证查询</td></tr></table>

##### 2.1.4.4 产品解决方案

当用户使用资产管理产品并启用资产税务账簿时，适用此调整方式；

在会计平台进行【平台配置】，设置【分类定义】、【入账规则】以及【转换模板】，其中【分类定义】和【转换模板】是有预置内容的，可根据用户需求自行调整。

编写固定资产的【设备卡片】，分为资产财务账簿和税务账簿两种方式计提折旧，保存的同时根据会计平台设置生成差异凭证。

自动生成的差异凭证到【差异凭证录入】中，可根据需要对差异凭证维护和审核；

➢ 可在【差异凭证查询】中查询生成的差异凭证。

## 注意：

此种调整方式依赖于用户安装使用资产管理产品，并对固定资产计提折旧；

➢ 预置的转换模板取数方式并不适用于所有资产管理系统,需要根据用户的实际情况自行调整;

固定资产折旧的差异凭证也可通过手工录入方式完成。

#### 2.1.5 递延所得税核算

##### 2.1.5.1 暂时性差异

###### 2.1.5.1.1 业务描述

资产、负债的账面价值与其计税基础不同产生的差额形成了暂时性差异；

企业在计算确定了应纳税暂时性差异与可抵扣暂时性差异后，应当按照所得税会计准则规定的原则确认相关的递延所得税负债和递延所得税资产；

递延所得税资产产生于可抵扣暂时性差异，递延所得税负债产生于应纳税暂时性差异；

暂时性差异数据是计算递延所得税的基础。

###### 2.1.5.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_288_454_909_912.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.1.5.1-1</div>


###### 2.1.5.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">税务管理</td><td style='text-align: center; word-wrap: break-word;'>期初暂时性差异</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>暂时性差异查询</td></tr></table>

###### 2.1.5.1.4 产品解决方案

### 1. 期初暂时性差异

在【期初暂时性差异】中录入税务账簿启用日期之前包括以前年度的所有暂时性差异记录；

【期初暂时性差异】是用于计算递延所得税的，其中录入的内容只需为暂时性差异凭证平衡分录的一方，即会计科目均为非损益类科目；

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_155_1034_354.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.5.1-2</div>


### 2. 暂时性差异查询

暂时性差异的数据是计算递延所得税的基础；

在【暂时性差异查询】中使用〖查询〗查询暂时性差异信息；

➢ 【暂时性差异查询】包含对【期初暂时性差异】和【差异凭证查询】中差异分录的查询；

【暂时性差异查询】自动计算并展示到查询的截止日期时的应纳税暂时性差异与可抵扣暂时性差异。

<div style="text-align: center;"><img src="imgs/img_in_image_box_156_706_1037_1219.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.1.5.1-3</div>

## 注意：

【期初暂时性差异】中录入的数据不仅限于税务账簿当年的数据，它包含公司成立以来截止到账簿启用日期之前的所有暂时性差异数据；

【暂时性差异查询】中自动计算出的应纳税暂时性差异和可抵扣暂时性差异的值不是按当前查询结果计算的，而是从查询的截止日期追溯到以往所有暂时性差异得到的数据；

##### 2.1.5.2 递延所得税计算

###### 2.1.5.2.1 业务描述

资产、负债的账面价值与其计税基础不同产生的差额形成了暂时性差异；

企业在计算确定了应纳税暂时性差异与可抵扣暂时性差异后，应当按照所得税会计准则规定的原则确认相关的递延所得税负债和递延所得税资产；

递延所得税资产产生于可抵扣暂时性差异，递延所得税负债产生于应纳税暂时性差异；

递延所得税资产和递延所得税负债的数据计入总账凭证，同时也是报表项目中的内容。

###### 2.1.5.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_246_959_689.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 2.1.5.2-1</div>


###### 2.1.5.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">税务管理</td><td style='text-align: center; word-wrap: break-word;'>递延所得税管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>递延所得税查询</td></tr></table>

###### 2.1.5.2.4 产品解决方案

## 1 ) 递延所得税管理

在【期末处理】中对需要计算递延所得税的会计期间【关账】；

在【递延所得税管理】中【计算】关账期间的递延所得税；

<div style="text-align: center;"><img src="imgs/img_in_image_box_162_157_1026_600.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.5.2-2</div>


➢ 对递延所得税单据执行〖审核〗，同时通过会计平台生成总账记账凭证；

可针对单据【联查】递延所得税单据的明细以及生成的总账凭证。

<div style="text-align: center;"><img src="imgs/img_in_image_box_153_782_1037_1103.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.1.5.2-3</div>


## 2 ) 递延所得税查询

通过〖查询〗可查看对应税务账簿和期间的递延所得税单据；

➢ 在查询结果中自动依据查询条件显示对应的币种数据；

可针对单据【联查】递延所得税单据的明细以及生成的总账凭证。

## 注意：

➢ 计算递延所得税之前要先进行当前税务账簿的当期会计期间关账；

➢ 计算递延所得税自动生成当期会计期间最后一天的单据；

递延所得税明细单据为对一级会计科目的查询；

当税务账簿结账后，不允许再进行结账期间的递延所得税计算。

#### 2.1.6 独立计提

##### 2.1.6.1 日常申报

###### 2.1.6.1.1 业务描述

虽然企业所得税是按年计算的，但是企业需要按月或按季度定时向税务机关预缴；

➢ 预缴企业所得税的金额是根据税收政策规定的计提规则来确定的；

独立计提方式适用于法人公司未被下级分公司委托核算企业所得税，或分子公司未委托上级法人公司核算企业所得税时，各自独立计算和计提。

###### 2.1.6.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_289_239_910_918.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.1.6.1-1</div>


###### 2.1.6.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">税务管理</td><td style='text-align: center; word-wrap: break-word;'>日常申报一税款计提规则定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>日常申报一税款计提执行</td></tr></table>

###### 2.1.6.1.4 产品解决方案

### 1. 规则设置

当法人公司没有被分公司委托核算企业所得税，或者分子公司需要自行核算企业所得税时，只需要设置【税款计提规则定义】；

➢ 使用【税款计提规则定义】设置税款计提规则，涉及取数方式、生成的税款计提总账凭证的

内容等;

税款计提的金额通过税务报表获取，为税款计提结果中的应纳税所得额，并非分录对应的金额；

➢ 因为此场景计提税款时不需要使用分配规则，将分配规则选项置空。

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_331_1029_594.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.6.1-3</div>


## 1 ) 税款计提

在【税款计提执行】中【执行】进行当期的税款计提，生成当前组织自行计提的税款结果；

<div style="text-align: center;"><img src="imgs/img_in_image_box_160_769_1029_929.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.1.6.1-4</div>


在计提完成时自动审核通过生成总账凭证；

可针对税款计提单据【联查】计提的总账凭证。

## 注意：

➢ 日常申报用于计算企业所得税；

➢ 只有法人公司才可以进行【税款计提执行】操作；

➢ 税款计提的数据是通过税务报表获取的。

##### 2.1.6.2 汇算清缴

###### 2.1.6.2.1 业务描述

对于企业所得税，我国的税收政策规定，按月或按季度预缴，到年底汇算清缴；

到年底需要针对全年的企业实际所得以及企业已预缴的税收进行比对调整，多退少补；

最终形成企业年终的汇算清缴申报表提交给税务机关。

###### 2.1.6.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_289_599_897_1105.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">图 2.1.6.2-1</div>


###### 2.1.6.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">税务管理</td><td style='text-align: center; word-wrap: break-word;'>汇算清缴—税款计提规则定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>汇算清缴—税款计提执行</td></tr></table>

###### 2.1.6.2.4 产品解决方案

### 1. 规则设置

使用【税款计提规则定义】设置税款计提规则，涉及取数方式、生成的税款计提总账凭证的内容等；

➢ 税款计提的金额通过税务报表获取。

### 2. 税款计提

在【税款计提执行】中【执行】进行当年汇算清缴的税款计提；

☑ 【执行】时需要确认汇算清缴的总账凭证计入到哪个会计期间；

税款计提执行完毕将自动生成总账凭证到设置好的会计期间中；

可针对汇算清缴的税款计提单据〖联查〗计提的总账凭证。

## 注意：

此场景是为法人公司提供使用；

➢ 汇算清缴的税款计提结果不需审核直接生成总账凭证。

### 2.2 独立核算，委托调整

支持独立总账核算的下属分公司，委托上级法人公司对下属分公司进行统一的企业所得税财税差异调整。

#### 2.2.1 手工差异调整

同独立核算，独立调整中的手工差异调整。

#### 2.2.2 自动差异调整

同独立核算，独立调整中的自动差异调整。

#### 2.2.3 多税种统一调整

同独立核算，独立调整中的多税种统一调整。

#### 2.2.4 自动生成固定资产折旧差异凭证

同独立核算，独立调整中的自动生成固定资产折旧差异凭证。

#### 2.2.5 递延所得税核算

##### 2.2.5.1 暂时性差异

同独立核算，独立调整中的递延所得税核算——暂时性差异。

##### 2.2.5.2 递延所得税计算

同独立核算，独立调整中的递延所得税核算——暂时性差异。

#### 2.2.6 统一计算、自动分配、统一计提

##### 2.2.6.1 日常申报

###### 2.2.6.1.1 业务描述

虽然企业所得税是按年计算的，但是企业需要按月或按季度定时向税务机关预缴；

➢ 预缴企业所得税的金额是根据税收政策规定的计提规则来确定的；

对于委托核算的情况，还需要按一定的分配原则将企业所得税进行分配。

###### 2.2.6.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_288_239_913_917.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.2.6.1-1</div>


###### 2.2.6.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">财务会计</td><td rowspan="3">税务管理</td><td style='text-align: center; word-wrap: break-word;'>日常申报—分配规则定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>日常申报—税款计提规则定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>日常申报—税款计提执行</td></tr></table>

###### 2.2.6.1.4 产品解决方案

### 1. 规则设置

当法人公司被下级公司委托核算企业所得税时，【分配规则定义】中【新增】分配规则；

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_139_1039_764.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.2.6.1-2</div>


使用【税款计提规则定义】设置税款计提规则，涉及取数方式、生成的税款计提总账凭证的内容等；

税款计提的金额通过税务报表获取，为税款计提结果中的应纳税所得额，并非分录对应的金额；

当有委托核算关系的需要税款计提时，需要在【税款计提规则定义】中定义规则并引用分配规则。

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_1098_1030_1389.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2.2.6.1-3</div>


### 2. 税款计提

➢ 在【税款计提执行】中【执行】进行当期的税款计提，生成当前组织自行计提的税款结果；

<div style="text-align: center;"><img src="imgs/img_in_image_box_191_204_1057_444.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.2.6.1-4</div>


➢ 【执行】时使用的税款计提规则引用了分配规则时，还需设置分配规则的取数期间；

当税款计提时有委托核算的情况，则需要通过【审核】后生成总账凭证；

对于有委托核算关系的情况，在【审核】之前可通过【修改】对税款计提单据进行手工维护；

可针对税款计提单据【联查】计提的总账凭证。

## 注意：

➢ 日常申报用于计算企业所得税；

只有法人公司才可以进行【税款计提执行】操作；

手工修改税款计提单据后，将清空动因数据，且不能再维护动因数据，若想恢复，只能通过重新计提操作来完成；

➢ 税款计提的数据是通过税务报表获取的。

##### 2.2.6.2 汇算清缴

###### 2.2.6.2.1 业务描述

对于企业所得税，我国的税收政策规定，按月或按季度预缴，到年底汇算清缴；

到年底需要针对全年的企业实际所得以及企业已预缴的税收进行比对调整，多退少补；

最终形成企业年终的汇算清缴申报表提交给税务机关。

###### 2.2.6.21.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_289_245_914_754.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.2.6.2-1</div>


###### 2.2.6.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">税务管理</td><td style='text-align: center; word-wrap: break-word;'>汇算清缴—税款计提规则定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>汇算清缴—税款计提执行</td></tr></table>

###### 2.2.6.2.4 产品解决方案

### 1. 规则设置

使用【税款计提规则定义】设置税款计提规则，涉及取数方式、生成的税款计提总账凭证的内容等；

➢ 税款计提的金额通过税务报表获取。

### 2. 税款计提

在【税款计提执行】中【执行】进行当年汇算清缴的税款计提；

☑ 【执行】时需要确认汇算清缴的总账凭证计入到哪个会计期间；

➢ 税款计提执行完毕将自动生成总账凭证到设置好的会计期间中；

可针对汇算清缴的税款计提单据【联查】计提的总账凭证。

## 注意：

此场景是为法人公司提供使用；

因汇算清缴时将不再做委托核算关系的分配工作，所以汇算清缴的税款计提不需要设置分配规则；

➢ 汇算清缴的税款计提结果不需审核直接生成总账凭证。

## 第三章 初始准备

### 3.1 企业建模平台

#### 3.1.1 基础数据维护

##### 3.1.1.1 税种

税种是“税收种类”的简称，构成一个税种的主要因素有征税对象、纳税人、税目、税率、纳税环节、纳税期限、缴纳方法、减税、免税及违章处理等。不同的征税对象和纳税人是一个税种区别于另一个税种的主要标志，也往往是税种名称的由来。同时，每个税种都有其特定的功能和作用，其存在依赖于一定的客观经济条件。目前我国税收分为流转税、所得税、资源税、财产税、行为税五大类，共二十多种。

税种档案主要维护我国现行税种。

##### 3.1.1.2 税率

税率是按照计税依据征税的比例或者额度。税收的固定性特征是通过税率体现的。税率是税收制度的核心要素，是计算应纳税额的尺度。在计税依据已经确定的前提下，国家征税的数量和纳税人的负担水平就取决于税率，国家一定时期的税收政策也体现在税率方面。

目前税率档案，只是针对各个时期的企业所得税税率进行维护，在计算递延所得税和税款计提时应用。

### 3.2 财务会计

#### 3.2.1 税务管理 - 基础设置

##### 3.2.1.1 差异类型

企业在针对不同税种进行财税差异调整时，需要确认差异调整的内容归属哪一个类别，由此来判断调整的税种和属性，便于对调整事项进行归集，为形成不同税种的税务报表提供数据基础。

差异类型，就是在税务管理产品中对差异调整项目的分类。

##### 3.2.1.2 差异调整项

企业在进行财税差异调整时，需要确认调整属于差异类型下具体的差异调整项目，用于区分调整凭证针对的税种，以及调整事项的属性，依此计算应交税金并出具相应的税务报表。

差异调整项是对差异类型的细化，在企业所得税的运用中，通过差异调整项来区分暂时性差异和永久性差异。

## 第四章 操作指南

本手册具体详细操作应用，请登录 NC 系统参见相关产品帮助。

## 附录

<div style="text-align: center;">附录 4：本文参见其他手册清单</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>手册名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_490_438_697_590.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform
