# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import os
import json
import requests

class MylistPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    def __init__(self):
        self.file = open('1.txt','a')
    def process_item(self, item, spider):
        v = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(v)
        self.file.write('\n')
        self.file.flush()
        return item
class FilePipeline(object):
    def __init__(self):
        if not os.path.exists('Exercises'):      #创建个文件夹
            os.makedirs('Exercises')
    def process_item(self, item, spider):
        '''
        每个练习写到单独的文件里，取消注释就OK
        file_name = '%s.txt' %item['name']
        with open(os.path.join('Exercises', file_name), mode='ab') as f:
            title = bytes('题目:%s\n'%item['title'] ,encoding='utf-8')
            content = bytes('Demo:\n%s\n输出:\n%s\n'%(item['demo'],item['output']),encoding='utf-8')
            f.write(title)
            f.write(content)
            f.flush()
        '''
        with open('Exercises.txt', mode='ab') as f:
            name = bytes("================= %s ====================\n"%item['name'],encoding='utf-8')
            title = bytes('题目:%s\n'%item['title'] ,encoding='utf-8')
            content = bytes('Demo:\n%s\n输出:\n%s\n'%(item['demo'],item['output']),encoding='utf-8')
            f.write(name)
            f.write(title)
            f.write(content)
            f.flush()
        return item












