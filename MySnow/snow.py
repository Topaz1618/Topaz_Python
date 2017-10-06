#_*_coding:utf-8_*_
# Author:Topaz
import socket
import select
import time
import re
# from django.http import HttpResponse

class Snow(object):
    def __init__(self,routes):
        self.routes = routes
        self.inputs = set()
        self.request = None
        self.async_request_header = {}


    def run(self,host="localhost",port=9999):
        my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_socket.bind((host,port))
        my_socket.listen(5)
        my_socket.setblocking(0)
        self.inputs.add(my_socket)
        try:
            while True:
                r_list,w_list,e_list = select.select(self.inputs,[],[],0.05)
                print("喵~")
                time.sleep(2)
                for conn in r_list:
                    if my_socket == conn:
                        print("有新连接来了\n    sock: %s\n    conn:%s"%(my_socket,conn))
                        client,addr = conn.accept()
                        client.setblocking(0)
                        self.inputs.add(client)
                    else:
                        print("熟客 处理掉\n    sock: %s\n    conn:%s"%(my_socket,conn))
                        gen = self.process(conn)
                        # print('gen',gen,gen.header_dic,gen.method,gen.url,gen.protocol)
                        if isinstance(gen,HttpResponse):
                            print("看看输出啥",gen.response())
                            conn.sendall(gen.response())
                            self.inputs.remove(conn)
                            conn.close()
                        else:
                            print("非阻塞")
                            yieldld = next(gen)
                            self.async_request_header[conn] = yieldld
                            # print('next获取到的',gen,yieldld)
                            # time.sleep(7)
                            # if yieldld.ready:
                            #     print("ok")
                            #     m = HttpResponse("Timeout")
                            #     conn.sendall(m.response())
                            #     self.inputs.remove(conn)
                            #     conn.close()
                self.asynchronous()
        except Exception as e:
            print('抓到一个错误',e)
        finally:
            my_socket.close()

    def asynchronous(self):
        for conn in list(self.async_request_header.keys()):
            yieldld = self.async_request_header[conn]
            print("真正的yield",yieldld)
            if not yieldld.ready:
                print("等。。。")
                continue
            else:
                print("超时了",yieldld)
            if yieldld.callback:
                print('看看这儿',yieldld,yieldld.callback)
                ret = yieldld.callback(self.request,yieldld)
            m = HttpResponse("Timeout")
            conn.sendall(m.response())
            self.inputs.remove(conn)
            del self.async_request_header[conn]
            conn.close()

    def process(self,conn):
        print("process")
        func = None
        self.request = HttpResquest(conn)
        for route in self.routes:
            if  re.match(route[0],self.request.url):
                func = route[1]
                break
        if not func:
            return HttpNotFound("404")
        else:
            return func(self.request)

class Future(object):
    def __init__(self,callback):
        self._ready = False
        self.callback = callback
    def set_result(self,value=None):
        self.value = value
        self._ready = True
    @property
    def ready(self):
        return self._ready

class TimeoutFuture(Future):
    def __init__(self,timeout):
        self.timeout = timeout
        super(TimeoutFuture,self).__init__()
        self.start_time = time.time()
    @property
    def ready(self):
        current_time = time.time()
        if current_time - self.start_time > self.timeout:
            self._ready = True
        return self._ready

class HttpResquest(object):
    def __init__(self,conn):
        print("HttpResquest")
        self.conn = conn
        self.header = bytes()
        self.body = bytes()
        self.header_dic = {}
        self.method =""
        self.url = ""
        self.protocol = ""
        self.cutting()
        self.save()

    def cutting(self):
        while True:
            try:
                rec = self.conn.recv(8096)
            except Exception as e:
                rec = None
            if not rec:
                break
            cut = rec.split(b'\r\n\r\n')    #分隔符为\r\n\r\n
            if len(cut) == 1:
                self.header += cut
            else:
                h,b = cut
                self.header += h
                self.body += b

    @property
    def header_str(self):
        return str(self.header,encoding="utf-8")

    def save(self):
        headers = self.header_str.split('\r\n')
        first_line = headers[0].split(' ')
        if len(first_line) == 3:
            self.method,self.url,self.protocol = first_line
            for line in headers:
                kv = line.split(':')
                if len(kv) == 2:
                    k,v = kv
                    self.header_dic[k] = v

class HttpResponse(object):
    def __init__(self,message):
        self.message = message
        print('message类型',type(self.message))
    def response(self):
        return bytes(self.message,encoding="utf-8")

class HttpNotFound(HttpResponse):
    def __init__(self,message):
        super(HttpNotFound,self).__init__(message)














