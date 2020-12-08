---


---

<h1 id="openeuler-infra-faq">openEuler-Infra-FAQ</h1>
<hr>
<ol>
<li><strong>请问我为什么不能fork一个src-openeuler/abcd仓库到我自己个人账号下？</strong><br>
这个问题通常是因为在你的个人账号下，已经有abcd的同名仓库，比如你之前已经从openeuler组织下fork的abcd仓库；因为码云是通过你的个人账号加仓库名寻址的，所有不允许在你个人账号下有同名仓库。<br>
修改个人账户下已有仓库的名称和路径，然后再从 src-openeuler/abcd 仓库fork。</li>
</ol>
<hr>
<ol start="2">
<li><strong>请问普通贡献者（非maintainer）是否可以直接往非保护分支push代码？</strong><br>
抱歉，普通贡献者不能直接向仓库push代码，包括保护分支和非保护分支。<br>
保护分支与非保护分支的区别在于maintainer是否可以直接push；如果是非保护分支，maintainer可以有权限直接push；如果是保护分支maintainer也没有权限直接push，只能通过评估最终由CI-bot代为合入。</li>
</ol>
<hr>
<ol start="3">
<li><strong>请问maintainer可否直接push代码到仓库？</strong><br>
该问题需要确定代码合入到仓库的具体分支属性，如果分支为保护分支，maintainer没有权限直接push代码；如果分支为非保护分支，maintainer可以直接push代码。</li>
</ol>
<hr>
<ol start="4">
<li><strong>请问直接push代码到仓库和通过评论/lgtm 、/approve合入代码有何区别？</strong><br>
通过git命令直接push代码到仓库缺少必要的审核环节，存在一定合入风险；主要应用场景是比如需要上传的文件过大超过个人仓库限制，只能通过直接push到企业仓库的非保护分支，然后再通过非保护分支往保护分支merge；<br>
通过评论/lgtm /approve合入代码从流程上增加了评审环节，保证一份代码的合入至少需要提交者以外的一位maintainer的评审同意，即便提交者本人是maintainer也需要另一位maintainer同意。</li>
</ol>
<hr>
<ol start="5">
<li><strong>请问openEuler社区仓库评论区都支持哪些命令，分别都是什么含义？</strong><br>
目前社区仓库评论区主要支持的命令:<br>
<a href="https://gitee.com/openeuler/community/blob/master/en/sig-infrastructure/command.md">https://gitee.com/openeuler/community/blob/master/en/sig-infrastructure/command.md</a></li>
</ol>

