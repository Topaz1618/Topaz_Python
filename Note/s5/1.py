模块:用一坨代码实现某个功能的代码集合，多个.py文件组成的代码集合就叫做模块
模块分为3种：
	自定义模块
	内置标准模块（又称标准库）
	开源模块
PS:自定义模块和开源模块的使用参考： http://www.cnblogs.com/wupeiqi/articles/4963027.html

time模块
	import time
	time.process_time() #测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
	time.altzone()  #返回与utc时间的时间差,以秒计算
	time.asctime() #以格式 "Fri Aug 19 11:14:16 2016" 返回时间
	time.ctime() #同上
	time.localtime() #返回本地时间的 struct 时间对象格式
	time.gmtime(time.time()-800000) #返回utc时间的struc时间对象格式
	时间转换关系：
	print("时间转换关系")
		a = time.strptime("2017/08/09","%Y/%m/%d")  #"2017/08/15" ==> struct对象时间
		b = time.mktime(a)              #struct时间对象 ==> 时间戳
		c = time.gmtime(b)              #时间戳 ==> struct时间对象
		d = time.strftime('%Y%m%d',time.gmtime()) #struct时间对象 ==> "20170815"
		
datetime模块
	print(datetime.datetime.now())	#当前时间
	print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
	print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
	print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
	print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
	print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2016-08-19
	ctime  = datetime.datetime.now()
	print(c_time.replace(minute=3,hour=2)) #时间替换
	
	
random模块
	>>> random.random()		#产生随机数
	0.3481685190239724
	>>> random.randint(1,20)	#设定产生随机数范围 
	2
	>>> random.randrange(1,20)	#同上
	3
	例子：
		import random
		checkcode = ""
		for i in range(4):
			c = random.randrange(0,4)
			print(c)
			if c != i:
				temp = chr(random.randint(65,90))   #生成字符
			else:
				temp = random.randint(0,9)
			checkcode += str(temp)
			# print(checkcode)
		print(checkcode)
	
os模块
	os.getcwd() 		#获取当前工作目录，即当前python脚本工作的目录路径
	os.chdir("dirname")	#改变当前脚本工作目录；相当于shell下cd
	os.curdir  		#返回当前目录: ('.')
	os.pardir  		#获取当前目录的父目录字符串名：('..')
	os.makedirs('dirname1/dirname2')    #可生成多层递归目录
	os.removedirs('dirname1')   #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
	os.mkdir('dirname')    		#生成单级目录；相当于shell中mkdir dirname
	os.rmdir('dirname')    		#删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
	os.mknod("test.txt") 		#创建空文件，需要root权限
	os.listdir('dirname')    	#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
	os.remove()  				#删除一个文件
	os.rename("oldname","newname")  #重命名文件/目录
	os.stat('path/filename')  		#获取文件/目录信息
	os.sep    		#输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
	os.linesep    	#输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
	os.pathsep   	#输出用于分割文件路径的字符串
	os.name    		#输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
	os.system("bash command")  #运行shell命令，直接显示
	os.environ  			#获取系统环境变量
	os.path.abspath(path)  	#返回path规范化的绝对路径
	os.path.split(path)  	#将path分割成目录和文件名二元组返回
	os.path.dirname(path)  	#返回path的目录。其实就是os.path.split(path)的第一个元素
	os.path.basename(path) 	#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
	os.path.exists(path)  	#如果path存在，返回True；如果path不存在，返回False
	os.path.isabs(path)   	#如果path是绝对路径，返回True
	os.path.isfile(path)  	#如果path是一个存在的文件，返回True。否则返回False
	os.path.isdir(path)   	#如果path是一个存在的目录，则返回True。否则返回False
	os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
	os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
	os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间
	更多参考:https://docs.python.org/2/library/os.html?highlight=os#module-os
	
sys模块
	sys.argv           #命令行参数List，第一个元素是程序本身路径
	sys.exit(n)        #退出程序，正常退出时exit(0)
	sys.version        #获取Python解释程序的版本信息
	sys.maxint         #最大的Int值
	sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
	sys.platform       #返回操作系统平台名称
	sys.stdout.write('please:')
	val = sys.stdin.readline()[:-1]

shutil模块
	高级的文件，文件夹，压缩包处理模块
	最后再看吧，偷个懒
	参考：http://www.cnblogs.com/wupeiqi/articles/4963027.html 
	
json & pickle模块
	json:用于字符串和python数据类型间进行转换
	pickle：用于python特有的类型和python的数据类型键进行转换
	Json模块提供了四个功能：dumps、dump、loads、load
	pickle模块提供了四个功能：dumps、dump、loads、load
	例1:
		import json
		import pickle
		import os
		data = "aaa"
		mydata = pickle.dumps(data)
		print(mydata)
		yourdata = pickle.loads(mydata)
		print(yourdata)
		mydata2 = json.dumps(data)
		print(mydata2)
	例2：
		import json
		import pickle
		import os
		data = "aaa"
		print("============ pickle =============")
		mydata = pickle.dumps(data) #将数据通过特殊形式转换成只有python语言认识的字符串
		print(mydata)
		yourdata = pickle.loads(mydata)
		print(yourdata)
		print("============ json =============")
		mydata2 = json.dumps(data)  #将数据通过特殊形式转换成所有程序语言都认识的字符串
		print(mydata2)
		yourdata2 = json.loads(mydata2)
		print(yourdata2)	
		with open('G:/Topaz/Mall/aaa','w') as f:    #将数据通过特殊形式转换成所有程序语言都认识的字符串,并写入文件
			json.dump(data,f)
	
xml处理模块
	将数据转换成所有程序语言都认识的字符串，和json一样，不过json使用更简单
	xmltest.xml
		<data right="bitchhh">
			11113
			<a>2222
				<biu>333</biu>
				<xiu>444</xiu>
			</a>
			<h1>
				"nini"
				<biu>11</biu>
			</h1>
			<h1>
				<biu>34</biu>
				<biu>24</biu>
			</h1>
		</data>
	操作：
		import xml.etree.ElementTree as ET
		tree = ET.parse("G:/Topaz/Mall/xmltest.xml")    #拿到文本对象
		root = tree.getroot()
		'''打印xml文档'''
		print(root.tag)                     #打印第一层标签
		for child in root:
			print(child.tag)                #打印子标签
			for i in child:
				print(i.tag,i.text)                #打印孙子标签
		for node in root.iter('data'):      #遍历当前文档所有指定标签
			print(node.tag,node.text)       #打印标签名，打印文本内容
		'''修改xml文档'''
		for child in root.iter('data'):
			print(child.tag, child.text)
			new_data = int(child.text) + 1	
			child.text = str(new_data)		#修改标签内容
			child.set('right','bitchhh')	#增加标签属性
		tree.write("G:/Topaz/Mall/xmltest.xml")
		'''删除xml文档'''
		for child in root.findall('h1'):        # findall 能找到所有指定标签
			rank = int(child.find('biu').text)  # find 只找第一个指定标签
			if rank < 20:
				root.remove(child)				#真正干活der~
		tree.write("G:/Topaz/Mall/xmltest.xml")	
	自己创建xml文档
	from django.test import TestCase
	import xml.etree.ElementTree as ET
	new_xml = ET.Element("namelist")    #最外层标签名
	name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})   #声明一个新标签name，名字，属性
	age = ET.SubElement(name, "age", attrib={"checked": "no"})          #声明一个name的子标签，标签名age，属性
	sex = ET.SubElement(name, "sex")
	sex.text = '33'
	name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})   #什么一个新标签name2
	age = ET.SubElement(name2, "age")
	age.text = '19'
	et = ET.ElementTree(new_xml)  # 生成文档对象
	et.write("test.xml", encoding="utf-8", xml_declaration=True)	
	ET.dump(new_xml)  # 打印生成的格式
		
PyYAML模块
	Python也可以很容易的处理ymal文档格式，只不过需要安装一个模块，参考文档：http://pyyaml.org/wiki/PyYAMLDocumentation 	

ConfigParser模块
	用于生成和修改常见配置文档，当前模块的名称在 python 3.x 版本中变更为 configparser。
	my.cnf(假装是完整的my.cnf)
		[mysqld]
		port = 3306
		max_allowed_packet = 1M
		key_buffer_size = 16K
		socket = /tmp/mysql.sock
		
		[mysqldump]
		max_allowed_packet = 16M
		
		[myisamchk]
		key_buffer_size = 8M
	configParser模块生成my.cnf：
		import configparser
		config = configparser.ConfigParser()
		config['mysqld'] = {'port':3306,
							'socket':'/tmp/mysql.sock',
							'key_buffer_size':'16K',
							'max_allowed_packet':'1M'}
		
		config['mysqldump'] = {'max_allowed_packet':'16M'}
		
		config['myisamchk'] = {}
		config['myisamchk']['key_buffer_size'] = '8M'
		
		with open('my.cnf.bak','w') as f:
			config.write(f)
	增删改读配置文件，参考：http://www.cnblogs.com/alex3714/articles/5161349.html
	
hashlib模块
	用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
	操作：
		import hashlib
		# ######## md5 ########
		hash = hashlib.md5()
		hash.update('admin')
		print(hash.hexdigest())
		# ######## sha1 ########
		hash = hashlib.sha1()
		hash.update('admin')
		print(hash.hexdigest())
		# ######## sha256 ########	
		hash = hashlib.sha256()
		hash.update('admin')
		print(hash.hexdigest())	
		# ######## sha384 ########	
		hash = hashlib.sha384()
		hash.update('admin')
		print(hash.hexdigest())	
		# ######## sha512 ########	
		hash = hashlib.sha512()
		hash.update('admin')
		print(hash.hexdigest())
	'''
		def digest(self, *args, **kwargs): # real signature unknown
			""" Return the digest value as a string of binary data. """
			pass

		def hexdigest(self, *args, **kwargs): # real signature unknown
			""" Return the digest value as a string of hexadecimal digits. """
			pass'''
	还不够吊？python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
	散列消息鉴别码，简称HMAC，是一种基于消息鉴别码MAC（Message Authentication Code）的鉴别机制。使用HMAC时,消息通讯的双方，通过验证消息中加入的鉴别密钥K来鉴别消息的真伪；
	一般用于网络通信中消息加密，前提是双方先要约定好key,就像接头暗号一样，然后消息发送把用key把消息加密，接收方用key ＋ 消息明文再加密，拿加密后的值 跟 发送者的相对比是否相等，这样就能验证消息的真实性，及发送者的合法性了。
	import hmac
	h = hmac.new(b'天王盖地虎', b'宝塔镇河妖')
	print h.hexdigest()
	更多关于md5,sha1,sha256等介绍的文章看这里：https://www.tbs-certificates.co.uk/FAQ/en/sha256.html 
	
Subprocess模块 
	没啥好说的，自己看
	subprocess实现sudo 自动输入密码： http://www.cnblogs.com/alex3714/articles/5161349.html
		
logging模块
	提供了标准的日志接口，你可以通过它存储各种格式的日志
	logging五个日志级别：debug(), info(), warning(), error(), critical()
	logging模块四个主要类：
		1)logger：提供了应用程序可以直接使用的接口
			每个程序在输出信息之前都要获得一个Logger。Logger通常对应了程序的模块名
			LOG=logging.getLogger(”chat.gui”)	#聊天工具的图形界面模块可以这样获得它的Logger
			LOG=logging.getLogger(”chat.kernel”)	#核心模块可以这样
			Logger.setLevel(lel)				#指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
			Logger.addFilter(filt)、Logger.removeFilter(filt)	#添加或删除指定的filter
			Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)#增加或删除指定的handler
			Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()	#可以设置的日志级别		
		2)handler：将logger创建的日志记录发送到合适的目的输出
			handler对象负责发送相关的信息到指定目的地。Python的日志系统有多种Handler可以使用。有些Handler可以把信息输出到控制台，有些Logger可以把信息输出到文件，还有些 Handler可以把信息发送到网络上。如果觉得不够用，还可以编写自己的Handler。可以通过addHandler()方法添加多个多handler
			Handler.setLevel(lel)	#指定被处理的信息级别，低于lel级别的信息将被忽略
			Handler.setFormatter()	#给这个handler选择一个格式
			Handler.addFilter(filt),Handler.removeFilter(filt)	#新增或删除一个filter对象		
			每个Logger可以附加多个Handler。接下来我们就来介绍一些常用的Handler：
			a. logging.StreamHandler
				使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
				它的构造函数是：StreamHandler([strm])	#strm(文件对象)，默认是sys.stderr
			b. logging.FileHandler
				类似StreamHandler，不过FileHandler会帮你打开这个文件
				它的构造函数是：FileHandler(filename[,mode])	# filename(文件名,必须指定),mode(文件打开方式,默认是’a',参见Python内置函数open()的用法。。)
			c. logging.handlers.RotatingFileHandler
				类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建 一个新的同名日志文件继续输出。比如日志文件是chat.log。当chat.log达到指定的大小之后，RotatingFileHandler自动把 文件改名为chat.log.1。不过，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2。。。最后重新创建 chat.log，继续输出日志信息。它的构造函数是：
				RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]])
				#maxBytes(日志文件的最大文件大小,值为0文件可以无限大，重命名过程就不会发生)
				#backupCount(指定保留的备份文件的个数,超过个数删除旧文件)
			d. logging.handlers.TimedRotatingFileHandler
				和RotatingFileHandler类似，区别是间隔一定时间自动创建新的日志文件，重命名的过程与RotatingFileHandler类似，不过新的文件不是附加数字，而是当前时间
				它的构造函数：TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])
				#interval(时间间隔)
				#when(字符串,时间间隔的单位,S 秒,M 分,H 小时,D 天,W 每星期,midnight 每天凌晨)
	例1：
		import logging
		'''INFO以及级别更高的消息记录到文件里，时间格式'''
		logging.basicConfig(filename='example.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
		logging.warning('小问题不碍事儿')
		logging.critical("赶紧解决，不然罚款罚死你丫")
		logging.debug("我呢 把我也记上行不行")
		logging.info("嘘")
		example.log：
		08/16/2017 06:58:39 PM 小问题不碍事儿
		08/16/2017 06:58:39 PM 赶紧解决，不然罚款罚死你丫
		08/16/2017 06:58:39 PM 嘘
	例2:日志记录和切割
		import logging
		from logging import handlers
		logger = logging.getLogger(__name__)
		log_file = "example.log"
		fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3) #输出方式，写入日志文件，并按时间切割
		formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')      #日志内容格式
		fh.setFormatter(formatter)  #设定格式
		logger.addHandler(fh)       #设定输出方式
		logger.warning("test1")
		logger.warning("test12")
		logger.warning("test13")
		logger.warning("test14")
re模块
	常用正则表达式符号：
		'.'     #默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
		'^'     #匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
		'$'     #匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
		'*'     #匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
		'+'     #匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
		'?'     #匹配前一个字符1次或0次
		'{m}'   #匹配前一个字符m次
		'{n,m}' #匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
		'|'     #匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
		'(...)' #分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
		'\A'    #只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
		'\Z'    #匹配字符结尾，同$
		'\d'    #匹配数字0-9
		'\D'    #匹配非数字
		'\w'    #匹配[A-Za-z0-9]
		'\W'    #匹配非[A-Za-z0-9]
		's'     #匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
		'(?P<name>...)' #分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
	最常用的匹配语法：
		re.match 从头开始匹配
		re.search 匹配包含
		re.findall 把所有匹配到的字符放到以列表中的元素返回
		re.splitall 以匹配到的字符当做列表分隔符
		re.sub      匹配字符并替换
	反斜杠的困扰：
		正则表达式里使用"\"作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符"\"，那么使用编程语言表示的正则表达式里将需要4个反斜杠"\\\\"：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。Python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r"\\"表示。同样，匹配一个数字的"\\d"可以写成r"\d"
	仅需轻轻知道的几个匹配模式：
		re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
		M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
		S(DOTALL): 点任意匹配模式，改变'.'的行为
	
	练习：
	开发一个简单的python计算器
	实现加减乘除及拓号优先级解析
	用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致
