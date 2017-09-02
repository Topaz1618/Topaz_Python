面向对象高级语言
1.经典类：深度优先（python2.x默认）
2.新式类：C3算法，并非广度优先（python3之后所有类都是新式类）参考：http://www.cnblogs.com/blackmatrix/p/5630515.html
3.静态方法
	通过@staticmethod装饰器即可把其装饰的方法变为一个静态方法
	什么是静态方法呢？其实不难理解，普通的方法，可以在实例化后直接调用，并且在方法里可以通过self.调用实例变量或类变量，但静态方法是不可以访问实例变量或类变量的，一个不能访问实例变量和类变量的方法，其实相当于跟类本身已经没什么关系了，它与类唯一的关联就是需要通过类名来调用这个方法
	代码：
		class Dog(object):	
			def __init__(self,name):
				self.name = name
			@staticmethod #把eat方法变为静态方法
			def eat(self):
				print("%s is eating" % self.name)
		d = Dog("ChenRonghua")
		d.eat()
	报错：
		Traceback (most recent call last):
		File "/Users/jieli/PycharmProjects/python基础/自动化day7面向对象高级/静态方法.py", line 17, in <module>
			d.eat()
		TypeError: eat() missing 1 required positional argument: 'self'
		上面的调用会出以下错误，说是eat需要一个self参数，但调用时却没有传递，没错，当eat变成静态方法后，再通过实例调用时就不会自动把实例本身当作一个参数传给self了
	想让上面的代码可以正常工作有两种办法
		调用时主动传递实例本身给eat方法，即d.eat(d) 
		在eat方法中去掉self参数，但这也意味着，在eat中不能通过self.调用实例中的其它变量了
		
4.类方法
	类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
	代码：
		class Dog(object):
			def __init__(self,name):
				self.name = name
		
			@classmethod
			def eat(self):
				print("%s is eating" % self.name)
		d = Dog("ChenRonghua")
		d.eat()
	报错：Dog没有name属性，因为name是个实例变量，类方法是不能访问实例变量的
		Traceback (most recent call last):
		File "/Users/jieli/PycharmProjects/python基础/自动化day7面向对象高级/类方法.py", line 16, in <module>
			d.eat()
		File "/Users/jieli/PycharmProjects/python基础/自动化day7面向对象高级/类方法.py", line 11, in eat
		print("%s is eating" % self.name)
		AttributeError: type object 'Dog' has no attribute 'name'
	解决：定义一个类变量
		class Dog(object):
			name = "我是类变量"
		执行结果 ==> 我是类变量 is eating

5.属性方法
	属性方法的作用就是通过@property把一个方法变成一个静态属性
	代码：
		class Dog(object):
			def __init__(self,name):
				self.name = name
			@property
			def eat(self):
				print(" %s is eating" %self.name)
		d = Dog("ChenRonghua")
		d.eat()
	报错：
		Traceback (most recent call last):
		ChenRonghua is eating
		File "/Users/jieli/PycharmProjects/python基础/自动化day7面向对象高级/属性方法.py", line 16, in <module>
			d.eat()
		TypeError: 'NoneType' object is not callable
		NoneType is not callable, 因为eat此时已经变成一个静态属性了， 不是方法了， 想调用已经不需要加()号了，直接d.eat就可以了
	解决：
		d.eat

6.类的特殊成员方法
	1)__init__:构造方法，通过类创建对象时，自动触发执行。
	2)__doc__ :表示类的描述信息
	3)__module__:当前操作的对象在哪个模块
	4)__class__ :当前操作的对象的类是什么
	5)__call__ :构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
	6)__dict__：查看类或对象中的所有成员 　
	7)__str__: 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回
	8)__getitem__、__setitem__、__delitem__：用于索引操作，如字典。以上分别表示获取、设置、删除数据
	9)__del__  :析构方法，当对象在内存中被释放时，自动触发执行，此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的
	代码：
	class Dog(object):
		'''上天'''
		def __init__(self,sec):					#构造函数，创建对象就触发
			self.name = '智慧树下智慧果'
			self.sec = sec
		def __call__(self, *args, **kwargs):	#call方法，类后面+俩括号就触发
			print("打call是什么意思？？")
		def __str__(self):						#str方法
			return "智慧树下做游戏"
		def __getitem__(self, item):			#getitem方法
			print(item)
		def __setitem__(self, key, value):		#setitem方法
			print(key,value)
		def __delitem__(self,key):				#delitem方法
			print("__delitem__",key)
	#==================== 开始表演 ========================
		'''实力演示__doc__ 方法'''
		print(Dog.__doc__) 		#输出结果 ==> 上天
		''' model & class 演示'''
		from hhh import Dog
		wisdom = Dog()
		print(wisdom.__module__)	#输出结果 ==> hhh
		print(wisdom.__class__)	#输出结果 ==>	<class 'hhh.Dog'>
		'''两种姿势演示__call___方法'''
		wisdom = Dog()				#输出结果 ==> 打call是什么意思？？
		wisdom()			
		Dog()()					#输出结果 ==> 打call是什么意思？？
		'''演示__dict__方法'''
		print(Dog.__dict__) #获取类的成员，即：静态字段、方法,输出结果 ==> {'__init__': <function Dog.__init__ at 0x00000221E920E840>, '__module__': '__main__', '__doc__': '上天', '__call__': <function Dog.__call__ at 0x00000221E920E8C8>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>}
		wisdom = Dog('智慧树上只有我') # 获取 对象obj1 的成员,输出结果 ==> {'sec': '智慧树上只有我', 'name': '智慧树下智慧果'}
		print(wisdom.__dict__)
		'''演示__str__方法'''
		wisdom = Dog('智慧树上只有我')	
		print(wisdom)		#输出 ==> 智慧树下做游戏
	10)__new__ 和 __metaclass__
		'''
			上述代码中，wisdom 是通过 Foo 类实例化的对象，其实不仅 obj 是一个对象，Foo类本身也是一个对象，因为在Python中一切事物都是对象
				print(type(wisdom))	#输出 ==> <class '__main__.Dog'> , 表示，wisdom 对象由 Dog 类创建
				print(type(Dog))	#输出 ==> <class 'type'>  , 表示 Dog 类对象由 type 类创建
			wisdom对象是通过执行Foo类的构造方法创建，widdom对象是Dog类的一个实例，Dog类对象是 type 类的一个实例，即：Dog类对象是通过type类的构造方法创建
			那么，创建类就可以有两种方式：
			a)普通方式
				class Dog(object):
					def __init__(self,sec):
					self.name = '智慧树下智慧果'
					print(self.name,sec)
				obj = Dog('智慧树上只有我')
			b)特殊方式
				def __init__(self,sec):
					self.name = '智慧树下智慧果'
					print(self.name,sec)
				Dog = type('Dog',(object,),{'__init__':__init__})
				obj = Dog('智慧树上只有我')	
			So 明白了吗婊贝，类是由 type 类实例化产生'''
		那么问题来了，类默认是由 type 类实例化产生，type类中如何创建类的？类又是如何创建对象？
		答：类中有一个属性 __metaclass__，用来表示该类由谁来实例化创建，所以，我们可以为 __metaclass__ 设置一个type类的派生类，从而查看类创建的过程。
			类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__
		参考：http://www.cnblogs.com/alex3714/articles/5213184.html
		metaclass 详解文章：http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python 得票最高那个答案写的非常好
	
7.反射
	通过字符串映射或修改程序运行时的状态、属性、方法
	getattr
	hasattr(object,name) #判断object中有没有一个name字符串对应的方法或属性
	setattr(x,y,v)
	delattr(x,y)
	代码：
		class Dog(object):
		def __init__(self):
			self.name = 'Topaz'
		def func(self):
			return '想静静'
		obj = Dog()
		###### 检查是否含有成员 ####
		hasattr(obj, 'name')    #存在输出==>True
		hasattr(obj, 'func')    #存在输出==>True
		##### 获取成员 ####
		getattr(obj, 'name')    #输出==>Topaz
		getattr(obj, 'func')    #输出==>想静静
		###### 设置成员 ####
		setattr(obj, 'age', 18)
		setattr(obj, 'show', lambda num: num + 1)
		print(obj.age,obj.show(1))  #输出==>18,2
		###### 删除成员 ####
		delattr(obj, 'name')
		print(obj.name)     #删了哦，报错 ==> AttributeError: 'Dog' object has no attribute 'name'
		delattr(obj, 'func')
		print(obj.func())       #删了哦，报错 ==> AttributeError: func
	动态导入模块：
		- Pyの交易
			- member
				- __init__.py
				- 铁柱.py
				- 犬次郎.py
			- sugar_mummy.py
		然后来看看怎么导入♂的：
			sugar_mummy.py
				import importlib
				#__import__('import_lib.metaclass')  这是解释器自己内部用的，与下面这句效果一样
				importlib.import_module('member.铁柱') #官方建议用这个

8.异常处理：
	1）异常的作用
		在编程过程中为了增加友好性，在程序出现bug时一般不会将错误信息显示给用户，而是现实一个提示的页面，通俗来说就是不让用户看见大黄页！！！
	2）异常种类
		python中的异常种类非常多，每个异常专门用于处理某一项异常
		AttributeError 	#试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
		IOError 		#输入/输出异常；基本上是无法打开文件
		ImportError 	#无法引入模块或包；基本上是路径问题或名称错误
		IndentationError 	#语法错误（的子类） ；代码没有正确对齐
		IndexError 			#下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
		KeyError 		#试图访问字典里不存在的键
		KeyboardInterrupt #Ctrl+C被按下
		NameError 		#使用一个还未被赋予对象的变量
		SyntaxError 	#Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
		TypeError 		#传入对象类型与要求的不符合
		UnboundLocalError #试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
		ValueError 		#传入一个调用者不期望的值，即使值的类型是正确的
		a)实例：IndexError
			Dog = ['小白','小黑','小黄','咪咪']
			try:
				Dog[10]
			except IndexError as e:
				print(e)		#==>list index out of range
			Dog[10] 			#==>IndexError: list index out of range(上面还有三行报错，占地儿就不复制过来了)
		b)实例：KeyError
			Dog = {'哈士奇':'可爱炸','泰迪':'bitch'}
			try:
				Dog['金毛']
			except KeyError as e:
				print(e)   # ==>'金毛'
		c)实例：ValueError
			Dog = 'oops'
			try:
				int(Dog)
			except ValueError as e:
				print(e)   #==> invalid literal for int() with base 10: 'oops'
		#PS:对于上述实例，异常类只能用来处理指定的异常情况，如果非指定异常则无法处理,就是说不能用IndexError捕捉KeyError的错误		
		所以，写程序时需要考虑到try代码块中可能出现的任意异常，可以这样写：		
			s1 = 'hello'
			try:
				int(s1)
			except IndexError,e:
				print e
			except KeyError,e:
				print e
			except ValueError,e:
				print e	
		万能异常：Exception，他可以捕获任意异常
			s1 = 'hello'
			try:
				int(s1)
			except Exception,e:
				print e			
		接下来你可能要问了，既然有这个万能异常，其他异常是不是就可以忽略了！
		答：当然不是，对于特殊处理或提醒的异常需要先定义，最后定义Exception来确保程序正常运行。				
			s1 = 'hello'
			try:
				int(s1)
			except KeyError,e:
				print '键错误'
			except IndexError,e:
				print '索引错误'
			except Exception, e:
				print '错误'	
	3）异常的其它结构
		try:
			# 主代码块
			pass
		except KeyError,e:
			# 异常时，执行该块
			pass
		else:
			# 主代码块执行完，执行该块
			pass
		finally:
			# 无论异常与否，最终执行该块
			pass
	4）主动触发异常
		try:
			raise Exception('自己触发异常')
		except Exception as e:
			print(e) 
	5）自定义异常
		class Topaz(Exception):
			def __init__(self,msg):
				self.msg = msg
			def __str__(self):
				return self.msg
		try:
			raise Topaz('自定义异常')
		except Topaz as e:
			print(e)
	6）断言
		# assert 条件
		assert 1 == 1
		assert 1 == 2
	更多参考：http://www.cnblogs.com/wupeiqi/articles/5017742.html
	
练习：开发一个支持多用户在线的FTP程序
要求：
用户加密认证
允许同时多用户登录
每个用户有自己的家目录 ，且只能访问自己的家目录
对用户进行磁盘配额，每个用户的可用空间不同
允许用户在ftp server上随意切换目录
允许用户查看当前目录下文件
允许上传和下载文件，保证文件一致性
文件传输过程中显示进度条
附加功能：支持文件的断点续传	

示例：https://github.com/triaquae/py_training/tree/master/sample_code/ftp_sample
