



from multiprocessing import Manager, Process, Lock



def func(dic, lock):
    lock.acquire()
    dic['count'] -= 1
    # print('子进程 %s' %(dic['count']))
    lock.release()






if __name__ == '__main__':
    m = Manager()
    dic = m.dict({'count':100})
    l = Lock()
    p_lst = []
    for i in range(50):
        p = Process(target=func, args=(dic, l))
        p.start()
        p_lst.append(p)

    for p in p_lst:
        p.join()

    print('主进程 %s' %(dic['count']))



