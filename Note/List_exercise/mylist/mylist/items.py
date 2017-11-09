# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MylistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class listItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    analysis = scrapy.Field()
    demo = scrapy.Field()
    output =scrapy.Field()
