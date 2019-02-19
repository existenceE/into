import time

def countdown(n):
    while n > 0:
        print("T-minus: ", n)
        n -= 1
        time.sleep(1)

from threading import Thread
t = Thread(target=countdown, args=(3, ))
t.start()

class CountdownTask:
    def __init__(self):
        self._running=True

    def terminate(self):
        self._running=False
    def run(self, n):
        while self._running and n > 0:
            print("Task-minus: ", n)
            n -= 1
            time.sleep(1)
c = CountdownTask()
t1 = Thread(target=c.run, args=(5, ))
t1.start()
c.terminate()
t1.join()

