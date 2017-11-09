#_*_coding:utf-8_*_
# Author:Topaz
import scrapy
import re
import json
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse,Request
from ..items import listItem
#scrapy crawl list_exercise

class My_List(scrapy.spiders.Spider):
    name = "list_exercise"
    allowed_domains = ["runoob.com"]
    start_urls = [
        "http://www.runoob.com/python/python-100-examples.html",
    ]
    def parse(self,response):
        #分析页面
        #找到a标签，访问
        #获取a标签内需要的内容，也就是题目和答案啦
        item = listItem()
        hxs = HtmlXPathSelector(response)
        instance = hxs.select('//div[@ id = "content"]')
        item['name'] = instance.select('//h1/text()').extract_first()
        item['title'] = instance.select('//p[2]/text()').extract_first()
        item['analysis'] = instance.select('//p[3]/text()').extract_first()
        all_span = instance.select('//div/div/div/span/text()')
        mydemo = ''
        for span in all_span:
            mydemo += span.extract()
        item['demo'] = mydemo
        all_output = instance.select('//div[@id="content"]/pre/text()')
        myoutput = ''
        for span in all_output:
            myoutput += span.extract()
        item['output'] = myoutput.replace('\r\n', '\n')
        yield item
        all_urls = hxs.xpath('//a/@href').extract()
        for url in all_urls:
            if url.startswith('/python/python-exercise-example'):
            # if re.match('/python/python-exercise-example\d+.html',url):
                q_url = "http://www.runoob.com%s"%url
                yield Request(q_url, callback=self.parse)




