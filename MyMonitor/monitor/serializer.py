#_*_coding:utf-8_*_
# Author:Topaz
from monitor import models
from django.core.exceptions import  ObjectDoesNotExist

class AgentHandler(object):
    def __init__(self,client_id):
        self.client_id = client_id
        self.item_dic = {
            "items":{},
        }
    def get_configs(self):
        print("来取数据库配置啦")
        try:
            host_obj = models.Host.objects.get(id=self.client_id)
            templates_list = host_obj.template.select_related()
            for template in templates_list:
                for item in template.item.select_related():
                    self.item_dic['items'][item.name] = [item.interval]
        except ObjectDoesNotExist as e:
            print('抓到一个错误',e)
        return self.item_dic

    def get_host_triggers(self,h_obj):
        pass
