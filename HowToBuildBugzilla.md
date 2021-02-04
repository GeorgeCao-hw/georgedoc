# openEuler如何构建bugzilla系统？

背景：随着openEuler社区开发者队伍的壮大，对bug管理系统的要求越来越高，通过与TC和各SIG组（SIG-kernel/SIG-release/SIG-QA等）讨论，社区希望引入bugzilla系统用于bug跟踪。

bugzilla是一个成熟的、开源的bug跟踪系统，社区有现成的容器镜像可以使用，但是该容器镜像是4.0.5版本，相对比较早。社区希望使用最新的稳定版本，即5.0.6的版本。因此openEuler基础设施使用开源社区资源独立构建容器镜像并上线了服务。

本文简要介绍服务上线流程：
1. 容器镜像构建
2. 服务拉起
3. 服务配置

## 容器镜像构建
容器镜像构建流程我们已经使用流水线工程实施，
工程路径：https://jenkins.osinfra.cn/view/openEuler/job/openEuler_APPs/job/bugzilla/
该工程中使用到的[Dockerfile](https://github.com/opensourceways/app-bugzilla/blob/main/Dockerfile)和构建流程[脚本](https://github.com/opensourceways/app-bugzilla/blob/main/jenkins/jenkins)都已上库到以下代码仓库：
https://github.com/opensourceways/app-bugzilla

## 服务拉起
按照K8S服务配置，定义了相关的deployment.yaml、kustomization.yaml、namespace.yaml、secrets.yaml、service.yaml文件，文件路径：
https://github.com/opensourceways/app-bugzilla/tree/main/deploy
重点关注容器拉起后需要执行

<!--stackedit_data:
eyJoaXN0b3J5IjpbNDY3NjExNTQzLC0xMTM5NjU3NTM1LC0xNj
E3Nzg2OTQ3LC0xNDYwNTMxMzk1XX0=
-->