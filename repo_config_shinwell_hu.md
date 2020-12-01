# openEuler 仓库配置管理文件格式规范

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_2)

[2](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_2)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_3)

[3](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_3)

版本记录：

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_4)

[4](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_4)

| 版本 | 作者 | 启用时间 | 变更说明 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_5)

[5](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_5)

| :-- | :-- | :-- | :-- |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_6)

[6](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_6)

| 1.0| 曹志 George.Cao，胡欣蔚 Shinwell_Hu| 2020-??-?? | 描述初始版本格式以及2.0格式建议 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_7)

[7](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_7)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_8)

[8](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_8)

## 背景说明

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_9)

[9](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_9)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_10)

[10](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_10)

https://gitee.com/openeuler/community 代码仓中 repository 目录下的 openeuler.yaml 和 src-openeuler.yaml 两个文件，管理了整个 openEuler 开源项目中所有代码仓的元数据信息，指导社区自动化工具对这些代码仓的管理。本格式规范是对上述两个配置文件格式的说明，便于各个工具开发团队以及社区贡献者了解如何提交符合要求的Pull Request。

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_11)

[11](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_11)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_12)

[12](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_12)

以下各个版本格式规范按时间由近及远排列，便于检索。已停用的格式规范依然在此归档，便于将来回溯查询。

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_13)

[13](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_13)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_14)

[14](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_14)

## 版本 2

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_15)

[15](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_15)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_16)

[16](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_16)

### 主要改变

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_17)

[17](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_17)

- 增加格式版本信息

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_18)

[18](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_18)

- 增加代码仓内分支的继承关系信息

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_19)

[19](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_19)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_20)

[20](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_20)

### 格式规范

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_21)

[21](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_21)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_22)

[22](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_22)

配置文件整体以yaml格式承载，包含三个基本元素：

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_23)

[23](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_23)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_24)

[24](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_24)

| 名称 | 类型 | 说明 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_25)

[25](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_25)

| :-- | :-- | :-- |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_26)

[26](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_26)

|format_version| 浮点数 |**本版本新增**该配置管理文件版本号，文件格式变更时变更|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_27)

[27](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_27)

|community| 枚举类型，可选 openeuler或者 src-openeuler|组织名称，当前组织名称openeuler和src-openeuler|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_28)

[28](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_28)

|repositories|清单|该组织下所有仓库信息|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_29)

[29](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_29)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_30)

[30](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_30)

repositories清单中每个元素代表一个代码仓，以关系数组的方式呈现，需要包含以下子元素：

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_31)

[31](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_31)

| 名称 | 类型 | 说明 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_32)

[32](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_32)

| :-- | :-- | :-- |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_33)

[33](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_33)

| name|字符串|仓库名称|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_34)

[34](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_34)

| rename_from|字符串|仓库原名称。这个子元素为可选，只有该代码仓是从另一个代码仓改名而来时才需要|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_35)

[35](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_35)

| description| 字符串 | 仓库包含组件的描述 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_36)

[36](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_36)

| type|枚举类型，可选 public 或者 private | 仓库类型。private代码仓不提供开放访问|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_37)

[37](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_37)

|upstream|字符串|本代码仓对应的上游社区信息。当 community 为 src-openeuler时，这个子元素必须提供；当 community 为 openeuler 且项目本身就是社区原创项目时，可以不设置|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_38)

[38](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_38)

| branches|清单|**本版本变更**本代码仓下所有分支信息|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_39)

[39](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_39)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_40)

[40](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_40)

branches 清单中每个元素代表一个受管理的分支，以关系数组的方式呈现，需要包含以下子元素:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_41)

[41](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_41)

| 名称 | 类型 | 说明 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_42)

[42](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_42)

| :-- | :-- | :-- |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_43)

[43](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_43)

| name| 字符串 | 分支名称 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_44)

[44](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_44)

| type | 枚举类型，可选protected/readonly | 分支类型，对照码云分支属性设置，protected 表示该分支可以被发布版本集成，readonly 表示该分支停止维护 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_45)

[45](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_45)

| create_from | 字符串 | 分支创建起点，当 branches.name 为 master 时，字符串为空；新创其他分支时设置已存在的分支名或tag名，缺省为master |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_46)

[46](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_46)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_47)

[47](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_47)

### 说明

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_48)

[48](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_48)

当工具处理本文件时未能获取 format_version，可以认为 format_version 为 1.0

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_49)

[49](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_49)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_50)

[50](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_50)

后续当format_version变更时，约定若format_version的整数部分不变，则工具可以不做任何修改；若format_version整数部分变动，则所有工具都需要重新适配。

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_51)

[51](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_51)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_52)

[52](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_52)

### 样例

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_53)

[53](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_53)

```

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_54)

[54](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_54)

format_version: 2.0

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_55)

[55](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_55)

community: src-openeuler

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_56)

[56](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_56)

repositories:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_57)

[57](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_57)

- name: A-Tune

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_58)

[58](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_58)

description: 'This is a repo for ……'

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_59)

[59](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_59)

branches:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_60)

[60](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_60)

- name: master

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_61)

[61](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_61)

type: protected

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_62)

[62](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_62)

- openEuler-20.03-LTS

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_63)

[63](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_63)

type: protected

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_64)

[64](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_64)

create_from: master

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_65)

[65](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_65)

- openEuler-20.09

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_66)

[66](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_66)

type: protected

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_67)

[67](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_67)

create_from: master

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_68)

[68](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_68)

type: public

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_69)

[69](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_69)

- name: A-Tune-UI

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_70)

[70](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_70)

description: 'Web server for A-Tune'

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_71)

[71](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_71)

upstream: https://gitee.com/openeuler/A-Tune-UI

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_72)

[72](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_72)

branches:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_73)

[73](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_73)

- name: master

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_74)

[74](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_74)

type: protected

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_75)

[75](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_75)

type: public

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_76)

[76](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_76)

```

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_77)

[77](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_77)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_78)

[78](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_78)

## 版本 1

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_79)

[79](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_79)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_80)

[80](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_80)

### 主要改变

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_81)

[81](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_81)

- openEuler 社区最初版本

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_82)

[82](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_82)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_83)

[83](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_83)

### 格式规范

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_84)

[84](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_84)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_85)

[85](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_85)

配置文件整体以yaml格式承载，包含两个基本元素：

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_86)

[86](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_86)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_87)

[87](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_87)

| 名称 | 类型 | 说明 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_88)

[88](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_88)

| :-- | :-- | :-- |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_89)

[89](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_89)

| community| 枚举类型，可选 openeuler 或者 src-openeuler | 组织名称|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_90)

[90](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_90)

| repositories| 清单 | 该组织下所有仓库信息，包含子字段 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_91)

[91](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_91)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_92)

[92](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_92)

repositories清单中每个元素代表一个代码仓，以关系数组的方式呈现，需要包含以下子元素：

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_93)

[93](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_93)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_94)

[94](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_94)

| 名称 | 类型 | 说明 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_95)

[95](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_95)

| :-- | :-- | :-- |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_96)

[96](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_96)

| name | 字符串 | 仓库名称 |

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_97)

[97](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_97)

| rename_from|字符串|仓库原名称。这个子元素为可选，只有该代码仓是从另一个代码仓改名而来时才需要|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_98)

[98](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_98)

| description | 字符串 | 仓库信息描述|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_99)

[99](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_99)

| protected_branches| 清单 | 保护分支的分支名列表|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_100)

[100](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_100)

| type| 枚举类型，可选 public 或者 private | 仓库类型。private代码仓不提供开放访问|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_101)

[101](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_101)

|upstream|字符串|本代码仓对应的上游社区信息。当 community 为 src-openeuler时，这个子元素必须提供；否则为可选项 **该子元素为中期添加，当时本文件尚未形成格式版本管理**|

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_102)

[102](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_102)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_103)

[103](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_103)

样例：

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_104)

[104](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_104)

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_105)

[105](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_105)

```

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_106)

[106](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_106)

community: src-openeuler

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_107)

[107](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_107)

repositories:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_108)

[108](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_108)

- name: A-Tune

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_109)

[109](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_109)

description: 'This is a repo for ……'

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_110)

[110](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_110)

protected_branches:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_111)

[111](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_111)

- master

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_112)

[112](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_112)

- openEuler-20.03-LTS

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_113)

[113](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_113)

- openEuler-20.09

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_114)

[114](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_114)

type: public

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_115)

[115](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_115)

- name: A-Tune-UI

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_116)

[116](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_116)

description: 'Web server for A-Tune'

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_117)

[117](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_117)

upstream: https://gitee.com/openeuler/A-Tune-UI

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_118)

[118](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_118)

protected_branches:

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_119)

[119](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_119)

- master

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_120)

[120](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_120)

type: public

[](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_121)

[121](https://gitee.com/open_euler/dashboard/projects/openeuler/community/pulls/1279?tab=diffs#3fdec95304edbd03fe98f219f355ef86f7f0725d_0_121)

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjIyODA4ODA0LDE3NjYxMzg4MzVdfQ==
-->