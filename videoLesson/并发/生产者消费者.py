from multiprocessing import Queue, Process, JoinableQueue
import time
import random


def consumer(name, q):
    while True:
        food = q.get()
        if food is None:
            print('%s获取到一个空值' % (name))
            break
        print('%s消费了%s' %(name, food))
        time.sleep(random.randint(1,3))
        q.task_done()  #在while之内，每次消费一个，数量减一


def producer(name, food, q):
    for i in range(4):
        time.sleep(random.randint(1,3))
        f = '%s生产了一个%s%s' % (name, food, i)
        print(f)
        q.put(food)
    q.join()  #等所有消费者处理完数据，结束。




if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=('amy', '包子', q))
    p2 = Process(target=producer, args=('Bob', '泔水', q))
    c1 = Process(target=consumer, args=('Alex', q))
    c2 = Process(target=consumer, args=('Charles', q))
    p1.start()
    p2.start()
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()    #感知一个进程的结束。
    p2.join()  #结束以后，c结束。
    # q.put(None)  #low
    # q.put(None)
