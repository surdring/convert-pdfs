# NCV6.5产品手册-增值税

产品手册- V6.5

增值税管理

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权.....1  
导读.....3  
名词解释.....4  
第一章 概述.....5  
1.1 产品概述.....5  
1.2 产品价值.....5  
第二章 VAT取税模型.....6  
第三章 应用场景.....8  
3.1 中国大陆购销业务场景.....8  
3.1.1 中国大陆进出口业务.....8  
3.1.2 中国大陆国内购销业务.....9  
3.1.3 中国大陆集团内部交易业务.....11  
3.1.4 中国大陆进项税不可抵扣业务.....12  
3.2 EU购销业务场景.....14  
3.2.1 EU成员国内购销业务.....14  
3.2.2 EU成员国内进项税不可抵扣业务.....14  
3.2.3 EU内跨EU成员国购销业务.....14  
3.2.4 EU成员国与非EU成员国的跨国购销业务.....16  
3.2.5 EU海外工厂交货业务.....17  
3.2.6 EU三角贸易业务.....17  
3.3 EU报税应用.....19  
第四章 初始准备.....20  
4.1 企业建模平台.....20  
4.1.1 业务单元.....20  
4.1.2 基础数据维护.....21  
4.2 VAT增值税基础数据维护.....24  
4.2.1 基础设置.....24  
4.3 会计平台增值税相关设置.....27  
4.3.1 转换模板.....27  
第五章 操作指南.....28  
附录.....29

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供客户业务需求如何与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是 VAT 取税模型；第三部分是对有关 VAT 的主要业务场景介绍，分为国内 VAT 场景以及欧盟 VAT 业务场景两块；第四部分介绍了 VAT 增值税管理启用前的初始准备设置。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释，并在附录进行了汇总，列示为单据流转、控制点、与查询报表，以便用户查找对照。

为突出重点，本手册定位于方案性说明，仅对产品操作中的重要控制点有所描述。若读者希望深入了解特定板块的产品应用，可结合本手册，查阅如下资料：

1. 《产品手册—组织管理》——深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助——针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《产品手册—流程管理》----提供关于交易类型、流程设计工具的应用指导。

4. 《产品手册—基础数据》-----可对手册第四部分（即初始准备）中的有关基础数据的理解和应用进行更详细深入地了解。

## 名词解释

## EU

即：欧盟，政治和关税联盟，目前包括 27 个成员国。

## 增值税

增值税是对销售货物或者提供加工、修理修配劳务以及进口货物的单位和个人就其实现的增值额征收的一个税种。由消费者支付，但却在生产和分配链的每个阶段征收，增值税已经成为增值税由国家税务局负责征收。进项税可以抵销项税；增值税是对每个增值环节的征税。最终客户所支付的增值税是所有环节支付的增值税的和。

## 税类

是针对供应商、客户、物料等基础数据指定的税务分类。

## 报税国家

是制定税收政策和收取税金、进行出口退税的国家。销项税抵扣进项税在同一报税国家的范围内进行。

## 税码

是软件系统中的概念，基本的作用是用于反映报税国家在不同的条件下，采取的不同的增值税政策，通过税码可以取得税率，并计算税额。税码用于 EU 时，同时作为税务报表的统计维度。

## 计税金额

是计算税额的基础，有些资料也称为计税价格。

## EU VAT 注册码

EU 内，应税人从税务机关所取得的注册码，采用该注册码可以进行报税。

## EU 逆向征税

EU 企业从另外一个 EU 成员国采购或从 EU 外的国家进行采购时，对增值税的核算可以在财务上进行特定的处理，经过这种会计处理，增值税可以直接抵扣掉不需要实际支付。这种机制称为逆向征税。

## 第一章 概述

### 1.1 产品概述

VAT 在 NC 中不是一个独立的模块，是 NC 供应链、财务等业务处理过程中的一个特定应用。即：NC 的供应链、财务等系统进行业务处理时，需要能够准确的确定当前交易的 VAT 税率、VAT 税额等信息。目前，NC 支持 VAT 在国内的应用，也支持 VAT 在 EU 内的应用。

### 1.2 产品价值

1. 支持中国大陆的增值税制度；

2. 支持 EU 内增值税制度；

3. 支持 EU 内逆向征税的处理；

4. 支持 EU 内的 VAT 报税；

## 第二章 VAT 取税模型

<div style="text-align: center;"><img src="imgs/img_in_image_box_321_282_879_696.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 2-01 VAT 取税模型</div>


1. 录入采购、销售单据时，系统自动确定报税国、购销类型、是否三角贸易、物料税类、客户税类、供应商税类、发货国、收货国、客户是否有 VAT 注册码等信息。

其中，采购订单各信息项的取数逻辑如下：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>发货国家</td><td style='text-align: center; word-wrap: break-word;'>如果 供应商发货地址非空取发货地址国家否则取供应商档案国家</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收货国家</td><td style='text-align: center; word-wrap: break-word;'>如果 是直运业务收货地址非空时，取收货地址国家否则，取表头的收货客户档案国家。否则取收货库存组织国家如果为空，取结算财务组织在国家；</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报税国家</td><td style='text-align: center; word-wrap: break-word;'>如果 采购结算组织与收货库存组织跨公司取结算财务组织所在国家否则取收货库存组织所在国家</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="3">购销类型</td><td style='text-align: center; word-wrap: break-word;'>如果 报税国=发货国</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>国内采购</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>否则 进口采购</td></tr><tr><td rowspan="4">三角贸易</td><td style='text-align: center; word-wrap: break-word;'>如果 购销类型=进口采购 而且 报税国≠收货国</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>三角贸易=是</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>否则 为否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>（主要用于EU的三角贸易）</td></tr></table>

销售订单各信息项的取数逻辑如下：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>发货国家</td><td style='text-align: center; word-wrap: break-word;'>发货库存组织所在国家&gt;销售组织所在国家</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>收货国家</td><td style='text-align: center; word-wrap: break-word;'>收货地址国家&gt;收货客户档案中的国家</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>报税国家</td><td style='text-align: center; word-wrap: break-word;'>If 销售结算组织与发货库存组织跨公司结算财务组织所在国家（主要用于EU的三角贸易）Else发货库存组织所在国家</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>购销类型</td><td style='text-align: center; word-wrap: break-word;'>=收货国<img src="imgs/img_in_seal_box_436_915_559_1037.jpg" alt="Image"" />国内销售出口销售</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>是否三角贸易</td><td style='text-align: center; word-wrap: break-word;'>If 购销类型=出口销售&amp;&amp;报税国!=发货国Then三角贸易（主要用于EU的三角贸易）</td></tr></table>

2. 依据上述信息匹配【增值税税码税率】档案确定税码，并依据单据日期匹配增值税税码税率的有效期，最终确定扣税类别、税率、不可抵扣税率等信息。

## 第三章 应用场景

### 3.1 中国大陆购销业务场景

#### 3.1.1 中国大陆进出口业务

### 1. 业务描述

进口

中国大陆企业进口时，商品要征收进口增值税，进口增值税由中国大陆海关代为征收，上缴到中央财政。

## 出口

中国大陆企业出口时，商品一般免税，即：增值税税率一般为 0，销项税在中国大陆进行报税。

### 2. 产品解决方案

## 1 ）设置增值税税码税率

按照 “中国” 设置增值税税码税率档案，购销类型可以选择 “进口”。

<div style="text-align: center;"><img src="imgs/img_in_image_box_191_983_1107_1250.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 3.1-01 中国大陆进口业务：设置增值税税码税率，购销类型 “进口”</div>


## 2 ）采购业务的自动取税

录入单据时，系统自动匹配增值税税码税率档案，确定所应用的税码和税率等信息。

需要注意的是在进口业务中，增值税是支付给海关的，不是支付给供应商的，因此在进口业务中，无税金额=价税合计。

<div style="text-align: center;"><img src="imgs/img_in_image_box_190_160_1114_317.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 3.1-02 中国大陆进口业务：采购业务的自动取税</div>


## 出口业务

## 1 ）设置增值税税码税率

按照 “中国” 设置增值税税码税率档案，购销类型可以选择 “出口”。

<div style="text-align: center;"><img src="imgs/img_in_image_box_191_570_1109_872.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 3.1-03 中国大陆出口业务：设置增值税税码税率，购销类型“出口”</div>


录入单据时，系统自动匹配增值税税码税率档案，确定所应用的税码和税率等信息。

## 2 ) 销售业务的自动取税

<div style="text-align: center;"><img src="imgs/img_in_image_box_136_1031_1051_1193.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 3.1-04 中国大陆出口业务：销售业务的自动取税</div>


#### 3.1.2 中国大陆国内购销业务

### 1. 业务描述

此场景是供应商、客户都在中国大陆境内。

销售：

国内销售时，客户如果是一般增值税纳税人，需要向客户收取 17%（对于一般纳税商品）的增值税；客户如果是慈善机构时，销售是免税的。

## 采购：

国内采购时，供应商如果是一般增值税纳税人，需要向供应商支付 17%（对于一般纳税商品）的增值税。

### 2. 产品解决方案

## 国内采购

## 1 ) 设置增值税税码税率

按照 “中国” 设置增值税税码税率档案，购销类型可以选择 “国内采购” 或 “不区分”。

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_586_1075_864.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 3.1-05 中国大陆国内采购业务：设置增值税税码税率，购销类型 “国内采购”</div>


## 2 ) 采购业务的自动取税

录入单据时，系统自动匹配增值税税码税率档案，确定所应用的税码和税率等信息。

## 国内销售

## 1 ) 设置增值税税码税率

按照 “中国” 设置增值税税码税率档案，购销类型可以选择 “国内销售” 或 “不区分”。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_1199_1079_1468.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 3.1-06 中国大陆国内销售业务：设置增值税税码税率，购销类型 “国内销售”</div>

## 2 ) 销售业务的自动取税

录入单据时，系统自动匹配增值税税码税率档案，确定所应用的税码和税率等信息。

#### 3.1.3 中国大陆集团内部交易业务

### 1. 业务描述

集团内的两个法人公司之间进行商品的调拨，视同普通的销售、采购业务。

### 2. 产品解决方案

## 1 ) 设置增值税税码税率

按照 “中国” 设置增值税税码税率档案，购销类型可以选择 “不区分”。或者分别按购销类型 “国内销售” “国内采购” 进行设置。

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_813_1113_1104.jpg" alt="Image" width="77%" /></div>


图 3.1-07 中国大陆内部交易业务：设置增值税税码税率，购销类型 “不区分”

## 2 ) 调拨订单的自动取税

在调拨订单上，系统自动取得调出方的税码和税率等信息。

<div style="text-align: center;"><img src="imgs/img_in_image_box_147_124_1119_463.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.1-08 中国大陆内部交易业务：调拨订单的自动取税</div>


## 3 ) 内部结算清单的自动取税

内部结算清单中，系统分别自动取得调出方的调出税码、调入方的调入税码以及相应的税率等信息。

<div style="text-align: center;"><img src="imgs/img_in_image_box_147_652_1118_1078.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.1-09 中国大陆内部交易业务：内部结算清单的自动取税</div>


#### 3.1.4 中国大陆进项税不可抵扣业务

### 1. 业务描述

进行国内采购时，采购方所支付的进项税不能完全进行抵扣，进项税的不可抵扣部分可能要计入商品的成本中。

<div style="text-align: center;"><img src="imgs/img_in_image_box_356_169_876_379.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图 3.1-10 不可抵扣进项税影响商品成本</div>


### 2. 产品解决方案

## 1 ) 设置增值税税码税率

按照 “中国”， 设置增值税税码税率档案， 要定义不可抵扣税率。

<div style="text-align: center;"><img src="imgs/img_in_image_box_191_588_1159_892.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.1-11 不可抵扣进项税业务：增值税税码税率设置</div>


## 2 ) 采购业务的自动取税

录入单据时，系统自动匹配增值税税码税率档案，确定所应用的税码和税率、不可抵扣税率等信息。另外，系统自动计算“计成本金额”。

<div style="text-align: center;"><img src="imgs/img_in_image_box_189_1137_1160_1305.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.1-12 不可抵扣进项税业务：采购业务的自动取税</div>


## 3 ) 暂估和结算

后续的采购暂估和采购结算业务，系统按照“计成本金额”进行材料成本的核算。

### 3.2 EU 购销业务场景

#### 3.2.1 EU 成员国内购销业务

### 1. 业务描述

EU 成员国内的购销业务是在 EU 同一成员国内供应商与客户之间所形成的购销业务与中国大陆的国内购销业务类似。

#### 3.2.2 EU 成员国内进项税不可抵扣业务

### 1. 业务描述

此场景是 EU 同一成员国内供应商与客户之间就某些商品交易所形成的购销业务，与中国大陆进项税不可抵扣业务类似。

EU 成员国内，某个 EU 的企业从另一个 EU 的企业采购某些能源商品时（比如：汽油等），采购方所支付的进项税不能完全进行抵扣。按照 EU 法律的规定，进项税的不可抵扣部分可能要计入商品的成本中，也可能计入到其他相应的总账会计科目中。

目前，NC 仅支持进项税的不可抵扣部分计入商品成本这种情况。

#### 3.2.3 EU 内跨 EU 成员国购销业务

### 1. 业务描述

此场景是 EU 内不同成员国间的购销业务的典型形态。

## 1 ) EU 成员国间销售：

一个 EU 成员国的企业销售商品给另一个 EU 成员国的客户时, 如果客户在收货的 EU 成员国有 VAT 注册码, 那么销售是免税的; 由销售方在发货国进行报税。

## 2 ) EU 成员国间采购：

一个EU成员国的企业从另一个EU成员国的供应商采购时,如果供应商在发货的EU成员国有VAT注册码,那么采购方需要采用本国的税率,进行逆向缴纳处理。由采购方在本国进行报税。

<div style="text-align: center;"><img src="imgs/img_in_image_box_241_156_961_391.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">图 3.2-01 EU 内跨 EU 成员国的购销业务</div>


### 2. 产品解决方案

## EU 成员国间销售

## 1 ) 设置增值税税码税率

按照 EU 成员国设置增值税税码税率档案，购销类型要选择“出口”，另外要设置客户是否有 VAT 注册码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_749_1132_1049.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 3.2-02 EU 成员国间销售业务：增值税税码税率设置，购销类型“出口”</div>


## EU 成员国间采购

## 1 ) 设置增值税税码税率

按照 EU 成员国设置增值税税码税率档案，购销类型要选择 “进口”。

## 2 ) 采购单据自动取税

录入单据时，系统自动匹配增值税税码税率档案，确定所应用的税码和税率、不可抵扣税率等信息。另外，采购发票表头“是否逆向征税”，由系统自动维护该标识，该标识会传入到应付单中，最终影响总账凭证的会计分录。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_150_1081_317.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.2-03 采购发票，具有“逆向征税”标识</div>


#### 3.2.4 EU 成员国与非 EU 成员国的跨国购销业务

### 1. 业务描述

此场景是 EU 成员国与非 EU 成员国之间的购销业务。

1) 出口:

一个 EU 成员国的企业出口到 EU 之外的国家，该业务与中国大陆的出口业务类似。

2) 进口：

一个 EU 成员国的企业从 EU 之外的国家进口，该业务与中国大陆的进口业务类似，但是有一定的差异。在 EU 中，增值税一般不真正支付给 EU 的海关，而是需要进行逆向缴纳处理。

### 2. 产品解决方案

出口

1) 设置增值税税码税率

按照 EU 成员国设置增值税税码税率档案，购销类型要选择 “出口”

## 进口

2) 设置增值税税码税率

按照 EU 成员国设置增值税税码税率档案，购销类型要选择 “进口”。

另外，在进口业务中采购发票表体明细行“逆向征税”的标识，系统会自动维护该标识，该标识会传入到应付单中，最终影响总账凭证的会计分录。

#### 3.2.5 EU 海外工厂交货业务

### 1. 业务描述

德国企业 A 在不同的 EU 成员国（德国、法国）有 VAT 注册码，德国企业 A 在法国有一家工厂或仓储中心 A1，德国企业 A 从法国仓储中心 A1 发货销售商品给法国的客户。

德国企业 A 需要执行法国的税率并在法国进行报税。

<div style="text-align: center;"><img src="imgs/img_in_image_box_286_431_919_761.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 3.2-04 EU 海外工厂交货业务</div>


### 2. 产品解决方案

## 1 ) 设置增值税税码税率

上述案例中，需要按 “法国” 设置增值税税码税率档案，购销类型要选择 “国内销售”。

#### 3.2.6 EU 三角贸易业务

### 1. 业务描述

EU 的三角贸易场景是在三个不同的 EU 成员国间形成的直运业务。

一个法国企业 A 销售商品给德国企业 C 时，商品由英国企业 B 直接发给德国企业 C。英国企业 B 给法国企业 A 开具发票，法国企业 A 给德国企业 C 开具发票。

A 的 VAT:

A 的销售、采购业务，视同英国发货，德国收货，单据打“三角贸易”标识，在 A 所在的国家法国进行报税。三角贸易影响相应的 EU 报表。

## C 的 VAT:

C 公司进项税，视同英国发货，德国收货，单据不打三角贸易标识，在 C 所在的国家德国进行报税。

## B 的 VAT:

B 公司销售，视同英国发货，德国收货，单据不打三角贸易标识，在 B 所在的国家英国进行报税。

<div style="text-align: center;"><img src="imgs/img_in_image_box_323_302_919_651.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 3.2-05 EU 三角贸易业务</div>


### 2. 产品解决方案

## 1 ) 场景匹配

NC 中有 4 个场景可以满足 EU 的三角贸易

场景 1：供应商 B 和客户 C 都是外部的，直运销售采购业务。

场景 2：中间厂商 A 和供应商 B 属于同一个集团，客户 C 是外部的，跨组织销售业务。

场景 3：中间厂商 A 和客户 C 属于同一个集团，供应商 B 是外部的，集采分收业务。

场景 4：A、B、C 都属于同一个集团，三方调拨业务。

上述场景请参见相应的 NCV6.33 产品手册。

## 2 ) 增值税税码税率

中间厂商 A 所采用的增值税税码税率有特殊性，其中“是否三角贸易”要勾选“是”。

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_1180_1119_1485.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.2-06 EU 三角贸易业务：增值税税码税率，勾选“三角贸易”标识</div>

### 3.3 EU 报税应用

按照 EU 的规定，企业需要定期向税务机关进行报税。在 NC 中，向 EU 税务机关进行报税的纳税申报表是从总账系统中取数的。

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_372_1030_963.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 3.3-01 EU 报税应用</div>


因此，应付单、应收单等单据传递到总账生成总账凭证时，需要携带报税国、发货国、收货国、交易代码、客户 VAT 注册码、税码、计税金额等辅助核算信息。NC 的会计平台支持这些固定的辅助核算项。

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_1131_1077_1370.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.3-02 转换模板</div>

## 第四章 初始准备

### 4.1 企业建模平台

#### 4.1.1 业务单元

为了保证取税的准确性，业务单元中需要定义相应的国家地区；另外，针对 EU 的企业，需要在财务组织上定义该企业在不同 EU 成员国所拥有的 VAT 注册码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_587_1076_965.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 4.1-01 定义业务单元</div>


在业务单元功能节点，通过【辅助功能】中的【维护 VAT】业务功能按钮，可以维护此财务组织（实际上是法人公司）在欧盟不同国家内的 VAT 注册码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_157_152_926_645.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 4.1-02 维护 VAT 注册码</div>


#### 4.1.2 基础数据维护

##### 4.1.2.2 客户

在客户档案中需要设定客户所在的国家地区，还需要设定客户税类，在 EU 应用时还需要设定客户的 VAT 注册码。

注意：

只有当前集团所属的国家是 EU 成员国时，才会出现 “客户 VAT” 子页签。

<div style="text-align: center;"><img src="imgs/img_in_image_box_108_150_1077_521.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 4.1-03 设定客户的客户税类</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_107_569_1068_936.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 4.1-04 设定客户的 VAT 注册码</div>


##### 4.1.2.3 供应商

在供应商档案中需要设定供应商所在的国家地区，还需要设定供应商税类，当在 EU 应用时还需要设定供应商 VAT 注册码。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_1190_988_1341.jpg" alt="Image" width="73%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_114_154_1078_510.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 4.1-05 设定供应商的供应商税类</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_211_575_982_1074.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 4.1-06 设定供应商的 VAT 注册码</div>


##### 4.1.2.4 物料信息

在物料档案上需要设定物料税类，当在 EU 应用时需要按照国家设置物料税类。

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_1300_1029_1448.jpg" alt="Image" width="73%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_161_1119_591.jpg" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 4.1-07 设定物料的物料税类</div>


### 4.2 VAT 增值税基础数据维护

#### 4.2.1 基础设置

##### 4.2.1.1 客户税类设置

客户税类描述了销售业务中的客户应税（增值税）类别（从增值税角度，对客户的一个分类）。

NC 中，客户税类可以是决定销售业务税码税率的一个取税维度（请参见本文的“增值税税码税率”）。比如：同一商品销售给一般增值税纳税人和慈善机构等，其税码税率是不同的。一般增值税纳税人、慈善机构就可以分别隶属于不同的客户税类。

一个具体的客户隶属于哪个客户税类是在客户档案中定义的（请参见本文的“客户”档案）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_1273_1075_1462.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 4.2-01 定义客户税类</div>

##### 4.2.1.2 供应商税类设置

供应商税类描述了采购业务中的供应商应税（增值税）类别（从增值税角度，对供应商的一个分类）。

NC 中，供应商税类可以是决定采购业务税码税率的一个取税维度（请参见本文的“增值税税码税率”）。比如：同一商品从一般增值税纳税人和小规模纳税人采购，其税码税率是不同的。一般增值税纳税人、小规模纳税人就可以分别隶属于不同的供应商税类。

一个具体的供应商隶属于哪个供应商税类是在供应商档案中定义的（请参见本文的“供应商”档案）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_486_1117_672.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 4.2-02 定义供应商税类</div>


##### 4.2.1.3 物料税类设置

物料税类描述了采购销售业务中商品或服务的应税（增值税）类别（从增值税角度，对商品或服务的一个分类）。物料税类体现了一国税务机关对商品或服务的增值税政策。

NC 中，物料税类可以是决定采购销售业务税码税率的一个取税维度（请参见本文的“增值税税码税率”）。比如：中国大陆，一般纳税商品其税率 17%，而某些简易征税商品其税率是 4%，一般纳税商品和简易征收商品其物料税类就可以是不同的。

一个具体的商品属于哪个物料税类是在物料档案中定义的，而且是按照国家进行设置的（请参见本文的“物料”档案）。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>物料报表</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 4.2-03 定义物料税类</div>


##### 4.2.1.4 增值税税码税率设置

增值税税码税率，用于定义报税国在不同的业务条件下的增值税的税码、税率等相关信息，用以反映报税国在不同业务条件下，采取的不同增值税政策。

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_909_1117_1191.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 4.2-04 定义增值税税码税率</div>

### 4.3 会计平台增值税相关设置

#### 4.3.1 转换模板

在 EU 应用时，会计平台上的转换模板需要针对 VAT 的相关科目设置 “增值税信息表” 的固定辅助核算项。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>业务单元</td><td style='text-align: center; word-wrap: break-word;'>会计科目</td><td style='text-align: center; word-wrap: break-word;'>币种</td><td style='text-align: center; word-wrap: break-word;'>摘要内容</td><td style='text-align: center; word-wrap: break-word;'>拆本汇率</td><td style='text-align: center; word-wrap: break-word;'>集团汇率</td><td style='text-align: center; word-wrap: break-word;'>全局汇率</td><td style='text-align: center; word-wrap: break-word;'>借方数量</td><td style='text-align: center; word-wrap: break-word;'>原币借发生额</td><td style='text-align: center; word-wrap: break-word;'>组织本币借发生</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>[AR01 / 应收...</td><td style='text-align: center; word-wrap: break-word;'>#币种</td><td style='text-align: center; word-wrap: break-word;'>#摘要</td><td style='text-align: center; word-wrap: break-word;'>#组织本币汇率</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#借方原币金额</td><td style='text-align: center; word-wrap: break-word;'>#组织本币金...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>[AR03 / 收入...</td><td style='text-align: center; word-wrap: break-word;'>#币种</td><td style='text-align: center; word-wrap: break-word;'>#摘要</td><td style='text-align: center; word-wrap: break-word;'>#组织本币汇率</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>[AR05 / 应交...</td><td style='text-align: center; word-wrap: break-word;'>getcolvalue(...</td><td style='text-align: center; word-wrap: break-word;'>#摘要</td><td style='text-align: center; word-wrap: break-word;'>#组织本币汇率</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 4.3-01 转换模板的“增值税信息表”</div>

## 第五章 操作指南

本手册具体详细操作应用，请登录 NC 系统参见相关产品帮助。

## 附录

本文参见其他手册清单。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>资料目录</td><td style='text-align: center; word-wrap: break-word;'>相关学习点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—采购管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—销售管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—内部交易》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—组织管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—权限管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—基础数据》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册—欧盟报表》</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_491_440_698_593.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform
