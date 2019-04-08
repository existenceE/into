# 基于，安装paramiko
# 放在中间机器上


import paramiko
import requests
import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')
#######获取今天未采集的主机名############
#
# res = requests.get('http://127.0.0.1')  #API地址 去API里取数据
#
# res = ['c1.com','c2.com']


#######通过paramiko连接远程服务器，执行命令############

#创建ssh对象
ssh = paramiko.SSHClient()
#允许不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect('192.168.56.101', port=22, username='flower', password='123')

stdin, stdout, stderr = ssh.exec_command('df')
# stdin.write('Y')
result = stdout.read()
print(result)
ssh.close()


#######发送数据####
# data_dict = {result}
# result.post('127....',data=data_dict)