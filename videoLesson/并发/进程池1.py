from multiprocessing import Pool, Process
import time




def func(n):
    for i in range(10):
        print(n+1)

def func2(n):
    for i in range(10):
        print(n+2)


if __name__ == '__main__':
    start = time.time()
    pool = Pool(5)
    pool.map(func, range(100))  #100个任务
    # pool.map(func2, [('alex', 1), 'egon'])
    t1 = time.time() - start

    start = time.time()
    p_lst = []
    for i in range(100):
        p = Process(target=func, args=(i, ))
        p_lst.append(p)
        p.start()
    for p in p_lst:
        p.join()
    t2 = time.time() - start
    print(t1, t2)


