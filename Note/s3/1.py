函数：
定义：函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可
特性：	
	1.减少重复代码 
	2.提高扩展性
	3.易于维护
函数参数与局部变量：
	形参：只有在被函数调用的时候才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此形参只在函数
	内部有效，函数调用结束后，返回主调用函数后则不能再使用该形参变量
	实参：可以是常量，变量，表达式，函数等，无论是什么类型的量，在进行函数调用时，必须有确定的值，
	以便把这些值传给形参，因此应预先用赋值，输入等办法使参数获得确定值
	例子：tests.py
		def topaz(a,y):		#形参
			res = a + y
			return res

		def Top():
			c = topaz(1,2)	#实参
			print(c)
		Top()	==> 3	
	默认参数：
		def stu(name, age, country, course):	#这个例子，每次传参都传了相同参数，CN
			print("----注册学生信息------")
			print("姓名:", name)
			print("age:", age)
			print("国籍:", country)
			print("课程:", course)	
		stu("刘老根", 25, "CN", "linux")		
		stu("张叫春",21,"CN","linux")
		stu("刘老根",25,"CN","linux")
		
		def stu(name,age,course,country="CN"):		#加上默认参数就不需要指定了，对有没有发现放到最后了，这就要了解关键参数
			print("----注册学生信息------")
			print("姓名:", name)
			print("age:", age)
			print("国籍:", country)
			print("课程:", course)
		stu("刘老根", 25, "linux")
		stu("张叫春",21,"CN","linux")
		stu("刘老根",25,"CN","linux")
	关键参数
		正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，只需指定参数名即可，但记住一个要求就是，关键参数必须放在位置参数之后。
		stu_register(age=22,name='alex',course="python",)
	非固定参数:
		定义函数时，不确定用户要传多少个参数，就可以用非固定参数
		1)*args:会把多传入的参数变成元组形式
		def test(a,*args):
			print(a,args)
		test("奶妈","快来","奶我")	==> 奶妈 ('快来', '奶我')
		2)**kargs:把多传入的参数变成一个dict形式 & 只有关键参数才能传到kargs里
		def test(a,*args,**kwargs):		
			print(a,args,kwargs)
		test("奶妈","快来","奶我","加满",奶妈="蔡文姬",我="妲己") ==> 奶妈 ('快来', '奶我', '加满') {'我': '妲己', '奶妈': '蔡文姬'}
	局部变量：
	例子：
		name = "Alex Li"
		def change_name(name):
			print("before change:",name)
			name = "金角大王,一个有Tesla的男人"
			print("after change", name)
		change_name(name)
		print("在外面看看name改了么?",name)
	输出：
		before change: Alex Li
		after change 金角大王,一个有Tesla的男人
		在外面看看name改了么? Alex Li
	全局与局部变量：
		在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
		全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
		当全局变量与局部变量同名时：在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。

返回值：
	1.想要获得函数的执行结果，就可以用return语句把函数返回
	2.函数执行过程中遇到return语句，就会停止执行并返回结果，so也可以理解为return语句代表着函数的结束
	3.如果没在函数中指定return，那么函数的返回值为None
	
递归：
	def calc(n):
		print(n)
		if int(n/2) ==0:
			return n
		return calc(int(n/2))
	calc(10)
	输出：
	10
	5
	2
	1
	递归特性：
	1.必须有一个明确的结束条件
	2.每次进入更深一层递归时，问题规模相比上次递归应有所减少
	3.递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
	每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所
	以，递归调用的次数过多，会导致栈溢出）
	递归函数实际应用案例，二分查找：
	data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
	def binary_search(dataset,find_num):
		print(dataset)
		if len(dataset) >1:
			mid = int(len(dataset)/2)
			if dataset[mid] == find_num:  #find it
				print("找到数字",dataset[mid])
			elif dataset[mid] > find_num :# 找的数在mid左面
				print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
				return binary_search(dataset[0:mid], find_num)
			else:# 找的数在mid右面
				print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
				return binary_search(dataset[mid+1:],find_num)
		else:
			if dataset[0] == find_num:  #find it
				print("找到数字啦",dataset[0])
			else:
				print("没的分了,要找的数字[%s]不在列表里" % find_num)
	binary_search(data,66)
		
匿名函数：		
	#这段代码
	def calc(n):
		return n**n
	print(calc(10))
	#换成匿名函数
	calc = lambda n:n**n
	print(calc(10))
	你也许会说，用上这个东西没感觉有毛方便呀， 。。。。呵呵，如果是这么用，确实没毛线改进，不过匿名函数主要是和其它函数搭配使用的呢，如下
	res = map(lambda x:x**2,[1,5,7,4,8])
	for i in res:
		print(i)
	顺便map用法：
	def topaz(n):
		n += 1
		return n
	h = [1,2,3]
	a = map(topaz,h)
	for i in a:
		print(i)
		
函数式编程
	1）介绍：
	函数式Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层层的函数调用，就可以把复杂的任务分解成简单的任务
	1.函数式编程中的函数这个术语不是指计算机中的函数（实际上是Subroutine），而是指数学中的函数，即自变量的映射。
	2.也就是说一个函数的值仅决定于函数参数的值，不依赖其他状态。比如sqrt(x)函数计算x的平方根，只要x不变，不论什么时候调用，调用几次，值都是不变的。
	3.函数就是面向过程的程序设计的基本单元,这种分解可以称之为面向过程的程序设计。
	4.Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。		
	2）定义
	简单说，"函数式编程"是一种"编程范式"（programming paradigm），也就是如何编写程序的方法论。
	主要思想是把运算过程尽量写成一系列嵌套的函数调用。举例来说，现在有这样一个数学表达式：
		(1 + 2) * 3 - 4
	传统的过程式编程，可能这样写：
		var a = 1 + 2;
		var b = a * 3;
		var c = b - 4;
	函数式编程要求使用函数，我们可以把运算过程定义为不同的函数，然后写成下面这样：
		var result = subtract(multiply(add(1,2), 3), 4);
	这段代码再演进以下，可以变成这样
		add(1,2).multiply(3).subtract(4)
	这基本就是自然语言的表达了。再看下面的代码，大家应该一眼就能明白它的意思吧：
		merge([1,2],[3,4]).sort().search("2")
	因此，函数式编程的代码更容易理解。要想学好函数式编程，不要玩py,玩Erlang,Haskell, 好了，我只会这么多了。。。

高阶函数：
	变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

内置函数：
	内置参数详解 https://docs.python.org/3/library/functions.html?highlight=built#ascii

练习：http://www.cnblogs.com/alex3714/articles/5740985.html
现需要对这个员工信息文件，实现增删改查操作
可进行模糊查询，语法至少支持下面3种:
	select name,age from staff_table where age > 22
	select  * from staff_table where dept = "IT"
	select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数 
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码！
