#配置文件 安装saltstack

'''

    Master :
        准备：
        a.配置文件，监听本机IP
            vim /etc/salt/master
            interface:本机IP地址
        b.启动master
            /etc/init.d/salt-master start


'''
#######获取今天未采集的主机名############
#
# res = requests.get('http://127.0.0.1')  #API地址 去API里取数据
#
# res = ['c1.com','c2.com']


##########远程服务器执行命令############### 放master上
import subprocess
result = subprocess.getoutput("salt 'c1.com' cmd.run 'ifconfig'")

import salt.client
local = salt.client.LocalClient()
result = local.cmd('c2.salt.com','cmd.run',['ifconfig'])


###############发送数据####################
# request.post('127.0.0.1')

