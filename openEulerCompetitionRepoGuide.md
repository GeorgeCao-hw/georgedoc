---


---

<h1 id="teaminfo-格式规范">TEAMINFO 格式规范</h1>
<h2 id="背景">背景</h2>
<p>2020 openEuler 高校开发者大赛采用一个参赛团队一个代码仓库，分组提交参赛代码的方式。依托码云（gitee）良好的代码托管服务，我们组委会为大家申请了一个专门为本次大赛服务的竞赛组织 <a href="https://gitee.com/openeuler2020">openEuler2020</a>, 并计划在该组织下为各个参赛团队新建代码仓库和添加参赛者权限。我们会根据各位参赛者在本仓库的teaminfo.yaml中提交的仓库信息和团队成员信息来建仓和加权限。所以希望各位参赛者能完整、清晰地提交团队、参赛者、仓库、导师等信息。<br>
具体的配置文件信息说明请见下文。</p>
<h2 id="格式说明">格式说明</h2>
<p>大赛代码仓库的组织管理信息采用yaml格式文件记录承载，格式如下：</p>

<table>
<thead>
<tr>
<th>字段</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>community</td>
<td>字符串</td>
<td>组织名称，由大赛组委会指定</td>
</tr>
<tr>
<td>verison</td>
<td>浮点数</td>
<td>文件规范版本，由大赛组委会指定</td>
</tr>
<tr>
<td>giteeurl</td>
<td>字符串</td>
<td>在码云上的组织URL地址，由大赛组委会指定</td>
</tr>
<tr>
<td>teams</td>
<td>清单</td>
<td>各个参赛队的团队信息</td>
</tr>
</tbody>
</table><p>其中teams清单中单个队伍的信息格式如下：</p>

<table>
<thead>
<tr>
<th>字段</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>teamid</td>
<td>整型</td>
<td>参赛队ID号，必填</td>
</tr>
<tr>
<td>teamname</td>
<td>字符串</td>
<td>参赛队名称，必填</td>
</tr>
<tr>
<td>description</td>
<td>字符串</td>
<td>参赛队详细信息描述，必填，需注明参赛赛题题号、队伍编号、团队名称</td>
</tr>
<tr>
<td>repository</td>
<td>字符串</td>
<td>参赛队详细信息描述，必填</td>
</tr>
<tr>
<td>repotype</td>
<td>枚举，public/private</td>
<td>参赛队的代码仓库类型，public为公开仓代码所有人可见，private为私有仓仅仓库成员和组织管理员可见；由于比赛性质，建议比赛阶段设置为private，比赛结束后改为public；必填</td>
</tr>
<tr>
<td>tutor</td>
<td>清单</td>
<td>一位或两位出题导师信息清单，一条记录为一位导师信息，必填</td>
</tr>
<tr>
<td>members</td>
<td>清单</td>
<td>参赛队队员信息清单，一条记录为一位参赛队员信息，必填</td>
</tr>
</tbody>
</table><p>其中tutor和members清单中一条记录的信息格式如下：</p>

<table>
<thead>
<tr>
<th>字段</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>giteeid</td>
<td>字符串数组</td>
<td>该用户的gitee ID信息</td>
</tr>
<tr>
<td>email</td>
<td>字符串数组</td>
<td>该用户向gitee注册的邮箱地址信息</td>
</tr>
</tbody>
</table><h2 id="样例">样例</h2>
<pre><code>community: openeuler2020
version: 1.0
giteeurl: https://gitee.com/openeuler2020
teams:
- teamid: 123324214343
  teamname: "OSCHINA"
  description: "赛题77，团队编号：0000，团队名称：OSCHINA"
  repository: template
  repotype: private
  tutor: 
  - giteeid: biglizi
    email: chenshuyu@oschina.cn
  members:
  - giteeid: leikeke
    email: leikeke2@huawei.com
  - giteeid: georgecao
    email: caozhi1214@qq.com
</code></pre>

