import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))


msg, addr = sk.recvfrom(1024) #只能被动等待消息
print(msg.decode('utf-8'))
sk.sendto(b'bye', addr)


sk.close()


#udp的server不需要进行监听，也不需要建立连接
#在启动服务之后只能被动等待客户端发送消息来
#客户端发送消息的时候还会自带地址信息
#消息回复的时候不仅仅需要发送消息，还需要把对方的地址填写发送过去