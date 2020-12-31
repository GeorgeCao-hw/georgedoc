---


---

<h1 id="openeuler基础设施介绍">openEuler基础设施介绍</h1>
<h2 id="引言">引言</h2>
<p>您是否已经参与openEuler社区代码贡献？提交代码后可曾留意到PR评论区有个CI-bot的机器人在为您的PR发出评论？<br>
CI-bot机器人就是我们基础设施在社区最直接的展示，它会通过评论和社区用户交互，帮助用户的代码合入。<br>
当前openEuler基础设施支撑1400多开发者，它是如何设计、实现的？它又是如何确保各类服务快速上线的？还有基础设施的架构能否支持伸缩扩展，达到支撑10000开发者目标？<br>
今天带大家一起看看openEuler基础设施的建设情况。</p>
<h2 id="认识基础设施团队">认识基础设施团队</h2>
<p>我们团队建立之初只有3人，发展到现在，已经有committer 15人；额外的contributor接近40人。这其中有不少开源老炮，有开源CI专家，有UI专家，还有操作系统构建专家……<br>
committers:</p>
<blockquote>
<p>@dogsheng @miao_kaibo @freesky-edward @imjoey @TommyLike @xiangxinyong @yinjiayi @tracedeng @zengchen1024 @zerodefect @zhuchunyi @zhongjun2 @zhengyuhanghans @genedna @georgecao</p>
</blockquote>
<h2 id="见证社区基础设施的成长">见证社区基础设施的成长</h2>
<p>2019.08.10  openEuler Infrastructure SIG 诞生；<br>
2019.08.13 Infrastructure 在Gitee创建代码仓；<br>
2019.08.20 Infrastructure 代码仓提交第一个PR；<br>
2019.08.21 Infrastructure 代码仓创建第一条issue；<br>
2019.09.04 Infrastructure 仓库收获第一颗Star开始被外界关注；<br>
2019.10.15 Infrastructure 重点服务 openEuler ci bot上线,发出第一条评论，开始 ta 的职业生涯；<br>
2019.12.31 openEuler社区开源 Infrastructure 转正，面向社区所有开发者提供线上服务；<br>
2020.08.10 Infrastructure 一周岁，累计上线服务30+；<br>
截止2020.12.24 基础设施的数据：</p>

<table>
<thead>
<tr>
<th>数据项</th>
<th>数值</th>
</tr>
</thead>
<tbody>
<tr>
<td>Infrastructure-SIG Committer</td>
<td>15</td>
</tr>
<tr>
<td>Gatekeeper-SIG Committer</td>
<td>10</td>
</tr>
<tr>
<td>CI-Bot commit 代码行</td>
<td>225’211’000</td>
</tr>
<tr>
<td>CI-Bot 社区评论</td>
<td>46’500</td>
</tr>
<tr>
<td>Infra Jenkins 任务数</td>
<td>29’850</td>
</tr>
<tr>
<td>Open Build Service 构建包</td>
<td>4’300</td>
</tr>
<tr>
<td>社区用户</td>
<td>19’072</td>
</tr>
<tr>
<td>社区开发者</td>
<td>1’459</td>
</tr>
</tbody>
</table><h2 id="openeuler基础设施现状">openEuler基础设施现状</h2>
<p>基础设施前期的目标是借助云原生生态支撑基础设施能力的快速构建，提供统一规范的基础设施发布平台，支撑社区服务应用快速上线和迭代;<br>
当前这个目标已经基本达成，openEuler社区上线包括网站，会议系统，CLA，Jenkins，机器人，运营看板，CVE管理等基础设施服务32个。<br>
<img src="./image/wordcloud.png" alt="enter image description here"><br>
基础设施都是采用组件化服务，不论是部署业界已有的服务还是我们基础设施自己开发的新服务，一律使用开源组件；这样的好处是可以有效避免后期缺乏维护的风险，且组件可以及时更新完善。<br>
我们这里列举一些您经常会使用到的组件：</p>
<ol>
<li><strong>CLA Sign</strong>：进入社区开始贡献前，您第一步需要签署代码贡献协议，需要签署CLA，基础设施提供CLA Sign服务；</li>
<li><strong>Prow+</strong>：</li>
</ol>

