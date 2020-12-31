# openEuler基础设施介绍
## 引言
您是否已经参与openEuler社区代码贡献？提交代码后可曾留意到PR评论区有个CI-bot的机器人在为您的PR发出评论？
CI-bot机器人就是我们基础设施在社区最直接的展示，它会通过评论和社区用户交互，帮助用户的代码合入。
当前openEuler基础设施支撑1400多开发者，它是如何设计、实现的？它又是如何确保各类服务快速上线的？还有基础设施的架构能否支持伸缩扩展，达到支撑10000开发者目标？
今天带大家一起看看openEuler基础设施的建设情况。
## 认识基础设施团队
我们团队建立之初只有3人，发展到现在，已经有committer 15人；额外的contributor接近40人。这其中有不少开源老炮，有开源CI专家，有UI专家，还有操作系统构建专家……
committers:
> @dogsheng @miao_kaibo @freesky-edward @imjoey @TommyLike @xiangxinyong @yinjiayi @tracedeng @zengchen1024 @zerodefect @zhuchunyi @zhongjun2 @zhengyuhanghans @genedna @georgecao

## 见证社区基础设施的成长
2019.08.10  openEuler Infrastructure SIG 诞生；
2019.08.13 Infrastructure 在Gitee创建代码仓；
2019.08.20 Infrastructure 代码仓提交第一个PR；
2019.08.21 Infrastructure 代码仓创建第一条issue；
2019.09.04 Infrastructure 仓库收获第一颗Star开始被外界关注；
2019.10.15 Infrastructure 重点服务 openEuler ci bot上线,发出第一条评论，开始 ta 的职业生涯；
2019.12.31 openEuler社区开源 Infrastructure 转正，面向社区所有开发者提供线上服务；
2020.08.10 Infrastructure 一周岁，累计上线服务30+；
截止2020.12.24 基础设施的数据：
|  数据项| 数值 |
|--|--|
|Infrastructure-SIG Committer | 15 |
|Gatekeeper-SIG Committer | 10 |
|CI-Bot commit 代码行 | 225'211'000|
|CI-Bot 社区评论|46'500|
|Infra Jenkins 任务数|29'850|
|Open Build Service 构建包|4'300|
|社区用户|19'072|
|社区开发者|1'459|
## openEuler基础设施现状
基础设施前期的目标是借助云原生生态支撑基础设施能力的快速构建，提供统一规范的基础设施发布平台，支撑社区服务应用快速上线和迭代;
当前这个目标已经基本达成，openEuler社区上线包括网站，会议系统，CLA，Jenkins，机器人，运营看板，CVE管理等基础设施服务32个。
![enter image description here](./image/wordcloud.png)
基础设施都是采用组件化服务，不论是部署业界已有的服务还是我们基础设施自己开发的新服务，一律使用开源组件；这样的好处是可以有效避免后期缺乏维护的风险，且组件可以及时更新完善。
我们这里列举一些您经常会使用到的组件：

