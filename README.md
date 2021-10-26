## 功能说明
该工具主要用于比较两个linux操作系统RPM包差异性。提供以下功能：
一、给定repo地址下载RPM包功能，
二、对比两个操作系统RPM包集合，获取同名同版本号RPM包信息功能
三、对比上诉同名同版本包相似度功能

## 目录文件说明
| 目录 | 说明  |
|--|--|
| script | 用于存放功能脚本和下载的rpm包，rpm包根据不同版本分子目录存放  |
|result |用于存放工具的执行结果，按照工具运行的时间戳，每执行一次，存当次执行的过程数据和结果报告|

## 使用方法
1. 确认需要对比的发行版版本信息。目前该工具机器上已经下载有：centos8.0，centos8.1，centos8.2，centos8.3，centos8.4 和openEuler21.09 一共6个版本。如果需要对比的版本再其中，可直接跳过第2步下载，进行第3步比较。
2. 如果需要对比的包在当前机器没有，则需要自行下载，以下载openEuler21.03 为例，可以执行下列命令进行下载：
    python3 script/downloadSrcRpms.py euler21.03  https://repo.openeuler.org/openEuler-21.03/

 3.对比已经下载好的RPM可以执行以下命令，假设以centos8.2版为基础，对比openEuler21.09：
     python3 script/findDifferentPkgs.py -b script/centos8.2 -c script/euler21.09
     其中-b 后接对比的基础版本RPM包本地目录， -c 后接需要对比版本RPM包的本地目录。
     


