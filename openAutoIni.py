#!/usr/bin/env python
#-*-coding:utf-8-*-
#python 2.7
#pip install IPy
import re
from IPy import IP
from flask import Flask
from flask import request
import os
import sys
reload(sys).setdefaultencoding('utf-8')

def createIni(index, siteName, startIP, stopIP, ipMask, gateWayIP):
    iniConf = ('''
[RANGE_SET]
#%s
#%s
FilterMacRange=4c:fa:ca:00:00:00-4c:fa:ca:ff:ff:ff
FilterMacRange=a8:58:40:00:00:00-a8:58:40:ff:ff:ff
FilterMacRange=70:d9:31:00:00:00-70:d9:31:ff:ff:ff
DHCPRange=%s-%s
SubnetMask=%s
Router=%s
AddressTime=172800
            ''' % (index, siteName, startIP, stopIP, ipMask, gateWayIP))
    with open('opendhcp.ini', 'a') as f:
        f.write(iniConf)
        f.close()
        #    os.system('service nginx start')### 换实际命令
    return '<h1>文件已添加，配置已经生效</h1>'


def countIndex():
    count = 1
    with open('opendhcp.ini','r') as r:
        co = r.xreadlines()
        for line in co:
            if (str(line.strip('\n\r'))=='[RANGE_SET]'):
                count +=1
        return count


def getIP(ipAddr,ipMask,index,siteName):
    try:
        ipNet = IP('%s/%s'%(ipAddr,ipMask),make_net=True)
        ipList = []
        for oneip in ipNet:
            ipList.append(oneip)
        startIP = ipList[6].strNormal()
        stopIP = ipList[-6].strNormal()
        gateWayIP = ipList[1].strNormal()
        ipMask = str(ipMask)
        return [startIP,stopIP,ipMask,gateWayIP]
    except Exception as e:
        return '''
<h1>无法识别你的IP地址，请检查你的输入是否有误:%s/%s</h1>
<h2>不要悲伤，路还有很远，但如果你实在忍不住，那就哭出来吧</h2>
<img src="https://gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/5243fbf2b211931319317d7460380cd790238d80.jpg">
'''%(ipAddr,ipMask)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>OPENDHCP 管理页</h1>'

@app.route('/addip', methods=['GET'])
def addip_form():
    return '''<form action="/addip" method="post">
              <p><input name="site" >请输入站点名称</p>
              <p><input name="ip" >请输入IP地址</p>
              <p><input name="netmask">请输入掩码地址</p>
              <p><button type="submit">提交</button></p>
              </form>'''
@app.route('/addip', methods=['POST'])
def addip():
    index = countIndex()
    ipAddr = request.form['ip']
    ipMask = request.form['netmask']
    siteName = request.form['site']
    try:
        andw = getIP(ipAddr,ipMask,index,siteName)
        andw1 = createIni(index, siteName, *andw)
        return andw1
    except:
        return '<h1>%s</h1>' % andw
if __name__ == '__main__':
    #main()
    app.run()
