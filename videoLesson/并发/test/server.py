from socket import *
from multiprocessing import Pool
import os

sk = socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8080))
sk.listen(2)


def talk(conn):
    while True:
        try:
            print('进程pid%s' %(os.getpid()))
            msg = conn.recv(1024).decode('utf-8')
            if not msg: break
            print(msg)
            conn.send(msg.upper().encode('utf-8'))
        except Exception:
            break

p = Pool(2)
while True:
    conn, addr = sk.accept()
    p.apply_async(talk, args=(conn,))


conn.close()
sk.close()
# from socket import *
# from multiprocessing import Pool
# import os
#
# server=socket(AF_INET,SOCK_STREAM)
# server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# server.bind(('127.0.0.1',8080))
# server.listen(5)
#
# def talk(conn):
#     print('进程pid: %s' %os.getpid())
#     while True:
#         try:
#             msg=conn.recv(1024)
#             if not msg:break
#             conn.send(msg.upper())
#         except Exception:
#             break
#
# if __name__ == '__main__':
#     p=Pool(2)
#     while True:
#         conn,*_=server.accept()
#         p.apply_async(talk,args=(conn,))
#         # p.apply(talk,args=(conn,client_addr)) #同步的话，则同一时间只有一个客户端能访问