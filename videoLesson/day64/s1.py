

import socket
from socket import SOL_SOCKET,SO_REUSEADDR


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
    # f = open('article.html', 'rb') #r打开是字符串
    f = open('article.tpl', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    import time
    ctime = time.time()
    data = data.replace('@@sw@@', str(ctime))
    return bytes(data, encoding='utf-8')


def f3(request):
    import pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1qaz2wsx', db='s4')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select * from aa')
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(user_list)
    content_list = []
    for row in user_list:
        tp = '''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row['emp_id'], row['emp_name'], row['age'], row['dept_id'])
        content_list.append(tp)
    content = "".join(content_list)
    f = open("userlist.html", 'r', encoding='utf-8')
    template = f.read()
    f.close()
    # 模板渲染 （模板 + 渲染
    data = template.replace("@@content@@", content)
    return bytes(data, encoding='utf-8')


def f4(request):
    import pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1qaz2wsx', db='s4')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select * from aa')
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('hostlist.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()

    #基于第三方工具实现的模板渲染
    from jinja2 import Template
    template = Template(data)
    data = template.render(use_list=user_list)
    print(data)

    return data.encode('utf-8')




routers = [
    ('/xxx', f1),
    ('/ooo', f2),
    ('/userlist.htm', f3),
    ('/host.html', f4)
]  #url和函数的对应关系


def run():
    sk = socket.socket()
    sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
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








