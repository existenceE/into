"""
非阻塞，体现在不等待。同一时刻请求发出去不等待结果。连A连B连C.

import socket
sk = socket.socket()
sk.connect((ip, port))
sk.connect((ip, port))
sk.connect((ip, port))
默认情况connect阻塞
sk.setblocking(False)
不阻塞，之后再检测是否成功。


异步：体现在回调。成功主动通知

def callback(contents):
    print(contents)
事件循环：一直在循环检测三个socket任务，检查三个的状态。是否连接成功，是否返回结果。

总结： twisted 基于事件循环的异步非阻塞模块。
    白话： 一个线程同时可以向多个目标发送http请求。

"""

from twisted.web.client import getPage, defer
from twisted.internet import reactor


# 第一步，代理开始接收任务
def callback(contents):
    print(contents)


deferred_list = []
url_list = ["http://www.bing.com", "http://www.baidu.com",
            "https://segmentfault.com"]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf-8'))
    deferred.addCallback(callback)
    deferred_list.append(deferred)

# 第二步，代理执行完后停止
dlist = defer.DeferredList(deferred_list)


def all_done(arg):
    reactor.stop()


dlist.addBoth(all_done)

# 第三部，代理开始处理
reactor.run()
