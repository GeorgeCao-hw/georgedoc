---


---

<h1 id="format-guide-of-openeuler-repository-configuration-file">Format Guide of openEuler Repository Configuration File</h1>
<p>Versions：</p>

<table>
<thead>
<tr>
<th align="left">version</th>
<th align="left">author</th>
<th align="left">begin</th>
<th align="left">explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">1.0</td>
<td align="left">George.Cao，Shinwell_Hu</td>
<td align="left">2020-11-24</td>
<td align="left">Describe the format of the initial version and the recommended format of version 2.0.</td>
</tr>
</tbody>
</table><h2 id="background">Background</h2>
<p>The <strong>openeuler.yaml</strong> and <strong>src-openeuler.yaml</strong> files in the directory of the <a href="https://gitee.com/openeuler/community/tree/master/repository">https://gitee.com/openeuler/community/tree/master/repository</a> manage metadata information of all repositories in openEuler community and guide all automation tools. This document describes the formats of the preceding two configuration files, helping tool development teams and community contributors understand how to submit pull requests that meet requirements.</p>
<p>The format specifications of the following versions are sorted in descending order of time to facilitate search. Disabled format specifications are still archived here for backtracking.</p>
<h2 id="version-2">Version 2</h2>
<h3 id="major-changes">Major changes</h3>
<ul>
<li>Add format version information.</li>
<li>Add the inheritance relationship information of branches in the repositories.</li>
</ul>
<h3 id="format-guide">Format Guide</h3>
<p>The configuration file is in YAML format and contains the following basic elements:</p>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">Type</th>
<th align="left">Remarks</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">format_version</td>
<td align="left">float</td>
<td align="left"><strong>New in this version</strong>, Version id of this configuration file. The value is changed when the file format changes.</td>
</tr>
<tr>
<td align="left">community</td>
<td align="left">enumeration，optional， openeuler or src-openeuler</td>
<td align="left">organization name，current names：openeuler or src-openeuler</td>
</tr>
<tr>
<td align="left">repositories</td>
<td align="left">list</td>
<td align="left">All repositories under the organization</td>
</tr>
</tbody>
</table><p>Each element in the <strong>repositories</strong> list represents a code repository and is presented as a relational array. The following subelements are required:</p>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">Type</th>
<th align="left">Remarks</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">name</td>
<td align="left">string</td>
<td align="left">repository name</td>
</tr>
<tr>
<td align="left">rename_from</td>
<td align="left">string</td>
<td align="left">Original repository name. This sub-element is optional and is required only when the repository is renamed from another repository.</td>
</tr>
<tr>
<td align="left">description</td>
<td align="left">string</td>
<td align="left">Description of the component contained in the repository</td>
</tr>
<tr>
<td align="left">type</td>
<td align="left">enumeration，optional，public or private</td>
<td align="left">repository type. The private repository does not provide open access.</td>
</tr>
<tr>
<td align="left">upstream</td>
<td align="left">string</td>
<td align="left">Indicates the upstream community information of the repository. When organization is src-openeuler, this sub-element must be provided. This parameter is optional when organization is openEuler and the project is an original project of the community.</td>
</tr>
<tr>
<td align="left">branches</td>
<td align="left">list</td>
<td align="left"><strong>Changed in this version</strong>，Information about all branches in this repository</td>
</tr>
</tbody>
</table><p>branches 清单中每个元素代表一个受管理的分支，以关系数组的方式呈现，需要包含以下子元素:</p>

<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">类型</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">name</td>
<td align="left">字符串</td>
<td align="left">分支名称</td>
</tr>
<tr>
<td align="left">type</td>
<td align="left">枚举类型，可选protected/readonly</td>
<td align="left">分支类型，对照码云分支属性设置，protected 表示该分支可以被发布版本集成，readonly 表示该分支停止维护</td>
</tr>
<tr>
<td align="left">create_from</td>
<td align="left">字符串</td>
<td align="left">分支创建起点，当 <a href="http://branches.name">branches.name</a> 为 master 时，字符串为空；新创其他分支时设置已存在的分支名或tag名，缺省为master</td>
</tr>
</tbody>
</table><h3 id="说明">说明</h3>
<p>当工具处理本文件时未能获取 format_version，可以认为 format_version 为 1.0</p>
<p>后续当format_version变更时，约定若format_version的整数部分不变，则工具可以不做任何修改；若format_version整数部分变动，则所有工具都需要重新适配。</p>
<h3 id="样例">样例</h3>
<pre><code>format_version: 2.0
community: src-openeuler
repositories:
- name: A-Tune
  description: 'This is a repo for ……'
  branches:
  - name: master
    type: protected
  - openEuler-20.03-LTS
    type: protected
    create_from: master
  - openEuler-20.09
    type: protected
    create_from: master
  type: public
- name: A-Tune-UI
  description: 'Web server for A-Tune'
  upstream: https://gitee.com/openeuler/A-Tune-UI
  branches:
  - name: master
    type: protected
  type: public
</code></pre>
<h2 id="版本-1">版本 1</h2>
<h3 id="主要改变">主要改变</h3>
<ul>
<li>openEuler 社区最初版本</li>
</ul>
<h3 id="格式规范">格式规范</h3>
<p>配置文件整体以yaml格式承载，包含两个基本元素：</p>

<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">类型</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">community</td>
<td align="left">枚举类型，可选 openeuler 或者 src-openeuler</td>
<td align="left">组织名称</td>
</tr>
<tr>
<td align="left">repositories</td>
<td align="left">清单</td>
<td align="left">该组织下所有仓库信息，包含子字段</td>
</tr>
</tbody>
</table><p>repositories清单中每个元素代表一个代码仓，以关系数组的方式呈现，需要包含以下子元素：</p>

<table>
<thead>
<tr>
<th align="left">名称</th>
<th align="left">类型</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">name</td>
<td align="left">字符串</td>
<td align="left">仓库名称</td>
</tr>
<tr>
<td align="left">rename_from</td>
<td align="left">字符串</td>
<td align="left">仓库原名称。这个子元素为可选，只有该代码仓是从另一个代码仓改名而来时才需要</td>
</tr>
<tr>
<td align="left">description</td>
<td align="left">字符串</td>
<td align="left">仓库信息描述</td>
</tr>
<tr>
<td align="left">protected_branches</td>
<td align="left">清单</td>
<td align="left">保护分支的分支名列表</td>
</tr>
<tr>
<td align="left">type</td>
<td align="left">枚举类型，可选 public 或者 private</td>
<td align="left">仓库类型。private代码仓不提供开放访问</td>
</tr>
<tr>
<td align="left">upstream</td>
<td align="left">字符串</td>
<td align="left">本代码仓对应的上游社区信息。当 community 为 src-openeuler时，这个子元素必须提供；否则为可选项 <strong>该子元素为中期添加，当时本文件尚未形成格式版本管理</strong></td>
</tr>
</tbody>
</table><p>样例：</p>
<pre><code>community: src-openeuler
repositories:
- name: A-Tune
  description: 'This is a repo for ……'
  protected_branches:
  - master
  - openEuler-20.03-LTS
  - openEuler-20.09
  type: public
- name: A-Tune-UI
  description: 'Web server for A-Tune'
  upstream: https://gitee.com/openeuler/A-Tune-UI
  protected_branches:
  - master
  type: public
</code></pre>

