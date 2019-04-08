from threading import Thread
from multiprocessing import Process
import time
def sayhi(name):
    time.sleep(1)
    print('%s say hello' %name)
def saybye():
    time.sleep(3)
    print('say bye ')

# 兼容模式
# 制定规则 版本 内核 全部规则化
#根据机器的唯一标识来进行状态更新 用SN号（物理机不会重合，虚拟机的SN号全都一样。IP会变。
#单纯用主机名也会人为修改，指定规则，原则上主机名不能重复。
# 数据库里，如果没有 新增 如果有 更新

#遇到坑 SN 各种资产对不上号
#有些公司说没虚拟机，就用SN号就行了
#物理机和虚拟机都有，
#虚拟机不是资产。宿主机是资产。 SN号

#重装：业务线更改。
#openstack 创建一个实例，有一个快照。

#获取主机名，写到本地文件里。

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    # t.setDaemon(True) #必须在t.start()之前设置
    #t.daemon = True
    t2 = Thread(target=saybye)
    t.start()
    t2.start()

    print('主线程')
    time.sleep(1.5)
    print(t.is_alive())
    print(t2.is_alive())
    '''
    主线程
    True
    '''