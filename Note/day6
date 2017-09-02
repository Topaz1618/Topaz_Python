面向对象的特性：
	封装：其实就是使用构造方法将内容封装到某个具体对象中，然后通过对象直接或者self间接获取被封装的内容
	继承：
		面向对象编程 (OOP) 语言的一个主要功能就是“继承”。继承是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。
		通过继承创建的新类称为“子类”或“派生类”。
		被继承的类称为“基类”、“父类”或“超类”。
		继承的过程，就是从一般到特殊的过程。
		要实现继承，可以通过“继承”（Inheritance）和“组合”（Composition）来实现。
		在某些 OOP 语言中，一个子类可以继承多个基类。但是一般情况下，一个子类只能有一个基类，要实现多重继承，可以通过多级继承来实现。
		继承概念的实现方式主要有2类：实现继承、接口继承。
			实现继承是指使用基类的属性和方法而无需额外编码的能力；
			接口继承是指仅使用属性和方法的名称、但是子类必须提供实现的能力(子类重构爹类方法)；
		在考虑使用继承时，有一点需要注意，那就是两个类之间的关系应该是“属于”关系。例如，Employee 是一个人，Manager 也是一个人，因此这两个类都可以继承 Person 类。但是 Leg 类却不能继承 Person 类，因为腿并不是一个人。
		抽象类仅定义将由子类创建的一般属性和方法。
		OO开发范式大致为：划分对象→抽象类→将类组织成为层次化结构(继承和合成) →用类与实例进行设计和实现几个阶段。
	例1：
		class SchoolMember(object):
		members = 0  # 初始学校人数为0
		def __init__(self, name, age):
			self.name = name
			self.age = age
		def enroll(self):
			'''注册'''
			SchoolMember.members += 1
			print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
			self.name, SchoolMember.members))
		def __del__(self):		#函数都结束了会执行这个
			'''析构方法'''
			print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)

		class Teacher(SchoolMember):        #t1 = Teacher("Alex", 22, 'Python', 20000
			def __init__(self, name, age, course, salary):
				super(Teacher, self).__init__(name, age)
				self.course = course
				self.salary = salary
				self.enroll()		
			def teaching(self):
				'''讲课方法'''
				print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))
			def tell(self):
				'''自我介绍方法'''
				msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
				print(msg)
				
		class Student(SchoolMember):
			def __init__(self, name, age, grade, sid):
				super(Student, self).__init__(name, age)    #super(子类名称，self).__init__(继承父类的属性1，属性2)：初始化父类，继承Person父类的name和gender属性
				self.grade = grade
				self.sid = sid
				self.enroll()
			def tell(self):
				'''自我介绍方法'''
				msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
				print(msg)

		if __name__ == '__main__':
			t1 = Teacher("Alex", 22, 'Python', 20000)
			t2 = Teacher("TengLan", 29, 'Linux', 3000)		
			s1 = Student("Qinghua", 24, "Python S12", 1483)
			s2 = Student("SanJiang", 26, "Python S12", 1484)
			t1.teaching()
			t2.teaching()
			t1.tell()
	例2：（照葫芦画个瓢）
		class daddy(object):
		'''先来个父类'''
		def __init__(self,name,job):
			self.name = name
			self.job = job
		def why(self):
			print("关于 %s %s 的故事有很多,不知道你想听哪一个" %(self.name,self.job))
		def __del__(self):
			print("now who you daddy right %s" %self.name)

		class master(daddy):
			def __init__(self,name,job):
				super(master,self).__init__(name,job)
				self.why()
			def person(self):
				print("【%s】 意识nb 草丛queen 国服第一%s"%(self.name,self.job))

		class adc(daddy):
			def __init__(self,name,job,hurt):
				super(adc,self).__init__(name,job)
				self.hurt = hurt
			def person(self):
				print("【%s】 %s走位风骚，伤害高"%(self.name,self.job))
		
		a = adc('Topaz','后羿','10000+')
		a1 = adc('阿猫','孙尚香','20000+')
		b = master('Topaz喵','妲己')
		b1 = master('Topaz喵','貂蝉')
		a.person()
		a1.person()
		b.person()
		b1.person()
		
	多态：
		多态性（polymorphisn）是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，父对象就可以根据当前赋值给它的子对象的特性以不同的方式运作。简单的说，就是一句话：允许将子类类型的指针赋值给父类类型的指针。
		那么，多态的作用是什么呢？我们知道，封装可以隐藏实现细节，使得代码模块化；继承可以扩展已存在的代码模块（类）；它们的目的都是为了——代码重用。而多态则是为了实现另一个目的——接口重用！多态的作用，就是为了类在继承和派生的时候，保证使用“家谱”中任一类的实例的某一属性时的正确调用。
		Pyhon 很多语法都是支持多态的，比如 len(),sorted(), 你给len传字符串就返回字符串的长度，传列表就返回列表长度。
	例1：
		class Animal(object):
			def __init__(self, name):  # Constructor of the class
				self.name = name
			def talk(self):  # Abstract method, defined by convention only
				raise NotImplementedError("Subclass must implement abstract method")

		class Cat(Animal):
			def talk(self):
				print('%s: 喵喵喵!' % self.name)
		
		class Dog(Animal):
			def talk(self):
				print('%s: 汪！汪！汪！' % self.name)
		
		def func(obj):  # 一个接口，多种形态
			obj.talk()

		c1 = Cat('Topaz')
		d1 = Dog('李二蛋')
		func(c1)
		func(d1)
	例2：（又照葫芦画个瓢）
		class daddy(object):
			def __init__(self,name):
		self.name = name
		class adc(daddy):
			def judge(self):
				print("%s 第一个红能不能给刺客" %self.name)
		class master(daddy):
			def judge(self):
				print("%s 球球你别和露娜抢蓝"%self.name)
		def func(o):
			o.judge()
		a = adc("鲁班")
		b = master("妲己")
		func(a)
		func(b)

领域模型：
	参考：http://www.cnblogs.com/alex3714/articles/5188179.html

练习: 选课系统
	角色:学校、学员、课程、讲师
	要求:
	1. 创建北京、上海 2 所学校
	2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
	3. 课程包含，周期，价格，通过学校创建课程 
	4. 通过学校创建班级， 班级关联课程、讲师
	5. 创建学员时，选择学校，关联班级
	5. 创建讲师角色时要关联学校， 
	6. 提供两个角色接口
	6.1 学员视图， 可以注册， 交学费， 选择班级，
	6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
	6.3 管理视图，创建讲师， 创建班级，创建课程
	7. 上面的操作产生的数据都通过pickle序列化保存到文件里
示例：https://github.com/triaquae/py_training/tree/master/sample_code/day5-atm
