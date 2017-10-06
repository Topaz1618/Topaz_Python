#_*_coding:utf-8_*_
# Author:Topaz
from snow1 import TimeoutFuture
from snow1 import Snow
from snow1 import HttpResponse
# from django.http import HttpResponse
from snow1 import Future
request_list = []
def index(request):
    print("what ???")
    return HttpResponse("ok")
#异步非阻塞：超时
def async(request):     #异步非阻塞，超时
    obj = TimeoutFuture(5)
    print("    服务端拿到了生成器元素",obj)
    yield obj

#异步非阻塞：等待
def callback(request, future):
    print('future value & a',future.value)
    return HttpResponse(future.value) #
def req(request):
    obj = Future(callback=callback) #==><snow1.Future object at 0x000001D417244BA8>
    print('    req',obj)
    request_list.append(obj)
    yield obj
def stop(request):
    obj = request_list[0]   #==><snow1.Future object at 0x000002A3F6624BA8>
    del request_list[0]
    print('    stop',obj)
    obj.set_result('done')
    print("    okokokokokokokok")
    return HttpResponse('stop')

routes = [
    (r'/index/', index),
    (r'/async/', async ),
    (r'/req/', req),
    (r'/stop/', stop),
]
app = Snow(routes)
app.run(port=8001)
