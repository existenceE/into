from socket import *
import time
sk = socket()
sk.connect(('127.0.0.1', 8080))
while True:
    time.sleep(2)
    sendmsg = time.asctime()
    time.sleep(3)
    sk.send(sendmsg.encode('utf-8'))
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    if not msg:
        break

sk.close()


# from socket import *
#
# client=socket(AF_INET,SOCK_STREAM)
# client.connect(('127.0.0.1',8080))
#
#
# while True:
#     msg=input('>>: ').strip()
#     if not msg:continue
#
#     client.send(msg.encode('utf-8'))
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))