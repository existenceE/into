
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #TCP
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8000)) # 插手机卡 元组


phone.listen(5)  #开机 最多可以有
while True:
    conn, addr = phone.accept()  #拿到链接，接到别人电话  阻塞
    print(addr)
    while True:
        msg = conn.recv(1024).decode('utf-8') #收多少字节信息  听别人说话  阻塞
        if msg == "bye":
            print('aaaa')
            break
        print('客户端发来的消息是', msg)
        print("where I am")
        info=input(">>>").encode('utf-8')
        if info == b"bye":
            print('ppppppp')
            conn.send(info) #二进制 必须传bytes类型
            break
        print("bbbb")
        conn.send(info)

    conn.close() #挂电话

phone.close() #关机



# while True:
#     conn,addr = phone.accept()
#     while True:
#         msg = conn.recv(1024).decode("utf-8")
#         print(msg)
#         if msg == 'bye': break
#         info = input(">>>")
#         if info == "bye":
#             conn.send(b'bye')
#             break
#         conn.send(info.encode('utf-8'))
#     conn.close()
# phone.close()

















