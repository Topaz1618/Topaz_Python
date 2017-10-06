#_*_coding:utf-8_*_
# Author:Topaz
import scrapy
import hashlib
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.http.cookies import CookieJar
from scrapy import FormRequest
from ..items import XiaoHuarItem

class XiaoHuarSpider(scrapy.Spider):
    name = "hira"
    allowed_domains = ["xiaohuar.com"]
    start_urls = ["http://www.xiaohuar.com/list-1-1.html",]
    has_request_set = {}
    def parse(self, response):
        hxs = Selector(response)
        items = hxs.xpath('//div[@class="item_list infinite_scroll"]/div')
        for item in items:
            src = item.xpath('.//div[@class="img"]/a/img/@src').extract_first()        #==> /d/file/20170324/7c5825a2da9703ed0102839ffb9a1000.jpg
            name = item.xpath('.//div[@class="img"]/span/text()').extract_first()      #==>周路
            school = item.xpath('.//div[@class="img"]/div[@class="btns"]/a/text()').extract_first()    #==>广西大学
            url = "http://www.xiaohuar.com%s" % src
            obj = XiaoHuarItem(name=name,school=school, url=url)
            print('你要的object',obj)
            yield obj
        urls = hxs.xpath('//a[re:test(@href, "http://www.xiaohuar.com/list-1-\d+.html")]/@href').extract()    #拿到所有页面
        for url in urls:
            print("here is url:",url)
            key = self.md5(url)
            print('key!!!!!',key)
            if key in self.has_request_set:
                # print('你要的大字典',self.has_request_set)
                pass
            else:
                # print('看看是哪个url',url)
                self.has_request_set[key] = url
                req = Request(url=url,method='GET',callback=self.parse)
                yield req
    @staticmethod
    def md5(val):
        ha = hashlib.md5()
        ha.update(bytes(val, encoding='utf-8'))
        key = ha.hexdigest()
        return key