# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class CutetopazItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiaoHuarItem(scrapy.Item):
    name = scrapy.Field()
    school = scrapy.Field()
    url = scrapy.Field()
#https://doc.scrapy.org/en/latest/topics/items.html#item-fields
    #Field对象中定义的每个键可以被不同的组件使用   ==> 所以pipeline可以用它，真的就相当于django的models
    #Field对象不会被分配为类属性，使用Item.fields访问它们