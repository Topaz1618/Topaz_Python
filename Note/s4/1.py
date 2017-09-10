列表生成式
	#列表 a = [0,1,2,3,4,5,6,7,8,9], 把列表里的每个值加1，怎么实现？
	#方法一：
	b = []
	for i in a:
		b.append(i+1)
	a = b
	print(a)	
	#方法二：原值修改
	for index,i in enumerate(a):
		a[index] += 1
	print(a)
	#方法三
	list = map(lambda n:n+1,a)
	for i in list:
		print(i)
	#方法四
	a = [i+1 for i in range(10)]
	print(a)
	#以上就是列表生成

生成器：
	1.python中一边循环一遍计算的机制叫生成器:generator
	2.为啥要有生成器：列表受内存限制，容量有限
	3.使用生成器的前提：列表的元素可以按照某种算法推算出来，能在循环过程中不断推算出后面的元素，就可以使用生成器，不用创建完整列表了
	4.创建generator
		1)一个列表生成式的[]改成()，就创建了一个generator
			>>> L = [x * x for x in range(10)]
			>>> L
			[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
			>>> g = (x * x for x in range(10))
			>>> g
			<generator object <genexpr> at 0x1022ef630>
			#创建L和g的区别仅在于最外层的[]和()
		2)在普通函数中包含yield关键字，就变成了一个generator
			'''来把两种创建生成器的方式结合一下'''
			list_gen = (i for i in range(3))	#第一种
			def fun_gen(n):						#第二种，就是普通函数加上yield这种
				while n < 3:
					print("hello here is fun_gen ==>",n)
					yield n
					n += 1		
			for num in list_gen:    #0,1,2
				for i in fun_gen(num):  #循环拿到0,1,2的生成器fun_gen
					print(i)             #拿到fun_gen yield的值
	5.打印generator中的元素
		1)通过next()函数获得generator的下一个返回值
			>>> next(g)
			0
			>>> next(g)
			1
			#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
		2)最好使用for循环，因为generator也是可迭代对象
			
			>>> g = (x * x for x in range(10))
			>>> for n in g:
			...     print(n)
			0
			1
			4
	6.算法复杂的列表，可以用函数来生成
		比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
		1, 1, 2, 3, 5, 8, 13, 21, 34, ...
		def fib(max):
			'''	
				1.这段代码定义了波拉契数列的推算规则，逻辑和generator很相似
				2.只要把print(b)改为yield b，fib函数就变成generator了，就是上面说的第二种定义generator的方法
				3.函数和generator的区别：
				函数 ==> 顺序执行，遇到return语句或者最后一行函数语句返回
				generator ==> 每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行 '''
			n, a, b = 0, 0, 1
			while n < max:
				print(b)
				a, b = b, a + b
				n = n + 1
			return 'done'
		>>> fib(5)
		1
		1
		2
		3
		5
		done
	7.拿到generator的return返回值
		但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
		>>> g = fib(3)
		>>> while True:
		...    try:
		...        x = next(g)
		...        print('g:', x)
		...    except StopIteration as e:
		...        print('Generator return value:', e.value)
		...        break
		g: 1
		g: 1
		g: 2
		Generator return value: done
	8.例子：通过yield实现在单线程的情况下实现并发运算的效果　	
	例1：
		import time
		def consumer(name):
			print("%s 准备吃包子啦!" %name)
			while True:
			baozi = yield
			# print(baozi)
			print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
		
		def producer():
			c = consumer('豹子头林冲')       #这步什么都不会发生
			c2 = consumer('花和尚鲁智深')
			c.__next__()            #调用next，打印到yield之前,然后不会有任何期待的事情发生  ==> A 准备吃包子啦!
			c2.__next__()
			print("老子开始准备做包子啦!")    #打印做包子
			for i in range(10):                 #这步主要是为了做10次包子
				time.sleep(1)
				print("做了2个包子!")
				c.send(i)                       #直到遇到了send，期待的事发生了，consumer yield后面的语句打印惹~
				c2.send(i)
		producer()
		# send是什么  ==>　http://www.cnblogs.com/coderzh/archive/2008/05/18/1202040.html
	例2：（简陋的例子，方便理解send写的）
		def h(name):
			print(name)
			while True:
				print("打死你")
				m = yield
				print(m)
		def i():
			c = h("你说我啥")
			c.__next__()
			c.send("怕不怕")
			c.__next__()
		i()
		'''
		不写while会引发的报错 ==> 每次调用next(g)，就计算出g的下一个元素的值。。。
		Traceback (most recent call last):
		File "G:/Topaz/Mall/shopping/tests.py", line 43, in <module>
			i()
		File "G:/Topaz/Mall/shopping/tests.py", line 41, in i
			c.send("怕不怕")
		StopIteration
		'''

迭代器：
	可迭代对象(Iterable): 
		1.可以for循环的对象统称可迭代对象，有以下两类：
			集合类型:list,tuple,dict,set,str
			generator:包括生成器和带 yield 的 generator function
		2.使用isinstance()判断一个对象是否是Iterable对象
		>>> from collections import Iterable
		>>> isinstance([],Iterable)
		True
		>>> isinstance({},Iterable)
		True
		>>> isinstance('abc',Iterable)
		True
		>>> isinstance(100,Iterable)
		False
	迭代器(Iterator)：
		1.迭代器可以被next()函数调用，并不断返回下一个值，举个例子：生成器
		2.使用isinstance()判断一个对象是否是Iterator对象
		>>> from collections import Iterator
		>>> isinstance([],Iterator)
		False
		>>> isinstance((x for x in range(10)),Iterator)
		True
	PS：使用iter()函数，把list，dict，str等Iterable变成Iterator
		>>> isinstance(iter([]),Iterator)
		True
		>>> isinstance(iter('abc'),Iterator)
		True
		你可能会问，为什么list、dict、str等数据类型不是Iterator？
		这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
		Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
	小结：
		1.生成器又是Iterator又是Iterable
		2.可以for循环的都是可迭代对象
		3.可以调用next()函数的都是Iterator类型，Iterator类型是惰性计算的序列
		3.集合数据类型（str，dict，list）可以通过iter()函数获得一个Iterator对象
		4.Python的for循环本质上就是不断调用next()函数
			for x in [1, 2, 3, 4, 5]:
				pass
			等价于：
			a = iter([1,2,3,4,5])
			while True:
				try:
					x = next(a)
				except StopIteration:
					break

装饰器:
	遵循软件开发的“开放-封闭”原则，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：
		封闭：已实现的功能代码块
		开放：对扩展开发		
	实例：
		已有功能：多个视频专区模块video，movie
		扩展功能：用户登陆认证
		应用：在某个或多个视频专区(video,movie)里应用用户登陆认证功能	
		1.0v 独立的函数：需要认证的调用它
			问题:已实现功能的代码被修改	
		1.1v 高阶函数：把需要认证的函数当做参数传给认证函数
			问题：调用方式发生变化，之前的调用方式 video(),现在的调用方式login(video)
			PS:如果100个视频模块要认证，100个不是一个人写的，都要改调用方式，被骂死惹
		1.2v 高阶函数调用方式不变的修改
			america = login(america)	#函数赋值给变量名
			america()					#用户调用是这样的，还是原来的配方美滋滋
			问题：大哥你就没发现，用户没调用之前它自己就执行了吗,来下一个版本我们解决这个问题
		1.3v 高阶函数调用方式不变，不自己执行的修改（就是装饰器啦）
			def login(func):	#把要执行的模块从这里传进来
				def inner():	#再定义一层函数
					if user_status == True:
					func() # 看这里看这里，只要验证通过了，就调用相应功能
				 return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数
		究极体2.0v  以上实现了装饰器(诨名语法糖儿)，不过还能写的更简单~
			america = login(america)	#这个去掉
			@login						#在需要调用用户认证的函数上@login
			def video():
		究极体变异(传参)：
			def inner(arg1)		#在inner里加参数就可以了，还可以用非固定参数(*args,**kargs)
				func(arg1)
		代码：
		#练习1：我不想多加一层，试下能不能直接返回func，可以的。
			def login(func):
				print("here is login~~")
				# 不加直接返回func的内存地址
				# print(func)      #<function video at 0x000001BBA1D25510>
				return func
				'''
				在里面加一层返回inner的内存地址
				def inner(*args):
					return func(*args)
				# print(inner)        #<function login.<locals>.inner at 0x000001E5E1BBD840>
				return inner
				'''
			@login
			def video(*args):
				print("video",*args)
			def movie():
				print("movie")
			video(1,2,3)		#调用
		输出：
			here is login~~
			video 1 2 3
		#练习2：(login本身有参数，只能再多加一层传func。但是inner是不需要的)
			def login(auth_type): #把要执行的模块从这里传进来
				def auth(func):
					def inner(*args,**kwargs):#再定义一层函数
						if auth_type == "qq":
							_username = "topaz" #假装这是DB里存的用户信息
							_password = "123" #假装这是DB里存的用户信息
							global user_status
			
							if user_status == False:
								username = input("user:")
								password = input("pasword:")
			
								if username == _username and password == _password:
									print("welcome login....")
									user_status = True
								else:
									print("wrong username or password!")
			
							if user_status == True:
								return func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
						else:
							print("only support qq ")
					return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数
				return auth
			def home():
				print("---首页----")
			@login('qq')
			def america(*args,**kwargs):
				#login() #执行前加上验证
				print("----欧美专区----",args)
			home()
			america()
			#另一种调用方式，等同于america()
			america = login('qq')(america)
			america(1,2,3)

软件目录结构规范：
	可读性高：不熟悉代码的人，能一眼看懂目录结构，知道程序启动脚本是哪个，测试目录在哪，配置文件在哪，快速了解项目
	可维护性高：定义好组织规则后，维护者能明确知道，新增的哪个文件和代码应该放在什么目录下，好处是，随着时间推移，代码/配置规模增加，项目结构不会混乱
	目录结构：
		Foo/
		|-- bin/		#存放项目的一些可执行文件，当然你可以起名script/之类的也行。
		|   |-- foo
		|
		|-- foo/		#存放项目的所有源代码,源代码中的所有模块、包都应该放在此目录。不要置于顶层目录
		|   |-- tests/	#tests/存放单元测试代码
		|   |   |-- __init__.py
		|   |   |-- test_main.py
		|   |
		|   |-- __init__.py
		|   |-- main.py	#程序的入口最好命名为main.py
		|
		|-- docs/		#存放一些文档
		|   |-- conf.py
		|   |-- abc.rst
		|
		|-- setup.py	#安装、部署、打包的脚本
		|-- requirements.txt	#存放软件依赖的外部Python包列表
		|-- README		#项目说明文件
	更多参考：https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
	README需要说明以下几个事项:
		软件定位，软件的基本功能。
		运行代码的方法: 安装环境、启动命令等。
		简要的使用说明。
		代码目录结构说明，更详细点可以说明软件的基本原理。
		常见问题说明。
	参考：Redis源码中Readme的写法 https://github.com/antirez/redis#what-is-redis
	setup.py：
		一般来说，用setup.py来管理代码的打包、安装、部署问题。业界标准的写法是用Python流行的打包工具setuptools来管理这些事情。这种方式普遍应用于开源项目中。不过这里的核心思想不是用标准化的工具来解决这些问题，而是说，一个项目一定要有一个安装部署工具，能快速便捷的在一台新机器上将环境装好、代码部署好和将程序运行起来。
		我刚开始接触Python写项目的时候，安装环境、部署代码、运行程序这个过程全是手动完成，遇到过以下问题:
		安装环境时经常忘了最近又添加了一个新的Python包，结果一到线上运行，程序就出错了。
		Python包的版本依赖问题，有时候我们程序中使用的是一个版本的Python包，但是官方的已经是最新的包了，通过手动安装就可能装错了。
		如果依赖的包很多的话，一个一个安装这些依赖是很费时的事情。
		新同学开始写项目的时候，将程序跑起来非常麻烦，因为可能经常忘了要怎么安装各种依赖。
		setup.py可以将这些事情自动化起来，提高效率、减少出错的概率。"复杂的东西自动化，能自动化的东西一定要自动化。"是一个非常好的习惯。
		setuptools的文档比较庞大，刚接触的话，可能不太好找到切入点。学习技术的方式就是看他人是怎么用的，可以参考一下Python的一个Web框架，flask是如何写的:https://github.com/mitsuhiko/flask/blob/master/setup.py
		当然，简单点自己写个安装脚本（deploy.sh）替代setup.py也未尝不可。
	requirements.txt：
		方便开发者维护软件的包依赖。将开发过程中新增的包添加进这个列表中，避免在setup.py安装依赖时漏掉软件包。
		方便读者明确项目使用了哪些Python包。
		这个文件的格式是每一行包含一个包依赖的说明，通常是flask>=0.10这种格式，要求是这个格式能被pip识别，这样就可以简单的通过 pip install -r requirements.txt来把所有Python包依赖都装好了。具体格式说明<a href="https://pip.readthedocs.org/en/1.1/requirements.html">点这里</a>	
	关于配置文件的使用方法
		注意，在上面的目录结构中，没有将conf.py放在源码目录下，而是放在docs/目录下。
		很多项目对配置文件的使用做法是:
			配置文件写在一个或多个python文件中，比如此处的conf.py。
			项目中哪个模块用到这个配置文件就直接通过import conf这种形式来在代码中使用配置。
		这种做法我不太赞同:
			这让单元测试变得困难（因为模块内部依赖了外部配置）
			另一方面配置文件作为用户控制程序的接口，应当可以由用户自由指定该文件的路径。
			程序组件可复用性太差，因为这种贯穿所有模块的代码硬编码方式，使得大部分模块都依赖conf.py这个文件。
		所以，我认为配置的使用，更好的方式是：
			模块的配置都是可以灵活配置的，不受外部配置文件的影响。
			程序的配置也是可以灵活控制的。
			能够佐证这个思想的是，用过nginx和mysql的同学都知道，nginx、mysql这些程序都可以自由的指定用户配置。
		所以，不应当在代码中直接import conf来使用配置文件。上面目录结构中的conf.py，是给出的一个配置样例，不是在写死在程序中直接引用的配置文件。可以通过给main.py启动参数指定配置路径的方式来让程序读取配置内容。当然，这里的conf.py你可以换个类似的名字，比如settings.py。或者你也可以使用其他格式的内容来编写配置文件，比如settings.yaml之类的。


	
