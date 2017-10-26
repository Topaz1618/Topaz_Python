#_*_coding:utf-8_*_
# Author:Topaz
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from monitor import serializer
from monitor.serializer import AgentHandler
from monitor.backends import my_redis
from monitor.backends import data_optimization
from monitor.backends import data_processing
from django.conf import settings
from monitor import models
import time
import json

RedisObj = my_redis.redis_conn(settings)
# print('Redis Status',RedisObj.set("catty",time.ctime()))


def agent_con(request,agent_id):
    agent_obj = AgentHandler(agent_id)
    config = agent_obj.get_configs()
    if config:
        return  HttpResponse(json.dumps(config))

@csrf_exempt
def put_data(request):
    if request.method == "POST":
        try:
            # print('request',request.POST.get('client_id'),request.POST.get('item_name'),request.POST.get('data'))
            data = json.loads(request.POST.get('data'))
            client_id = request.POST.get('client_id')
            item_name = request.POST.get('item_name')
            data_optimization.DataStore(data,client_id,item_name,RedisObj)  #来了数据就去存起来
            print('Redis Status', RedisObj.set("catty", time.ctime()))
            #同时触发trigger检查
            expressions_handler = data_processing.DataHandler(settings)
            h= models.Host.objects.get(id=client_id)
            expressions_handler.wtf(h,RedisObj)
        except Exception as e:
            print("来人呀这里有错误",e)
    return HttpResponse("咋回事儿呢")