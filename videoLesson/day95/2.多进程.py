
# 多线程更好
# 真正工作者是线程
# 5个教室，一个教室一个人。一个教室5个人。线程共享进程里的资源
# IO密集用多线程，计算密集用多进程
# 如果多个线程，情况好的时候同时工作。工作计算要涉及到CPU。
# 如果两个线程同时到达cpu,不同的cpu，cpu1 cpu2 可以同时运行。
# GIL锁，对于一个进程内部，同一时刻只能一个线程被CPU调度
# 即使一个进程开了两个线程，也只有一个线程能通过GIL的防线被cpu调度
# 即使开了多个线程，也不能充分利用CPU。如果计算，开多个线程，效率反而不高
# 对IO操作不用通过CPU，不受GIL的限制
# http请求是IO请求 在这里线程更好

from concurrent.futures import ProcessPoolExecutor
import requests

import time

pool = ProcessPoolExecutor(7)


def task(url):
    # response = requests.get(url)
    # print(url, response)
    time.sleep(1)




url_list = [
    'http://www.baidu.com',
    'http://www.cnblogs.com/wupeiqi',
    'http://www.bing.com',
    'http://www.zhihu.com',
    'http://www.autohome.com.cn',
    'http://www.sina.com',
]


for url in url_list:
    pool.submit(task, url)

pool.shutdown(wait=True)



# way2
# 分离下载和处理下载完成之后的操作。解耦。

def task(url):
    response = requests.get(url)
    return response


def done(future, *args, **kwargs):
    response = future.result()
    print(response.status_code, response.content)
    print(future, args, kwargs)


pool = ProcessPoolExecutor(7)

url_list = [
    'http://www.baidu.com',
    'http://www.cnblogs.com/wupeiqi',
    'http://www.bing.com',
    'http://www.zhihu.com',
    'http://www.autohome.com.cn',
    'http://www.sina.com',
]

for url in url_list:
    v = pool.submit(task, url)
    v.add_done_callback(done)

pool.shutdown(wait=True)














