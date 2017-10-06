# _*_coding:utf-8_*_
# Author:Topaz
import scrapy
import hashlib
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
import json
from selenium import webdriver
import os
class ZhiHuSpider(scrapy.Spider):
    name  = 'zhihu'
    allow_domains = ["zhihu.com"]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    cookie_dict = {}
    def start_requests(self):
        # print(self.headers)
        start_url = 'https://www.zhihu.com/'
        req = Request(url=start_url,
                      headers=self.headers,
                      callback=self.login,)
        # print('=====Start_requests',req)
        yield req
    def login(self,response):
        # print('reponse',reponse.url)
        my_cookies = CookieJar()
        my_cookies.extract_cookies(response,response.request)
        # print('cookies!!!!',my_cookies._cookies)    # ==> 社会主义cookie，有用的cookie，想要的都有，取就是了
        for k,v in my_cookies._cookies.items():
            for i,j in v.items():
                for m,n in j.items():
                    self.cookie_dict[m] = n.value
        req = Request(      #https://www.rddoc.com/doc/Scrapy-1.3/topics/request-response/
            url = 'https://www.zhihu.com/login/email',
            method = 'POST',
            headers=self.headers,
            body='email=18310703270&password=nihao123@',
            cookies=self.cookie_dict,
            callback=self.home_page,
        )
        yield req
    def home_page(self,response):
        # print(response.url)
        req = Request(
            url = 'https://www.zhihu.com/question/28853910',
            method='GET',
            headers=self.headers,
            callback=self.get_question,
        )
        yield req
    def get_question(self,response):
        results = Selector(response).xpath('//body')
        print(type(results))
        if results.get('is_end') == True:
            print("true")
            next_page = results.get('next')
            print(next_page)
        else:
            print("false")
            print(type(results))
            # next_page = results.get('paging')
            next_page = results.get('next')
            # aa = json.loads(next_page)
            print(type(next_page),json.loads(next_page))


        # print(html)
    # def show(self,response):
    #     print('show啦啦啦啦啦啦',response.request)



    #     url_list = Selector(response=response).xpath('//div[@class="List-item"]/div[@class="ContentItem AnswerItem"]/meta[@itemprop="url"]/@content')
    #     # url_list = Selector(response=response).xpath('//div[@class="List-item"]/div[@class="ContentItem AnswerItem"]/meta[@itemprop="url"]/@content')
    #     # print(url_list.extract())
    # # def click(self,response):
    # #     chromedriver = "F:\software\package\chromedriver_win32\chromedriver.exe"
    #     # os.environ["webdriver.chrome.driver"] = chromedriver
    #     # driver = webdriver.Chrome(chromedriver)
    #     # driver.get('https://www.zhihu.com/question/28853910')
    #     # next = driver.find_element_by_xpath('//div[@id="QuestionAnswers-answers"]/div[@class="Card"]/button[@class="Button QuestionMainAction"]')
    #     # while next:
    #     # # url_list = Selector(response=response).xpath('//div[@class="List-item"]/div[@class="ContentItem AnswerItem"]/meta[@itemprop="url"]/@content')
    #     #     html = driver.page_source
    #     #     print(html.encode('utf-8'))
    #     #     next.click()
    #     # else:
    #     #     print("没有了")
    #
    #     # req = Request(
    #     #     url=url,
    #     #     headers=self.headers,
    #     #     callback=self.show,
    #     # )
    #     # yield req



