1.编程语言的分类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**1.1编译型和解释型**:  
  * **编译器：把源程序的语句都编译成机器语言，保存成二进制文件，运行时直接运行机器语言，速度很快**
  * **解释器：执行程序时，才一条条解释成机器语言给计算机执行，运行速度不如编译后的程序快**  
  编译型语言（c，c++，go，swift）：
    优点：运行时不需要编译，执行效率高，可以脱离语言环境独立运行
    缺点：平台兼容性差，需要根据运行的操作系统环境编译成不同的可执行文件
  解释型语言（python，ruby，php，perl）：
    优点：平台兼容性好，代码可以直接修改，不用停机维护
    缺点：每次运行都要解释，性能不如编译型语言
	
**1.2静态语言和动态语言**
  * **动态类型语言：运行期间才做数据类型检查的语言，第一次赋值给变量时，在内部将数据类型记录下来，python和ruby就是动态类型语言**		
  * **静态类型语言：在编译期间检查数据类型的语言，写程序时要声明所有变量的数据类型，c/c++就静态类型语言代表**

**1.3强类型定义语言和弱类型定义语言**
  * **强类型定义语言：一个变量被指定了某个数据类型，需要强制转换才能更改类型，速度不如弱类型语言，但是严谨性能避免许多错误**
  * **弱类型定义语言：数据类型可以被忽略的语言，与强类型语言相反，一个变量可以赋不同数据类型的值**

小结： python是一门解释型动态强类型语言

2.python优缺点
~~~~~~~~~~~~~~~
**优点**
	* **开发效率高**
	* **高级语言（不需要考虑底层细节）**
	* **可移植性（基本不需要修改就能运行在所有系统平台上）**
	* **可扩展性（python里面加入c，c++）**
	* **可嵌入性（可以把python嵌入到c，c++）**
**缺点**
	* **速度慢**
	* **代码不能加密（因为是解释型语言，源码都是明文形式的）**
	* **线程不能利用多CPU问题**
	
3.python的解释器
~~~~~~~~~~~~~~~
	Python的解释器很多，但使用最广泛的还是CPython。如果要和Java或.Net平台交互，最好的办法不是用Jython或IronPython，而是通过网络调用来交互，确保各程序之间的独立性
	
4.变量定义的规则
~~~~~~~~~~~~~~~
* **变量名只能是 字母、数字或下划线的任意组合**
* **变量名的第一个字符不能是数字**
* **以下关键字不能声明为变量**
  
  ..  code:: bash
  
	['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

5.简述python运行过程
~~~~~~~~~~~~~~~
* **python程序首次运行时，编译结果保存在位于内存的pycodeobject中，当python程序运行结束时，python解释器则将pycodeobject写会pyc文件中**
* **python程序第二次运行时，首先程序会在硬盘中找pyc文件，找到就直接载入否则重复上面过程**
* **pyc是pycodeobject的持久化保存方式**

6.用户输入
~~~~~~~~~~~~~~~

..  code:: python
	
	import getpass
	name = input("输入名字>>>")
	print(name)
	pwd = getpass.getpass()
	print(pwd)

.. code:: bash

  >>> python tests.py
    输入名字>>>topaz
	  topaz
    Password:
    aa

7.模块
~~~~~~~~~~~~~~~

【sys】

..  code:: python

		import sys
		print(sys.argv)	#获取传入参数
	
..  code:: bash
  
  >>> python tests.py hello tutu biubiu	
    ['tests.py', 'hello', 'tutu', 'biubiu']
		
【os】

..  code:: python
		
		import os
		os.system("dir") #调用系统命令
 
..  code:: bash
  
  >>> python tests.py
		 2017/08/01  00:55               221 api_urls.py
		 2017/08/01  03:17               348 api_views.py

结合一下两个模块

..  code:: python
			
	import os,sys
	a = sys.argv
	print(a)
	os.system(a[1])
 
..  code:: bash

  >>> python tests.py dir
	  ['tests.py', 'dir']
	  2017/07/31  07:14             2,167 admin.py
	  2017/08/01  00:55               221 api_urls.py



8.数据类型
~~~~~~~~~~~~~~~

* **数字**

::

  int（整型）	在32位机器上，整数的位数为32位，64位机器上，整数的位数为64位
	long（长整型）
	float（浮点型）
	complex（复数）
* **布尔值**
	
::
  
  真或假/1或0
* **字符串：移除空白，分割，长度，索引，切片**
	
::

  格式化输出字符串是%s，整数%d，浮点数%f
* **列表：索引，切片，追加，删除，长度，切片，循环，包含
    
..  code:: python
  
	name_list = ['alex', 'seven', 'eric'] 或 name_list ＝ list(['alex', 'seven', 'eric'])
* **元组**
  
..  code:: python
  
	ages = (11, 22, 33, 44, 55) 或 ages = tuple((11, 22, 33, 44, 55))
* **字典：索引，新增，删除，键、值、键值对，循环，长度**
  
..  code:: python
  
  person = {"name": "mr.wu", 'age': 18} 或 person = dict({"name": "mr.wu", 'age': 18})
  
* **运算**
 
 ::

	算数运算：+ - * / % ** //
	比较运算： == != <> > < <= >=
	赋值运算：= += -= *= /= %= 
	逻辑运算：and or not
	成员运算：in,not in
	身份运算：is,is not
	位运算：& | ^ 
	运算符优先级：（自己查吧）
	
