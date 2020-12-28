---


---

<h1 id="openeuler基础设施介绍">openEuler基础设施介绍</h1>
<h2 id="引言">引言</h2>
<p>您是否已经参与openEuler社区代码贡献？提交代码后可曾留意到PR评论区有个CI-bot的机器人在为您的PR发出评论？<br>
CI-bot机器人就是我们基础设施在社区最直接的展示，它会通过评论和社区用户交互，帮助用户的代码合入。<br>
当前openEuler基础设施支撑1400多开发者，它是如何设计、实现的？它又是如何确保各类服务快速上线的？还有基础设施的架构能否支持伸缩扩展，达到支撑10000开发者目标？<br>
今天带大家一起看看openEuler基础设施的建设情况。</p>
<h2 id="openeuler基础设施团队">openEuler基础设施团队</h2>
<p>committers:</p>
<blockquote>
<p>@dogsheng @miao_kaibo @freesky-edward @imjoey @TommyLike @xiangxinyong<br>
@zerodefect @zhuchunyi @zhongjun2 @zhengyuhanghans @genedna @georgecao</p>
</blockquote>
<h2 id="openeuler基础设施成长">openEuler基础设施成长</h2>
<p>2019.08.10  openEuler Infrastructure SIG 诞生<br>
2019.08.13 Infrastructure 在Gitee创建代码仓<br>
2019.08.20 Infrastructure代码仓提交第一个PR<br>
2019.08.21 Infrastructure 代码仓创建第一条issue<br>
2019.09.04 Infrastructure仓收获第一颗Star开始被外界关注<br>
2019.10.15 Infra重点服务 openEuler ci bot上线,发出第一条评论，开始 ta 的职业生涯<br>
2019.12.31 openEuler社区开源 Infra转正<br>
2020.08.10 Infrastructure 一周岁，累计上线服务30+<br>
截止2020.12.24 基础设施的数据</p>

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
<p>基础设施前期目标是借助云原生生态支撑基础设施能力的快速构建，提供统一规范的基础设施发布平台，支撑社区服务应用快速上线和迭代;<br>
当前这个目标已经基本达成，openEuler社区已经上线包括网站，会议系统，CLA，Jenkins，机器人，运营看板，CVE管理等基础设施服务32个。<br>
<img src="./image/wordcloud.png" alt="enter image description here"></p>

