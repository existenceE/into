from multiprocessing import Process
import json
from multiprocessing import Lock
import time


def show(i):
    with open('ticket') as f:
        dic = json.load(f)
    print('%i 余票为 %s' % (i, dic['ticket']))


def buy_ticket(i, lock):
    lock.acquire()
    with open('ticket') as f:
        dic = json.load(f)
    time.sleep(0.5)
    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        print('%i 买到票了！余票为%s' % (i, dic['ticket']))
        with open('ticket', 'w') as f:
            json.dump(dic, f)
    else:
        print('没有票了，票数为 %s' % (dic['ticket']))
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=show, args=(i,))
        p.start()
    for i in range(10):
        p = Process(target=buy_ticket, args=(i, lock))
        # p = Process(target=buy_ticket, args=(i, ))
        p.start()
