
# 线程池 线程有上下文切换 切换也会非常耗时 所以不适合开很多
# 可以实现并发，但是，请求发送出去后，和返回回来之前，中间线程空闲
# 编写方式 直接返回，通过回调函数处理

from concurrent.futures import ThreadPoolExecutor
import requests

import time

# pool = ThreadPoolExecutor(7)
#
#
# def task(url):
#     # response = requests.get(url)
#     # print(url, response)
#     time.sleep(1)
#
#
#
#
# url_list = [
#     'http://www.baidu.com',
#     'http://www.cnblogs.com/wupeiqi',
#     'http://www.bing.com',
#     'http://www.zhihu.com',
#     'http://www.autohome.com.cn',
#     'http://www.sina.com',
# ]
#
#
# for url in url_list:
#     pool.submit(task, url)
#
# pool.shutdown(wait=True)
#


# way2
# 分离下载和处理下载完成之后的操作。解耦。

def task(url):
    response = requests.get(url)
    return response


def done(future, *args, **kwargs):
    response = future.result()
    print(response.status_code, response.content)
    print(future, args, kwargs)


pool = ThreadPoolExecutor(7)

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














