

import socket



def f1(request):
    '''
    处理用户请求（获取用户提交来的数据）并返回相应内容
    :param request: 用户请求的所有信息
    :return:
    '''
    # return b"f1" #能从数据库拿来，也能从本地html读到内存放到这里
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data

def f2(request):
    f = open('article.html', 'rb')
    data = f.read()
    f.close()
    return data

routers = [
    ('/xxx', f1),
    ('/ooo', f2),
]


def run():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen(5)


    while True:
        conn,addr = sk.accept()
        print(conn, addr)
        data = str(conn.recv(8096), encoding='UTF-8')
        headers, bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method, url, protocol = temp_list[0].split(' ')
        conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name(data)  #包含请求头加请求体所有内容
        else:
            response = b"404"

        conn.send(response)
        conn.close()

run()








