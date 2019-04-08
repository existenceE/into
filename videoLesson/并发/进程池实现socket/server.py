import socket

from multiprocessing import Pool


def func(conn):
    conn.send(b'hello')
    print(conn.recv(1024).decode('utf-8'))
    conn.close()


if __name__ == '__main__':
    pool = Pool(5)
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        pool.apply_async(func, args=(conn, ))
    sk.close





