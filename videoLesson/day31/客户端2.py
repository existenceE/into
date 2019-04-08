import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #买手机
phone.connect(('127.0.0.1', 8000))  #拨别人的号

# while True:
#     #phone.send(bytes('hello', encoding='utf-8')) #基于二进制字节格式
#     info = input(">>>")
#     phone.send(info.encode('utf-8')) #基于二进制字节格式
#     data = phone.recv(1024).decode('utf-8')
#     print('收到服务端发来的消息 ', data)
#     if data == "bye":
#         break
#     if info == "bye":
#         break
# phone.close()
#
#
# # print('hello'.encode('utf-8'))


while True:
    msg = input("client2:>>")
    if msg == "bye":
        phone.send(b'bye')
        break
    phone.send(msg.encode('utf-8'))
    ret = phone.recv(1024).decode('utf-8')
    if ret == 'bye':
        print('c2aaaa')
        break
    print(ret)
phone.close()
