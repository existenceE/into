#两部分： 每台机器上采集自己的数据、发送数据到API

import subprocess
import requests

#######采集数据############每台机器上放agent,采集自己的信息，直接发送api
res = subprocess.getoutput('ifconfig')

#正则处理 获取想要的数据


#整理资产信息
data_dict = {
    'nic':{},
    'disk':{},
    'memory':{}
}
##########发送信息###############
requests.post('http://127.0.0.1:8000/assets.html', data=data_dict)



