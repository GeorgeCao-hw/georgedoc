# 仓库配置管理文件格式说明
配置文件以yaml格式承载，共分三级结构：

 一级字段：
- version：该配置管理文件版本号，文件格式变更时变更
- community：组织名称，当前组织名称openeuler和src-openeuler
- repositories：该组织下所有仓库信息，包含子字段

二级字段（一级字段repositories下）：
- name：仓库名称
- description：仓库信息描述
- type：仓库类型，包括public/private
- branches：仓库下所有分支信息，包含子字段
 
三级字段（二级字段branches下）：
 - name：分支名称
 - type：分支类型，可选protected/normal/readonly，对照码云分支属性设置，缺省为protected
 - create_from：分支创建起点，可以是合法分支名和tag名，缺省为master

文件样例截图：
![enter image description here](https://gitee.com/ci-bot/build-test/raw/master/repocfgyaml.png)
