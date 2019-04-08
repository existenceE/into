from multiprocessing import Process, Pipe, Lock

import time
import random


def consumer(pro, cos, name, lock):
    pro.close()
    while True:
        lock.acquire()
        msg = cos.recv()
        lock.release()
        if msg:
            print('%s 消费了 %s' % (name, msg))
            time.sleep(random.random())
        else:
            cos.close()
            break


def producer(pro, cos, name, food):
    cos.close()
    for i in range(10):
        pro.send(food)
        print('%s生产了%s' %(name, food))
    pro.send(None)
    pro.send(None)
    pro.close()




if __name__ == '__main__':
    lock = Lock()
    pro, cos = Pipe()
    p1 = Process(target=producer, args=(pro, cos, 'amy', '包子'))
    c1 = Process(target=consumer, args=(pro, cos, 'Alex', lock))
    c2 = Process(target=consumer, args=(pro, cos, 'Bob', lock))
    p1.start()
    c1.start()
    c2.start()
    pro.close()
    cos.close()
