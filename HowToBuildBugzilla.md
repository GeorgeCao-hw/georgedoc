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
重点关注容器拉起后需要执行以下启动行命令，命令行可以在deployment.yaml中查询到：
sh ./cfg.sh
a2ensite bugzilla
a2enmod cgi headers expires
service apache2 restart
sleep infinity
|命令|  用途|
|-----------|--|
|sh ./cfg.sh| 脚本配置bugzilla运行所需的配置参数，包括数据库连接参数等 |
|a2ensite bugzilla / a2enmod cgi headers expires / service apache2 restart | 配置并重启apache服务 |
|sleep infinity | 服务处于等待状态 |

## 服务配置
该服务配置后期可以通过步骤2 服务拉起中cfg.sh脚本实现，当前系统暂时使用的登录bugzilla节点手动配置：
1. 第一次进入容器节点，执行：./checksetup.pl 脚本配置管理员账户信息，需要管理员邮箱，用户名和密码。如果非第一次登录（管理员账户信息已经存入数据）则不再需要配置。
2. 执行cpan upgrade Net::SMTP::SSL升级节点内smtp系统，否则会影响邮件服务器注册。执行过程中有两次用户交互，直接回复yes即可。
3. 使用1步骤中录入的管理员账号登录bugzilla.openeuler.org系统。按照以下步骤进行邮件smtp服务注册：
【Administration】——>【Parameters】——>【Email】
各个参数信息根据实际情况配置。

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc3NTMwMjY4NCwtMTEzOTY1NzUzNSwtMT
YxNzc4Njk0NywtMTQ2MDUzMTM5NV19
-->