import socket
import os
import time

sk = socket.socket()
sk.connect(('127.0.0.1',8080))
while True:
    info = time.asctime().encode('utf-8')
    sk.send(info)
    msg = sk.recv(1024).decode('utf-8')
    if not msg:
        break
    print(msg,os.getpid())


sk.close()



