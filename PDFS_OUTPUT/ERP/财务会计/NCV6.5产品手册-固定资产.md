# NCV6.5产品手册-固定资产

<div style="text-align: center;"><img src="imgs/img_in_image_box_200_471_386_568.jpg" alt="Image" width="15%" /></div>


产品手册- V6.5

固定资产管理

## 版权

## © 用友集团版权所有

未经用友集团的书面许可，本操作手册任何整体或部分的内容不得被复制、复印、翻译或缩减以用于任何目的。本操作手册的内容在未经通知的情形下可能会发生改变，敬请留意。请注意：本操作手册的内容并不代表用友软件所做的承诺。

## 目录

版权 ..... 2  
名词解释 ..... 6  
第一章 概述 ..... 7  
1.1 产品概述 ..... 7  
1.2 产品价值 ..... 8  
第二章 应用场景 ..... 10  
2.1 资产新增 ..... 10  
2.1.1 采购新增 ..... 10  
2.1.2 设备转固 ..... 13  
2.1.3 盘盈新增 ..... 15  
2.1.4 工程转固 ..... 17  
2.1.5 申请审批新增 ..... 20  
2.1.6 手工新增 ..... 21  
2.2 资产变动 ..... 22  
2.2.1 价值调整 ..... 23  
2.2.2 资产追溯调整 ..... 24  
2.2.3 设备联动调整 ..... 26  
2.2.4 其他变动 ..... 28  
2.3 资产调拨 ..... 33  
2.3.1 业务描述 ..... 33  
2.3.2 业务流程 ..... 34  
2.3.3 功能清单 ..... 34  
2.3.4 解决方案 ..... 34  
2.4 资产维护 ..... 37  
2.4.1 资产评估 ..... 37  
2.4.2 资产减值 ..... 38  
2.4.3 资产拆分 ..... 39  
2.4.4 资产合并 ..... 41  
2.4.5 资产减少 ..... 42  
2.5 资产盘点 ..... 45  
2.5.1 业务描述 ..... 45  
2.5.2 业务流程 ..... 46  
2.5.3 功能清单 ..... 47  
2.5.4 解决方案 ..... 47  
2.6 折旧与摊销 ..... 49  
2.6.1 单组织计提摊销 ..... 49  
2.6.2 多组织计提摊销 ..... 53  
2.6.3 跨组织计提摊销 ..... 54  
2.6.4 多部门计提摊销 ..... 58  
2.6.5 按日计算折旧 ..... 61  
2.7 月末结账 ..... 65

2.7.1 业务描述 ..... 65  
2.7.2 业务流程 ..... 66  
2.7.3 功能清单 ..... 66  
2.7.4 解决方案 ..... 66  
2.8 固定资产对账 ..... 66  
2.8.1 业务描述 ..... 66  
2.8.2 业务流程 ..... 67  
2.8.3 功能清单 ..... 67  
2.8.4 解决方案 ..... 67  
2.9 模拟折旧 ..... 69  
2.9.1 业务描述 ..... 69  
2.9.2 业务流程 ..... 69  
2.9.3 功能清单 ..... 70  
2.9.4 解决方案 ..... 70  
2.10 固定资产多账簿 ..... 71  
2.10.1 业务描述 ..... 71  
2.10.2 应用模型 ..... 71  
2.10.3 功能清单 ..... 72  
2.10.4 解决方案 ..... 73  
第三章 初始准备 ..... 77  
3.1 管控模式 ..... 77  
3.2 动态建模平台 ..... 78  
3.2.1 组织管理 ..... 78  
3.2.2 权限管理 ..... 79  
3.2.3 基础数据维护 ..... 80  
3.2.4 流程配置 ..... 80  
3.2.5 系统平台设置 ..... 82  
3.3 固定资产模块初始化 ..... 83  
3.3.1 基础设置 ..... 83  
3.3.2 期初数据准备 ..... 86  
3.4 多账簿设置 ..... 87  
第四章 操作指南 ..... 89  
附录 ..... 89  
附录 1：单据流转 ..... 89  
附录 2：控制点 ..... 91  
附录 3：查询报表 ..... 92  
附录 4：本文参见其他手册清单 ..... 94

## 导读

此手册面向实施顾问以及企业关键用户，主要目的是为实施规划、解决方案制定和落实提供指导。手册主要围绕产品能够解决的主要业务场景展开，并以此为依托展现产品的关键应用功能，帮助用户建立业务需求与产品解决方案的匹配思路。

本手册主要包括四大部分，第一部分是对产品及其价值的概要介绍；第二部分是对有关固定资产管理的主要业务场景、流程、以及对应的产品功能的介绍；第三部分是关于产品实现的初始准备设置；第四部分是关于产品的功能点的具体操作，此部分并不在手册中描述，具体请参见产品帮助。此外，为了便于用户对整体内容理解，手册中对一些关键的名词进行了解释，并在附录中列示了单据流转、控制点、查询报表，以便用户查找对照。

最后，结合本手册，用户可通过以下资料，针对性地深入了解特定板块的产品应用：

1. 《组织管理手册》。深入阐述了产品关键概念（如集团、组织、业务委托关系等）以及建模思路，是实施规划、蓝图设计的重要参考资料。

2. 产品帮助。针对具体功能点的关键字段、按钮操作进行详细解释，并提供关键应用示例。

3. 《流程管理手册》。提供关于交易类型、流程设计工具的应用指导。

4. 《基础数据手册》。可对手册第三部分（即初始准备设置）中的有关基础数据的理解和应用进行更详细深入地了解。

## 名词解释

## 在建工程

在建工程，指企业固定资产的新建、改建、扩建，或技术改造、设备更新和大修工程等尚未完工的工程支出。例如：正在建设中的宿舍楼、正在安装调试大型设备。

## 第一章 概述

### 1.1 产品概述

NC 固定资产管理模块实现对固定资产从新增到报废整个生命过程的价值进行跟踪管理，其不仅仅关注固定资产的价值管理，同时也实现对无形资产、递延资产的管理。实现了对最新的会计准则进行了全面支持与适配，既支持包括固定资产建卡、变动、减值、评估、拆分合并、折旧与摊销、盘点、减少等日常业务应用，也支持包括资产追溯调整、资产组减值、模拟折旧等高级业务应用。

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_530_1027_1339.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 1.1-01 模块功能结构图</div>


固定资产管理是 NC 资产管理解决方案的核心模块之一，与资产实物管理一起实现对企业资产的价值与实物两个生命周期的全面跟踪与管控，帮助企业提高资产利用率，降低资产维护运营成本，并对资产投资、配置决策提供详尽的数据支持。

<div style="text-align: center;"><img src="imgs/img_in_image_box_176_166_1040_1128.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 1.1-02 资产领域功能结构图</div>


### 1.2 产品价值

1. 支持多组织应用，强化集团管控能力；

➢ 支持多组织查询，统一结账

➢ 支持多组织统一计提折旧

➢ 满足集团对下级公司管理要求

➢ 支持资产跨组织管理、核算

### 2. 支持固定资产多账簿；

为不同账簿中不同资产提供多种核算方式

➢ 满足一个集团内不同财务、税法核算要求

➢ 支持多账簿模拟折旧

### 3. 高度集成性、良好开放性；

与总账无缝集成，保证数据准确一致

➢ 支持国家颁发的会计准则接口

实现与财政部资产清查软件对接

实现与国资委资产管理软件对接

### 4. 支持预算控制，监督资产配置计划贯彻执行；

实现新增资产审批受全面预算控制

## 第二章 应用场景

### 2.1 资产新增

新增固定资产是指企业通过采购、调拨、投资、工程转固、盘点盘盈等方式，实现固定资产的增加。鉴于固定资产新增的方式以及管理方式的不同，可以细分为如下子场景：

➢ 采购新增

➢ 设备转固

➢ 盘盈新增

➢ 工程转固

➢ 申请审批新增

➢ 手工新增

以上各子业务场景详细业务过程描述，详见如下内容。

#### 2.1.1 采购新增

##### 2.1.1.1 业务描述

采购新增即企业通过采购直接进行固定资产的卡片建立和入账，此场景适用于不需要进行设备实物管理的周转材料，例如：建筑、采矿行业的租赁类周转材料。此业务场景包括3个解决方案：

解决方案 1：在采购到货环节，通过采购到货单推式生成『采购转固单』，用于解决不进行库存管理的周转材料类固定资产的采购建卡。

解决方案 2：在采购入库环节，通过采购入库单推式生成『采购转固单』，用于解决进行库存管理的周转材料类固定资产的采购建卡。

解决方案 3：在采购到货、采购入库环节都不推式生成『采购转固单』，而是采购入库后，将资产调拨至该库存组织的其他仓库或者其他库存组织的仓库，再通过『调拨入库单』推式生成『采购转固单』，此解决方案主要解决资产集中管理的业务场景，例如：某集团下属所有组织的资产采购，全部由集团总部采购组织完成，并入库到集团库存组织，然后通过调拨的方式，把资产分别调拨到资产使用组织的本地库存组织或者仓库。

这 3 个解决方案在产品实现中为互斥流程, 即如果通过方案 1 在采购货单环节推式生成『采购转固单』, 则不能通过方案 2 在采购入库环节推式生成『采购转固单』, 也不能通过调拨入库单推式生成『采购转固单』, 反之亦然。详细业务流程如下所示。

##### 2.1.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_261_236_912_1009.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 2.1-01 采购新增固定资产流程</div>


##### 2.1.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="5">供应链</td><td rowspan="3">采购管理</td><td style='text-align: center; word-wrap: break-word;'>请购单维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>采购订单维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>到货单维护</td></tr><tr><td rowspan="2">库存管理</td><td style='text-align: center; word-wrap: break-word;'>采购入库</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调拨入库</td></tr><tr><td rowspan="2">财务会计</td><td rowspan="2">固定资产管理</td><td style='text-align: center; word-wrap: break-word;'>采购转固单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr></table>

##### 2.1.1.4 解决方案

关于此场景涉及的资产采购过程相关功能节点的细节，请参见供应链采购管理产品手册或者参见产品帮助。以下将主要介绍资产收货过程以及建卡过程涉及到的主要功能点：

### 1. 资产到货

在供应链的【采购管理】→【到货单】→【到货单维护】功能节点，完成资产到货的登记以及相关检验业务，采购到货单签字后，通过辅助功能中的“生成转固单”功能，推式生成固定资产『采购转固单』，此“转固单”可以在【固定资产】→【新增资产】→【采购转固单】功能节点进行查询、审批，一旦『采购到货单』生成『采购转固单』，此单据则不能被参照生成采购入库单，也就是说采购到货的固定资产不能继续入库了。

### 2. 资产入库

如果采购的资产没有通过『采购到货单』生成『采购转固单』单，则可以在【库存管理】→【入库业务】→【采购入库】功能节点，通过『采购入库单』推式生成『采购转固单』。生成『采购转固单』的资产前已完成入库操作。

如果资产由其他库存组织或者仓库调拨入库，则可以在【库存管理】→【入库业务】→【采购入库】功能节点，通过『调拨入库单』推式生成『采购转固单』。

### 3. 资产建卡

首先在【财务会计】→【固定资产】→【新增资产】→【采购转固单】功能节点，对『采购到货单』或者『采购入库单』推式生成的『采购转固单』进行审批，然后在【财务会计】→【固定资产】→【新增资产】→【资产增加】节点参照『采购转固单』完成固定资产建卡。

## 注意：

只有价值管理模式为“固定资产”，实物管理模式“周转材料”或者为“空”的物料，才适用此场景。关于价值管理模式与实物管理模式的设置与解释，请参见物料档案的产品帮助。

系统支持业务消息配置功能，供应链推采购转固单时可以给固定资产会计发送消息。

固定资产模块支持业务消息配置的业务包括：

☑ 供应链推式生成采购转固单；

项目管理的产出物交付单推式生成工程转固单；

☑ 固定资产调出推式生成固定资产调入；

☑ 设备建卡和设备变动联动固定资产。

➢ 支持资产按成本中心核算功能，在录入卡片时，可选择录入成本中心字段。

#### 2.1.2 设备转固

##### 2.1.2.1 业务描述

设备转固就是将已经创建设备卡片的资产转为固定资产入账，此场景适用于那些既需要进行固定资产价值核算又需要进行设备实物管理的资产。通常情况下，企业采购的资产到货后，先建立设备卡片进行实物管理，然后再在固定资产入账的时候建立固定资产卡片。

##### 2.1.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_300_561_873_1425.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">图 2.1-02 设备转固定资产流程</div>

##### 2.1.2.3 功能模型


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">资产信息管理</td><td style='text-align: center; word-wrap: break-word;'>设备卡片</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产生成设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>固定资产管理</td><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr></table>

##### 2.1.2.4 解决方案

### 1. 设备建卡

用户通过采购、调拨、租赁等方式获取设备，在系统【资产管理】→【资产信息管理】→【设备卡片】功能节点建立设备卡片，关于建立设备卡片的详细场景请参见《资产信息管理产品手册》相关章节。

➢ 已经建立设备卡片的资产，如果转为固定资产可通过【资产管理】→【资产信息管理】→【资产生成设置】功能节点，设置为可以生成固定资产，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_247_763_1057_1110.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 2.1-03 资产生产设置</div>


上图中红框内标识，默认状态由卡片对应的设备类别决定，如果设备类别中勾选了此复选框，那么在创建对应设备类别的卡片时，此复选标识自动勾选，如果设备类别中未设置该类设需要固定资产核算，可以通过上述方式进行手工更改，再生成固定资产卡片 s 进行核算。

### 2. 资产建卡

在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，选择【新建-设备卡片】功能按钮，参照设备卡片完成固定资产卡片的生成。

## 注意：

如果希望将设备安装调试费用也转为固定资产原值进行入账，则需要在【财务会计】→【固定资产】→【基础设置】→【账簿信息】功能节点，设置固定资产本币原值的来源=原币原值+安装调试费，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_374_325_932_744.jpg" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 2.1-04 本币原值来源</div>


设备卡片能否生成固定资产，取决于设备类别属性中的定义，是否固定资产，设置为是，即可生成固定资产卡片，设置为否，则不生成固定资产卡片：也可以通过【资产管理】→【资产信息管理】→【资产生成设置】功能节点，修改该设备是否可生成固定资产。

#### 2.1.3 盘盈新增

##### 2.1.3.1 业务描述

盘盈新增主要用来解决将盘点盘盈的固定资产进行建卡入账。当企业进行大批量同类固定资产采购的过程中，或者由于管理漏洞，造成少量固定资产已经投入使用，但却没有及时进行建卡入账，在盘点过程中发现此问题，可以采用此解决方案完成固定资产的建卡入账。

##### 2.1.3.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_329_249_856_1091.jpg" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 2.1-05 盘盈新增固定资产流程</div>


##### 2.1.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">资产管理</td><td rowspan="3">固定资产管理</td><td style='text-align: center; word-wrap: break-word;'>资产盘点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>盘盈资产</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr></table>

##### 2.1.3.4 解决方案

### 1. 资产盘点

首先在【财务会计】→【固定资产】→【资产盘点管理】→【资产盘点】功能节点完成盘点数据采集，提交审批资产盘点单后，系统自动生成『盘盈资产单』。

然后在【财务会计】→【固定资产】→【资产盘点管理】→【资产盘点】功能节点完成『盘盈资产单』审批。

### 2. 资产建卡

在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，选择【新建-盘盈资产】功能按钮，参照『盘盈资产单』完成固定资产卡片的生成。

## 注意：

此场景提及的“盘点”是指固定资产盘点，而非资产实物盘点。资产实物盘点的盘盈设备需要首先建立设备卡片，再由设备卡片转为固定资产。

#### 2.1.4 工程转固

##### 2.1.4.1 业务描述

工程转固是指将企业的在建工程项目或项目成本，进行资本化的过程。

解决方案 1：将项目产出物进行转固，通过项目产出物交付将项目进行转固处理。例如：企业建造一座职工宿舍楼，在建设过程中该宿舍楼则属于在建工程，当宿舍楼完工交付使用的时候，企业则要将其转为固定资产进行管理。

解决方案 2：在项目为完成交付之前，按项目成本进行转固，此场景可分为两种转固方式。分别是场景 1：项目成本直接转固；场景 2：项目成本预转固再进行决算转固并调整资产价值。

##### 2.1.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_237_980_1382.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">图 2.1-06 工程转固流程</div>

##### 2.1.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">管理会计</td><td rowspan="2">项目成本会计</td><td style='text-align: center; word-wrap: break-word;'>成本预转固</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目成本财务决算</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目管理</td><td style='text-align: center; word-wrap: break-word;'>决算及转固</td><td style='text-align: center; word-wrap: break-word;'>产出物交付单</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产管理</td><td style='text-align: center; word-wrap: break-word;'>工程转固单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr></table>

##### 2.1.4.4 解决方案

### 1. 项目产出物交付

在【项目管理】→【决算及转固】→【工程转固】→【产出物交付单】功能节点，完成『产出物交付单』的创建及审批。『产出物交付单』的表体数据的交付方式为“建固定资产卡片”。

### 2. 项目成本转固

1）如果将项目成本按照估计价值确定其成本进行预转固，在项目进行成本决算时调整由项目成本预转固生成的资产原值。在【管理会计】→【项目成本会计】→【成本结转】→【成本预转固】功能节点，对项目成本进行预转固并生成【工程转固单】。当项目决算时，将决算与预转固的价值差额通过资产价值调整来调整固定资产原值。

2）如果项目没有进行预转固处理而直接办理竣工决算，将实际成本转固，生成相应的『工程转固单』。在【管理会计】→【项目成本会计】→【项目财务决算】→【项目成本财务决算】功能节点，对项目成本进行预转固并生成『工程转固单』。

### 3. 工程转固

1）在【财务会计】→【固定资产】→【新增资产】→【工程转固】功能节点，查询由『项目产出物交付单』、『成本转固单』、『成本转固单』生成的『工程转固单』，并进行审批。

2) 如果用户没有启用项目管理产品，则需要在【财务会计】→【固定资产】→【新增资产】→【工程转固】功能节点完整『工程转固单』的创建及审批。『工程转固单』的表体行数据参照项目档案，项目档案在【动态建模平台】→【基础数据】→【项目信息】功能节点维护。

### 4. 资产建卡

在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，选择【新建-工程转固】功能按钮，参照【工程转固单】完成固定资产卡片的生成。对于项目成本预转固的资产进行项目成本决算时可对资产卡片进行原值进行调整。

#### 2.1.5 申请审批新增

##### 2.1.5.1 业务描述

申请审批新增是指通过“资产申请→审批”的方式新增固定资产，此业务场景适用于解决此业务需求。此场景中的『新增资产审批单』可受预算模块控制，控制点包括申请资产数量和申请金额。

##### 2.1.5.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_265_540_907_1377.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 2.1-07 审批新增固定资产流程</div>

##### 2.1.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产管理</td><td style='text-align: center; word-wrap: break-word;'>新增资产审批单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr></table>

##### 2.1.5.4 解决方案

### 1. 新增资产审批

在【财务会计】→【固定资产】→【新增资产】→【新增资产审批单】功能节点完成『新增资产审批单』的创建及审批。如果启用了全面预算模块，同时在全面预算模块需要对固定资产新增进行了控制，那么在单据审批的时候，系统会检查预算控制条件是否满足，如果不满足控制条件不允许通过审批。预算模块可以对申请资产的数量和金额进行控制，关于预算控制相关细节参见帮助系统。

### 2. 资产建卡

在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，选择【新建-新增资产审批单】功能按钮，参照【新增资产审批单】完成固定资产卡片的生成。此过程受参数 FA81 控制，如果启用该参数，当资产的入账价值大于【新增资产审批单】上资产价值的时候则不允许通过审批。

#### 2.1.6 手工新增

##### 2.1.6.1 业务描述

手工新增即不参照任何上游业务单据，直接创建资产卡片。此场景适用于用户没有启用出固定资产之外的其他模块，即资产的采购、安装调试等过程都在 ERP 系统之外完成的情况。

##### 2.1.6.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_344_248_833_718.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 2.1-08 手工新增固定资产流程</div>


##### 2.1.6.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr></table>

##### 2.1.6.4 解决方案

在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，选择【新建-自制】功能按钮，完成固定资产卡片的创建。

### 2.2 资产变动

资产变动是固定资产使用、维护、管理过程中的重要业务，资产的变动会对固定资产的折旧分摊造成直接的影响，所以为了保证变动严肃性，NC系统记录资产变动的过程，做到有痕迹变动，使用户对变动业务进行跟踪、监控。资产变动业务可以细分为如下几个子场景：

价值调整

➢ 资产追溯调整

➢ 设备联动调整

## 其他变动

详细场景描述，参见下文。

#### 2.2.1 价值调整

##### 2.2.1.1 业务描述

价值调整是是指固定资产原值调整，包括对设备技术改造或者维修过程中，发生的维修费用的资本化，以及项目产出物价值调整。设备技术改造（原工单资本化）的条件受参数 EWMG02 控制，用户可以通过设置此参数控制维修费用占设备原值的比例数量，只有维修费用占设备原值大或等于该比例时才可以进行维修费用的资本化。

##### 2.2.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_710_885_1381.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.2-01 价值调整流程</div>

##### 2.2.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>价值调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>维修管理</td><td style='text-align: center; word-wrap: break-word;'>工单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目管理</td><td style='text-align: center; word-wrap: break-word;'>项目过程管理</td><td style='text-align: center; word-wrap: break-word;'>产出物价值调整单</td></tr></table>

##### 2.2.1.4 解决方案

### 1. 资产维修

在【资产管理】→【维修管理】→【工单】→【工单】功能节点完成设备维修过程记录，当工单处于完成或已报告状态时，可以通过功能菜单界面的“辅助功能”的【资本化】功能按钮实现工单的资本化，通过【取消资本化】按钮撤销资本化，但必须先删除已经保存的「价值调整单」单据，如果单据已经审批则需要撤销审批再删除单据。

### 2. 项目产出物价值调整

在【项目管理】→【项目过程管理】→【项目产出物管理】→【产出物价值调整单】功能节点，完成产出物价值调整。

### 3. 价值调整

一旦工单进行了资本化操作，或项目产出物进行价值调整操作，系统会自动发送工作任务消息给指定角色或者操作员，在消息中心双击该消息，系统弹出选择框，让操作员选择是“价值调整”还是“追溯调整”，选择价值调整，会弹出【价值调整单】界面，完成对该单据进行保存。然后在【财务会计】→【固定资产】→【资产变动】→【价值调整】功能节点，对已经保存的『价值调整单』单据进行审批。选择追溯调整，会弹出【追溯调整单】界面，完成对该单据进行保存。然后在【财务会计】→【固定资产】→【资产变动】→【追溯调整】功能节点，对已经保存的『价值调整单』单据进行审批。

#### 2.2.2 资产追溯调整

##### 2.2.2.1 业务描述

资产追溯是指对前期损益的调整，应追溯调整前期相关可比资料并予以重新表述，会计政策变更要假设变更后的新会计政策，已应用于全部相关的会计期间，新会计政策已从相关项目的初始日开始应用，追溯计算会计政策变更所产生的累积影响损益数，调整本期期初留存收益，并对相关期间可比资料重新表述。

对于前期错误应视为在该项错误发生的当期就已更正，相关的更正金额列入该期净损益，追溯调整前期已列报的相关期间的可比资料，调整本期期初留存收益。

系统支持与项目管理进行集成，支持通过价值预估实现资本化的资产，进行价值变动追溯。由项目产出物价值调整业务，直接实现对资产价值的追溯调整。

##### 2.2.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_335_446_879_1030.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">图 2.2-02 固定资产追溯调整流程</div>


##### 2.2.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目管理</td><td style='text-align: center; word-wrap: break-word;'>项目过程管理</td><td style='text-align: center; word-wrap: break-word;'>产出物价值调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产追溯调整</td></tr></table>

##### 2.2.2.4 解决方案

在【财务会计】→【固定资产】→【资产变动】→【资产追溯调整】功能节点完成资产追溯业务。

#### 2.2.3 设备联动调整

##### 2.2.3.1 业务描述

设备联动调整是指，当企业同时启用固定资产、资产实物管理模块时，由资产实物管理相关业务（例如：资产领用、资产借用、资产调拨）触发的固定资产的变动业务。例如：资产借用会发生资产使用人的变化，借用的设备为固定资产的时候，系统则会自动触发固定资产卡片使用人的变动。所有设备联动变化单据全部由相关资产实物管理业务触发。

##### 2.2.3.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_218_617_953_1458.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 2.2-03 设备联动调整流程</div>

##### 2.2.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="12">资产管理</td><td rowspan="11">资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产借用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>借用归还</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产领用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>领用归还</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>管理部门变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用部门变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>责任人变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>位置变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用权调拨</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>盘点差异调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>设备联动调整</td></tr></table>

##### 2.2.3.4 解决方案

### 1. 设备管理

在资产使用管理模块的如下功能节点完成实物管理业务，在业务单据审批后，系统自动推出系统任务消息。

【资产借用】

【借用归还】

【资产领用】

【领用归还】

【管理部门变动】

【使用部门变动】

【责任人变动】

【位置变动】

【项目变动】

【使用权调拨】

【盘点差异调整】

### 2. 设备联动调整

在系统消息中心打开资产变动任务消息直接关联到『设备联动调整单』编辑界面，保存后即完成设备联动调整，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_186_288_989_769.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 2.2-04 设备联动调整</div>


【财务会计】→【固定资产】→【资产变动】→【设备联动调整】功能节点，查询由资产实物管理业务推式生成的『设备联动调整单』，如果不希望影响固定资产变动，可以撤销审批并删除『设备联动调整单』单据。

#### 2.2.4 其他变动

##### 2.2.4.1 业务描述

除了上述的资产变动外，NC系统支持其他资产属性的变动业务，可分为两大类，一类为直接影响资产折旧摊销数额的变动，例如：本币原值变动、折旧方法变动、累计折旧变动、净残值（率）变动等；另外一类则为影响折旧计提费用归集汇总的变动，例如：折旧承担部门变动、资产使用部门变动、资产类别变动等等。

此外，除了系统 NC 系统现在已经明确列出 22 种常用资产变动外，用户还可以通过增加交易类型，配置变动单的单据模版，实现对固定资产其他维度的变动。

##### 2.2.4.2 业务流程

无

##### 2.2.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="20">资产管理</td><td rowspan="20">固定资产</td><td style='text-align: center; word-wrap: break-word;'>原币原值变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本币原值变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>购买价款调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计折旧调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>净残值（率）调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数量调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧方法调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用月限调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用状况调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>增加方式调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>管理部门调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用部门调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧承担部门调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用部门调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用人调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产类别调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>类别和管理部门调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>项目档案调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工作总量调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产组调整</td></tr></table>

##### 2.2.4.4 解决方案

所有上表列出资产变动业务，系统全部通过单独的功能节点实现，对于超出系统默认提供的 22 中资产变动业务之外的其他用户自定义变动业务，也可以通过 UAP 平台配置，发布为单独的资产变动功能节点，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_468_176_727_531.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 2.2-05 新增资产变动功能节点</div>


## ■ 如何自定义变动业务，并发布为节点呢？

## 第一步：分析变动业务特点，抽取变动内容

系统已经预置了 22 种常用的资产变动业务，基本可以覆盖绝大多数企业的资产变动场景，在新增自定义变动之前必须确认与预置的资产变动没有重复，即资产变动项没有在预置变动中覆盖。

## 第二步：为变动单增加新的交易类型

在【动态建模平台】→【流程管理】→【交易类型管理】功能节点，新增变动单交易类型，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_263_902_1004_1390.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.2-06 增加交易类型</div>


## 第三步：发布新增交易类型为功能节点

在【动态建模平台】→【流程管理】→【交易类型管理】功能节点，将第二步新增的交易类

型发布为功能节点，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_196_965_603.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.2-07 发布功能节点</div>


## 第四步：为新发布的功能节点配置单据模板

在【动态建模平台】→【客户化配置】→【模板管理】→【模板配置】功能节点，为新发布的功能节点配置单据模板，默认情况新发布的功能节点会继承“项目档案调整”的默认模板，如下图所示，用户需要对该单据模板进行修改，关于单据模板配置的详细过程，请参见客户化手册相关章节内容。

<div style="text-align: center;"><img src="imgs/img_in_image_box_206_861_982_1410.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">图 2.2-08 为新节点配置单据模板</div>


单据模板配置完毕后，系统默认所有用户、所有组织都是用该模板，如果用户需要对模板授权给不同的用户角色、组织单元，则需要在【动态建模平台】→【客户化配置】→【模板管理】

→【模板配置】功能节点，新增新的单据模板，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_221_197_961_823.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.2-09 为新节点配置单据模板 2</div>


然后在【动态建模平台】→【客户化配置】→【模板管理】→【模板分配】功能节点，将新增加的单据模板指派给指定组织单元、用户、角色，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_958_961_1483.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.2-10 为新节点配置单据模板 3</div>

## 第五步：测试验证自定义业务

上述 4 步完成后，双击【财务会计】→【固定资产】→【资产变动】→【自定义资产变动】功能节点，完成一次变动业务，验证固定资产卡片是否发生预期的变动。

## 注意：

所有资产变动业务必须在最小未结账月进行。

关于使用部门变动、管理部门变动、折旧承担部门变动、资产类别变动等，涉及到变动前后折旧额归集主体变化的变动业务，折旧归集主体变动时机是可以通过参数控制的。例如：可以控制使用部门变动业务发生后，变动当月的折旧额归属于变动前部门还是变动后部门。关于参数设置的详细内容，请参见【财务会计】→【固定资产】→【基础设置】→【参数设置】功能节点产品帮助。

原币原值变动：原币原值一般指购买固定资产时所用的币种及价值，如果账簿信息中设置了本币原值来源于原币原值，那么当原币原值变动时，会自动联动本币原值变动，但如果本币原值来源设置为非原币原值，或者设置为原币原值+安装调度费用+包装费等其他有计算关系的设置，则原币原值变动不会联动本币原值。

### 2.3 资产调拨

#### 2.3.1 业务描述

资产调拨是指一个集团下不同财务组织之间，进行资产的所有权转移。例如：当某个企业技术改造造成部分生产设备闲置，而集团内其他兄弟企业需要此部分闲置设备，企业集团平衡内部资源则进行固定资产的调拨。需要强调的是，此资产调拨是指资产的所有权发生转移，而不是使用权、使用部门、管理部门转移，非所有权发生的改变可以通过资产变动业务完成。

#### 2.3.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_238_1020_1032.jpg" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 2.3-01 固定资产调拨流程</div>


#### 2.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产调出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产调入</td></tr></table>

#### 2.3.4 解决方案

### 1. 资产调出

在【财务会计】→【固定资产】→【资产调拨】→【资产调出】功能节点，完成固定资产的调出。『资产调出单』审批后，调出组织的固定资产自动减少，系统自动协同生成调入财务组织的『资产调入单』，单据为未审核状态。如果希望调入组织在当月就完成资产调入业务，可以勾选『资产调出单』上的“是否本月确认调入”复选框。这样调入组织必须确认资产调入业务，调出组织才能进行当月的固定资产结账业务。

注意：

资产调出、资产合并和资产拆分对于调出、被合并、被拆分卡片来说是资产减少的一种形式。

### 2. 资产调入

1）在【财务会计】→【固定资产】→【资产调拨】→【资产调入】功能节点，查询由『资产调出单』协同生成的『资产调入单』，审批后完成资产调入。『资产调入单』审批后，系统自动生成调入组织新的固定资产卡片。

2）默认情况下，调入资产的编码、入账价值与调出卡片相同，但可以通过修改参数 BD803 来控制调入资产的入账价值，通过修改参数 FA11 控制调入资产编号是否可修改。

3）默认情况下，调入资产携带原卡片上的自定义项，如果不希望调入资产携带原卡片上的自定义项，可以通过修改参数 FA40 实现。

4) 为了强化资产调拨业务的管控力度，保证企业资产安全，系统支持调出发起者对调入公司系统权限的检查，即资产调出业务发起用户必须具备调入组织的权限，才可以审批资产调拨业务。可以通过修改参数 FA75 实现上述控制，默认情况下系统不做此限制。

### 3. 国际货币结算

集团内总公司与子公司或各子公司之间发生资产调拨，从会计处理上属于视同销售行为。跨国或跨地区集团在发生这类业务时，可能需要通过第三方国际货币作为结算货币。在系统中的实现方式如下：

1） 修改资产调出的模板，将“结算币种”字段改为可编辑（根据需要可以新建交易类型，发布专门的节点处理这类业务）；

<div style="text-align: center;"><img src="imgs/img_in_image_box_237_148_978_547.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.3-02 单据模板</div>


2）用户做按国际货币结算的资产调拨业务时，“结算币种”选择对应的国际货币，系统会自动根据结算币种和本币金额折算出调拨价格；

<div style="text-align: center;"><img src="imgs/img_in_image_box_235_694_980_1098.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.3-03 资产调出修改结算币种</div>


3）结算币种会默认为主账簿的本位币，用户不做修改时，即以本位币调拨，和以前版本的逻辑相同。

4）不同场景下调出、调入资产卡片资产账簿的对应关系：

a） 按第三方国际货币结算，调入卡片主账簿来源于调出卡片主账簿；调入卡片报告账簿通过自身主账簿折算；

b) 按调出公司本位币折算，调入卡片主账簿来源于调出卡片主账簿；调入卡片报告账簿与调出卡片账簿相同的，来源于调出卡片的相同账簿；调入卡片报告账簿与调出卡片账簿没有相同的，通过自身主账簿折算。

### 2.4 资产维护

#### 2.4.1 资产评估

##### 2.4.1.1 业务描述

当企业在上市、兼并、收购、抵押贷款、破产等业务时，通常需要对资产进行评估，即由专门的机构，通过严谨、科学的方法，处于特定的评估目的，对企业资产进行重新估价。资产评估是个复杂的过程，必须由专门的独立的机构完成。NC系统不对资产评估的过程进行跟踪记录，只对评估的结果进行记录。

##### 2.4.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_292_667_889_1222.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 2.4-01 资产评估流程</div>


##### 2.4.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产评估</td></tr></table>

##### 2.4.1.4 解决方案

### 1. 资产评估

通常情况下资产评估需要由专门的评估机构或者团队完成，资产评估过程为 NC 系统外部过程，不在 NC 系统中进行跟踪和记录。

### 2. 资产评估结果登记

在【财务会计】→【固定资产】→【资产维护】→【资产评估】功能节点，将资产评估的结果进行登记、审批。业务单据审批后，系统自动修改固定资产卡片上相关信息，不会生成变动单据，同时生成总账凭证。

#### 2.4.2 资产减值

##### 2.4.2.1 业务描述

当企业外部财务、市场环境发生变化，会给企业的固定资产带来减值风险，即固定资产的现值小于市场公允价值，为了规避这种风险，减少可能为企业带来的不利影响。NC系统不对资产减值测算的过程进行跟踪记录，只对减值测算的结果进行记录。

##### 2.4.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_957_903_1443.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 2.4-02 资产减值流程</div>

##### 2.4.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产减值</td></tr></table>

##### 2.4.2.4 解决方案

### 1. 资产减值

资产减值测算过程为 NC 系统外部过程，不在 NC 系统中进行跟踪和记录。

### 2. 资产减值结果登记

1）在【财务会计】→【固定资产】→【资产维护】→【资产减值】功能节点，将资产减值测算的结果进行登记、审批。业务单据审批后，系统自动修改固定资产卡片上相关信息，不会生成变动单据，同时生成总账凭证。

2）系统不仅支持单个资产减值业务，也支持对资产组的减值业务，关于资产组的设置请参见【财务会计】→【固定资产】→【基础设置】→【资产组】功能节点的帮助。

#### 2.4.3 资产拆分

##### 2.4.3.1 业务描述

资产拆分是指将一个资产拆分为两个或者多个资产的过程。此类业务多发生于企业对大型设备进行拆分改造，拆解改造后的设备分别投入使用。或者企业由于经营管理方式的改变，将原来多个独立资产集合管理的方式，变为拆分独立管理。例如：某企业为了方便管理，将某个办公室的所有个人电脑集中创建一个固定资产卡片管理，由于企业组织结构变化，该办公室拆分为两个部门，因此办公个人电脑也分布到两个部门，为了分别管理两个不同部门的个人电脑，资产会计将原来的固定资产卡片进行拆分，按照最新的部门设置拆分为两个卡片。

##### 2.4.3.2 业务流程

资产拆分流程如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_254_158_959_903.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 2.4-03 资产拆分流程</div>


##### 2.4.3.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产拆分</td></tr></table>

##### 2.4.3.4 解决方案

1. 在【财务会计】→【固定资产】→【资产维护】→【资产拆分】功能节点，完成资产拆分业务处理。资产拆分单审批后，被拆分的资产自动减少，拆分出的新资产自动增加。

2. 如果被拆分的固定资产关联的设备卡片，在被拆分之后，可以将该设备卡片与拆分后资产进行关联，当然拆分后的资产也可以指定其他设备卡片进行关联，关于与卡片关联的详细内容参见设备卡片以及资产拆分功能节点的产品帮助。

#### 2.4.4 资产合并

##### 2.4.4.1 业务描述

资产合并是指把原来独立的 2 个或多个资产，合并为一张固定资产卡片进行管理。例如为了便于核算管理，有些企业选择将某个部门相同配置、型号的个人笔记本电脑，合并作为一张多数量的固定资产卡片进行管理。

##### 2.4.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_246_569_926_1418.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;">图 2.4-04 资产合并流程</div>

##### 2.4.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产合并</td></tr></table>

##### 2.4.4.4 解决方案

1. 在【财务会计】→【固定资产】→【资产维护】→【资产合并】功能节点，完成资产合并业务处理。资产合并单审批后，被合并的资产自动减少，合并后自动增加新资产。

2. 如果被合并资产都关联了设备卡片，那么合并后的资产可以与和被合并资产关联的设备卡片中的任意一个进行关联。

#### 2.4.5 资产减少

##### 2.4.5.1 业务描述

资产减少即资产的财务生命周期结束，引起资产减少的原因很多，包括：资产报废、资产处置、资产捐赠等。在 NC 系统中，如果固定资产关联了实物设备，那么当设备卡片发生资产报废、处置、捐献、所有权调拨等业务的时候，系统会自动联动固定资产减少业务。这也就是说，在 NC 系统中，用户即可以直接在固定资产模块完成资产减少业务，也可以通过事务管理的上述相关业务联动完成固定资产减少业务。

##### 2.4.5.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_219_155_954_1003.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 2.4-05 资产减少流程</div>


##### 2.4.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="6">资产管理</td><td rowspan="5">资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产报废</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产处置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产捐赠</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>所有权调出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产盘亏</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产减少</td></tr></table>

##### 2.4.5.4 解决方案

### 1. 设备管理

当固定资产与资产使用管理都启用的时候，资产使用管理的资产报废、资产处置、资产捐赠、所有权调出、资产盘亏业务都可以联动触发固定资产的减少业务，前提是发生实物业务的设备为固定资产。用户在上述业务对应的功能节点完成资产实物业务，系统则自动推出消息，通知固定资产相关操作员或者角色，及时完成固定资产减少业务。

用户可以在【资产管理】→【基础设置】→【规则设置】→【交易规则】功能节点设置固定资产减少系统消息接收人、角色。

### 2. 资产减少

如果由资产实物业务关联触发的固定资产减少，相关固定资产管理员角色或者操作用户，可以在系统消息中心接收到由系统推出的固定资产减少提醒消息，双击该消息可以打开减少单编辑界面，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_218_711_964_1157.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.4-06 资产减少</div>


用户可以在上图截图绿色框区，完善减少单相关信息，点击保存按钮，完成固定资产减少的生成，然后在【财务会计】→【固定资产】→【资产维护】→【资产减少】功能节点，查询减少单，并完成审核。

如果固定资产模块不与资产管理模块同时部署，而是单独部署应用，那么只能在【财务会计】→【固定资产】→【资产维护】→【资产减少】功能节点，通过新建、审核『资产减少单』的方式完成资产减少业务。

### 2.5 资产盘点

#### 2.5.1 业务描述

资产盘点是保证固定资产实物与账务数据一致的重要业务，也是减少资产流失的重要手段。通常情况下，资产盘点过程会持续一段时间，特别是资产密集型企业。资产盘点不仅仅关注实物数量、价值信息，也关注存放位置、使用部门等信息。盘点结束后，输出盘盈、盘亏以及差异调整数据，并完成必要的调整，例如：盘亏则需要做固定资产减少，盘盈则考虑新增固定资产，盘点差异则需要按照实际信息调整账面信息。

NC 固定资产盘点支持条形码盘点模式，同时提供两种盘点解决方案：

## 解决方案 1：固定资产直接盘点

当固定资产模块独立部署应用的时候，所有资产的盘点业务直接在固定模块内完成。

## 解决方案 2：资产实物盘点联动固定资产

当固定资产模块与资产管理同时部署应用的时候，凡是已经关联设备片的固定资产的盘点，在资产使用管理模块的资产盘点功能节点完成，没有管理设备卡片的固定资产的盘点则在固定资产模块完成。

#### 2.5.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_250_1071_1426.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 2.5-01 资产盘点流程</div>

#### 2.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="10">资产管理</td><td style='text-align: center; word-wrap: break-word;'>资产信息管理</td><td style='text-align: center; word-wrap: break-word;'>设备卡片</td></tr><tr><td rowspan="3">资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产盘点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产盘亏</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>差异调整</td></tr><tr><td rowspan="6">固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产盘点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>盘盈资产</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>盘点差异调整</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产新增</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产减少</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>设备联动调整</td></tr></table>

#### 2.5.4 解决方案

### 1. 解决方案 1：固定资产直接盘点

该方案适用于用户单独部署固定资产模块，详细过程如下：

## 1 ) 盘点

用户通过实地清点的方式，收集资产实物信息后，然后登陆系统在【财务会计】→【固定资产】→【资产盘点管理】→【资产盘点】功能节点，将实地清点的资产数据录入到系统中。系统也支持用户通过 excle 数据批量导入、条形码采集设备扫描这两种方式，实现资产清点数据到系统中的输入。根据用选择的盘点依据，系统自动核对账面数据与实际清单数据，并对核对差异做出明确标识。保存单据审批后，系统会推式生成盘盈资产、盘点差异调整、资产减少单据，盘盈单为未审批状态，盘单据为已经审批态。

## 2 ) 盘点差异调整

所谓盘点差异是指系统中以及清点过程中都存在该设备，即通过盘点依据核对资产的编码或卡片编号、条形码信息完全一致，但数量、使用部门、位置、信息不一致。用户在【财务会计】→【固定资产】→【资产盘点管理】→【盘点差异调整】功能节点，查询出由【资产盘点】功能节点推出『盘点差异调整单』，审批后系统自动按照实际清点的信息修正固定资产卡片对应信息。

当然如果实际清点过程中发现应归为 A 部门的资产却在 B 部门，可以要求 B 部门尽快归还资产，取消这张【盘点差异调整单】。

## 3 ) 盘亏处理

所谓盘亏是指系统中存在的某些资产，没有在资产清点过程中发现，那么即可认定该资产盘

亏。在盘点业务完成后，系统对盘亏的资产进行资产减少处理，不在生成资产盘亏单据。

## 4 ) 盘盈处理

盘盈资产是指清点过程中发现的不在系统账上的资产，这些资产通常是因为一些特殊原因，会计人员遗漏登账的固定资产。用户在【财务会计】→【固定资产】→【资产盘点管理】→【盘盈资产】功能节点，查询出由【资产盘点】功能节点推出『盘盈资产单』，可对其进行修改、删除、审批。审批后的盘盈资产，可以最为新增资产登记入企业财务账，用户在【财务会计】→【固定资产】→【资产新增】→【资产增加】功能节点，参照审批后的『盘盈资产单』生成新的固定资产卡片，进而完成固定资产入账。

### 2. 解决方案 2：资产实物盘点联动固定资产

该方案适用于用户同时部署了固定资产模块和资产管理模块，在这种情况下，凡是已经和设备卡片进行关联的固定资产，都不能在固定资产模块进行盘点业务，只能在资产使用管理模块进行资产盘点业务，详细过程如下：

## 1 ) 盘点

用户通过实地清点的方式，收集设备资产实物信息后，然后登陆系统在【资产管理】→【资产使用管理】→【资产盘点】→【资产盘点】功能节点，将实地清点的设备资产数据录入到系统中。系统同时支持用户通过 excel 数据批量导入、条形码采集设备扫描这两种方式，实现设备资产清点数据到系统中的输入。根据用选择的盘点依据，系统自动核对账面数据与实际清单数据，并对核对差异做出明确标识。保存单据审批后，系统会推式生成资产盘盈、资产盘亏、差异调整单据，这些单据为保存未审批态。

## 2 ) 盘点差异调整

用户可以在【资产管理】→【资产使用管理】→【资产盘点】→【差异调整】功能节点，查询出由【资产盘点】节点推出的「差异调整单」，可对其继续编辑、删除，审批后系统直接修改设备卡片相关属性值，同时推出「设备关联调整」，此单据用户可以在【财务会计】→【固定资产】→【资产变动】→【设备联动调整】功能节点进行查询、审批。

## 3 ) 盘亏处理

在【资产管理】→【资产使用管理】→【资产盘点】→【资产盘亏】功能节点，查询出由【资产盘点】节点推出的『资产盘亏单』，可对其继续编辑、删除，审核后系统会推出固定资产减少系统消息，固定资产管理员接收消息后，通过消息打开固定资产减少单，将其保存、审批，完成固定资产减少业务。

## 4 ) 盘盈处理

在【资产管理】→【资产使用管理】→【资产盘点】→【资产盘盈】功能节点，查询出由【资产盘点】节点推出的『资产盘盈单』，可对其继续编辑、删除，审核后的『资产盘盈单』可以在【资产管理】→【资产信息管理】→【设备卡片】功能节点，被按照生成新的设备卡片。

如果该设备为固定资产，可以在【财务会计】→【固定资产】→【新增资产】→【资产

增加】功能节点，参照该设备卡片生成新的固定资产。

注意：生成固定资产之前请在【资产管理】→【资产信息管理】→【资产生成设置】功能节点，检查该设备卡片“是否生成资产”的标识是否为选中状态，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_210_267_971_725.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 2.5-02 资产生成设置</div>


如果上图中的 “生成固定资产” 标识未被选中，那么在盘盈的设备卡片则不能被参照生成固定资产卡片。

### 2.6 折旧与摊销

固定资产折旧摊销是固定资产管理的核心业务，也是财务会计的重要业务处理之一。固定资产折旧摊销过程涉及到所有固定资产折旧数值的计算，实现按照不同口径的归集分摊，折旧计算过程需要考虑资产在会计期间内做的所有变动调整，最后将数据整理登账。NC系统支持单财务组织、多财务组织折旧摊销业务，详细业务过程和解决方案参见以下章节。

#### 2.6.1 单组织计提摊销

##### 2.6.1.1 业务描述

单组织计提是指只对一个财务组织进行固定资产计提摊销，相对于多组织折旧摊销，单组织折旧摊销相对简单。单组织计提摊销适用于某个财务组织的固定资产会计或者财务会计，对自己负责的财务组织的固定资产计提摊销。

##### 2.6.1.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_270_244_900_1250.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.6-01 固定资产计提分摊流程</div>

##### 2.6.1.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧与摊销</td></tr></table>

##### 2.6.1.4 解决方案

### 1. 参数设置

1）鉴于固定资产在使用过程中会发生各种变动，例如：资产类别变动、折旧方法变动、原值变动等等，上述各种变动会直接影响折旧额以及折旧分摊归集。而对于不同企业往往对资产变动影响的范围和时机有不同的业务处理要求，例如：当在会计期间中途发生资产类别变动时，有些企业希望将变动当期的折旧额分摊到变动前类别，而有些企业则希望分摊到变动后类别。对于诸如上述所提及的不同业务需求，NC系统通过参数配置来进行适应。

一般情况下，参数设置都在启用固定资产产品时确认，日常业务中除一些政策性的变化外，不建议频繁修改。

通过 FA83 参数：支持多成本分摊，来设置是否支持按多成本中心进行核算。

2) 用户在【财务会计】→【固定资产】→【基础设置】→【参数设置】功能节点，完成控制折旧分摊归集机制的设置，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_233_1052_1054_1468.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 2.6-02 参数设置</div>

如上图所示，NC系统中可以对以下5个层面对固定资产折旧分摊业务进行控制，近而适应不同业务场景需求：

## ➢ 变动时机控制

控制当资产发生使用年限、折旧方法、工作量、使用状况变动时，变动是否在当月就生效，即变动当月计算折旧额的时候，是否使用变动后的数据。

## 折旧分摊归集方式控制

控制当资产发生类别、使用部门、管理部门、项目变动时，变动当期的折旧额是归属变动前还是变动后。

## 折旧分摊周期控制

控制系统多长时间向总账系统生成折旧额登帐凭证，NC系统支持每月一次、每两月一次、每季度一次、每半年一次、每年一次。

## ➢ 折旧汇总项目控制

即折旧计提数据汇总的维度，以及汇总排序方式，例如系统支持资产类别、使用部门、管理部门、折旧方法、成本中心等多个维度进行折旧数据汇总，同时支持用户设置哪个各个汇总维度的排序。

按成本中心分摊支持两种场景：可通过客户化参数配置：支持多成本中心分摊和支持指定的成本中心分摊：

（1）选择多成本中心分摊时，需要将成本中心与使用部门设置对应关系，资产卡片上无需指定成本中心；多使用部门对应多成本中心，折旧分摊时，选择成本中心维度分摊。

（2）选择指定成本中心分摊：需要在卡片上录入成本中心，折旧分摊时，选择按成本中心分摊。

## 会计凭证生成方式设置

制单方式是指生成凭证时，按什么口径去生成会计凭证，系统默认为“默认方式”，即将所有本期计提的折旧生成一张会计凭证；选择“资产类别”，则系统会按您选择的类别口径生成多账会计凭证；若选择的类别都为一级，那么该公司有几个一级类别，则生成几张会计凭证，如果选择明细级，则按类别明细级的个数生成多张会计凭证。

### 2. 折旧与摊销

在【财务会计】→【固定资产】→【期末处理】→【折旧与摊销】功能节点，完成固定资产折旧额计算、修改、分摊。一个会计月度内，用户可以多次计提分摊以最后一次为准。参数 FA15 控制折旧清单是否可以修改，默认情况下折旧清单都可以修改，如果用户不希望可以对折旧清单进行修改调整，可以设置该参数值为“否”。

#### 2.6.2 多组织计提摊销

##### 2.6.2.1 业务描述

多组织计提是指只对多个财务组织进行固定资产计提摊销，多组织计提摊销适用于集团固定资产会计或者财务会计，对自己负责的财务组织的固定资产一次性进行折旧摊销，可大大提升折旧提及与摊销的效率。

##### 2.6.2.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_271_562_898_1426.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.6-03 固定资产计提分摊流程</div>

##### 2.6.2.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧与摊销</td></tr></table>

##### 2.6.2.4 解决方案

多组织计提与摊销与单组织解决方案在操作层面基本一致，不同点是当进行多组织计提摊销时，需要保证所有计提摊销的财务组织最小未结账月必须相同，否则计提失败。如果财务组织的最小未结账月不相同，只能通过单组织多次计提的方式进行。

#### 2.6.3 跨组织计提摊销

##### 2.6.3.1 业务描述

在有些企业中会存在同固定资产所有权归属 A 公司或者组织，由 B 公司或者组织使用，因此 B 公司承担资产的折旧费用。

##### 2.6.3.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_215_1004_956_1490.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-04 固定资产计提分摊流程 2</div>

##### 2.6.3.3 功能节点


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="4">资产管理</td><td rowspan="3">固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧与摊销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产信息管理</td><td style='text-align: center; word-wrap: break-word;'>设备卡片</td></tr></table>

##### 2.6.3.4 解决方案

固定资产跨组织折旧分摊关键应用点是根据设备使用组织进行固定资产折旧的分摊。因此解决方案需要用户同时启用资产实物管理模块。

### 1. 建立固定资产与设备卡片关联

首先创建设备卡片，货主为：A 组织-炼钢厂，然后将该设备的使用权分配给 “B 组织-物资公司”，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_778_1009_1268.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.6-05 固定资产与设备卡片关联</div>


在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，通过参照设备卡片生成固定资产卡片，固定资产卡片财务组织为“A组织-炼钢厂”。如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_148_1014_533.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.6-06 拉设备卡片生成固定资产</div>


保存固定资产卡片后，也就完成了设备卡片与固定资产卡片的关系建立。

### 2. 折旧分摊策略设置

在【财务会计】→【固定资产】→【基础设置】→【参数设置】功能节点，完成控制折旧分摊归集机制的设置，详细参见2.6.1章节解决方案部分内容。

在【动态建模平台】→【会计平台】→【通用平台】→【入账规则（对照）-业务单元】功能节点，配置入账规则。将“设备使用权”作为影响因素进行配置，即不同的使用权向不同的账簿传凭证，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_218_889_962_1391.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-07 设置入账规则-1</div>


编辑对照表，不同的使用权对应相应的财务组织账簿，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_222_155_962_564.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-08 设置入账规则-2</div>


最终配置结果如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_657_1011_1222.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 2.6-09 设置入账规则-3</div>


### 3. 折旧与摊销

在【财务会计】→【固定资产】→【期末处理】→【折旧与摊销】功能节点，完成固定资产折旧额计算、修改、分摊。一个会计月度内，用户可以多次计提分摊以最后一次为准。参数FA15控制折旧清单是否可以修改，默认情况下折旧清单都可以修改，如果用户不希望可以对折旧清单进行修改调整，可以设置该参数值为“否”。

#### 2.6.4 多部门计提摊销

##### 2.6.4.1 业务描述

在企业固定资产使用的过程中，会存在一个固定资产被多个部门共享使用，为了更精确的归集固定资产折旧费用，部分企业要求所有共享使用该固定资产的部分都按照比例承担该固定资产的折旧费用。

##### 2.6.4.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_292_535_920_1381.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 2.6-10 固定资产计提分摊流程</div>

##### 2.6.4.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产</td><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧与摊销</td></tr></table>

##### 2.6.4.4 解决方案

### 1. 卡片设置

首先需要在固定资产卡片上设置多部门使用属性，用户可以在资产新增的时候，在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点新增资产的时候设置，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_145_592_1041_1150.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.6-11 多使用部门-卡片设置</div>


如果资产在购进的时候还不是多部门共同使用，在后期使用过程中才变为多个部门共同使用，这种情况下可以通过在【财务会计】→【固定资产】→【资产变动】→【使用部门调整】功能节点进行使用部门调整，实现多个部门共同使用该资产如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_221_147_962_670.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-12 多使用部门-单据</div>


完成上述设置后，在对应固定资产进行折旧分摊的时候，系统会自动将会按照分摊比例在不同部门间分摊折旧数据，但分摊结果只能体现在固定资产模块的各种报表中，如果用户希望折旧分摊的明细体现在总账，则需要继续设置会计平台和固定资产参数，详细参见以下内容。

### 2. 折旧分摊策略设置

详细设置过程请参见单组织计提摊销场景。这里需要强调的是，如果用户希望在财务账上体现分摊明细，则需要设置“制单方式”，选择按照使用各部门制单，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_218_953_964_1463.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-13 折旧分摊策略设置</div>

如果用户不希望按照部门独立生成凭证，则可以设置通过凭证辅助核算的方式实现对部门明细折旧分摊的体现，详情参见如下第3点。

### 3. 会计平台设置

关于会计平台的详细操作，请参见相关帮助。这里强调的是，如果希望通过辅助核算的方式，实现固定资产部门分摊的明细则需要在【动态建模平台】→【会计平台】→【通用平台】→【转换模板】功能节点设置辅助核算，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_215_387_963_966.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-14 会计平台设置</div>


### 4. 折旧计提与摊销

折旧计提摊销操作请参见单组织计提摊销场景相关内容，此处不过赘述。

#### 2.6.5 按日计算折旧

##### 2.6.5.1 业务描述

根据欧盟会计准则的要求，固定资产要按日计算折旧。资产新增、减少以及原值变动等业务，从业务日期当天开始影响折旧的计提，计提折旧仍然按会计期间计提。

##### 2.6.5.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_241_961_1343.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-15 固定资产按日计算折旧流程</div>

##### 2.6.5.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="9">资产管理</td><td rowspan="9">固定资产</td><td style='text-align: center; word-wrap: break-word;'>折旧方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>参数设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产类别</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>账簿信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产维护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产调拨</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧与摊销</td></tr></table>

##### 2.6.5.4 解决方案

按日计算折旧是一种会计制度的处理要求，如主管部门要求企业的资产折旧需要按照这种方式进行，那么在系统中主要的准备工作包括：启用日折旧、资产类别以及账簿信息中分配日折旧的折旧方法、资产卡片引用到日折旧的折旧方法。

### 1. 启用日折旧

进入【财务会计】-【固定资产】-【基础设置】-【折旧方法】节点，启用日折旧。选择需要使用按日计算折旧的财务组织（由于按日计算折旧特性是按组织个数授权的，启用组织时请谨慎，组织下存在按日计算折旧的卡片，即不能取消）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_235_1094_978_1467.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-16 启用日折旧</div>

### 2. 资产类别及账簿信息中分配日折旧的折旧方法

资产类别和账簿信息中需要为每个资产类别分配默认的折旧方法。

<div style="text-align: center;"><img src="imgs/img_in_image_box_234_249_979_699.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-17 资产类别分配默认折旧方法</div>


账簿信息中会默认关联资产类别的折旧方法，可以根据实际情况修改账簿信息中关联资产类别默认的折旧方法。此处的修改不影响资产类别的默认值，资产卡片默认的折旧方法以账簿信息为准。

<div style="text-align: center;"><img src="imgs/img_in_image_box_235_841_979_1277.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-18 账簿信息分配默认折旧方法</div>


### 3. 资产卡片引用日折旧的折旧方法

新增资产卡片时，如所属的资产类别默认了按日计算折旧的折旧方法，该卡片即按日计算折旧。

<div style="text-align: center;"><img src="imgs/img_in_image_box_236_146_980_548.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.6-19 资产卡片引用折旧方法</div>


### 4. 资产业务对按折旧计算折旧的影响

1）影响折旧计算的资产价值信息发生变动，从发生变动业务日期当天或下一天开始以变动后的信息计算折旧（取决于账簿信息中的折旧属性）；

2）影响折旧分配的重要档案发生变动，从发生变动业务日期当天或下一天开始折旧分配到变动后的档案上（取决于固定资产下的参数设置）；

3）资产由于拆分、合并、调拨或减少等业务退出本企业的，当期折旧计算至业务日期当天或前一天（取决于账簿信息中的折旧属性）；

4） 资产由于拆分、合并、调拨等业务增加的，当期折旧计算从业务日期当天或下一天开始（取决于账簿信息中的折旧属性）；

5）资产评估以及资产减值对折旧计算的影响，同价值信息变动；

6）总原则是，折旧的计算与分配明细到每一天。

### 2.7 月末结账

#### 2.7.1 业务描述

月末结账很好地体现了财务会计期间的应用特点，通过月末结账动作，集中处理各类财务业务，同时将财务数据按照期间进行归类、划分、标识，为以后的数据统计、查询、分析提供规范的基础。结账后的会计期间是不能业务操作和处理了，也就是通常所说的“封账”，如果希望进行业务处理则需要取消结账状态。

#### 2.7.2 业务流程

无

#### 2.7.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>月末结账</td></tr></table>

#### 2.7.4 解决方案

### 1. 结账

1) 用户在【财务会计】→【固定资产】→【期末处理】→【月末结账】功能节点完成月末结账操作。通常情况下用户在进行月末结账处理之前，需要确认当期所有相关业务都已经处理完毕，例如：资产变动单是否全部审核，折旧计提是否完成等等。一旦月末结账处理完毕，则不能再对此会计期间做任何业务即数据上的改动。

2) 系统支持单组织结账，也支持多组织结账。

### 2. 反结账

1) 如果企业的确需要修改往期已经结账的业务数据，可以通过反结账操作取消结账状态，但只能取消最近未结账的会计期间结账状态。例如：如果当前结账月为7月，用户希望修改6月的业务数据，则需要先取消7月份结账状态，再取消6月份结账状态。

2) 虽然系统允许进行反结账，但用户一定要慎用此功能，因为反结账会清除当前期间的很多业务痕迹，例如：资产变动、资产拆分合并等等，也就是说反结账是以牺牲被反结账期间的业务痕迹为代价的。

3) 支持单组织反结账，也支持多组织反结账。

### 2.8 固定资产对账

#### 2.8.1 业务描述

对账是财务会计最常见的业务之一，对账的主要目的是保证总账与业务账之间的数据一致。固定资产对账是指将固定资产模块的业务数据与总账中固定资产账务数据进行核对。对账业务通常发生在财务月末结账之前，因为一旦发觉业务系统与总账之间的数据不一致，通常情况下需要在月末结账之前查找原因，必要的情况下需要消除异常的差异。

#### 2.8.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_318_244_904_1088.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图 2.8-01 固定资产与总账对账流程</div>


#### 2.8.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>财务会计</td><td style='text-align: center; word-wrap: break-word;'>总账</td><td style='text-align: center; word-wrap: break-word;'>对账设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>对账</td></tr></table>

#### 2.8.4 解决方案

### 1. 对账策略设置

根据企业不同的对账需求，用户可以在【财务会计】→【总账】→【总账与业务系统对账】→【对账设置】功能节点，设置对账规则即对账策略。用户可以针对不同财务核算账簿、业务系统、设置多个对账规则，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_169_265_1056_688.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.8-02 对账设置</div>


关于对账规则设置的详细内容请参见产品帮助。

### 2. 对账执行

用户在每月末结账之前在【财务会计】→【固定资产】→【月末处理】→【对账】功能节点，或者在【财务会计】→【总账】→【总账与业务系统对账】→【对账执行】功能节点，完成对账。用户可以选择对账规则、对账期间等信息，如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_936_957_1393.jpg" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 2.8-03 对账执行</div>


并以通过对账结果联查总账、业务账、明细，如下图所示：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">执行对账</td><td colspan="2">联查总账</td><td colspan="2">联查业务账</td><td colspan="2">明细</td><td colspan="2">打印</td><td colspan="2">刷新</td><td colspan="2">切换</td></tr><tr><td colspan="2">核算账簿</td><td colspan="4">炼钢厂-中国大陆报告账簿</td><td colspan="2">对账期间</td><td colspan="5">2011.01---2011.01</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">是否相符</td><td rowspan="3">规则编码</td><td rowspan="3">规则名称</td><td rowspan="3">业务系统</td><td rowspan="3">币种</td><td rowspan="3">对账维...</td><td rowspan="3">会计科目</td><td colspan="7">期末余额</td></tr><tr><td colspan="3">总账</td><td colspan="3">业务系统</td><td style='text-align: center; word-wrap: break-word;'>差额</td></tr><tr><td colspan="3">本币</td><td colspan="3">本币</td><td style='text-align: center; word-wrap: break-word;'>本币</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>✗</td><td style='text-align: center; word-wrap: break-word;'>1001</td><td style='text-align: center; word-wrap: break-word;'>总账固...</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>人民币</td><td style='text-align: center; word-wrap: break-word;'>资产类...</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td colspan="3">25,902,600.00</td><td colspan="2">26,272,676.92</td><td colspan="2">-370,076.92</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>✗</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>总计</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td colspan="2">25,902,600.00</td><td colspan="2">26,272,676.92</td><td colspan="2">-370,076.92</td></tr></table>

<div style="text-align: center;">图 2.8-04 对账执行结果</div>


### 2.9 模拟折旧

#### 2.9.1 业务描述

所谓模拟折旧就是指对未来某个时期的固定资产折旧计提进行模拟计算，为企业的全面预算以及未来资产相关决策提供数据依据。

#### 2.9.2 业务流程

<div style="text-align: center;"><img src="imgs/img_in_image_box_347_871_861_1375.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图 2.9-01 固定资产模拟折旧流程</div>

#### 2.9.3 功能清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="2">资产管理</td><td rowspan="2">固定资产</td><td style='text-align: center; word-wrap: break-word;'>模拟折旧设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模拟折旧</td></tr></table>

#### 2.9.4 解决方案

### 1. 模拟折旧方案设置

1）在【财务会计】→【固定资产】→【基础设置】→【模拟折旧设置】功能节点，完成模拟折旧方案的设置。用户可以根据不同管理目的，创建不同的模拟折旧方案。

2）可以指定资产类别、时间范围、折旧方法、原值、残值（率）、累计折旧、使用年限等参数，进行不同方式的模拟计算。

### 2. 模拟折旧计算

1）在【财务会计】→【固定资产】→【模拟折旧】功能节点，调用不同的模拟折旧方案进行模拟折旧计算，并可以对不同的模拟折旧方案进行模拟数据对比，生成保存模拟折旧结果以备后期查询。

2） 共最多支持 4 个不同账簿、不同模拟折旧方案的同时模拟计算，支持任意 2 个账簿间对比分析。

3) 支持联查模拟折旧的明细数据。

4) 支持将模拟折旧结果传送给预算管理模块，如下图所示。同一财务组织的相同账簿，在指定时间区间内只能有一个模拟折旧结果可以被传递给预算。

<div style="text-align: center;"><img src="imgs/img_in_image_box_166_1017_1016_1476.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 2.9-02 模拟折旧预算取数</div>

### 2.10 固定资产多账簿

#### 2.10.1 业务描述

为了满足不同的会计制度和不同的管理需求，对同一资产，提供不同的折旧、变动、统计汇总等业务处理方式。需要注意的是，固定资产多账簿主要指财务核算层面，而对于实物管理也就是业务管理，则不涉及多账簿。当然也正是由于一套实物数据对应多套财务核算数据的原因，才使固定资产多账簿应用变的复杂。固定资产多账簿的意义在于：

✓ 满足同一公司管理会计与财务会计对固定资产的不同管理需求；

✓ 满足跨国集团因会计制度、税务制度、财务政策等差异对固定资产管理的不同需求。

#### 2.10.2 应用模型

### 1. 财、税分离应用模式

企业由于内部财务管理与对外财务报告、报税的不同需求，需要对固定资产进行两套账分别管理，具体应用模型如下：

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_804_1057_1201.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 2.10-01 财税分离应用模式</div>


当然，我们推荐企业通过管理会计模块完成内部财务的管理。

### 2. 跨国集团公司不同财务制度

对于跨国集团公司，经常会面临旗下子公司归属不同的国家，进而需要遵循不同的财务政策、法规以及处理方法。这种情况下，为了更加清楚的管理整个集团的资产，往往需要将不同国家下公司的资产独立成账。因此，一个大型的跨国集团，出现多套固定资产账簿也是很常见的，具体应用模型如下：

<div style="text-align: center;"><img src="imgs/img_in_image_box_168_155_1058_561.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 2.10-02 跨国集团应用模式</div>


### 3. 证券行业外币分账制

证券行业为了更好管理业务及经营数据，习惯于将不同币种交易与业务的进行分账，从而造成其对资产管理也有分账的要求，也就是多账簿。具体应用模型如下：

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_758_1052_1222.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 2.10-03 证券行业外币分币制模式</div>


#### 2.10.3 功能清单

固定资产多账簿是一个固定资产整体解决方案，原则上包括固定资产模块的所有功能节点。以下列出的功能节点为支持多账簿功能的功能节点，以下功能节点的业务有些默认是对所有账簿起作用，有些则可以选择对指定账簿起作用，详细信息请参见解决方案部分的内容。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>领域</td><td style='text-align: center; word-wrap: break-word;'>产品模块</td><td style='text-align: center; word-wrap: break-word;'>功能节点</td></tr><tr><td rowspan="3">资产管理</td><td rowspan="3">固定资产</td><td style='text-align: center; word-wrap: break-word;'>录入原始卡片</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产增加</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（22个预置变动业务）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产评估</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产减值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产拆分</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产合并</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产减少</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产盘点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>折旧与摊销</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>月末结账</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>模拟折旧</td></tr></table>

#### 2.10.4 解决方案

固定资产多账簿解决方案除了需要完成必要的基础设置外，还在多个业务功能点进行全面支撑，进而满足固定资产多账簿业务场景。以下内容对所有支持多账簿业务操作的功能点进行全面介绍。

### 1. 资产新增

固定资产新增资产场景对固定资产多账簿的支撑，体现在【财务会计】→【固定资产】→【新增资产】→【资产增加】功能节点，当新增的固定资产的资产类别在多个固定资产账簿内，在操作界面下端则会出现对应账簿的切换按钮，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_191_1023_930_1471.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.10-04 固定资产多账薄</div>

用户可以切换上图红框内账簿按钮，编辑新增固定资产在不同账簿的财务信息，即上图绿色框区域内信息，而业务类信息所有账簿是保持相同的。编辑结束，点击“保存”按钮，系统自动保存多个账簿新增资产的信息。

### 2. 资产变动

原则上所有固定资产业务类信息的资产变动，变动固定资产所有关联账簿都进行更新；财务类型信息变动，用户则可以选择指定账簿进行变动。下表列出系统预置的资产变动业务对多账簿支持的模式：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编号</td><td style='text-align: center; word-wrap: break-word;'>变动业务名称</td><td style='text-align: center; word-wrap: break-word;'>多账簿支持模式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>01</td><td style='text-align: center; word-wrap: break-word;'>原币原值调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>02</td><td style='text-align: center; word-wrap: break-word;'>本币原值调整</td><td style='text-align: center; word-wrap: break-word;'>可指定账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>03</td><td style='text-align: center; word-wrap: break-word;'>购买价款调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>04</td><td style='text-align: center; word-wrap: break-word;'>资产追溯调整</td><td style='text-align: center; word-wrap: break-word;'>可指定账簿<img src="imgs/img_in_seal_box_795_544_887_665.jpg" alt="Image"" /></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>05</td><td style='text-align: center; word-wrap: break-word;'>价值调整单</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>06</td><td style='text-align: center; word-wrap: break-word;'>累计折旧调整</td><td style='text-align: center; word-wrap: break-word;'>可指定账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>07</td><td style='text-align: center; word-wrap: break-word;'>净残值率</td><td style='text-align: center; word-wrap: break-word;'>可指定账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>08</td><td style='text-align: center; word-wrap: break-word;'>数量调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>09</td><td style='text-align: center; word-wrap: break-word;'>使用月限调整</td><td style='text-align: center; word-wrap: break-word;'>可指定账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>折旧方法调整</td><td style='text-align: center; word-wrap: break-word;'>可指定账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>使用状况调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>增加方式调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>管理部门调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>使用部门调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>折旧承担部门调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>使用人调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>17</td><td style='text-align: center; word-wrap: break-word;'>资产类别调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>类别和管理部门调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>19</td><td style='text-align: center; word-wrap: break-word;'>项目档案调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>工作总量调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>资产组调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>设备联动调整</td><td style='text-align: center; word-wrap: break-word;'>必须所有账簿</td></tr></table>

## 注意：

上表中不支持对指定账簿进行操作的资产变动业务，即便通过单据模板配置，将“资产账簿”字段配置显示，也不能实现对指定账簿的业务操作。

➢ 用户可以自定义变动业务，如果将业务属性和财务属性变动同时配置在一个自定义变动业务的话，就必须在单据模板选择显示并可编辑“资产账簿”字段。同时，在使用此自定义变动进行业务处理的时候，“资产账簿”字段只对资产的财务属性变动生效，而对业务属性变动不生效。

### 3. 资产调拨

固定资产调拨业务对所有账簿都生效，即用户不能选择固定资产账簿进行资产调拨。

### 4. 资产维护

资产评估、资产减值业务可以对指定账簿进行业务处理，资产减少业务可指定财簿进行业务处理，也可以不指定账簿，账簿为空时，表示为在所有账簿下减少；而资产拆分、资产合并不支持对指定账簿进行业务操作。

### 5. 资产盘点

固定资产盘点是对资产业务信息进行确认的过程，对于资产价值信息无需盘点。因此，固定资产盘点业务不支持对指定账簿进行操作。但固定资产盘亏触发的资产减少业务则可以对指定账簿进行减少。

### 6. 折旧与摊销

固定资产折旧与摊销也是支持多组织多账簿业务的，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_221_964_964_1317.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.10-05 折旧与摊销</div>


关于折旧与摊销场景的细节内容可参见本章“折旧与摊销”场景的相关内容。

### 7. 月末结账

月末结账支持多账簿业务，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_221_154_962_478.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 2.10-06 月末结账</div>


### 8. 模拟折旧

模拟折旧支持多账簿业务，用户可对同一个财务组织选择多个账簿同时进行折旧模拟，同时还能比较不同账簿的模拟差异，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_655_956_1060.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 2.10-07 模拟折旧</div>

## 第三章 初始准备

此章节重点介绍启用固定资产模块需要完成准备性工作，下图为准备工作的路线图，虚线框内容不在本手册展开说明，请参见组织管理手册、基础数据手册、流程管理手册相关章节：

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_393_1084_1318.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3-01 管理员职责划分</div>


### 3.1 管控模式

管控模式设定决定基础档案的数据维护管理模式的同时，也是用户通过控制基础档案实现对业务分级

管控的重要手段。管控模式的设定应该是企业通过管理咨询实现对自身业务深入分析，充分考虑 NC 系统的功能特点后以及业务解决能力之后，所作出的慎重决定。因为管控模式一旦系统中设定后，则不能在后续业务全面启动后随意更改。

用户通过系统管理员身份登录，在【应系统管理】→【系统初始化】→【管控模式】功能节点，完成各类基础数据、档案的管控模式设定。

### 3.2 动态建模平台

#### 3.2.1 组织管理

组织管理主要完成企业组织结构搭建、业务委托关系的定义。鉴于本文第二部分阐述的业务场景，不仅仅需要用户部署固定资产模块，还需要用户部署总账、资产信息管理、资产使用管理以及供应链的采购与库存管理模块，单本文档主要以固定资产管理为重点进行介绍说明，关于供应链领域产品相关初始化准备工作请参见相关产品手册。

##### 3.2.1.1 组织结构定义

### 1. 集团

使用系统给管理身份登录系统，可以创建新的集团，并给集团指定集团管理员。如果使用集团管理员身份登录系统，只能查看和修改该集团管理员所管理的集团部分档案信息。关于集团档案的维护的详细步骤请参见组织管理手册和相关产品帮助。

### 2. 业务单元

使用集团管理身份登录系统，在【动态建模平台】→【组织管理】→【组织结构定义】→【业务单元】功能节点，维护集团的业务单元结构。其中包括业务单元的层级、数量以及各个业务单元的组织职能。固定资产管理模块的主组织为财务组织，即只有组织职能为财务组织的业务单元才能处理固定资产相关业务，关于业务单元维护的详细过程请参见组织管理手册和产品相关帮助。

### 3. 部门

部门为依附于业务单元，每个业务单元下级可以创建多个部门。关于部门维护的详细过程请参见组织管理手册和产品相关帮助。

### 4. 账簿类型

账簿类型即财务核算账簿的模板，核算账簿创建在不同的账簿类型下。关于账簿类型维护的详细过程请参见组织管理手册和产品相关帮助。

### 5. 财务核算账簿

财务核算账簿是固定资产模块最重要的基础档案之一，每个财务组织同一核算账簿类型只能创建一个核算账簿，核算账簿需要启用固定资产账，启用固定资产账簿的前提是必须启用总账。关于财务核算账簿维护的详细过程请参见组织管理手册和产品相关帮助。

### 6. 业务人员来源

业务人员来源是固定资产模块重要基础档案之一，在做固定资产业务时，当行政组织与业务组织不一致时，固定资产业务组织可能会引用到其他行政组织的部门、人员信息，此时就可以通过业务人员来源来设置相关人员的来源。

##### 3.2.1.2 业务委托关系定义

集团内部存在众多的专业化的业务单元，这些组织单元要协同运作。每种业务单元的职责是明确的，例如：财务业务单元负责财务核算，采购业务单元负责采购，库存业务单元负责库存事务，等等，但是企业中几乎每一个完整的业务流程都无法由一种业务单元独立完成，必然需要跟其他的业务单元协同工作，这种协同关系就通过业务委托关系来实现。业务委托的主要意义在于处理多个不同类型组织之间的业务协同，形成完整的业务流，并对业务流加以约束和控制。完整的固定资产解决方案中共涉及如下几个重要业务委托关系需要设置：

### 1. 资产库存委托关系

即资产组织委托那个库存组织采购资产。例如：当通过参照采购到货单生成设备卡片的时候，只有与设备卡片上主组织建立库存业务委托关系的库存组织的到货单才能被参照生成卡片。

### 2. 资产货主业务委托关系

即货主委托其他资产组织代理其完成相关资产所有权业务。例如：A 货主委托 B 资产组织代理其处理 X 资产相关货主业务，那么 X 资产卡片的所有权调拨业务就可以由 B 资产组织完成，体现在系统中就是所有权调拨单的主组织为 B。

### 3. 资产使用权业务委托关系

即货主委托其他资产组织代理其完成资产使用权业务。例如：A 货主将 X 资产的使用权业务委托给 B 资产组织，那么 B 资产组织可以替 A 货主将 X 资产进行租出。

### 4. 核算委托业务关系

即资产管理组织委托其他财务组织对其进行核算。例如：A 资产管理组织将其管理的资产委托给 B 财务组织，那么 B 财务组织可以对 A 的资产进行核算。资产货主业务委托关系新增、修改时，需要将货主管理组织和财务组织的关系时需要同步到核算委托关系中。

关于委托关系维护的详细过程请参照组织管理手册。

#### 3.2.2 权限管理

权限是系统应用的重要前提之一，系统除了预置超级管理员账户、部分角色外，不会预置任何用户、

职责信息，所以正式启用前创建完善用户权限系统，关于用户权限的维护管理请参见权限管理手册。

#### 3.2.3 基础数据维护

系统正式启用前需要设置大量基础档案和参数，本章节重点介绍启用固定资产模块需要设置的基础档案和相关参数。

##### 3.2.3.1 基础档案

在组织管理平台中涉及到固定资产的基本档案主要包括项目相关信息，共包括：企业项目结构（EPS）、项目、项目类型、项目工作结构分解（WBS）。这些档案会在固定资产工程转固业务场景中被参照。用户在【动态建模平台】→【基础数据】→【项目信息】功能节点完成上述基础档案的设置。关于上述档案的详细内容以及维护过程，请参见基础数据手册相关章节。

如果系统启用了项目管理模块，则不需要在【动态建模平台】→【基础数据】→【项目信息】功能节点，进行项目基础信息的维护。若用户通过升级的方式启用了项目管理产品，在升级前的项目相关信息仍然保留可以查询，但不能通过【动态建模平台】→【基础数据】→【项目信息】功能节点，进行数据增补和修改了。

##### 3.2.3.2 参数设置

参数是控制业务模式的重要基础数据，为了实现不同的管控目的，适应企业不同层面的管控需求，NC系统中的参数也被分成不同的层级，包括全局级参数、集团级参数、业务单元+部门级、账簿级等。大多数参数都根据常用的业务模式做了默认值预设。原则上，如果没有特殊需要，用户采用默认参数值即可启用模块，大部分参数都可以在业务应用的过程中进行修改，但一旦修改会实时影响业务，因此，建议用户在正式启用模块做业务数据之前确认一下参数是否与企业业务模式匹配。

用户在【动态建模平台】→【基础数据】→【参数】→【参数设置】功能节点完成参数设置，关于参数的详细设置这里不做赘述，请参见基础数据手册相关部分内容。

#### 3.2.4 流程配置

流程是系统完成业务单据流转重要载体，NC系统包括三个类型流程：审批流、工作流、业务流。在正式启用固定资产业务模块之前，需要完成必要流程配置，以实现业务单据按照规定的方式流转，从而达到管理及控制的目的。固定资产模块不支持工作流程，因此不需要进行工作流配置。在配置流程之前，需要设置确认单据交易类型、单据接口定义。

### 1. 交易类型管理

交易类型可以理解为是业务单据类型的子分类，一个业务单据包括多个交易类型，在不同的交易类型上定义业务约束规则，进而实现不同的交易类型匹配不同业务。例如：资产变动单是一个单据类型，而原币原值变动、折旧方法变动、累计折旧变动属于不同类型的资产变动业务，即属于独立的交易类型。在系统中交易类型可以发布为功能节点，以下为固定资产模块预置的，超过2个交易类型的单据及其交易类型清单：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>单据类型</td><td style='text-align: center; word-wrap: break-word;'>交易类型</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td rowspan="2">转固单</td><td style='text-align: center; word-wrap: break-word;'>工程转固单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>采购转固单</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="25">资产卡片</td><td style='text-align: center; word-wrap: break-word;'>通用资产</td><td style='text-align: center; word-wrap: break-word;'>系统通过给不同交易类型配置不同的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>机械资产</td><td style='text-align: center; word-wrap: break-word;'>单据模板，实现不同类型资产的卡片的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运输资产</td><td style='text-align: center; word-wrap: break-word;'>个性化。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>建筑房产资产</td><td style='text-align: center; word-wrap: break-word;'>如果需要用也可以将不同交易类型发</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>土地资产</td><td style='text-align: center; word-wrap: break-word;'>布为不同的功能节点，来分别完成不同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>递延资产</td><td style='text-align: center; word-wrap: break-word;'>类型资产的建卡业务。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>原币原值变动</td><td style='text-align: center; word-wrap: break-word;'>系统通过给不同交易类型配置不同的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本币原值变动</td><td style='text-align: center; word-wrap: break-word;'>单据模板，实现不同变动业务的个性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>购买价款变动</td><td style='text-align: center; word-wrap: break-word;'>化。默认情况每个交易类型应独立发布</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产追</td><td style='text-align: center; word-wrap: break-word;'>为功能节点。用户可以根据需要配置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资本化</td><td style='text-align: center; word-wrap: break-word;'>个性化的资产变动交易类型，并分配对</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>累计折</td><td style='text-align: center; word-wrap: break-word;'>应的单据模板，进而实现资产变动业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>净残值</td><td style='text-align: center; word-wrap: break-word;'>的自定义。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数量调</td><td style='text-align: center; word-wrap: break-word;'><img src="imgs/img_in_seal_box_413_812_627_1154.jpg" alt="Image"" /></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用月</td><td style='text-align: center; word-wrap: break-word;'>资产变动</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧方</td><td style='text-align: center; word-wrap: break-word;'>使用状</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用方式调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用部门调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>管理部门调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>折旧承担部门调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用人调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产类别调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>类别与管理部门调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工作总量调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产组调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>设备联动调整</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

用户在【动态建模平台】→【流程管理】→【交易类型管理】功能节点完成交易类型管理，用户可以查询系统内置的各种单据类型的交易类型，也可以自定义交易类型，并发布成功能节点。关于交易类型管理详细操作请参见流程管理手册相关章节。

### 2. 单据接口定义

用于设置非流程单据与流程单据之间接口关系，例如：采购到货单推出的资产转固单。“业务流定义”只支持对流程单据进行配置，单据接口定义是对通过业务流定义单据间关系的补充。单据接口定义支持按照单据交易类型进行细分设置。用户可以在【动态建模平台】→【流程管理】→【单据接口定义】功能节点查询所有非流程单据与流程单据之间的接口定义关系，详细操作过程请参见流程管理手册相关章节。

### 3. 审批流

为某个具体的业务单据审批动作定义流程。定义了审批流程的业务单据，可以选择按照定义的审批流程被传递和审批。固定资产的绝大多数业务单据都支持审批流，通常审批流通过业务单据操作界面的【提交】按钮启动。用户可以在【动态建模平台】→【流程管理】→【流程设计】→【审批流定义】功能节点完整审批流的定义，详细定义过程请参见流程管理手册相关章节。

### 4. 业务流

定义企业业务流程的流程配置平台，可以任意根据用户的实际业务重新梳理业务单据、动作及组件，包括每种单据的来源单据是什么、又驱动生成哪些单据、完成什么动作、动作生效的约束条件以及动作生效后将配置哪些组件等，对发生的各种业务进行事前、事中、事后的控制，以此更好满足集团企业个性化管控需求。固定资产模块不支持业务流程配置。

#### 3.2.5 系统平台设置

##### 3.2.5.1 预警平台

用户通过预警平台统一设置系统预警任务，监控预警执行情况的平台。固定资产管理支持 2 个预警业务，以下为固定资产模块支持预警任务的清单：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>预警名称</td><td style='text-align: center; word-wrap: break-word;'>触发条件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>固定资产保修截止日期到期预警</td><td style='text-align: center; word-wrap: break-word;'>主要触发条件是，当系统当前业务日期接近固定资产卡片上的“保修截止日期”字段值的时候，即满足“当前系统日期-保修截止日期=X”的时候触发预警。同时还可以对资产的“残值/净值”、“账簿”、“所属财务组织”、“所属业务单元”进行配置，形成组合触发条件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固定资产逾龄资产预警</td><td style='text-align: center; word-wrap: break-word;'>固定资产逾龄资产预警</td><td style='text-align: center; word-wrap: break-word;'>主要触发条件是，当满足“（系统时间-开始使用日期）-使用年限=X”条件满足时，触发预警。</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>同还可以对“财务组织”、“财务核算账簿”、“净残值/净值”、“净残值/净额”、“累计工作量/工作总量”、“使用年限-已计提月份”进行设置，形成组合触发条件。</td></tr></table>

用户可以在【动态建模平台】→【系统平台】→【预警平台】功能节点，完成预警任务配置，包括预警条目配置、预警消息查询、业务预警监控、预警日志，默认情况下所有业务的预警任务都处于未配置状态。

### 3.3 固定资产模块初始化

#### 3.3.1 基础设置

基础设置共包括档案、期初数据录入两部分工作，其中档案为支撑固定资产模块正常业务运行的最基本的档案，需要在模块启用前完成维护。

##### 3.3.1.1 档案设置

用户可在【财务会计】→【固定资产】→【基础设置】功能节点完成下列重要档案的设置。

### 1. 资产类别

资产类别是对固定资产分类的描述性档案，资产类别为树状结构，NC 的固定资产类别不仅仅为简单的档案式描述内容，还包括了大量的业务逻辑与参数选项，也就是说不同资产类别可以具备不同的影响业务的属性，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_978_965_1374.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 3.3-01 资产类别</div>


### 2. 使用状况

使用状况是标识固定资产使用过程所处状态的重要档案，是个树状结构档案，系统预置了部分档案，通常情况预置的档案可以支撑固定资产常见业务的处理，用户可以新增自定义档案。

### 3. 折旧方法

折旧方法是固定资产最重要的基础档案之一，它直接影响固定资产的折旧与摊销规则，是系统自动计算折旧的基础。系统内置了常用的六种折旧方法：

➢ 不提折旧

➢ 平均年限法(一)

➢ 平均年限法(二)

➢ 工作量法

➢ 年数总和法

➢ 双倍余额递减法

五五摊销法

➢ 一次摊完法

并列出了它们的折旧计算公式。这几种方法是系统缺省的折旧方法，只能选用，不能删除和修改。如果内置的折旧设置不能满足企业业务的需要，系统提供了折旧方法的自定义功能，您可以定义自己合适的折旧方法的名称和计算公式。

### 4. 变动原因

固定资产在整个生命周期过程中，会发生很多变动，包括：使用部门、折旧方法、累计折旧调整等等，为了对变动进行跟踪分析，以便为固定资产的管理提供优化的数据支撑，有必要对每次变动的原因进行描述和记录。变动原因就是系统用来记录固定资产变动档案。

### 5. 减少原因

资产减少原因在发生资产减少业务时被引用。资产减少的原因主要有固定资产的调拨、报废、捐赠引发，所以减少的原因可以为业务动作的简称。减少原因没有系统内置，全部由用户自行维护。

### 6. 减值原因

减值原因是固定资产管理最基础的档案信息之一，即对造成资产减值原因的描述，例如：设备毁损、市场变动等，此档案在资产减值业务时被引用。此档案无内置信息，全部由用户自行维护。

### 7. 增减方式

在资产使用及管理过程中，很多资产业务都会造成资产实物的增加和减少，为了对资产的增加和减少行为进行跟踪分析，系统对资产增加减少方式进行档案管理。系统内置了常见业务可能引发的资产增加和减少方式的档案，如果这些档案不足以满足企业业务需求，用户可以根据自身需要定义适合自己企业的资产增减方式。

### 8. 资产组

资产组是指企业可以认定的最小资产组合，其产生的现金流入应当基本上独立于其他资产或者资产组。资产组应当由创造现金流入的相关资产组成。资产组档案在新增资产业务过程中可以被引用，是固定资产的一个重要属性。资产组也是总部资产的重要组成部分，关于总部资产概念请参见帮助相关术语。资产组是为了更加准确的计提固定资产减值准备而引入的概念，相关会计请参见会计准则。

##### 3.3.1.2 账簿信息

账簿信息是资产账簿设置的基础，在账簿信息中可以设置该账簿的核算范围、核算规则等信息。在多账簿应用中，通过设置不同的账簿，满足企业多账簿业务的需求。同一类资产可以在多个账簿中存在，并可以进行包括：折旧方法、减值是否转回、是否抵扣进项税等多个属性的设置。用户可以在【财务会计】→【固定资产】→【基础设置】→【账簿信息】功能节点完成账簿信息设置。

##### 3.3.1.3 参数设置

参数设置是通过对指定财务组织指定账簿的资产业务变动策略、帐表格式等信息的统一管理，实现对固定资产账簿，乃至具体业务的规范，如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_600_959_978.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 3.3-02 参数设置</div>


用户可在【财务会计】→【固定资产】→【基础设置】→【参数设置】功能节点，完成上述参数的维护设置，关于各个参数的详细说明以及设置过程，请参见系统帮助文档。

## 注意：

➢ 本章节涉及到的参数只能在最小未结账月进行修改。

##### 3.3.1.4 模拟折旧设置

如果用户希望进行固定资产模拟折旧，必须首先在【财务会计】→【固定资产】→【基础设置】→【模拟折旧设置】功能节点完成模拟折旧设置。模拟折旧设置即创建模拟折旧的方案，用户可以创建多种模拟折旧方案，根据不同的模拟折旧方案进行模拟折旧计算。

#### 3.3.2 期初数据准备

固定资产模块启动前需要录入大量期初数据，例如：原始卡片、资产分类，为了提高期初数据录入的效率和准确性，系统提供了部分工具。

##### 3.3.2.1 账簿初始化

如果用户存在多账簿应用需求，在固定资产多账簿的期初阶段，可以通过卡片导入将主账簿的卡片进行导入，然后可以通过账簿初始化将主账簿的数据初始化到报告账簿中，如果是用户在使用的固定资产一段时间后，有多账簿的应用需求，那么也可以启用另一个账簿，将当前的最大已结账月的数据初始化到另一个新建的账簿中。

##### 3.3.2.2 原始卡片录入

所谓原始卡片是用户在启用固定资产模块之前，就已经投入使用的固定资产，也就是说固定资产的开始使用时间早于固定资产账簿启用时间。用户可以在【财务会计】→【固定资产】→【期初数据】→【原始卡片录入】功能节点，完成原始卡片的录入工作。原始卡片上相关固定资产价值数据将作为总账资产科目的期初余额参考数据。系统不强制原始卡片必须在固定资产业务开始前完成录入，允许用户在固定资产模块正式启用后补录原始卡片，但补录的原始卡片仍然制作为期初数据体现，而不是新增资产。

##### 3.3.2.3 初始工具

为了提高设备类别、设备卡片的数据的录入效率，系统提供两个数据批量导入工具，如下：

### 1. 资产类别导入

用户可以在【财务会计】→【固定资产】→【初始工具】→【资产类别导入】功能节点，完成资产类别的批量导入。关于数据导入的详细操作请参见产品帮助。

### 2. 资产卡片导入

用户可以在【财务会计】→【固定资产】→【初始工具】→【资产卡片导入】功能节点，完成资产卡片的批量导入。关于数据导入的详细操作请参见产品帮助。

### 3. 附属设备导入

用户可以在【财务会计】→【固定资产】→【初始工具】→【附属设备导入】功能节点，完成资产卡片附属设备的批量导入。

### 3.4 多账簿设置

## 第一步：设置核算账簿类型

用户在【动态建模平台】→【组织管理】→【组织结构定义】→【账簿类型】功能节点，完成账簿类型设置。账簿类型是财务核算账簿的分类，是个模板式的档案，档案中集中描述了货币、会计期间、科目体系、核算要素等重要财务策略类信息。账簿类型是财务核算账簿的基础，必须完成账簿类型设置才能进行财务核算账簿设置。同时账簿类型也是进行固定资产账簿信息设置的基础。

## 第二步：设置财务核算账簿

用户在【动态建模平台】→【组织管理】→【组织结构定义】→【财务核算账簿】功能节点，完成财务核算账簿的设置。财务核算账簿是财务核算信息数据载体，同一个账簿类型下，同一个财务组织只能创建一个财务核算账簿。完成财务核算账簿创建后，需要启用对应核算账簿的总账、固定资产账。如下图所示：

<div style="text-align: center;"><img src="imgs/img_in_image_box_110_629_1077_1077.jpg" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 3.4-01 财务核算账薄</div>


## 第三步：设置固定资产账簿信息

用户在【财务会计】→【固定资产】→【基础设置】→【账簿信息】功能节点，依托第一步工作创建的账簿类型，完成固定资产多账簿的设置。用户可以自行添加资产分类，并完成完成各个资产类别默认的折旧方法、是否提取折旧、是否抵扣税、本币原值来源等信息设置。不同账簿类型下可以包含不同资产类别的资产，以及不同折旧方法、是否提取折旧、是否抵扣税、本币原值来源等信息，进而实现对不同会计政策的适配。如下图：

<div style="text-align: center;"><img src="imgs/img_in_image_box_221_149_962_482.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图 3.4-02 账簿信息</div>


关于账簿中各个字段属性的业务含义请参见帮助文档。

## 第三步：设置会计平台

如果用户同时部署了总账模块，则需要在【动态建模平台】→【会计平台】功能节点完成包括：转换模板、分类定义、入账规则等基础设置。详细设置过程请参见系统帮助。

## 第四章 操作指南

关于固定资产模块详细操作请参见产品帮助系统，此处不做赘述。

## 附录

## 附录 1：单据流转

### 1. 资产卡片


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="4">来源</td><td style='text-align: center; word-wrap: break-word;'>转固单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td rowspan="4">资产增加业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>新增资产审批单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>盘盈单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>设备卡片</td><td style='text-align: center; word-wrap: break-word;'>资产信息管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr></table>

### 2. 转固单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="3">来源</td><td style='text-align: center; word-wrap: break-word;'>采购到货单</td><td style='text-align: center; word-wrap: break-word;'>库存管理</td><td style='text-align: center; word-wrap: break-word;'>供应链</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>采购到货</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>采购入库单</td><td style='text-align: center; word-wrap: break-word;'>库存管理</td><td style='text-align: center; word-wrap: break-word;'>供应链</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>采购入库</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调拨入库单</td><td style='text-align: center; word-wrap: break-word;'>库存管理</td><td style='text-align: center; word-wrap: break-word;'>供应链</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>库存调拨</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>去向</td><td style='text-align: center; word-wrap: break-word;'>固定资产卡片</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>采购转固</td></tr></table>

### 3. 资产新增资产审批单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>去向</td><td style='text-align: center; word-wrap: break-word;'>资产卡片</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>新增资产审批</td></tr></table>

<div style="text-align: center;">4. 资产合并单</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="2">去向</td><td style='text-align: center; word-wrap: break-word;'>资产减少单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td rowspan="2">资产合并业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产卡片</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr></table>

### 5. 资产拆分单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="2">去向</td><td style='text-align: center; word-wrap: break-word;'>资产减少单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td rowspan="2">资产拆分业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产卡片</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr></table>

### 6. 盘点单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="3">去向</td><td style='text-align: center; word-wrap: break-word;'>资产盘盈单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td rowspan="3">资产盘点业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产减少单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr></table>

### 7. 盘盈单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>来源</td><td style='text-align: center; word-wrap: break-word;'>盘点单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产盘点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>去向</td><td style='text-align: center; word-wrap: break-word;'>资产卡片</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>盘盈新增卡片</td></tr></table>

### 8. 资产减少单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="5">来源</td><td style='text-align: center; word-wrap: break-word;'>资产报废</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产报废业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产所有权调出</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>所有权调出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产捐赠</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产捐赠</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产处置</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产处置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产盘亏</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产盘亏</td></tr></table>

### 9. 资产变动单（设备联动调整）


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="13">来源</td><td style='text-align: center; word-wrap: break-word;'>资产领用单</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>领用业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>领用归还单</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>领用归还业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产借用单</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产借用业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>借用归还单</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>借用归还业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（管理部门）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td rowspan="8"></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（使用部门）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（责任人）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（位置）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（状态）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（启封）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（封存）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产变动（项目）</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用权调出</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>使用权调出</td></tr></table>


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>盘点差异调整</td><td style='text-align: center; word-wrap: break-word;'>资产使用管理</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>盘点业务</td></tr></table>

### 10. 资产调出单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td rowspan="2">去向</td><td style='text-align: center; word-wrap: break-word;'>资产调入</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td rowspan="2">资产调出业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>资产减少单</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td></tr></table>

### 11. 资产调入单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>来源与去向</td><td style='text-align: center; word-wrap: break-word;'>单据名称</td><td style='text-align: center; word-wrap: break-word;'>所属模块</td><td style='text-align: center; word-wrap: break-word;'>所属领域</td><td style='text-align: center; word-wrap: break-word;'>是否流程</td><td style='text-align: center; word-wrap: break-word;'>对应业务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>来源</td><td style='text-align: center; word-wrap: break-word;'>资产调出</td><td style='text-align: center; word-wrap: break-word;'>固定资产</td><td style='text-align: center; word-wrap: break-word;'>资产管理</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>资产调入业务</td></tr></table>

## 附录 2：控制点

### 1. 模块参数

下表列示的为固定资产模块的所有参数及说明，关于参数配置的相关操作请参见基础数据手册相关章节。


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>所属组织</td><td style='text-align: center; word-wrap: break-word;'>参数编号</td><td style='text-align: center; word-wrap: break-word;'>参数说明</td></tr><tr><td rowspan="4">集团</td><td style='text-align: center; word-wrap: break-word;'>BD102</td><td style='text-align: center; word-wrap: break-word;'>资产类别编码级次</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BD103</td><td style='text-align: center; word-wrap: break-word;'>默认折旧方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BD803</td><td style='text-align: center; word-wrap: break-word;'>资产调拨时资产原值入账价值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA73</td><td style='text-align: center; word-wrap: break-word;'>资产类别集团控制到第几级</td></tr><tr><td rowspan="15">组织</td><td style='text-align: center; word-wrap: break-word;'>FA01</td><td style='text-align: center; word-wrap: break-word;'>本财务组织是否计提折旧</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA05</td><td style='text-align: center; word-wrap: break-word;'>折旧费用承担部门</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA06</td><td style='text-align: center; word-wrap: break-word;'>净残值率小数位</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA10</td><td style='text-align: center; word-wrap: break-word;'>账簿信息设置中资产类别中的参数在卡片中是否可修改</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA11</td><td style='text-align: center; word-wrap: break-word;'>公司间资产调拨产生新资产的资产编号是否可修改</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA15</td><td style='text-align: center; word-wrap: break-word;'>是否可修改折旧清单</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA30</td><td style='text-align: center; word-wrap: break-word;'>月折旧率小数位</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA40</td><td style='text-align: center; word-wrap: break-word;'>资产调入时是否携带出资产的自定义项</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA60</td><td style='text-align: center; word-wrap: break-word;'>净残值允许最大误差</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA74</td><td style='text-align: center; word-wrap: break-word;'>编辑资产管理部门、使用部门时是否允许选择非末级</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA75</td><td style='text-align: center; word-wrap: break-word;'>录入调出单时，是否控制调入公司权限</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA76</td><td style='text-align: center; word-wrap: break-word;'>资产套号编码方式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA77</td><td style='text-align: center; word-wrap: break-word;'>资产套号序号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA81</td><td style='text-align: center; word-wrap: break-word;'>资产入账价值（本币原值）是否允许大于新增资产审批单申请金额</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FA82</td><td style='text-align: center; word-wrap: break-word;'>模拟折旧资产类别显示到几级</td></tr></table>

## 附录 3：查询报表

### 1. 帐表查询

## 1 ) 卡片台账

卡片台账为查询统计固定资产卡片信息，既包括价值数据也包括业务数据。该台账可以对指定账簿、会计期间、卡片类别等固定资产卡片绝大多数字段信息进行查询统计，同时支持联查卡片详细信息。此台账适用于对固定资产的业务信息以及价值信息进行总体了解。支持卡片连续打印功能。

## 2 ) 变动单台账

变动单台账是对变动业务进行查询统计的台账，可对变动单上大多数字段信息进行条件是查询汇总，并支持联查变动单以及固定资产卡片。此台账适用于对变动业务进行总体了解。

## 3 ) 资产明细查询

资产明细查询是对固定资产卡片所有业务的汇总，包括：资产新增、变动、减值、减少、折旧提及等业务，对每笔业务对固定资产价值的影响进行列示，包括：原值、净值、累计折旧、减值准备等价值数据的借、贷、余额信息，并按照时间进行分组排序，甚至可以查询凭证信息。适用于对固定资产详细价值变动进行跟踪，可以作为编制资产负债表的辅助数据。

## 4 ) 折旧计算明细查询

折旧计算明细查询是对所有固定资产卡片折旧计提数据的统计，包括固定资产的原值、当期折旧、累计折旧、净值、净额、减值准备等信息。支持用户自定义分组，包括：资产类别、使用部门、管理部门、使用人、增减方式等维度，共支持9级分组。对于资产类别、使用部门等自身为树状的档案维度，支持按照多级展现，展现级次可以自定义。适用于用户对指定会计期间范围内的固定资产折旧数据进行分析。

## 5 ) 折旧汇总查询

折旧汇总查询是针对指定会计期间内，按查询对象展现固定资产折旧数据汇总报表。

## 6 ) 价值汇总表

资产明细查询是对指定条件下的固定资产卡片价值数据的汇总查询，支持：账簿、财务组织、资产类别、使用部门、管理部门等多种查询条件。价值数据包括：原值、净值、累计折旧、减值准备等价值数据，并按照期初、期期末、差异三个维度展现。支持按照资产类别、使用部门、管理部门等维度进行多级汇总。此报表适用于对固定资产价值信息进行较深入的分析。

## 7 ) 减值准备汇总表

减值准备汇总表是对指定条件下的固定资产减值准备数据进行查询统计的报表。支持固定资产卡片上绝大多数字段作为查询条件，按照期初、本期增加、本期回转、期末四个维度展示数据。

## 8 ) 增减变动查询

增减变动查询是对固定资产增减业务的查询，支持按照：增减方式、资产类别、使用部门、管理部门等维度自定义多级汇总，主要展现固定资产价值数据，包括：原值、累计折旧、净值、清理

收入、清理费用、增减日期等重要数据。

## 9 ) 统计分析查询

对固定资产价值数据进行全面统计分析的报表，支持固定资产卡片上绝大多数字段作为查询条件，支持按照：资产类别、使用部门、管理部门、使用人、折旧方法等维度进行多级别汇总设置。

## 10 ) 役龄统计表

对所有在役固定资产卡片进行统计。

## 11 ) 逾龄统计表

对所有已经超龄的固定资产卡片进行统计。系统提供三个逾龄条件供用户选择。

## 12 ) 附属设备明细表

对固定资产的附属设备信息进行统计查询。

## 13 ) 资产评估汇总表

对资产评估业务进行统计，支持固定资产卡片上大多数字段作为查询条件。

## 14 ）管理部门查询

按照管理部门查询固定资产价值信息，按照管理部门为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

## 15 ) 使用部门查询

按照使用部门查询固定资产价值信息，按照使用部门为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

## 16 ) 使用情况查询

按照使用情况查询固定资产价值信息，按照使用情况为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

## 17 ) 增减情况查询

按照增减情况查询固定资产价值信息，按照使增减情况为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

### 2. 管理报表

与帐表查询相比，管理报表可以通过定制任务的方式，为同一个报表定制多个不同查询条件、接收人、执行方式的报表任务。

## 1 ) 卡片统计表

卡片台账为查询统计固定资产卡片信息，既包括价值数据也包括业务数据。该台账可以对指定账簿、会计期间、卡片类别等固定资产卡片绝大多数字段信息进行查询统计，同时支持联查卡片详细信息。次台账适用于对固定资产的业务信息以及价值信息进行总体了解。

## 2 ) 总账

固定资产总账是对企业固定资产核算一定期间内的全部经济业务按一定分类标准，将原值、累计折旧、净值、（减值准备、净额）按借、贷、余三栏的格式汇总反映价值变化的账页。

## 3 ) 明细账

固定资产明细账是分类登记一定期间内资产的详细变动情况的一种账簿，它将某一资产的原值、累计折旧、净值、(减值准备、净额)按借、贷、余三栏的格式详细反映固定资产的价值变化的账页。

## 4 ) 折旧计算明细表

固定资产折旧计算明细表是按指定分类统计上月计提原值、上月计提折旧、上月原值增减、本月计提原值、本月计提折旧的详细列表；本表是对折旧清单的分类汇总。

## 5 ) 折旧汇总表

折旧汇总表是针对指定会计期间内，按查询对象展现固定资产折旧数据汇总报表。

## 6 ) 价值汇总表

固定资产价值汇总表用来反映一段期间内按部门或类别统计固定资产原值、累计折旧、净值、减值准备、净额的变动情况。

## 7 ) 增减变动表

固定资产增减变动表是反映一定期间内固定资产以不同增减方式进行增减变动的详细情况。

## 8 ) 统计分析表

固定资产统计分析表是按指定期间对企业内所有固定资产按照不同的分类标准进行统计分析的报表。

## 9 ) 管理部门一览表

按照管理部门查询固定资产价值信息，按照管理部门为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

## 10 ）使用部门一览表

按照使用部门查询固定资产价值信息，按照使用部门为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

## 11 ）使用状况一览表

按照使用状况查询固定资产价值信息，按照使用状况为纵向维度，资产类别作为横向一级维度，原值、累计折旧、减值准备为二级横向维度展现。

## 附录 4：本文参见其他手册清单


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>序号</td><td style='text-align: center; word-wrap: break-word;'>手册名称</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>01</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-资产信息管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>02</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-采购管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>03</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-基础数据》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>04</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-组织管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>05</td><td style='text-align: center; word-wrap: break-word;'>《产品手册-权限管理》</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_487_439_695_591.jpg" alt="Image" width="17%" /></div>


# 大型企业管理与电子商务平台

# Large-scale Enterprise Management and E-business Solution Platform

用友网络科技股份有限公司

Yonyou Network Tech Co. Ltd.
