from gevent import monkey

monkey.patch_all()
import gevent

import requests


def task(method, url, req_kwargs):
    print(method, url, req_kwargs)
    response = requests.request(method=method, url=url, **req_kwargs)
    print(response.url, response.content)


# gevent.joinall([
#     gevent.spawn(task, method='get', url='https://www.python.org',
#                  req_kwargs={}),
#     gevent.spawn(task, method='get', url='https://www.yahoo.com',
#                  req_kwargs={}),
#     gevent.spawn(task, method='get', url='https://www.github.com',
#                  req_kwargs={}),
# ])
from gevent.pool import Pool
pool = Pool(5)
gevent.joinall([
    pool.spawn(task, method='get', url='https://www.python.org',
                 req_kwargs={}),
    pool.spawn(task, method='get', url='https://www.yahoo.com',
                 req_kwargs={}),
    pool.spawn(task, method='get', url='https://www.github.com',
                 req_kwargs={}),
])