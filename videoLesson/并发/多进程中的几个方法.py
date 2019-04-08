
#join()
from multiprocessing import Process
import time

def func(arg1, arg2):
    print('*' * arg1)
    time.sleep(5)
    print("*" * arg2)


if __name__ == "__main__":
    p = Process(target=func, args=(10,20))
    p.start()
    #想让上面整体执行完再执行下面这一句
    print('hahahahhah')
    # 之间任意可以执行
    p.join() #作用是感知一个子进程的结束 将异步的程序改为同步
    print("=====: 运行完啦")
