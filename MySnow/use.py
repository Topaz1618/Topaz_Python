#_*_coding:utf-8_*_
# Author:Topaz
from snow import Snow
from django.shortcuts import redirect
from snow import HttpResponse
from snow import Future
from snow import TimeoutFuture

request_list = []

def index(request):
    return HttpResponse('ok')

def async(request):
    obj = TimeoutFuture(5)
    yield obj

def callback(request,future):
    return HttpResponse(future.value)
def req(request):
    obj = Future(callback=callback) # <snow.Future object at 0x000001535D47D278>
    request_list.append(obj)
    print('request_list',request_list)
    yield obj
def stop(request):
    obj = request_list[0]   #列表一直增加，这个就取第一个
    del request_list[0] #然后删除掉
    obj.set_result('done')
    return HttpResponse('Stop')

routes = [
    ('/index/',index),
    ('/async/',async),
    ('/req/',req),
    ('/stop/',stop),
]

app = Snow(routes)
app.run(port=8000)