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
     
## 统计结果说明：
在result目录下按照执行工具的时间戳保存单次执行的过程数据和统计数据，如result下1635273197文件加就是linux时间1635273197执行的比较命令，其过程数据和统计数据都在1635273197文件夹中：
|文件名|内容  |
|--|--|
|rpmdiff_detail.txt  |通过rpmdiff对比同名rpm包的执行结果的详细信息，按照rpm包名称分组  |
| analyze_ret.txt | 根据detail中给出的两包差异信息判断出的两包内容是否相同的结果。记录信息为 包名+same或包名+different  |
| statistic.txt | 记录的比较的统计结果具体含义见下表 |

|数据项|含义  |
|--|--|
|Total RPMs in base OS  |基线base操作系统src.rpm总数  |
| Total RPMs in compared OS |对比操作系统src.rpm总数  |
|Count of RPMs with same name and version  | 两操作系统中同名且同版本号的src.rpm包数量 |
|Same name RPMs that have same content  | 将上述同名同版本的对比，没有做实质修改的包的数量，此处‘实质修改’的含义是rpmdiff工具对比结果中，没有发现有md5☞变更的情况 |
| Same name PRMs that have diffent content | 将上述同名同版本的对比，有做实质修改的包的数量 |



