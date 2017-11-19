#_*_coding:utf-8_*_
# Author:Topaz
import socket
import select
import time
sock = socket.socket(socket.AF_INET)
sock.bind(('127.0.0.1',1233))
sock.setblocking(0)
sock.listen(128)
inputs = []
inputs.append(sock)       #套接字加入列表，有人发来请求inputs会发生变化
print("初始input\n %s" %inputs)
count = 0
while True:
    # print("select 监听的列表\n %s" %inputs)
    ''' 1.调用select函数对套接字进行监视之前，必须将要监视的套接字分配给数组(readfds,writefds,exceptfds)中的一个
        2.inputs列表加入readfds集合,有描述符(fd)就绪后select返回
        3.怎么叫就绪呢，readsfs满足四种条件之一就就绪，这里只说一种就是大于接受缓存区最低水位1,也就是有数据就就绪可读
        ）'''
    print(count,inputs )
    time.sleep(2)
    count += 1
    rlist,wlist,elist = select.select(inputs,[],[],0.1)
    for r in rlist:         #r的种类有很多种
        if r == sock:       #如果r == sock 就是有人发来请求
            print('wtr', r)
            # a = sock.accept()
            # print("accpet",a)
            conn,addr = sock.accept()   #accpet函数返回 conn新的套接字，addr存放客户端的地址
            conn.setblocking(0)
            inputs.append(conn) #把新来的连接也加到input，让select监测它
        else:
            data = b""
            while True:
                try:
                    chunk = r.recv(1024)    #接收数据
                    data = data + chunk
                except Exception as e:
                    chunk = None
                if not chunk:
                    print("收完了88")
                    break
            r.sendall(b'biu')
            inputs.remove(r)
            r.close()
