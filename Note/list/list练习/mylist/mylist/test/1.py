#_*_coding:utf-8_*_
# Author:Topaz
# from scrapy.selector import HtmlXPathSelector,Selector
# from scrapy.http import HtmlResponse,Request
#
# with open('list1.html', 'rb') as f:
#     data = f.read()
#     real_data = data.decode()
#
# response = HtmlResponse(url='text/list1.html',body='real_data',encoding='utf-8')
# hxs = Selector(response)
# print(hxs)
# all_urls = hxs.xpath('//a')
# print(all_urls)
# # for url in all_urls:
# #     if url.startswith('/python/python-exercise-example'):
# #         # if re.match('/python/python-exercise-example\d+.html',url):
# #         print('== get url', url)
#
#
# # item = hxs.xpath('//p')
# # print(item)

# with open('a.txt','rb') as f:
#     data = f.read()
#     data = data.encode('utf-8')
#     print(data)
class line(object):
    def __init__(self):
        self.file = open('1.txt','a')
    def item(self, item, spider):
        for i in range(10):
            self.file.write(i)

a = line()
a.item()












