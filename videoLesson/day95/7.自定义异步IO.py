# select+socket
# 通过一个线程向很多地方把请求发出去

###################################HTTP请求本质，阻塞####################
'''
import socket
import select

sk = socket.socket()
# 连接
sk.connect(('www.baidu.com', 80)) #IO阻塞
print('连接成功了...')

# 连接成功后发送http数据
sk.send(b'GET / HTTP/1.0\r\nHost:baidu.com\r\n\r\n')
# sk.send(b'POST / HTTP/1.0\r\nHost:baidu.com\r\n\r\nk1=v1&k2=v2')

# 等待着服务端响应
data = sk.recv(8096) #IO阻塞
print(data)

# 关闭连接
sk.close()

'''

###################################HTTP请求本质，非阻塞####################

'''
import socket
import select

sk = socket.socket()
sk.setblocking(False)
# 连接
try:
    sk.connect(('www.baidu.com', 80)) #IO阻塞
    print('连接成功了...')
except BlockingIOError as e:
    print(e)
while True:

# # 连接成功后发送http数据
# sk.send(b'GET / HTTP/1.0\r\nHost:baidu.com\r\n\r\n')
# # sk.send(b'POST / HTTP/1.0\r\nHost:baidu.com\r\n\r\nk1=v1&k2=v2')
#
# # 等待着服务端响应
# data = sk.recv(8096) #IO阻塞
# print(data)
#
# # 关闭连接
# sk.close()
'''

import socket
import select


class HttpRequest:
    def __init__(self, sk, host, callback):
        self.socket = sk
        self.host = host
        self.callback = callback
    def fileno(self):
        return self.socket.fileno()


class AsyncRequest:
    def __init__(self):
        self.conn = []
        self.connection = []

    def add_request(self, host, callback):
        try:
            sk = socket.socket()
            sk.setblocking(0)
            sk.connect((host, 80,))
        except BlockingIOError as e:
            pass
        request = HttpRequest(sk, host, callback)
        self.conn.append(request)
        self.connection.append(request)

    def run(self):
        while True:
            rlist, wlist, elist = select.select(self.conn, self.connection, self.conn, 0.05)
            for w in wlist:
                print(w.host, "连接成功...")
                # 只要能循环到 读取到 表示当前socket和服务器端连接成功
                tpl = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % (w.host, )
                w.socket.send(bytes(tpl, encoding='utf-8'))
                self.connection.remove(w)

            for r in rlist:
                print(r.host, "有数据返回 ")
                # r是httprequest
                recv_data = bytes()
                while True:
                    try:
                        chunk = r.socket.recv(8096)
                        recv_data += chunk
                    except:
                        break
                r.callback(recv_data)
                r.socket.close()
                self.conn.remove(r)

            if len(self.conn) == 0:
                break


def f1(data):
    print("this is f1", data)


def f2(data):
    print('this is f2', data)


url_list = [
    {'url': 'www.baidu.com', 'callback': f1},
    {'url': 'cn.bing.com', 'callback': f2},
    {'url': 'www.cnblogs.com', 'callback': f2}
]

req = AsyncRequest()
for item in url_list:
    req.add_request(item['url'], item['callback'])
req.run()
