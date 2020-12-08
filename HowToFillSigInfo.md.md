# sig-info文件格式说明
背景：随着openEuler社区各类自动化工具和流程的完善，需要提取准确的sig信息。例如会议预定系统、网站展示、代码仓权限管理等都需要准确的sig信息。当前sig信息记录在community仓库sig目录下，能获准确取到的信息包括该sig的maintainer的码云ID（通过OWNER文件获取）和每个sig所管辖的仓库名称（通过sig.yaml获取）。但该sig的邮件列表信息，maintainer的邮件和名称等联系信息，sig组的描述信息等不能完整准确获取，只能从README中获得部分，且格式不统一。因此新增一个yaml文件以规范sig组信息管理。

## 格式规范
配置文件以yaml格式承载，包含五个基本元素：
| 字段 | 类型 | 说明 |
|--|--|--|
| name | 字符串 | sig组名称 |
| desc | 字符串 | sig组描述信息 |
| maillist | 字符串 | sig组邮件列表信息 |
| maintainers | 清单 | sig组所有maintainer名单 |
| repositories| 清单 | sig组所管辖的码云仓库信息 |

其中 maintainers 清单中每一条记录代表一位maintainer的个人信息：

| 字段 | 类型 | 说明 |
|--|--|--|
| giteeid | 字符串 | maintainer的gitee ID, 必填 |
| name | 字符串 | maintainer的姓名, 选填  |
| organization| 字符串 | maintainer所在组织, 选填 |
| email| 字符串 | maintainer个人邮箱地址, 选填 |

其中 repositories 清单中每一条记录为sig所管理的一个仓库信息：

| 字段 | 类型 |  说明 |
|--|--|--|
| repo | 字符串 | 仓库名称 |
| type | 枚举, 可选code或者rpm |区分是代码仓还是二进制包仓|
| url | 字符串 |仓库地址|

## 样例：
```
name: Infrastructure
desc: This is a template sig info.
maillist: infra@openeuler.org
maintainers:
- giteeid: dotsheng
  name: DongDaJian
  organization: Huawei
  email: 123456789@qq.com
- giteeid: immjoey
  name: MaMouGE
  organization: CASC
  email: mamoumou@gmail.com
- giteeid: zhengyuhanghans
  name: ZhengYuHang
  organization: Huawei
  email: zhengyuhanghan@huawei.com
repositories:
- repo: infrastructure
  type: code
  url: https://gitee.com/openeuler/infrastructure
- repo: blog
  type: code
  url: https://gitee.com/openeuler/blog
- repo: go-gitee
  type: rpm
  url: https://gitee.com/openeuler/go-gitee
```
