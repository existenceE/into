from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor

def one_done(arg):
    print(arg)
def all_done(args):
    print('done')
    reactor.stop()

@defer.inlineCallbacks
def task(url):
    res = getPage(bytes(url, encoding='utf-8')) #发送http请求
    res.addCallback(one_done) #第一个请求完了执行one done
    yield res


start_url_list = [
    'http://www.cnblogs.com',
    'http://www.cnblogs.com',
    'http://www.cnblogs.com',
    'http://www.cnblogs.com',
    'http://www.cnblogs.com',
    'http://www.cnblogs.com',
]
deffer_list = [] #有很多特殊对象 回来没回来还不知道
for url in start_url_list:
    v = task(url)  #执行task，外面是装饰器，会立即返回.返回值标注往哪里发送请求了
    deffer_list.append(v)

d = defer.DeferredList(deffer_list) #包了很多饺子放锅里
d.addBoth(all_done)

reactor.run() #死循环 检测发出去的请求回来没有




