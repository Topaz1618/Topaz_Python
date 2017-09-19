request:
	Python标准库中提供了：urllib、urllib2、httplib等模块以供Http请求，但是，它的 API 太渣了。它是为另一个时代、另一个互联网所创建的。它需要巨量的工作，甚至包括各种方法覆盖，来完成最简单的任务。
	Requests 是使用 Apache2 Licensed 许可证的 基于Python开发的HTTP 库，其在Python内置模块的基础上进行了高度的封装，从而使得Pythoner进行网络请求时，变得美好了许多，使用Requests可以轻而易举的完成浏览器可有的任何操作

GET请求
	import requests
	payload = {'key1': 'value1', 'key2': 'value2'}
	ret = requests.get("http://httpbin.org/get", params=payload)    #加参数
	# ret = requests.get('https://github.com/timeline.json')      #不加参数
	print(ret.url)
	print(ret.text)
	
POST请求
	import requests
	import json
	url = 'https://api.github.com/some/endpoint'
	headers = {'content-type': 'application/json'}
	payload1 = {'key1': 'value1', 'key2': 'value2'}
	payload2 = {'some': 'data'}
	# ret = requests.post("http://httpbin.org/post", data=payload1)  #基本POST实例
	ret = requests.post(url, data=json.dumps(payload2),headers=headers) #发送请求头和数据实例
	print(ret.text)
	print(ret.cookies)

其他请求
	requests.get(url, params=None, **kwargs)
	requests.post(url, data=None, json=None, **kwargs)
	requests.put(url, data=None, **kwargs)
	requests.head(url, **kwargs)
	requests.delete(url, **kwargs)
	requests.patch(url, data=None, **kwargs)
	requests.options(url, **kwargs)
	# 以上方法均是在此方法的基础上构建
	requests.request(method, url, **kwargs)

参数示例
	def param_method_url():
		# requests.request(method='get', url='http://127.0.0.1:8000/test/')
		# requests.request(method='post', url='http://127.0.0.1:8000/test/')
		pass
	
	
	def param_param():
		# - 可以是字典
		# - 可以是字符串
		# - 可以是字节（ascii编码以内）
	
		# requests.request(method='get',
		# url='http://127.0.0.1:8000/test/',
		# params={'k1': 'v1', 'k2': '水电费'})
	
		# requests.request(method='get',
		# url='http://127.0.0.1:8000/test/',
		# params="k1=v1&k2=水电费&k3=v3&k3=vv3")
	
		# requests.request(method='get',
		# url='http://127.0.0.1:8000/test/',
		# params=bytes("k1=v1&k2=k2&k3=v3&k3=vv3", encoding='utf8'))
	
		# 错误
		# requests.request(method='get',
		# url='http://127.0.0.1:8000/test/',
		# params=bytes("k1=v1&k2=水电费&k3=v3&k3=vv3", encoding='utf8'))
		pass
	
	
	def param_data():
		# 可以是字典
		# 可以是字符串
		# 可以是字节
		# 可以是文件对象
	
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# data={'k1': 'v1', 'k2': '水电费'})
	
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# data="k1=v1; k2=v2; k3=v3; k3=v4"
		# )
	
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# data="k1=v1;k2=v2;k3=v3;k3=v4",
		# headers={'Content-Type': 'application/x-www-form-urlencoded'}
		# )
	
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# data=open('data_file.py', mode='r', encoding='utf-8'), # 文件内容是：k1=v1;k2=v2;k3=v3;k3=v4
		# headers={'Content-Type': 'application/x-www-form-urlencoded'}
		# )
		pass
	
	
	def param_json():
		# 将json中对应的数据进行序列化成一个字符串，json.dumps(...)
		# 然后发送到服务器端的body中，并且Content-Type是 {'Content-Type': 'application/json'}
		requests.request(method='POST',
						url='http://127.0.0.1:8000/test/',
						json={'k1': 'v1', 'k2': '水电费'})
	
	
	def param_headers():
		# 发送请求头到服务器端
		requests.request(method='POST',
						url='http://127.0.0.1:8000/test/',
						json={'k1': 'v1', 'k2': '水电费'},
						headers={'Content-Type': 'application/x-www-form-urlencoded'}
						)
	
	
	def param_cookies():
		# 发送Cookie到服务器端
		requests.request(method='POST',
						url='http://127.0.0.1:8000/test/',
						data={'k1': 'v1', 'k2': 'v2'},
						cookies={'cook1': 'value1'},
						)
		# 也可以使用CookieJar（字典形式就是在此基础上封装）
		from http.cookiejar import CookieJar
		from http.cookiejar import Cookie
	
		obj = CookieJar()
		obj.set_cookie(Cookie(version=0, name='c1', value='v1', port=None, domain='', path='/', secure=False, expires=None,
							discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False,
							port_specified=False, domain_specified=False, domain_initial_dot=False, path_specified=False)
					)
		requests.request(method='POST',
						url='http://127.0.0.1:8000/test/',
						data={'k1': 'v1', 'k2': 'v2'},
						cookies=obj)
	
	
	def param_files():
		# 发送文件
		# file_dict = {
		# 'f1': open('readme', 'rb')
		# }
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# files=file_dict)
	
		# 发送文件，定制文件名
		# file_dict = {
		# 'f1': ('test.txt', open('readme', 'rb'))
		# }
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# files=file_dict)
	
		# 发送文件，定制文件名
		# file_dict = {
		# 'f1': ('test.txt', "hahsfaksfa9kasdjflaksdjf")
		# }
		# requests.request(method='POST',
		# url='http://127.0.0.1:8000/test/',
		# files=file_dict)
	
		# 发送文件，定制文件名
		# file_dict = {
		#     'f1': ('test.txt', "hahsfaksfa9kasdjflaksdjf", 'application/text', {'k1': '0'})
		# }
		# requests.request(method='POST',
		#                  url='http://127.0.0.1:8000/test/',
		#                  files=file_dict)
	
		pass
	
	
	def param_auth():
		from requests.auth import HTTPBasicAuth, HTTPDigestAuth
	
		ret = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('wupeiqi', 'sdfasdfasdf'))
		print(ret.text)
	
		# ret = requests.get('http://192.168.1.1',
		# auth=HTTPBasicAuth('admin', 'admin'))
		# ret.encoding = 'gbk'
		# print(ret.text)
	
		# ret = requests.get('http://httpbin.org/digest-auth/auth/user/pass', auth=HTTPDigestAuth('user', 'pass'))
		# print(ret)
		#
	
	
	def param_timeout():
		# ret = requests.get('http://google.com/', timeout=1)
		# print(ret)
	
		# ret = requests.get('http://google.com/', timeout=(5, 1))
		# print(ret)
		pass
	
	
	def param_allow_redirects():
		ret = requests.get('http://127.0.0.1:8000/test/', allow_redirects=False)
		print(ret.text)
	
	
	def param_proxies():
		# proxies = {
		# "http": "61.172.249.96:80",
		# "https": "http://61.185.219.126:3128",
		# }
	
		# proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
	
		# ret = requests.get("http://www.proxy360.cn/Proxy", proxies=proxies)
		# print(ret.headers)
	
	
		# from requests.auth import HTTPProxyAuth
		#
		# proxyDict = {
		# 'http': '77.75.105.165',
		# 'https': '77.75.105.165'
		# }
		# auth = HTTPProxyAuth('username', 'mypassword')
		#
		# r = requests.get("http://www.google.com", proxies=proxyDict, auth=auth)
		# print(r.text)
	
		pass
	
	def param_stream():
		ret = requests.get('http://127.0.0.1:8000/test/', stream=True)
		print(ret.content)
		ret.close()
	
		# from contextlib import closing
		# with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
		# # 在此处理响应。
		# for i in r.iter_content():
		# print(i)
	
	def requests_session():
		import requests
	
		session = requests.Session()
	
		### 1、首先登陆任何页面，获取cookie
	
		i1 = session.get(url="http://dig.chouti.com/help/service")
	
		### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
		i2 = session.post(
			url="http://dig.chouti.com/login",
			data={
				'phone': "8615131255089",
				'password': "xxxxxx",
				'oneMonth': ""
			}
		)
	
		i3 = session.post(
			url="http://dig.chouti.com/link/vote?linksId=8589623",
		)
		print(i3.text)

实例
	抽屉网：点赞
		import requests
		# ############## 方式一 ##############
		# 1、首先登陆任何页面，获取cookie
		i1 = requests.get(url="http://dig.chouti.com/help/service")
		i1_cookies = i1.cookies.get_dict()
		# 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
		i2 = requests.post(
			url="http://dig.chouti.com/login",
			data={
				'phone': "8613217981270",
				'password': "123456",
				'oneMonth': ""
				},
			cookies=i1_cookies
			)
		#3、点赞（只需要携带已经被授权的gpsd即可）
		gpsd = i1_cookies['gpsd']
		i3 = requests.post(
			url="http://dig.chouti.com/link/vote?linksId=14211711",
			cookies={'gpsd': gpsd})
		print(i3.text)
		# ############## 方式二 ##############
		import requests
		session = requests.Session()
		i1 = session.get(url="http://dig.chouti.com/help/service")
		i2 = session.post(
			url="http://dig.chouti.com/login",
			data={
				'phone': "8613217981270",
				'password': "123456",
				'oneMonth': ""})
		i3 = session.post(url="http://dig.chouti.com/link/vote?linksId=14211711")
		print(i3.text)
	github：输出 ==> /Topaz1618/PyMySQL(909 KB); 项目路径:Topaz1618/PyMySQL
		import requests
		from bs4 import BeautifulSoup
		############## 方式一 ##############
		# 1. 访问登陆页面，获取 authenticity_token
		i1 = requests.get('https://github.com/login')
		soup1 = BeautifulSoup(i1.text, features='lxml')
		tag = soup1.find(name='input', attrs={'name': 'authenticity_token'})    #找到input标签，标签的name属性 = authenticity_token的
		authenticity_token = tag.get('value')   #拿找到标签的值
		c1 = i1.cookies.get_dict()              #拿到cookies
		i1.close()
		
		## 1. 携带authenticity_token和用户名密码等信息，发送用户验证
		form_data = {
		"authenticity_token": authenticity_token,
			"utf8": "",
			"commit": "Sign in",
			"login": "1234678@163.com",
			'password': 'wtf'
		}
		i2 = requests.post('https://github.com/session', data=form_data, cookies=c1)    #携带数据和上一次的cookies
		c2 = i2.cookies.get_dict()
		c1.update(c2)       #更新cookie
		i3 = requests.get('https://github.com/settings/repositories', cookies=c1)
		soup3 = BeautifulSoup(i3.text, features='lxml')
		list_group = soup3.find(name='div',class_='listgroup')  #找div标签 class里有listgroup的
		from bs4.element import Tag
		for child in list_group.children:
			if isinstance(child, Tag):      #看是不是tag的已知类型，isinstance(object, classinfo)
				project_tag = child.find(name='a', class_='mr-1')
				size_tag = child.find(name='small')
				temp = "项目:%s(%s); 项目路径:%s" % (project_tag.get('href'), size_tag.string, project_tag.string, )
				print(temp)
		# ############## 方式二 ##############
		session = requests.Session()
		# 1. 访问登陆页面，获取 authenticity_token
		i1 = session.get('https://github.com/login')
		soup1 = BeautifulSoup(i1.text, features='lxml')
		tag = soup1.find(name='input', attrs={'name': 'authenticity_token'})
		authenticity_token = tag.get('value')
		c1 = i1.cookies.get_dict()
		i1.close()
		# 1. 携带authenticity_token和用户名密码等信息，发送用户验证
		form_data = {
			"authenticity_token": authenticity_token,
			"utf8": "",
			"commit": "Sign in",
			"login": "wupeiqi@live.com",
			'password': 'xxoo'
		}
		i2 = session.post('https://github.com/session', data=form_data)
		c2 = i2.cookies.get_dict()
		c1.update(c2)
		i3 = session.get('https://github.com/settings/repositories')
		soup3 = BeautifulSoup(i3.text, features='lxml')
		list_group = soup3.find(name='div', class_='listgroup')
		from bs4.element import Tag
		for child in list_group.children:
			if isinstance(child, Tag):
				project_tag = child.find(name='a', class_='mr-1')
				size_tag = child.find(name='small')
				temp = "项目:%s(%s); 项目路径:%s" % (project_tag.get('href'), size_tag.string, project_tag.string, )
				print(temp)	
官方文档：http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id4

BeautifulSoup
	BeautifulSoup是一个模块，该模块用于接收一个HTML或XML字符串，然后将其进行格式化，之后遍可以使用他提供的方法进行快速查找指定元素，从而使得在HTML或XML中查找指定元素变得简单
	这个用的时候看就行
更多参数官方：http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
