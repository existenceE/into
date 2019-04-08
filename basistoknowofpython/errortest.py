# from urllib import request, error
# try:
#     resoinse = request.urlopen('https://cuiqingcai.com/index.htm')
# # #except error.URLError as e:
# # except error.HTTPError as e:
# #     print(e.reason, e.code, e.headers)
# #HTTPError 是URLError 的子类，先捕获子类再捕获父类
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully!')

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT!!!')