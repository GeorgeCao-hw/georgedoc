# 仓库配置管理文件格式说明

版本记录：
- 1.0	2019-12-30
- 1.1	2020-11-24 
### 版本1.0
配置文件以yaml格式承载，共分二级结构：

 一级字段：
- community：组织名称，当前组织名称openeuler和src-openeuler
- repositories：该组织下所有仓库信息，包含子字段

二级字段（一级字段repositories下）：
- name：仓库名称
- rename_from：仓库原名称，可选字段
- description：仓库信息描述
- protected_branches：保护分支的分支名列表
- type：仓库类型，包括public/private
- upstream：上游仓库地址，可选字段

样例：

 ---
community: src-openeuler
repositories:
-- name: A-Tune
&ensp; description: 'This is a repo for ……'
&ensp; protected_branches:
&ensp; -- master
&ensp; -- openEuler-20.03-LTS
&ensp; -- openEuler-20.09
&ensp; type: public
-- name: A-Tune-UI
&ensp; description: 'Web server for A-Tune'
&ensp; upstream: https://gitee.com/openeuler/A-Tune-UI
&ensp; protected_branches:
&ensp; -- master
&ensp; type: public

---



### 版本1.1
配置文件以yaml格式承载，共分三级结构：

 一级字段：
- version：该配置管理文件版本号，文件格式变更时变更
- community：组织名称，当前组织名称openeuler和src-openeuler
- repositories：该组织下所有仓库信息，包含子字段

二级字段（一级字段repositories下）：
- name：仓库名称
- rename_from：仓库原名称，可选字段
- description：仓库信息描述
- type：仓库类型，包括public/private
- upstream：上游仓库地址，可选项
- branches：仓库下所有分支信息，包含子字段
 
三级字段（二级字段branches下），该版本设计三个字段：
 - name：分支名称
 - type：分支类型，可选protected/normal/readonly，对照码云分支属性设置，缺省为protected
 - create_from：分支创建起点，新创master分支时该字段置空，新创其他分支时设置已存在的分支名或tag名，缺省为master

样例：

 ---
 version: v1.1
community: src-openeuler
repositories:
-- name: A-Tune
&ensp; description: 'This is a repo for ……'
&ensp; branches:
&ensp; -- name: master
&emsp;&emsp; type: protected
&ensp; -- openEuler-20.03-LTS
&emsp;&emsp; type: protected
&emsp;&emsp; create_from: master
&ensp; -- openEuler-20.09
&emsp;&emsp; type: protected
&emsp;&emsp; create_from: master
&ensp; type: public
-- name: A-Tune-UI
&ensp; description: 'Web server for A-Tune'
&ensp; upstream: https://gitee.com/openeuler/A-Tune-UI
&ensp; branches:
&ensp; -- name: master
&emsp;&emsp; type: protected
&ensp; type: public

---
