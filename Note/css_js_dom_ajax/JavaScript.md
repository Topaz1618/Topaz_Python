## 1.JavaScript 
	JavaScript 是一门编程语言,浏览器内置了JavaScript语言的解释器，可以对 JavaScript 解释并做出相应的处理
## 2.JavaScript存在形式
### 方式一
	<script type"text/javascript" src="JS文件"></script>
### 方式二
	<script type"text/javascript">
		Js代码内容
	</script>
## 3.JavaScript存放位置
#### HTML的head中
#### HTML的body代码块底部(推荐)
	由于Html代码是从上到下执行，如果Head中的js代码耗时严重，就会导致用户长时间无法看到页面，如果放置在body代码块底部，那么即使js代码耗时严重，也不会影响用户看到页面效果，只是js实现特效慢而已
### Demo
	<script src="https://www.gstatic.com/og/js/"></script>
	<script>
		alert('123');
	</script>
## 变量
### 局部变量必须以 var 开头，如果未使用var，则默认表示声明的是全局变量
### Demo
	<script type="text/javascript">
		// 全局变量	
		name = 'seven';
	
		function func(){
			// 局部变量
			var age = 18;
	
			// 全局变量
			gender = "男"
		}
	</script>
	
	PS：JavaScript中代码注释：单行 // 多行 /*  */  此注释仅在Script块中生效	
## 5.数据类型
### 原始类型
	数字
	字符串
	布尔值
### 对象类型
	数组
	字典	

	PS：数字、布尔值、null、undefined、字符串是不可变
		null是JavaScript语言的关键字，它表示一个特殊值，常用来描述“空值”
		undefined是一个特殊值，表示变量未定义
### 数字
	JavaScript所有数字均用浮点数值表示，因为不区分整数值和浮点数值
	转换：
		parseInt(..)    将某值转换成数字，不成功则NaN
		parseFloat(..)  将某值转换成浮点数，不成功则NaN
	
	特殊值：
		NaN，非数字。可使用 isNaN(num) 来判断。
		Infinity，无穷大。可使用 isFinite(num) 来判断
	数值计算:自己搜，网上一大把 http://www.cnblogs.com/wupeiqi/articles/5602773.html
### 字符串
	字符串是由字符组成的数组，但在JavaScript中字符串是不可变的，可以访问字符串任意位置的文本，不过JavaScript未提供修改已知字符串内容的方法
	常见功能：
		obj.length                           长度
		obj.trim()                           移除空白
		obj.trimLeft()
		obj.trimRight)
		obj.charAt(n)                        返回字符串中的第n个字符
		obj.concat(value, ...)               拼接
		obj.indexOf(substring,start)         子序列位置
		obj.lastIndexOf(substring,start)     子序列位置
		obj.substring(from, to)              根据索引获取子序列
		obj.slice(start, end)                切片
		obj.toLowerCase()                    大写
		obj.toUpperCase()                    小写
		obj.split(delimiter, limit)          分割
		obj.search(regexp)                   从头开始匹配，返回匹配成功的第一个位置(g无效)
		obj.match(regexp)                    全局搜索，如果正则中有g表示找到全部，否则只找到第一个。
		obj.replace(regexp, replacement)     替换，正则中有g则替换所有，否则只替换第一个匹配项，
													$数字：匹配的第n个组内容；
													$&：当前匹配的内容；
													$`：位于匹配子串左侧的文本；
													$'：位于匹配子串右侧的文本
													$$：直接量$符号
### 布尔类型
	布尔类型仅包含真假，与Python不同的是其首字母小写
		==      比较值相等
		!=       不等于
		===   比较值和类型相等
		!===  不等于
		||        或
		&&      且
### 数组
	JavaScript中的数组类似于Python中的列表
	常用功能：
		obj.length          数组的大小
		obj.push(ele)       尾部追加元素
		obj.pop()           尾部获取一个元素
		obj.unshift(ele)    头部插入元素
		obj.shift()         头部移除元素
		obj.slice( )        切片
		obj.reverse( )      反转
		obj.join(sep)       将数组元素连接起来以构建一个字符串
		obj.concat(val,..)  连接数组
		obj.sort( )         对数组元素进行排序
		obj.splice(start, deleteCount, value, ...)  插入、删除或替换数组的元素
								obj.splice(n,0,val) 指定位置插入元素
								obj.splice(n,1,val) 指定位置替换元素
								obj.splice(n,1)     指定位置删除元素							
## 6.其他
### 序列化
	JSON.stringify(obj)    序列化
	JSON.parse(str)        反序列化
		
### 转义
	decodeURI( )            URl中未转义的字符
	decodeURIComponent( )   URI组件中的未转义字符
	encodeURI( )            URI中的转义字符
	encodeURIComponent( )   转义URI组件中的字符
	escape( )               对字符串转义
	unescape( )             给转义字符串解码
	URIError                由URl的编码和解码方法抛出
### eval		
	JavaScript中的eval是Python中eval和exec的合集，既可以编译代码也可以获取返回值
	eval() 
	EvalError   执行字符串中的JavaScript代码
### 正则表达式
#### 定义正则表达式
	/.../  用于定义正则表达式
	/.../g 表示全局匹配
	/.../i 表示不区分大小写
	/.../m 表示多行匹配
	JS正则匹配时本身就是支持多行，此处多行匹配只是影响正则表达式^和$，m模式也会使用^$来匹配换行的内容
		var pattern = /^Java\w*/gm;
		var text = "JavaScript is more fun than \nJavaEE or JavaBeans!";
		result = pattern.exec(text)
	PS：定义正则表达式也可以  reg= new RegExp()	
#### 匹配
	JavaScript中支持正则表达式，其主要提供了两个功能
	test(string),检查字符串中是否和正则匹配
		n = 'uui99sdf'
		reg = /\d+/
		reg.test(n)  ---> true   #只要正则在字符串中存在就匹配，如果想要开头和结尾匹配的话，就需要在正则前后加 ^和$
	exec(string),获取正则表达式匹配的内容，如果未匹配，值为null，否则获取匹配成功的数组
		非全局模式: 获取匹配结果数组，注意：第一个元素是第一个匹配的结果，后面元素是正则子匹配（正则内容分组匹配）
			var pattern = /\bJava\w*\b/;
			var text = "JavaScript is more fun than Java or JavaBeans!";
			result = pattern.exec(text)
			var pattern = /\b(Java)\w*\b/;
			var text = "JavaScript is more fun than Java or JavaBeans!";
			result = pattern.exec(text)
		全局模式: 需要反复调用exec方法，来一个一个获取结果，直到匹配获取结果为null表示获取完毕
		    var pattern = /\bJava\w*\b/g;
			var text = "JavaScript is more fun than Java or JavaBeans!";
			result = pattern.exec(text)
			var pattern = /\b(Java)\w*\b/g;
			var text = "JavaScript is more fun than Java or JavaBeans!";
			result = pattern.exec(text)
		c.字符串中相关方法
			obj.search(regexp)                   获取索引位置，搜索整个字符串，返回匹配成功的第一个位置(g模式无效)
			obj.match(regexp)                    获取匹配内容，搜索整个字符串，获取找到第一个匹配内容，如果正则是g模式找到全部
			obj.replace(regexp, replacement)     替换匹配替换，正则中有g则替换所有，否则只替换第一个匹配项，
													$数字：匹配的第n个组内容；
													$&：当前匹配的内容；
													$`：位于匹配子串左侧的文本；
													$'：位于匹配子串右侧的文本
													$$：直接量$符号
#### 时间处理：JavaScript中提供了时间相关的操作，时间操作分为两种
	时间统一时间
	本地时间（东8区）
	更多操作参见：http://www.shouce.ren/api/javascript/main.html	
## 7.语句和异常
### 条件语句：JavaScript中支持两个中条件语句，分别是if 和 switch
#### if语句：		
	if(条件){
	
	}else if(条件){
	
	}else{
	}
#### switch语句：
	switch(name){
		case '1':
			age = 123;
			break;
		case '2':
			age = 456;
			break;
		default :
			age = 777;
	}
### 循环语句：JavaScript中支持三种循环语句
#### 方式一：
	var names = ["alex", "tony", "rain"];
	for(var i=0;i<names.length;i++){
		console.log(i);
		console.log(names[i]);
	}
#### 方式二：
	var names = ["alex", "tony", "rain"];
	for(var index in names){
		console.log(index);
		console.log(names[index]);
	}
#### 方式三：
	while(条件){
		// break;
		// continue;
	}
### 异常处理
	try {
		//这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
	}
	catch (e) {
		// 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
		//e是一个局部变量，用来指向Error对象或者其他抛出的对象
	}
	finally {
		//无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
	}
## 8.函数
### JavaScript中函数主要有三类
#### 普通函数
	function func(arg){
		return true;
	}
#### 匿名函数
	var func = function(arg){
		return "tony";
	}
#### 自执行函数
	(function(arg){
		console.log(arg);
	})('123')
			
	PS: 对于JavaScript中函数参数，实际参数的个数可能小于形式参数的个数，函数内的特殊值arguments中封装了所有实际参数
### 作用域：
	所有的作用域在创建函数且未执行时候就已经存在
	JavaScript中每个函数都有自己的作用域，当出现函数嵌套时，就出现了作用域链。当内层函数使用变量时，会根据作用域链从内到外一层层的循环，如果不存在，则异常	
#### Demo
	function f2(){
		var arg= 111;
		function f3(){
			console.log(arg);
		}
		return f3;
	}
	ret = f2();
	ret();
### 闭包
	a. 闭包是可以包含自由变量(未绑定到特定对象)的代码块
	b. 闭包是拥有多个变量和绑定了这些变量的环境表达式(通常是函数)，这些变量也是该表达式/函数的一部分
	c. 由于作用域链只能从内向外找，默认外部无法获取函数内部变量,闭包需要在外部获取函数内部的变量
#### 代码：
	function f2(){
		var arg= [11,22];
		function f3(){
			return arg;
		}
		return f3;
	}
	ret = f2();
	ret();
### 面向对象
	function Foo (name,age) {
		this.Name = name;
		this.Age = age;
		this.Func = function(arg){
			return this.Name + arg;
		}
	}
	var obj = new Foo('alex', 18);
	var ret = obj.Func("sb");
	console.log(ret);
#### 对于上述代码需要注意：
	Foo充当的构造函数
	this代指对象
	创建对象时需要使用 new
#### 上述代码中每个对象中均保存了一个相同的Func函数，从而浪费内存。使用原型和可以解决该问题
	function Foo (name,age) {
		this.Name = name;
		this.Age = age;
	}
	Foo.prototype = {
		GetInfo: function(){
			return this.Name + this.Age
		},
		Func : function(arg){
			return this.Name + arg;
		}
	}
		
