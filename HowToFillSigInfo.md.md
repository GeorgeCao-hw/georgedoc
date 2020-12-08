# sig-info.yaml 格式说明
背景：随着openEuler社区各类自动化工具和流程的完善，需要提取准确的sig信息。例如会议预定系统、网站展示、代码仓权限管理等都需要准确的sig信息。当前sig信息记录在community仓库sig目录下，能获准确取到的信息包括该sig的maintainer的码云ID（通过OWNER文件获取）和每个sig所管辖的仓库（通过sig.yaml获取）。但该sig的邮件列表信息，maintainer的邮件和名称等联系信息，sig组的描述信息等不能完整准确地从README中获取到。因此希望新增一个yaml文件以规范sig组信息完善。

## 文件格式说明


```
name: Infrastructure
desc: This is a template sig info.
maillist: infra@openeuler.org
maintainers:
- giteeid: dogsheng
  name: DongJian
  organization: Huawei
  email: 960055655@qq.com
- giteeid: imjoey
  name: MaJunJie
  organization: CASC
  email: majunjiev@gmail.com
- giteeid: zhengyuhanghans
  name: ZhengYuHang
  organization: Huawei
repositories:
- repo: infrastructure
  url: https://gitee.com/openeuler/infrastructure
- repo: blog
  url: https://gitee.com/openeuler/blog
- repo: go-gitee
  url: https://gitee.com/openeuler/go-gitee
- repo: tool-collections
  url: https://gitee.com/openeuler/tool-collections
```
