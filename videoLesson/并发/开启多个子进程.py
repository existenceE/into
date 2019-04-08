import os

from multiprocessing import Process
import time

def func(filename, content):
    with open(filename, 'w') as f:
        f.write(content*10*"*")
    # print('*' * arg1)
    # time.sleep(5)
    # print("*" * arg2)


if __name__ == "__main__":
    p_list=[]
    for i in range(5):  #10条马路
        p = Process(target=func, args=("info%s"%i,i))
        p_list.append(p)
        p.start()
        print('======')
        print(i, p.pid)
    # p.join()  #i=10的p
    print(p.pid)
    [p.join() for p in p_list]  #之前的进程都执行完才能执行下面的代码
    print("运行完了")
    print([i for i in os.walk(r'./')])

#角色转换