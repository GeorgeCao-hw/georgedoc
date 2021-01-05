---


---

<h1 id="the-configuration-guide-of-openeuler-repository">The Configuration Guide of openEuler Repository</h1>
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
</table><p>Each element in the <strong>repositories</strong> list represents a repository and is presented as a relational array. The following subelements are required:</p>

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
</table><p>Each element in the branches list represents a managed branch and is presented as a relational array. The following sub-elements are required:</p>

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
<td align="left">Branch name</td>
</tr>
<tr>
<td align="left">type</td>
<td align="left">enumeration，optional，protected/readonly</td>
<td align="left">Branch type. Set this parameter based on Gitee branch attribute. <strong>protected</strong> indicates that the branch can be integrated in the released version. <strong>readonly</strong> indicates that the branch is not maintained.</td>
</tr>
<tr>
<td align="left">create_from</td>
<td align="left">string</td>
<td align="left">Start point for creating a branch. When <strong><a href="http://branches.name">branches.name</a></strong> is master, this string is empty. Set it the name of an existing branch or tag when creating another branch. The default value is master.</td>
</tr>
</tbody>
</table><h3 id="remarks">Remarks</h3>
<p>If the tool fails to obtain <strong>format_version</strong> when processing this, the value of <strong>format_version</strong> is 1.0.</p>
<p>When <strong>format_version</strong> changes later, if the integer part of <strong>format_version</strong> remains unchanged, the tool does not need to be modified. If the integer part of <strong>format_version</strong> changes, all tools need to be adapted again.</p>
<h3 id="example">Example</h3>
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
<h2 id="version-1">Version 1</h2>
<h3 id="major-changes-1">Major changes</h3>
<ul>
<li>Initial version of the openEuler community</li>
</ul>
<h3 id="format-guide-1">Format Guide</h3>
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
</table><p>Each element in the <strong>repositories</strong> list represents a repository and is presented as a relational array. The following subelements are required:</p>

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
</table>
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
<td align="left">protected_branches</td>
<td align="left">list</td>
<td align="left">Name list of the protected branches</td>
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
</tbody>
</table><h3 id="example：">example：</h3>
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

