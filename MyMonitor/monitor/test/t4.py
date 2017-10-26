#_*_coding:utf-8_*_
# Author:Topaz
import os
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"MyMonitor.settings")
import django
django.setup()
from django.conf import settings
from monitor import models
monitor_dic = {}
host_list = models.Host.objects.all()
for h in host_list:
    monitor_dic[h] = {'items': {}, 'expressions': {}}
    item_list = []
    trigger_list = {}
    expression_list = []
    for template in h.template.select_related():
        # print(template.item.select_related())
        item_list.extend(template.item.select_related())
        for item in template.item.select_related():
            for key in item.keys.select_related():
                expression_list.extend(key.triggerexpression_set.select_related())
                for expression in key.triggerexpression_set.select_related():
                        expression_list.append([expression.id,expression])

                        # Entry.objects.filter(id__in=[1, 3, 4])
                        # print(trigger_name)
                        #
                        # monitor_dic[h]['expressions'][trigger_obj.name] ={}
                        # monitor_dic[h]['expressions'][trigger_obj.name][expression.id] = expression



type_list = ['and','or']
logic_type = 'and'
if  logic_type in type_list :
    print("ok")