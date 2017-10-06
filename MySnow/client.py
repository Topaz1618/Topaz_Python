#_*_coding:utf-8_*_
# Author:Topaz
import socket
import sys
import time
messages = [b'This is the message. ',
            b'It will be sent ',
            b'in parts.',
            ]
# Create a TCP/IP socket、
# client = socket.socket()
clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
           socket.socket(socket.AF_INET, socket.SOCK_STREAM),
           ]
# Connect the socket to the port where the server is listening
for client in clients:  # 建俩链接，为了不并发这样？？
    client.connect(('localhost', 1222))
for message in messages:
    '''这段儿就是每个消息都用两个连接分别发一遍'''
    n = 0
    for client in clients:
        n += 1
        print('%s发送数据啦 : sending "%s %s"' % (client.getsockname(), message, n))
        client.send(message)
    time.sleep(2)
    # Read responses on both sockets
    for client in clients:
        data = client.recv(1024)  # 每个连接再获取下返回数据
        print('%s接收数据啦: received "%s"' % (client.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', client.getsockname())

