import socket
from socket import SOL_SOCKET, SO_REUSEADDR
from threading import *
import os
from multiprocessing import Process

sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sk.bind(('127.0.0.1',8080))
sk.listen(2)
print(os.getpid())

def work(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        if not msg:
            break
        print(msg,addr,os.getpid())
        info = msg.upper().encode('utf-8')
        conn.send(info)
    conn.close()


while True:
    conn, addr = sk.accept()
    t = Process(target=work, args=(conn,))
    t.start()
sk.close()


