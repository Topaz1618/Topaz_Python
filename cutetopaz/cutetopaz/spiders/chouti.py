#_*_coding:utf-8_*_
# Author:Topaz
import scrapy
import hashlib
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.http.cookies import CookieJar
from scrapy import FormRequest
class MyLittleSpider(scrapy.Spider):
    name = 'topaz'
    allowed_domains = ['chouti.com']
    cookie_dict = {}
    has_request_set = {}
    def start_requests(self):
        url = 'http://dig.chouti.com/'
        obj = Request(url=url, callback=self.login)
        # print('obj',obj)        #==><GET http://dig.chouti.com/>
        yield obj
    def login(self,response):
        # print(response,response.request) # request==> <200 http://dig.chouti.com/>, response.request ==> <GET http://dig.chouti.com/>
        my_cookies = CookieJar()
        my_cookies.extract_cookies(response,response.request)
        for k, v in my_cookies._cookies.items():
            for i,j in v.items():
                for m,n in j.items():
                    self.cookie_dict[m] = n.value
        req = Request(
            url = 'http://dig.chouti.com/login',
            method ='POST',
            headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            body='phone=8618333333270&password=000000',
            cookies = self.cookie_dict,
            callback = self.check_login
        )
        yield req
    def check_login(self,response):
        req = Request(
            url = 'http://dig.chouti.com/',
            method='GET',
            cookies=self.cookie_dict,
            dont_filter=True,
            callback=self.show)
        yield req
    def show(self,response):        #第一页是check_login传给他的，后面的都是自己循环出来传给自己的
        print(response.url)
        new_list = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]')    #取出传进来的reponse页面上的全部段子div
        for new in new_list:
            link_id = new.xpath('*/div[@class="part2"]/@share-linkid').extract_first()  #==> 取出每条赞的id
            req = Request(
                url='http://dig.chouti.com/link/vote?linksId=%s' %(link_id,),
                method='POST',
                cookies=self.cookie_dict,
                callback=self.do_favor,
            )
            yield req
        page_list = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a[re:test(@href, "/all/hot/recent/\d+")]/@href').extract()
        for page in page_list:
            page_url = 'http://dig.chouti.com%s' %page
            hash = hashlib.md5()
            hash.update(bytes(page_url,encoding='utf-8'))
            key = hash.hexdigest()
            if key in self.has_request_set:
                # print(self.has_request_set)
                pass
            else:
                self.has_request_set[key] = page_url
                req =  Request(
                    url=page_url,
                    method='GET',
                    callback=self.show
                    )
                yield req
    def do_favor(self,reponse):
        print(reponse.text)










































