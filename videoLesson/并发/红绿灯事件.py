

import random
from multiprocessing import Event, Process
import time





def cars(i, e):
    if not e.is_set():  #false.即红灯亮
        print('car%s在等待'%(i))
        e.wait()  #阻塞
    print('car%s通过'%(i))



def light(e):
    while True:
        if e.is_set():  #if true
            e.clear()  #设置为false
            print('红灯亮')
        else:
            e.set()  #设置为true
            print('绿灯亮')
        time.sleep(2)



if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e,))
    traffic.start()
    for i in range(10):
        p = Process(target=cars, args=(i, e))
        p.start()
        time.sleep(random.random())

