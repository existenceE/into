import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    info = input('\033[1;31;40m c1>>>').encode('utf-8')
    sk.sendto(info, addr)

sk.close()

