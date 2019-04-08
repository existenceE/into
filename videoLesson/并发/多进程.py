import time
import os

from multiprocessing import Process #包罗关于进程很多模块
def func(args1, args2):
    print(args1, args2)
    print(1234)
    time.sleep(1)
    print('紫禁城',os.getpid())
    print(54321)
    print('子的父', os.getppid())


if __name__ == "__main__":
    p = Process(target=func, args=("参数1","参数2")) #元组必须加逗号不然认为是一个数字  #注册 把这个函数注册到这个进程对象p里 还没有启动进程
    #但凡起进程都要和操作系统打交道 用C语言 #主进程
    print('父进程',os.getpid())
    p.start() #开启一个新的进程 子进程 相当于又建立一个新的py 在里面执行这个函数
    print('*'*10) #与函数func同时执行 不存在谁快谁慢
    # 两条马路的两辆车 没有先后顺序关系
    # 操作系统控制 不受你控制
    print('父的父', os.getppid())  #pycharm



#进程的生命周期
# 主进程：正常情况 从运行第一句到运行到最后 就结束
# 子进程：start开始 执行完结束
# 开启了子进程的主进程：
#   自己的代码如果长，等待自己的代码执行结束。
#   子进程执行时间长，主进程会自己执行完后等待子执行完毕 之后再结束
# 父进程子进程不一定在 不一定依赖父进程


# python
# 浏览器业务


