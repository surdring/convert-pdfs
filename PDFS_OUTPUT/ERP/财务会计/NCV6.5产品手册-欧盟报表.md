# NCV6.5产品手册-欧盟报表

产品手册- V6.5

欧盟报表

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权.....1  
导读.....3  
名词解释.....4  
第一章 概述.....5  
第二章 欧盟报表.....5  
2.1.纳税申报表（VAT return）.....5  
2.1.1.纳税月报表（Monthly VAT return）.....6  
2.1.2.欧盟内销售清单（EU sales list）.....6  
2.1.3.年纳税报表（Annual VAT return）.....6  
2.2.欧盟内统计报告（Intrastat）.....6  
2.2.1 跨境到达统计报告（Receipt）.....7  
2.2.2 跨境发出统计报告（Dispatch）.....7  
第三章 初始准备.....7  
3.1 基本数据.....7  
3.1.1.运输方式.....7  
3.1.2.贸易术语.....8  
3.1.3.海关商品编码.....8  
3.2 增值税设置.....9  
3.2.1 增值税科目设置.....9  
3.2.2 组号匹配关系设置.....9  
3.2.3 检验规则设置.....10  
第四章 操作指南.....10  
附录.....11

## 导读

此手册面向实施顾问以及企业关键用户，旨在为实施规划、解决方案制定和落实提供指导。手册围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，提供客户业务需求如何与产品功能相匹配的思路。

本手册包括四大部分，第一部分是对产品的概要介绍；第二部分是对欧盟报表的产品功能进行介绍；第三部分介绍了欧盟报表使用前的初始准备设置；第四部分列举了关于欧盟报表的功能点的重要操作，此部分未就详细条目展开，详情可查阅产品相关模块的在线帮助说明。

此外，为了便于用户对整体内容加深理解，手册中对一些关键的名词进行了解释。

## 名词解释

## EU

即：欧盟，政治和关税联盟，目前包括27个成员国。

## 增值税（VAT）

增值税是对销售货物或者提供加工、修理修配劳务以及进口货物的单位和个人就其实现的增值额征收的一个税种。由消费者支付，但却在生产和分配链的每个阶段征收，增值税由国家税务局负责征收。进项税可以抵销项税；增值税是对每个增值环节的征税。最终客户所支付的增值税是所有环节支付的增值税的和。

## 税类

## 报税国家

是针对供应商、客户、物料等基础数据指定的税务分类。

是制定税收政策和收取税金、进行出口退税的国家。销项税抵扣进项税在同一报税国家的范围内进行。

税码（tax code）

是软件系统中的概念，基本的作用是用于反映报税国家在不同的条件下，采取的不同的增值税政策，通过税码可以取得税率，并计算税额。税码用于EU时，同时作为税务报表的统计维度。

### VAT 注册码（VAT registration No.）

EU 内，应税人从税务机关所取得的注册码，采用该注册码可以进行报税。

## 计税金额组（tax base grouping）

在 EU 内进行报税时，会将相应税码的计税金额汇总在某个组（box）中以便进行报税，这个组就是计税金额组。

## 税金组（tax amount grouping）

在 EU 内进行报税时，会将相应税码的税金汇总在某个组（box）中以便进行报税，这个组就是税金组。

## 第一章 概述

欧盟报表，主要用于 EU 内的企业在 EU 的成员国向相关机构进行报税，主要包括两部分内容：纳税申报表（VAT return）、欧盟内统计报告（Intrastat）。

欧盟报表是 EU 企业必须的法定报表（legal report）。

## 第二章 欧盟报表

#### 2.1. 纳税申报表（VAT return）

纳税申报表是从 NC 总账系统中汇总总账凭证的数据得到的，见下图。

<div style="text-align: center;"><img src="imgs/img_in_image_box_286_753_962_1164.jpg" alt="Image" width="56%" /></div>


<div style="text-align: center;">图 2.1-01 纳税申报表从总账系统取数</div>


应付单、应收单等单据传递到总账生成总账凭证时，携带了报税国、发货国、收货国、交易代码、客户 VAT 注册码、税码、计税金额等辅助核算信息。NC 的会计平台支持这些固定的辅助核算项。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_159_1076_393.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 2.1-02 转换模板</div>


##### 2.1.1. 纳税月报表（Monthly VAT return）

纳税月报表的报告周期，支持按月、季度进行纳税额申报。

纳税月报表有两个功能节点：纳税月报表导出、纳税月报表查询。纳税月报表导出，可以将某个报税周期中系统生成的报告导出生成 XML 文件，以便传给税务机关。纳税月报表查询，则可以对多个报税周期中生成的报告进行查询。

##### 2.1.2. 欧盟内销售清单（EU sales list）

欧盟内销售清单主要对客户中具有 VAT registration No.的这类客户的跨 EU 成员国销售业务进行统计，同时可以对商品（Goods）、服务（Service）、三角贸易（Triangular Tread）的交易性质进行统计。

欧盟内销售清单的报告周期，支持按月、季度、年度进行报告。

欧盟内销售清单，可以将某个报税周期中系统生成的报告导出生成 XML 文件，以便传送给相应的机构。

##### 2.1.3. 年纳税报表 (Annual VAT return)

年纳税报表的报告周期为年。

年纳税报表有两个功能节点：年纳税报表导出、年纳税报表查询。年纳税报表导出，可以将某个报税年度生成的报告导出生成 XML 文件，以便传给税务机关。年纳税报表查询，则可以对多个报税年度生成的报告进行查询。

#### 2.2. 欧盟内统计报告（Intrastat）

EU 的企业在 EU 成员国内进行贸易时，按法律规定必须定期向当地政府机关提交 Intrastat。根据商品的流入、流出方向，Intrastat 包括：流入（Receipt）、流出（Dispatch）两类统计报表。

#### 2.2.1 跨境到达统计报告（Receipt）

跨境到达统计报告反映的是货物从 EU 其他成员国到达本国的贸易情况。

当统计依据是 “入库” 时，系统可以从采购入库单、调拨入库单、集采分收采购入库单形成的待结算清单取数；当统计依据是 “发票” 时，系统可以从库存调拨的结算清单、采购发票、集采分收采购入库单形成的结算清单上获取数据。

生成的统计报告可以通过按钮“输出 SDF”，生成满足 EU 法定格式的 SDF 文件。

#### 2.2.2 跨境发出统计报告（Dispatch）

跨境发出统计报告反映的是货物从本国发到 EU 其他成员国的贸易情况。

当统计依据是 “出库” 时，系统可以从销售出库单、调拨出库单、跨公司销售出库单形成的待结算清单取数；当统计依据是 “发票” 时，系统可以从库存调拨的结算清单、销售发票、跨公司销售出库单形成的结算清单上获取数据。

生成的统计报告可以通过按钮 “输出 SDF”，生成满足 EU 法定格式的 SDF 文件。

## 第三章 初始准备

### 3.1 基本数据

##### 3.1.1. 运输方式

在欧盟报表模块中，运输方式主要用在 Intrastat 中。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>运输方式</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>新增</td><td style='text-align: center; word-wrap: break-word;'>修改</td><td style='text-align: center; word-wrap: break-word;'>删除</td><td style='text-align: center; word-wrap: break-word;'>刷新</td><td style='text-align: center; word-wrap: break-word;'>打印</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td colspan="2">运输方式编码</td><td style='text-align: center; word-wrap: break-word;'>运输方式名称</td><td style='text-align: center; word-wrap: break-word;'>创建人</td><td style='text-align: center; word-wrap: break-word;'>创建时间</td><td style='text-align: center; word-wrap: break-word;'>最后修改人</td><td style='text-align: center; word-wrap: break-word;'>最后修改时间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>铁路运输</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2012-10-15 09:...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>公路运输</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2012-10-15 09:...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>航空运输</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2012-10-15 09:...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">图 3.1-01 运输方式</div>

##### 3.1.2. 贸易术语

贸易术语（Incoterm）又称贸易条件、价格术语（Price Terms），用以说明进出口业务中价格的构成及买卖双方有关费用、风险和责任的划分，以确定买卖双方在交货和接货过程中应尽的义务。

在欧盟报表模块中，贸易术语主要用在 Intrastat 中。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能导航</td><td style='text-align: center; word-wrap: break-word;'>消息中心</td><td style='text-align: center; word-wrap: break-word;'>贸易术语</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>新增</td><td style='text-align: center; word-wrap: break-word;'>修改</td><td style='text-align: center; word-wrap: break-word;'>删除</td><td style='text-align: center; word-wrap: break-word;'>查询</td><td style='text-align: center; word-wrap: break-word;'>刷新</td><td style='text-align: center; word-wrap: break-word;'>打印</td></tr><tr><td colspan="2">代码</td><td colspan="4">贸易术语</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>EXW</td><td colspan="4">卖方工厂交货ExWorks</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>FCA</td><td colspan="4">货交承运人FreeCarrier</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>FAS</td><td colspan="4">指定装运港船边交货Free alongsideship</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>FOB</td><td colspan="4">指定装运港船上交货（fob价一般就是EXW加上装船以前费用）F...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>CFR</td><td colspan="4">成本加运费Cost and freight(C&amp;F)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>CIF</td><td colspan="4">成本加运费保险费Cost,insurance and freight</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>CPT</td><td colspan="4">运费付至Carriagepaidtoagreedestination</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>CIP</td><td colspan="4">运费、保险费付至Carriageandinsurancepaidtoagreed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>DAF</td><td colspan="4">边境交货Deliveredatfrontier</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>DES</td><td colspan="4">目的港船上交货Deliveredexship</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>DEQ</td><td colspan="4">目的港码头交货Deliveredexquay</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>DDU</td><td colspan="4">未完税交货Delivereddutyunpaid</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>DDP</td><td colspan="4">完税后交货Delivereddutypaid</td></tr></table>

<div style="text-align: center;">图 3.1-02 贸易术语</div>


##### 3.1.3. 海关商品编码

海关商品编码（HS code）是在进出口贸易中使用的对商品进行分类管理、表示进出口商品名称的数字化代码。海关商品编码广泛应用于进出口报关、出口退税、出口企业的业务处理等领域。在商品进行进出口交易的过程中必须有8位的海关商品编码。按照外贸规定一些海关商品编码中必须具有辅助计量单位，当海关商品编码中不带有辅助计量单位时，在报表中的净重按照kg来计算，如果海关商品编码中带有辅助计量单位，则净重是可选显示的，但是必须显示辅助计量。如下是2012年HS code中的一个例子：

海关编码 海关商品名称 法定单位

40011000 天然胶乳 千克

NC 中，一个商品对应哪个海关商品编码是在物料档案中进行定义的，请参考《NCV6.33 产品手册—基础数据》

在欧盟报表模块中，海关商品编码主要应用在 Intrastat 中。

<div style="text-align: center;"><img src="imgs/img_in_image_box_109_206_1034_362.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 3.1-03 海关商品编码</div>


### 3.2 增值税设置

#### 3.2.1 增值税科目设置

增值税科目设置，用于设置进项税、销项税与会计科目表中科目的对应关系，以便从总账中按会计科目取数进行进项税、销项税的报税。

<div style="text-align: center;"><img src="imgs/img_in_image_box_253_765_937_1071.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">图 3.2-01 增值税科目设置</div>


#### 3.2.2 组号匹配关系设置

在 EU 国家进行报税时，会按照计税金额组、税金组进行汇总报税。

组号匹配关系用来设置某个税码的计税金额、税金应该汇总在哪个计税金额组、税金组中。

<div style="text-align: center;"><img src="imgs/img_in_image_box_301_154_891_506.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 3.2-02 组号匹配关系设置</div>


#### 3.2.3 检验规则设置

在 EU 内向税务机关进行报税时，为了保证报税的准确性，税务机关会规定不同计税金额组、或税金组之间的数据存在相应的逻辑关系。比如：税金组 2 的值+税金组 6 的值，不能超过税金组 7 的值。

检验规则设置，用于设置不同计税金额组、或税金组之间的数据检验关系。

<div style="text-align: center;"><img src="imgs/img_in_image_box_205_817_987_1103.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 3.2-03 检验规则设置</div>


## 第四章 操作指南

本手册具体详细操作应用，请登录 NC 系统参见相关产品帮助。

## 附录

本文参见其他手册清单。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>资料目录</td><td style='text-align: center; word-wrap: break-word;'>相关学习点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册-基础数据》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《产品手册-增值税》</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_491_440_698_593.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">大型企业管理与电子商务平台</div>


# Large-scale Enterprise Management and E-business Solution Platform
