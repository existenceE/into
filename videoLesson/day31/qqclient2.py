import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

while True:
    info = input("c2>>>").encode('utf-8')
    sk.sendto(info, ip_port)
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()
