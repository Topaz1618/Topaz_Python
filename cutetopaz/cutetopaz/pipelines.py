# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import requests

class CutetopazPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    '''按照settings.py里的顺序，先执行这个'''
    def __init__(self):
        self.file = open('xiaohua.txt', 'w')
    def process_item(self, item, spider):
        v = json.dumps(dict(item), ensure_ascii=False)  #item ==> <class 'cutetopaz.items.XiaoHuarItem'>  dict(item) ==> <class 'dict'> ，肉眼看的话item就是个字典啊，去掉dict()报错is not JSON serializable
        self.file.write(v)
        self.file.write('\n')
        self.file.flush()
        return item     #返回一个json序列化后的item
class FilePipeline(object):
    def __init__(self):
        if not os.path.exists('imgs'):      #创建个文件夹
            os.makedirs('imgs')
    def process_item(self, item, spider):
        response = requests.get(item['url'], stream=True)
        print('看看',response.__attrs__)
        file_name = '%s_%s.jpg' % (item['name'], item['school'])
        with open(os.path.join('imgs', file_name), mode='wb') as f:
            f.write(response.content)
        return item