#!/usr/bin/env python
# coding:utf-8
import socket
def handle_request(client):
    buf = client.recv(1024)
    # 错误：TypeError: a bytes-like object is required, not 'str'
    # client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    # client.send(b"Hello, Seven")
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    client.send(bytes("Hello, Topaz",encoding='utf-8'))
    # client.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf8'))
    # client.send("Hello, Seven".encode('utf-8'))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()