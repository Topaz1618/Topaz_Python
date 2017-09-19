http://www.cnblogs.com/wupeiqi/articles/6229292.html	#爬虫性能相关和Scrapy框架
性能相关
	1.在编写爬虫时，性能的消耗主要在IO请求中，当单进程单线程模式下请求URL时必然会引起等待，从而使得请求整体变慢
	1.1单线程单进程模式
		实例1：#用时 ==> 19.061163187026978
		import requests,time
		time1 = time.time()
		a = requests.get('http://www.cnblogs.com/wupeiqi/articles/6229292.html')
		b = requests.get('https://h5.qichedaquan.com/jike/?jkcx=0&channel=jingxiyuean')
		print(a.text)
		print(b.text)
		print(time.time()- time1) 
		实例2：#用时 ==>19.067904472351074
		import requests,time
		time1 = time.time()
		def get_url(url):
			a = requests.get(url)
			return a.text
		url_list = ['http://www.cnblogs.com/wupeiqi/articles/6229292.html',
					'https://h5.qichedaquan.com/jike/?jkcx=0&channel=jingxiyuean']
		for i in url_list:
			mess = get_url(i)
			print(mess)
			print(time.time()-time1) 
	1.2多线程
		1.2.1 Python threading模块	#用时 ==> 9.92071795463562
			import requests
			import threading
			import time
			def get_url(url):
				a = requests.get(url)
				print(a.text)
				print(time.time() - mytime)     
			url_list = ['http://www.cnblogs.com/wupeiqi/articles/6229292.html',
						'https://h5.qichedaquan.com/jike/?jkcx=0&channel=jingxiyuean']
			if __name__ == '__main__':
				mytime = time.time()
				for url in url_list:
					t = threading.Thread(target=get_url,args=(url,))
					t.start()
		1.2.2 线程池 		#用时 ==> 10.068973302841187
			from concurrent.futures import ThreadPoolExecutor
			import requests
			import time
			def fetch_async(url):
				response = requests.get(url)
				return response.text
			def callback(future):
				print(future.result())
			url_list = ['http://www.cnblogs.com/wupeiqi/articles/6229292.html',
						'https://h5.qichedaquan.com/jike/?jkcx=0&channel=jingxiyuean']
			pool = ThreadPoolExecutor(2)	#创建个容量为2的线程池
			time1 = time.time()
			for url in url_list:
				v = pool.submit(fetch_async, url)
				v.add_done_callback(callback)
			pool.shutdown(wait=True)
			print(time.time()-time1)
			从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，对编写线程池/进程池提供了直接的支持
			参考：https://www.ziwenxie.site/2016/12/24/python-concurrent-futures/		
	1.3多进程		
		1.3.1 Python multiprocessing模块 #用时 ==>10.076193809509277
			from multiprocessing import Process
			import requests
			import time
			def fetch_async(url):
				response = requests.get(url)
				print(response)
				print(time.time() - time1)
			url_list = ['http://www.cnblogs.com/wupeiqi/articles/6229292.html',
						'https://h5.qichedaquan.com/jike/?jkcx=0&channel=jingxiyuean']
			time1 = time.time()
			if __name__ == '__main__':
				for url in url_list:
					p = Process(target=fetch_async, args=(url,))
					p.start()
			PS：跑个题，进程这儿涉及进程间不能通信的问题，queue，managers，pipes都能解决这个问题
		
		1.3.2进程池	#用时 ==> 11.25045657157898
			from concurrent.futures import ProcessPoolExecutor
			import requests
			import time
			def fetch_async(url):
				response = requests.get(url)
				return response
			def callback(future):
				print(future.result())
			url_list = ['http://www.cnblogs.com/wupeiqi/articles/6229292.html',
						'https://h5.qichedaquan.com/jike/?jkcx=0&channel=jingxiyuean']
			pool = ProcessPoolExecutor(2)
			time1 = time.time()
			if __name__ == '__main__':
				for url in url_list:
					v = pool.submit(fetch_async, url)
					v.add_done_callback(callback)
				pool.shutdown(wait=True)
				print(time.time() - time1)
	2.通过上述代码均可以完成对请求性能的提高，对于多线程和多进程的缺点是在IO阻塞时会造成了线程和进程的浪费，所以异步IO会是首选：
	2.1 asyncio示例	#用时 ==>0.6783857345581055	非常强
		asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持
		asyncio的编程模型就是一个消息循环，从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
		import asyncio
		import time
		@asyncio.coroutine  #把一个generator标记为coroutine类型，把这个coroutine扔到EventLoop中执行
		def wget(host, url='/'):
			print('路径： %s%s' % (host, url))
			reader, writer = yield from asyncio.open_connection(host, 80)
			header = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host)    #拼接header
			print("header",header)
			writer.write(header.encode('utf-8'))        #encode header
			# yield from asyncio.sleep(5)     #yield from语法调用另一个generator,asyncio.sleep()也是一个coroutine，把asyncio.sleep()看成是一个耗时n秒的IO操作，在此期间，主线程不等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
			yield from writer.drain()   #循环调写操作并刷新buffer, 写入数据量大时用这个     给你指个路==> https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter
			text = yield from reader.read()
			print(host, url, text.decode())
			writer.close()
		tasks = [
			wget('www.cnblogs.com', '/wupeiqi/'),
			wget('www.cnblogs.com', '/wupeiqi/articles/6229292.html')] #封装两个coroutine
		time1 =time.time()
		loop = asyncio.get_event_loop()  #获取EventLoop
		results = loop.run_until_complete(asyncio.gather(*tasks)) #执行coroutine
		loop.close()
		print(time.time() - time1)
		'''
		参考：https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection
		open_connection(host=None, port=None, *, loop=None, limit=None, **kwds)，是协程
		reader return一个StreamReader实例，writer return一个StreamWriter实例，传入的参数和create_connection()没啥区别
		'''	
	2.2	gevent + requests	
		import gevent
		import requests
		from gevent import monkey
		monkey.patch_all()  #打补丁
		def fetch_async(method, url, req_kwargs):
			print(method, url, req_kwargs)
			response = requests.request(method=method, url=url, **req_kwargs)
			print(response.url, response.content)
		
		# ##### 发送请求 #####
		gevent.joinall([
			gevent.spawn(fetch_async, method='get', url='https://www.python.org/', req_kwargs={}),
			gevent.spawn(fetch_async, method='get', url='https://www.yahoo.com/', req_kwargs={}),
			gevent.spawn(fetch_async, method='get', url='https://github.com/', req_kwargs={}),
		])
		'''
		##### 发送请求（协程池控制最大协程数量） #####
		from gevent.pool import Pool
		pool = Pool(None)
		gevent.joinall([
		    pool.spawn(fetch_async, method='get', url='https://www.python.org/', req_kwargs={}),
		    pool.spawn(fetch_async, method='get', url='https://www.yahoo.com/', req_kwargs={}),
		    pool.spawn(fetch_async, method='get', url='https://www.github.com/', req_kwargs={}),
		])	
		'''
	2.3 Tornado
		pass
	2.4 Twisted示例
		pass
	更多例子：http://www.cnblogs.com/wupeiqi/articles/6229292.html
	以上均是Python内置以及第三方模块提供异步IO请求模块，使用简便大大提高效率，而对于异步IO请求的本质则是【非阻塞Socket】+【IO多路复用】：
	pass	
Scrapy	
	Scrapy介绍：
		使用Twisted异步网络库处理网络通讯,爬取网站数据，提取结构性数据的应用框架，可以应用在数据挖掘，信息处理，监测和自动化测试或存储历史数据等一系列的程序中	
	Scrapy主要包含组件；
		引擎(Scrapy)：用来处理整个系统的数据流处理, 触发事务(框架核心)
		调度器(Scheduler)：用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
		下载器(Downloader)：用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)	
		爬虫(Spiders)：爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面
		项目管道(Pipeline)：负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据
		下载器中间件(Downloader Middlewares)：位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应
		爬虫中间件(Spider Middlewares)：介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出
		调度中间件(Scheduler Middewares)：介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应
	Scrapy运行流程
		1.引擎从调度器中取出一个链接(URL)用于接下来的抓取
		2.引擎把URL封装成一个请求(Request)传给下载器
		3.下载器把资源下载下来，并封装成应答包(Response)
		4.爬虫解析Response
		5.解析出实体（Item）,则交给实体管道进行进一步的处理
		6.解析出的是链接（URL）,则把URL交给调度器等待抓取
	安装：
		Linux
			pip3 install scrapy
		Windows
			a. pip3 install wheel
			b. 下载twisted http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
			c. 进入下载目录，执行 pip3 install Twisted-17.5.0-cp35-cp35m-win_amd64.whl
			d. pip3 install scrapy
			e. 下载并安装pywin32：https://sourceforge.net/projects/pywin32/files/
	基本命令：
		1. scrapy startproject 项目名称					
			- scrapy startproject cutetopaz					#在当前目录中创建中创建一个项目文件（类似于Django）
		2. scrapy genspider [-t template] <name> <domain>	
			- scrapy genspider -t basic topaz topaz.com		#创建爬虫应用
		3. scrapy list					#展示爬虫应用列表
		4. scrapy crawl 爬虫应用名称	#运行单独爬虫应用
		PS：
			scrapy genspider -l				#查看所有命令
			scrapy genspider -d 模板名称	#查看模板命令
	来俩实例练练手：
		练手之前了解下HtmlXpathSelector，HtmlXpathSelector用于结构化HTML代码并提供选择器功能，比beautiful快
			#_*_coding:utf-8_*_
			# Author:Topaz
			from scrapy.selector import Selector, HtmlXPathSelector
			from scrapy.http import HtmlResponse
			html = """<!DOCTYPE html>
			<html>
				<head lang="en">
					<meta charset="UTF-8">
					<title></title>
				</head>
				<body>
					<ul>
						<li class="item-"><a id='i12' href="link.html">first item</a></li>
						<li class="item-0"><a id='i2' href="llink.html">first item</a></li>
						<li class="item-1"><a href="llink2.html">second item<span>vv</span></a></li>
					</ul>
					<div><a href="llink2.html">second item</a></div>
				</body>
			</html>
			"""
			response = HtmlResponse(url='http://example.com', body=html,encoding='utf-8')
			hxs = Selector(response)    # ==> <Selector xpath=None data='<html>\n    <head lang="en">\n        <met'>
			hxs = Selector(response=response).xpath('//a')      #拿到了所有a标签
			hxs = Selector(response=response).xpath('//a[@id]')     #拿到所有有id属性的标签
			hxs = Selector(response=response).xpath('//a[starts-with(@href,"link")]' )  #拿到开头为link的href标签
			hxs = Selector(response=response).xpath('//a[contains(@href, "link")]') #拿到链接包含link的href标签
			hxs = Selector(response=response).xpath('//a[re:test(@id, "i\d+")]')    #正则 取出i开头后边是数字的
			hxs = Selector(response=response).xpath('//a[re:test(@id, "i\d+")]/text()').extract()   #===> ['first item', 'first item']
			hxs = Selector(response=response).xpath('//a[re:test(@id, "i\d+")]/@href').extract()    #==> ['link.html', 'llink.html']
			hxs = Selector(response=response).xpath('/html/body/ul/li/a/@href').extract()       #==> ['link.html', 'llink.html', 'llink2.html']
			hxs = Selector(response=response).xpath('//body/ul/li/a/@href').extract_first() #==> link.html
			print(hxs)
			参考：https://doc.scrapy.org/en/0.12/topics/selectors.html
		实例1：
		import scrapy
		from scrapy.selector import Selector		#一会儿结构化html用，跟beautiful一个作用
		from scrapy.http.request import Request		#Request是一个封装用户请求的类，在回调函数中yield该对象表示继续访问
		class DigSpider(scrapy.Spider):
			name = "dig"    # 爬虫应用的名称，通过此名称启动爬虫命令
			allowed_domains = ["chouti.com"]    # 允许的域名
			start_urls = ['http://dig.chouti.com/',]    # 起始URL
			has_request_set = {}
			def parse(self, response):
				# print('url:',response.url)
				page_list = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a[re:test(@href, "/all/hot/recent/\d+")]/@href').extract()
				for page in page_list:      #循环拿到的uri列表
					page_url = 'http://dig.chouti.com%s' % page #拼接
					key = self.md5(page_url)    #送它去加密
					if key in self.has_request_set:
						pass
					else:
						self.has_request_set[key] = page_url    #把key加到列表里
						obj = Request(url=page_url, method='GET', callback=self.parse)
						yield obj
			@staticmethod
			def md5(val):   #封装成静态方法，不让它访问类变量和实例变量
				import hashlib
				ha = hashlib.md5()
				ha.update(bytes(val, encoding='utf-8'))
				key = ha.hexdigest()
				return key
		实例2：scrapy自动登录抽屉并点赞：
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
				# print('cookies!!!!',my_cookies._cookies)    # ==> 社会主义cookie，有用的cookie，想要的都有，取就是了
				for k, v in my_cookies._cookies.items():
					# print('随意拿，不要害羞',v)  #==> 分成了两部分， 捂污吴~~
					for i,j in v.items():
						# print('来宝贝跟稳了我们一起看jj',j)                 # ==>有包含gpsd的部分哟~
						for m,n in j.items():
							# print('只是个M啦',m)              #==>gpsd等
							# print('n',n.value)                #==>gpsd的值等
							self.cookie_dict[m] = n.value
				# print('看看大字典',self.cookie_dict)   #==>{'gpsd': 'a460c7e96329f9b6257ebe805f54d9dc', 'route': '249e9500f56e96c9681c6db3bc475cbf', 'JSESSIONID': 'aaaqYBsRkE1JRa77_hH5v'}
				req = Request(
					url = 'http://dig.chouti.com/login',
					method ='POST',
					headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
					body='phone=8618310703270&password=123456',
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
						# print('调用自己',page_url) http://dig.chouti.com/all/hot/recent/9
						self.has_request_set[key] = page_url
						req =  Request(
							url=page_url,
							method='GET',
							callback=self.show
							)
						yield req
			def do_favor(self,reponse):
				print(reponse.text)
	项目结构以及爬虫应用简介
		cutetopaz/
			scrapy.cfg				#项目的主配置信息（真正爬虫相关的配置信息在settings.py文件中）
			cutetopaz/				
				__init__.py
				items.py			#设置数据存储模板，用于结构化数据 如：Django的Model
				pipelines.py		#数据处理行为 如：一般结构化的数据持久化
				settings.py			#配置文件 如：递归的层数、并发数，延迟下载等
				spiders/			#爬虫目录 如：创建文件，编写爬虫规则
					__init__.py
					爬虫1.py		#一般创建爬虫文件时，以网站域名命名	
	settings.py
		# -*- coding: utf-8 -*-
		# Scrapy settings for step8_king project
		#
		# For simplicity, this file contains only settings considered important or
		# commonly used. You can find more settings consulting the documentation:
		#
		#     http://doc.scrapy.org/en/latest/topics/settings.html
		#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
		#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
		
		# 1. 爬虫名称
		BOT_NAME = 'step8_king'
		
		# 2. 爬虫应用路径
		SPIDER_MODULES = ['step8_king.spiders']
		NEWSPIDER_MODULE = 'step8_king.spiders'
		
		# Crawl responsibly by identifying yourself (and your website) on the user-agent
		# 3. 客户端 user-agent请求头
		# USER_AGENT = 'step8_king (+http://www.yourdomain.com)'
	
		# Obey robots.txt rules
		# 4. 禁止爬虫配置
		# ROBOTSTXT_OBEY = False
		
		# Configure maximum concurrent requests performed by Scrapy (default: 16)
		# 5. 并发请求数
		# CONCURRENT_REQUESTS = 4
		
		# Configure a delay for requests for the same website (default: 0)
		# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
		# See also autothrottle settings and docs
		# 6. 延迟下载秒数
		# DOWNLOAD_DELAY = 2		
		
		# The download delay setting will honor only one of:
		# 7. 单域名访问并发数，并且延迟下次秒数也应用在每个域名
		# CONCURRENT_REQUESTS_PER_DOMAIN = 2
		# 单IP访问并发数，如果有值则忽略：CONCURRENT_REQUESTS_PER_DOMAIN，并且延迟下次秒数也应用在每个IP
		# CONCURRENT_REQUESTS_PER_IP = 3
		
		# Disable cookies (enabled by default)
		# 8. 是否支持cookie，cookiejar进行操作cookie
		# COOKIES_ENABLED = True
		# COOKIES_DEBUG = True
		
		# Disable Telnet Console (enabled by default)
		# 9. Telnet用于查看当前爬虫的信息，操作爬虫等...
		#    使用telnet ip port ，然后通过命令操作
		# TELNETCONSOLE_ENABLED = True
		# TELNETCONSOLE_HOST = '127.0.0.1'
		# TELNETCONSOLE_PORT = [6023,]
		
		
		# 10. 默认请求头
		# Override the default request headers:
		# DEFAULT_REQUEST_HEADERS = {
		#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		#     'Accept-Language': 'en',
		# }		
		# Configure item pipelines
		# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
		
		# 11. 定义pipeline处理请求
		# ITEM_PIPELINES = {
		#    'step8_king.pipelines.JsonPipeline': 700,
		#    'step8_king.pipelines.FilePipeline': 500,
		# }
					
		# 12. 自定义扩展，基于信号进行调用
		# Enable or disable extensions
		# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
		# EXTENSIONS = {
		#     # 'step8_king.extensions.MyExtension': 500,
		# }
					
		# 13. 爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
		# DEPTH_LIMIT = 3
		
		# 14. 爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo
		# 后进先出，深度优先
		# DEPTH_PRIORITY = 0
		# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
		# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
		# 先进先出，广度优先
		# DEPTH_PRIORITY = 1
		# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
		# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
		
		# 15. 调度器队列
		# SCHEDULER = 'scrapy.core.scheduler.Scheduler'
		# from scrapy.core.scheduler import Scheduler
		
		# 16. 访问URL去重
		# DUPEFILTER_CLASS = 'step8_king.duplication.RepeatUrl'
		# Enable and configure the AutoThrottle extension (disabled by default)
		# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
		
		"""
		17. 自动限速算法
			from scrapy.contrib.throttle import AutoThrottle
			自动限速设置
			1. 获取最小延迟 DOWNLOAD_DELAY
			2. 获取最大延迟 AUTOTHROTTLE_MAX_DELAY
			3. 设置初始下载延迟 AUTOTHROTTLE_START_DELAY
			4. 当请求下载完成后，获取其"连接"时间 latency，即：请求连接到接受到响应头之间的时间
			5. 用于计算的... AUTOTHROTTLE_TARGET_CONCURRENCY
			target_delay = latency / self.target_concurrency
			new_delay = (slot.delay + target_delay) / 2.0 # 表示上一次的延迟时间
			new_delay = max(target_delay, new_delay)
			new_delay = min(max(self.mindelay, new_delay), self.maxdelay)
			slot.delay = new_delay
		"""
		
		# 开始自动限速
		# AUTOTHROTTLE_ENABLED = True
		# The initial download delay
		# 初始下载延迟
		# AUTOTHROTTLE_START_DELAY = 5
		# The maximum download delay to be set in case of high latencies
		# 最大下载延迟
		# AUTOTHROTTLE_MAX_DELAY = 10
		# The average number of requests Scrapy should be sending in parallel to each remote server
		# 平均每秒并发数
		# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
		
		# Enable showing throttling stats for every response received:
		# 是否显示
		# AUTOTHROTTLE_DEBUG = True
		
		# Enable and configure HTTP caching (disabled by default)
		# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
		
		
		"""
		18. 启用缓存
			目的用于将已经发送的请求或相应缓存下来，以便以后使用
			
			from scrapy.downloadermiddlewares.httpcache import HttpCacheMiddleware
			from scrapy.extensions.httpcache import DummyPolicy
			from scrapy.extensions.httpcache import FilesystemCacheStorage
		"""
		# 是否启用缓存策略
		# HTTPCACHE_ENABLED = True
		
		# 缓存策略：所有请求均缓存，下次在请求直接访问原来的缓存即可
		# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.DummyPolicy"
		# 缓存策略：根据Http响应头：Cache-Control、Last-Modified 等进行缓存的策略
		# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"
		
		# 缓存超时时间
		# HTTPCACHE_EXPIRATION_SECS = 0
		
		# 缓存保存路径
		# HTTPCACHE_DIR = 'httpcache'
		
		# 缓存忽略的Http状态码
		# HTTPCACHE_IGNORE_HTTP_CODES = []
		
		# 缓存存储的插件
		# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
		
		
		"""
		19. 代理，需要在环境变量中设置
			from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
			
			方式一：使用默认
				os.environ
				{
					http_proxy:http://root:woshiniba@192.168.11.11:9999/
					https_proxy:http://192.168.11.11:9999/
				}
			方式二：使用自定义下载中间件
			
			def to_bytes(text, encoding=None, errors='strict'):
				if isinstance(text, bytes):
					return text
				if not isinstance(text, six.string_types):
					raise TypeError('to_bytes must receive a unicode, str or bytes '
									'object, got %s' % type(text).__name__)
				if encoding is None:
					encoding = 'utf-8'
				return text.encode(encoding, errors)
				
			class ProxyMiddleware(object):
				def process_request(self, request, spider):
					PROXIES = [
						{'ip_port': '111.11.228.75:80', 'user_pass': ''},
						{'ip_port': '120.198.243.22:80', 'user_pass': ''},
						{'ip_port': '111.8.60.9:8123', 'user_pass': ''},
						{'ip_port': '101.71.27.120:80', 'user_pass': ''},
						{'ip_port': '122.96.59.104:80', 'user_pass': ''},
						{'ip_port': '122.224.249.122:8088', 'user_pass': ''},
					]
					proxy = random.choice(PROXIES)
					if proxy['user_pass'] is not None:
						request.meta['proxy'] = to_bytes（"http://%s" % proxy['ip_port']）
						encoded_user_pass = base64.encodestring(to_bytes(proxy['user_pass']))
						request.headers['Proxy-Authorization'] = to_bytes('Basic ' + encoded_user_pass)
						print "**************ProxyMiddleware have pass************" + proxy['ip_port']
					else:
						print "**************ProxyMiddleware no pass************" + proxy['ip_port']
						request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])
			
			DOWNLOADER_MIDDLEWARES = {
			'step8_king.middlewares.ProxyMiddleware': 500,
			}
			
		"""
		
		"""
		20. Https访问
			Https访问时有两种情况：
			1. 要爬取网站使用的可信任证书(默认支持)
				DOWNLOADER_HTTPCLIENTFACTORY = "scrapy.core.downloader.webclient.ScrapyHTTPClientFactory"
				DOWNLOADER_CLIENTCONTEXTFACTORY = "scrapy.core.downloader.contextfactory.ScrapyClientContextFactory"
				
			2. 要爬取网站使用的自定义证书
				DOWNLOADER_HTTPCLIENTFACTORY = "scrapy.core.downloader.webclient.ScrapyHTTPClientFactory"
				DOWNLOADER_CLIENTCONTEXTFACTORY = "step8_king.https.MySSLFactory"
				
				# https.py
				from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
				from twisted.internet.ssl import (optionsForClientTLS, CertificateOptions, PrivateCertificate)
				
				class MySSLFactory(ScrapyClientContextFactory):
					def getCertificateOptions(self):
						from OpenSSL import crypto
						v1 = crypto.load_privatekey(crypto.FILETYPE_PEM, open('/Users/wupeiqi/client.key.unsecure', mode='r').read())
						v2 = crypto.load_certificate(crypto.FILETYPE_PEM, open('/Users/wupeiqi/client.pem', mode='r').read())
						return CertificateOptions(
							privateKey=v1,  # pKey对象
							certificate=v2,  # X509对象
							verify=False,
							method=getattr(self, 'method', getattr(self, '_ssl_method', None))
						)
			其他：
				相关类
					scrapy.core.downloader.handlers.http.HttpDownloadHandler
					scrapy.core.downloader.webclient.ScrapyHTTPClientFactory
					scrapy.core.downloader.contextfactory.ScrapyClientContextFactory
				相关配置
					DOWNLOADER_HTTPCLIENTFACTORY
					DOWNLOADER_CLIENTCONTEXTFACTORY			
		"""
		
		"""
		21. 爬虫中间件
			class SpiderMiddleware(object):
		
				def process_spider_input(self,response, spider):
					'''
					下载完成，执行，然后交给parse处理
					:param response: 
					:param spider: 
					:return: 
					'''
					pass
			
				def process_spider_output(self,response, result, spider):
					'''
					spider处理完成，返回时调用
					:param response:
					:param result:
					:param spider:
					:return: 必须返回包含 Request 或 Item 对象的可迭代对象(iterable)
					'''
					return result
			
				def process_spider_exception(self,response, exception, spider):
					'''
					异常调用
					:param response:
					:param exception:
					:param spider:
					:return: None,继续交给后续中间件处理异常；含 Response 或 Item 的可迭代对象(iterable)，交给调度器或pipeline
					'''
					return None
			
			
				def process_start_requests(self,start_requests, spider):
					'''
					爬虫启动时调用
					:param start_requests:
					:param spider:
					:return: 包含 Request 对象的可迭代对象
					'''
					return start_requests
			
			内置爬虫中间件：
				'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 50,
				'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
				'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 700,
				'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': 800,
				'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 900,
		
		"""
		# from scrapy.contrib.spidermiddleware.referer import RefererMiddleware
		# Enable or disable spider middlewares
		# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
		SPIDER_MIDDLEWARES = {
		# 'step8_king.middlewares.SpiderMiddleware': 543,
		}
		
		
		"""
		22. 下载中间件
			class DownMiddleware1(object):
				def process_request(self, request, spider):
					'''
					请求需要被下载时，经过所有下载器中间件的process_request调用
					:param request:
					:param spider:
					:return:
						None,继续后续中间件去下载；
						Response对象，停止process_request的执行，开始执行process_response
						Request对象，停止中间件的执行，将Request重新调度器
						raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
					'''
					pass
			
			
			
				def process_response(self, request, response, spider):
					'''
					spider处理完成，返回时调用
					:param response:
					:param result:
					:param spider:
					:return:
						Response 对象：转交给其他中间件process_response
						Request 对象：停止中间件，request会被重新调度下载
						raise IgnoreRequest 异常：调用Request.errback
					'''
					print('response1')
					return response
			
				def process_exception(self, request, exception, spider):
					'''
					当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
					:param response:
					:param exception:
					:param spider:
					:return:
						None：继续交给后续中间件处理异常；
						Response对象：停止后续process_exception方法
						Request对象：停止中间件，request将会被重新调用下载
					'''
					return None
		
			
			默认下载中间件
			{
				'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
				'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
				'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
				'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
				'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
				'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
				'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
				'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
				'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
				'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
				'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
				'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
				'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
				'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
			}
		
		"""
		# from scrapy.contrib.downloadermiddleware.httpauth import HttpAuthMiddleware
		# Enable or disable downloader middlewares
		# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
		# DOWNLOADER_MIDDLEWARES = {
		#    'step8_king.middlewares.DownMiddleware1': 100,
		#    'step8_king.middlewares.DownMiddleware2': 500,
		# }
	pipelines.py
		
							
	中间件

	自定制命令
	
	避免重复访问
									
	自定义扩展								
										
	真的の实例								
								
								
								
								
								
								
								
										
