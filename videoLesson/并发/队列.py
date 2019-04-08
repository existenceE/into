from multiprocessing import Queue,Process



def producer(q):
    q.put('hello')


def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    p.start()
    c = Process(target=consumer, args=(q,))
    c.start()