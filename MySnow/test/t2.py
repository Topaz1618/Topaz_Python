#_*_coding:utf-8_*_
# Author:Topaz
import time

class Future(object):
    def __init__(self):
        print("看这里")
        self._ready = False
    def set_result(self):
        self._ready = True
    @property
    def ready(self):
        return self._ready

class TimeoutFuture(Future):
    print("来啦")
    def __init__(self, timeout):
        super(TimeoutFuture, self).__init__()
        self.timeout = timeout
        self.start_time = time.time()
    @property
    def ready(self):
        current_time = time.time()
        if current_time - self.start_time > self.timeout:
            self._ready = True
        return self._ready

def t1(num):
    print(num)
    a = TimeoutFuture(num)
    yield a

def t2(func):
    b = next(func)
    print(b)
    #time.sleep(5)

t2(t1)


