# opendhcpAutoIni
基于flask，做了一个通过网页自动生成opendhcp [RANGE_SET]配置的程序
[点这里下载opendhcp](https://sourceforge.net/projects/dhcpserver/)

#### 功能
1.通过python IPr库自动识别IP地址掩码输入是否合法，有效。
1.通过有效IP地址生成相应网段的地址，截取dhcp pool需要的startIP stopIP Gateway
1.按序号生成配置文件，方便查看，opendhcp最大支持128个range，免得去数了
1.重启opendhcp 使配置生效
1.太懒，删改查功能未写，有谁做完了记得pppoe@139.com抄我一份

#### 安装步骤
1.解压openAutoIni.py到/etc/opendhcp/opendhcp目录（或随意相应openrun中未知也要改）
1.解压openrun到/etc/init.d/
1.执行 chmod a+x openrun
1.运行service openrun {start| stop| restart| status} 启动网页服务


#### 使用
1.建议通过nginx代理一下本地127.0.0.1:5000 端口如绑定在172.16.0.10:90端口
1.打开172.16.0.10:90/addip 页面
1.输入dhcp名称
1.输入ip地址
1.输入掩码

####生成示例
```
[RANGE_SET]
#7@大大
FilterMacRange=4c:fa:ca:00:00:00-4c:fa:ca:ff:ff:ff
FilterMacRange=a8:58:40:00:00:00-a8:58:40:ff:ff:ff
FilterMacRange=70:d9:31:00:00:00-70:d9:31:ff:ff:ff
DHCPRange=172.162.121.6-172.162.121.122
SubnetMask=255.255.255.128
Router=172.162.121.1
AddressTime=172800
            
[RANGE_SET]
#8@213123
FilterMacRange=4c:fa:ca:00:00:00-4c:fa:ca:ff:ff:ff
FilterMacRange=a8:58:40:00:00:00-a8:58:40:ff:ff:ff
FilterMacRange=70:d9:31:00:00:00-70:d9:31:ff:ff:ff
DHCPRange=192.136.12.6-192.136.12.250
SubnetMask=255.255.255.0
Router=192.136.12.1
AddressTime=172800
            
[RANGE_SET]
#9@123111
FilterMacRange=4c:fa:ca:00:00:00-4c:fa:ca:ff:ff:ff
FilterMacRange=a8:58:40:00:00:00-a8:58:40:ff:ff:ff
FilterMacRange=70:d9:31:00:00:00-70:d9:31:ff:ff:ff
DHCPRange=172.162.121.6-172.162.121.122
SubnetMask=255.255.255.128
Router=172.162.121.1
AddressTime=172800
```
