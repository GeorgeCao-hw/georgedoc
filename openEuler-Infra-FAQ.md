# openEuler-Infra-FAQ
 
---
 1. **请问我如何在Gitee平台申请加入openEuler企业，成为组织成员？**  
请点击[链接](https://gitee.com/open_euler?invite=4bd118cb5f4df496cf260b2eec4d904fb23724c478f1a1b48e7cde0b62298f898e2a5d1b1b8079876b17c049295f276a1049f26840b012af)填写相关内容后申请加入即可；
申请通常会在第二天10点前审核生效；如未及时生效可邮件通知 infra@openeuler.org 。
---
 2. **请问如何在openEuler社区创建代码仓库？**  
openEuler社区代码仓库的创建、删除管理方式如下：  
&emsp; a.用户通过修改仓库配置文件，提交合入申请；  
&emsp; b.TC审核申请，审核通过后合入配置文件；审核过程可能会有疑问，请申请人跟踪PR状态；  
&emsp; c.社区机器人CI-bot根据仓库配置文件自动创建代码仓库；    
所以新增代码仓库只需要在[相应代码路径](https://gitee.com/openeuler/community/tree/master/repository)修改对应配置文件(openeuler.yaml or src-open)并提交PR申请即可，随后跟踪PR审核状态与仓库创建状态；
如果仓库配置代码合入2小时后，代码仓库尚未创建，可邮件联系 infra@openeuler.org 或者 [infrastructure仓库](https://gitee.com/openeuler/infrastructure)提issue。
 ---
 3. **请问提交PR后出现openeuler-cla/no红色标签，如何处理？**  
 出现该标签表示该PR中所包含的commit中，有部分贡献者没有签署openEuler社区的贡献者协议CLA。[签署地址](https://clasign.osinfra.cn/sign/Z2l0ZWUlMkZvcGVuZXVsZXI=)可以在PR评论区找到。如果是个人贡献者请选择“签署个人CLA”，如果是作为企业的员工参与贡献请选择“签署员工CLA”；作为企业员工再签署是时需要使用企业邮箱，比如 xxx@huawei.com 、xxxx@kylinos.cn等。  
 CLA检查是使用commit中author邮箱作为检查凭证的。该author邮箱可以通过git log查询到。
 如需修改邮箱配置，可在本体通过 git config --global user.name ****  和  git config --global user.email  ****修改配置。

  ---
 4. **请问为什么不能fork一个src-openeuler/abcd仓库到个人账号下？**  
这个问题通常是因为在您的个人账号下，已经有abcd的同名仓库，比如你之前已经从openeuler组织下fork的abcd仓库；因为码云是通过你的个人账号加仓库名寻址的，所有不允许在你个人账号下有同名仓库。
修改个人账户下已有仓库的名称和路径，然后再从 src-openeuler/abcd 仓库fork即可。
---
 5. **请问非maintainer贡献者是否可以直接往非保护分支push代码？**  
抱歉，非maintainer贡献者不能直接向仓库push代码，包括保护分支和非保护分支。
保护分支与非保护分支的区别在于maintainer是否可以直接push；如果是非保护分支，maintainer可以有权限直接push；如果是保护分支maintainer也没有权限直接push，只能通过评论最终由CI-bot代为合入。
---
 6. **请问maintainer可否直接push代码到仓库？**  
该问题需要确定代码合入到仓库的具体分支属性，如果分支为保护分支，maintainer没有权限直接push代码；如果分支为非保护分支，maintainer可以直接push代码。
---
 7. **请问直接push代码到仓库和通过评论/lgtm 、/approve合入代码有何区别？**  
通过git命令直接push代码到仓库缺少必要的审核环节，存在一定合入风险；主要应用场景是比如需要上传的文件过大超过个人仓库限制，只能通过直接push到企业仓库的非保护分支，然后再通过非保护分支往保护分支merge；
通过评论/lgtm /approve合入代码从流程上增加了评审环节，保证一份代码的合入至少需要提交者以外的一位maintainer的评审同意，即便提交者本人是maintainer也需要另一位maintainer同意。
---
 8. **请问openEuler社区仓库评论区都支持哪些命令，分别都是什么含义？**  
目前社区仓库评论区主要支持的命令:
https://gitee.com/openeuler/community/blob/master/en/sig-infrastructure/command.md
---
 9. **请问在华为公司内部使用git clone从码云克隆代码报超时怎么办？( Failed to connect to gitee.com port 443: Timed out )**  
华为公司内克隆外网代码的时候提示
fatal: unable to access 'https://gitee.com/openeuler/community.git/': Failed to connect to gitee.com port 443: Timed out
解决方法是依次配置：
git config --global https.proxy https://域账号:密码@proxycn2.huawei.com:8080
git config --global http.proxy http://域账号:密码@proxycn2.huawei.com:8080
git config --global http.sslVerify false
注意如果个人域账号密码中有特殊字符需要转义。
 ---
 10. **请问我提交PR后为什么没有触发CI构建，需要如何处理？**
 CI未及时触发通常有两种情况：  
&emsp; a. 第一种可能是网络原因或系统任务调度原因，导致从代码仓库发出的webhook通知事件没有及时到达目标服务，所以没有触发CI构建；这种情况可以通过在PR评论去评论 /retest 重新触发；  
&emsp; b.第二种可能是代码仓库创建以后短时间内提交PR，此时jenkins服务器侧尚未创建CI构建工程，所以触发不到CI构建，评论 /retest 也不生效；这种情况或者稍等一下系统自动建工程，或者联系 infra@openeuler.org 处理。
 ---
 11. **请问如何修改一个仓库分支的属性？**
 




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYxMDY3NDMzMywtNjgyMTQ5MjEwLC0yMT
IzNzIyMTM4XX0=
-->