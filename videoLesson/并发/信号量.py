from multiprocessing import Semaphore, Process
import time
import random


def ktv(i, sem):
    sem.acquire()
    print('%s走进ktv' % (i,))
    time.sleep(random.randint(60, 180))
    print('%s走出ktv' % (i,))
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(20):
        p = Process(target=ktv, args=(i, sem))
        p.start()
