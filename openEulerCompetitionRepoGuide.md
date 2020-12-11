---


---

<h1 id="teaminfo-格式规范">TEAMINFO 格式规范</h1>
<h2 id="背景">背景</h2>
<p>2020 openEuler 高校开发者大赛采用一个团队一个代码仓库，分组提交参赛代码的方式。依托码云（gitee）良好的代码托管服务，我们组委会为大家申请了一个专门为本次大赛服务的竞赛组织 <a href="https://gitee.com/openeuler2020">openEuler2020</a>, 并计划在该组织下为各个参赛团队新建代码仓库和添加参赛者权限。我们会根据各位参赛者在本仓库的teaminfo.yaml中提交的仓库信息和团队成员信息来建仓和加权限。所以希望各位参赛者能完整、清晰地提交团队、参赛者、仓库、导师等信息。<br>
具体的配置文件信息说明请见下文。</p>
<h2 id="格式说明">格式说明</h2>
<p>团队信息采用yaml格式文件承载，格式如下：</p>

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
<td>giteeurl</td>
<td>字符串</td>
<td>在码云上的组织URL地址</td>
</tr>
<tr>
<td>teams</td>
<td>清单</td>
<td>各个参赛团队的团队信息</td>
</tr>
</tbody>
</table><pre><code>community: openeuler2020
giteeurl: https://gitee.com/openeuler2020
teams:
- teamid: 0000
  teamname: OSCHINA
  description: "This  is  a  template  repository."
  repository: template
  type: public
  tutor:
  - biglizi
  members:
  - leikeke
  - georgecao
</code></pre>

