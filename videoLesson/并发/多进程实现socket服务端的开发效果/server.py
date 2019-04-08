import socket

from multiprocessing import Process

def serv(conn):
    ret = "你好呀我是服务端".encode('utf-8')
    conn.send(ret)

    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()



sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

while True:

    conn, addr = sk.accept()
    p = Process(target=serv, args=(conn,))  #windows启动进程要放在main下面
    p.start()

sk.close()
