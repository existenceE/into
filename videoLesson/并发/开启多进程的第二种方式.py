import os
from multiprocessing import Process


# p = Process(target=func)


class MyProcess(Process):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1= arg1
        self.arg2=arg2
    def run(self):  #跟原来func里的代码一样
        print(os.getpid())
        print(self.pid)  #查看进程ID的两种方式
        print(self.name)
        print(self.arg1)
        print(self.arg2)

print('主：', os.getpid())
p1 = MyProcess(1,2)  #实例化自己写的类
p1.start()  #内部调用run方法
p2 = MyProcess(3,4)
p2.start()


#定义一个自己的类 继承Process类
#传参实现init方法，传入，实现父类的init方法
#必须实现一个run方法，方法中是在子进程中执行的代码

