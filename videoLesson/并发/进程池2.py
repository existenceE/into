from multiprocessing import Pool
import time
import os


def func(n):
    print('%s start func %s' %(n, os.getpid()))
    time.sleep(1)
    print('%s end func %s' %(n, os.getpid()))


if __name__ == '__main__':
    pool = Pool()

    for i in range(10):
        pool.apply_async(func, args=(i,))
    pool.close()
    pool.join()