协程：
	协程是一种轻量级的线程，协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈
	因此协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态，换种说法：进入上一次离开时所处逻辑流的位置

必须符合以下4点定义的才能叫协程：
	1)必须在只有一个单线程里实现并发
	2)修改共享数据不需加锁
	3)用户程序里自己保存多个控制流的上下文栈
	4)一个协程遇到IO操作自动切换到其它协程
	PS：yield就不符合了
协程优点：
	1)无需线程上下文切换的开销
	2)无需原子操作锁定及同步的开销
	　　"原子操作(atomic operation)是不需要synchronized"，所谓原子操作是指不会被线程调度机制打断的操作；这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch （切换到另一个线程）。
		原子操作可以是一个步骤，也可以是多个操作步骤，但是其顺序是不可以被打乱，或者切割掉只执行部分。视作整体是原子性的核心。
	3)方便切换控制流，简化编程模型
	4)高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理。
协程缺点：
	1)无法利用多核资源：协程的本质是个单线程,它不能同时将 单个CPU 的多个核用上,协程需要和进程配合才能运行在多CPU上.当然我们日常所编写的绝大部分应用都没有这个必要，除非是cpu密集型应用。
	2)进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序

Greenlet
	greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
	实例：
		from greenlet import greenlet
		def test1():
			print(1)
			gr2.switch()    #切到协程gr2
			print(3)
			gr2.switch()    #切gr2
		def test2():
			print(2)
			gr1.switch()    #切回协程gr1
			print(4)
		gr1 = greenlet(test1)       #实例化一个协程
		gr2 = greenlet(test2)       #实例化另一个协程
		gr1.switch()                #骚操作开始啦~ 切到协程gr1
	PS:还没有解决一个问题，就是遇到IO操作，自动切换	
 
Gevent
	Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度
	import gevent
	def dog():
	print("狗粮")
	gevent.sleep(1) 
	print("狗咬胶")
	def cat():
		print("猫粮")
		gevent.sleep(1)
		print("猫罐头")
	gevent.joinall([         #joinall把,看源代码是在里面hasattr了一下函数
		gevent.spawn(dog),  # Greenlet模式，看下面源代码，实例化dongbei,然后起了个协程
		gevent.spawn(cat),
	])	
	'''
		def spawn(cls, *args, **kwargs):
			g = cls(*args, **kwargs)
			g.start()
			return g
	'''

同步异步性能区别：
	import gevent
	def task(pid):
		gevent.sleep(0.5)
		print('Task %s done' % pid)
	def synchronous():  #同步，一个个打印
		for i in range( 10):
			task(i)
	def asynchronous(): #异步
		threads = [gevent.spawn(task, i) for i in range(10)]    #实例化一个协程
		gevent.joinall(threads)     #获取这个协会的函数
	# print('Synchronous（同步）:')   #同步
	# synchronous()
	print('Asynchronous（异步）:')  #异步
	asynchronous()
	上面程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。 初始化的greenlet列表存放在数组threads中，此数组被传给gevent.joinall 函数，后者阻塞当前流程，并执行所有给定的greenlet。执行流程只会在 所有greenlet执行完后才会继续向下走。　　	
	
遇到IO阻塞时会自动切换任务：
	from gevent import monkey;
	monkey.patch_all()
	import gevent
	from  urllib.request import urlopen
	def f(url):
		print('GET: %s' % url)
		res = urlopen(url)
		data = res.read()
		print('%d bytes from %s.' % (len(data), url))
	gevent.joinall([
		gevent.spawn(f, 'https://www.python.org/'),
		gevent.spawn(f, 'https://www.yahoo.com/'),
		gevent.spawn(f, 'https://github.com/'),
	])
	
	'''
		是不是都忘了阻塞是啥了，来，复习一下~
		参考1：
		“阻塞”与"非阻塞"与"同步"与“异步"不能简单的从字面理解，提供一个从分布式系统角度的回答。
			1.同步与异步同步和异步关注的是消息通信机制 (synchronous communication/ asynchronous communication)所谓同步，就是在发出一个*调用*时，在没有得到结果之前，该*调用*就不返回。但是一旦调用返回，就得到返回值了。换句话说，就是由*调用者*主动等待这个*调用*的结果。而异步则是相反，*调用*在发出之后，这个调用就直接返回了，所以没有返回结果。换句话说，当一个异步过程调用发出后，调用者不会立刻得到结果。而是在*调用*发出后，*被调用者*通过状态、通知来通知调用者，或通过回调函数处理这个调用。典型的异步编程模型比如Node.js
			举个通俗的例子：你打电话问书店老板有没有《分布式系统》这本书，如果是同步通信机制，书店老板会说，你稍等，”我查一下"，然后开始查啊查，等查好了（可能是5秒，也可能是一天）告诉你结果（返回结果）。而异步通信机制，书店老板直接告诉你我查一下啊，查好了打电话给你，然后直接挂电话了（不返回结果）。然后查好了，他会主动打电话给你。在这里老板通过“回电”这种方式来回调
			2. 阻塞与非阻塞阻塞和非阻塞关注的是程序在等待调用结果（消息，返回值）时的状态.阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才会返回。非阻塞调用指在不能立刻得到结果之前，该调用不会阻塞当前线程
			还是上面的例子，你打电话问书店老板有没有《分布式系统》这本书，你如果是阻塞式调用，你会一直把自己“挂起”，直到得到这本书有没有的结果，如果是非阻塞式调用，你不管老板有没有告诉你，你自己先一边去玩了， 当然你也要偶尔过几分钟check一下老板有没有返回结果
		在这里阻塞与非阻塞与是否同步异步无关。跟老板通过什么方式回答你结果无关。如果是关心blocking IO/ asynchronous IO, 参考  Unix Network Programming View Book
		
		参考2：http://blog.csdn.net/historyasamirror/article/details/5778378
	'''

通过gevent实现单线程下的多socket并发
	server端：
		#_*_coding:utf-8_*_
		# Author:Topaz
		import sys
		import socket
		import time
		import gevent
		from gevent import socket, monkey
		monkey.patch_all()
		def server(port):
			s = socket.socket()
			s.bind(('0.0.0.0', port))
			s.listen(500)
			while True:
				cli, addr = s.accept()
				gevent.spawn(handle_request, cli)		#实现多并发的精华就是这句了
		def handle_request(conn):
			try:
				while True:
					data = conn.recv(1024)
					print("recv:", data)
					conn.send(data)
					if not data:
						conn.shutdown(socket.SHUT_WR)
			except Exception as  ex:
				print(ex)
			finally:
				conn.close()
		if __name__ == '__main__':
			server(8001)
	client:
		import socket
		HOST = 'localhost'  # The remote host
		PORT = 8001  # The same port as used by the server
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
		while True:
			msg = bytes(input(">>:"), encoding="utf8")
			s.sendall(msg)
			data = s.recv(1024)
			# print(data)
			print('Received', repr(data))
		s.close()
	并发100个socket连接
		import socket
		import threading
		def sock_conn():
			client = socket.socket()
			client.connect(("localhost",8001))
			count = 0
			while True:
				#msg = input(">>:").strip()
				#if len(msg) == 0:continue
				client.send( ("hello %s" %count).encode("utf-8"))
				data = client.recv(1024)
				print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
				count +=1
			client.close()
		for i in range(100):
			t = threading.Thread(target=sock_conn)	
			t.start()

事件驱动与异步IO	
	通常，我们写服务器处理模型的程序时，有以下几种模型：
		1）每收到一个请求，创建一个新的进程，来处理该请求；
		2）每收到一个请求，创建一个新的线程，来处理该请求；
		3）每收到一个请求，放入一个事件列表，让主进程通过非阻塞I/O方式来处理请求
	上面的几种方式，各有千秋，
		第（1）中方法，由于创建新的进程的开销比较大，所以，会导致服务器性能比较差,但实现比较简单。
		第（2）种方式，由于要涉及到线程的同步，有可能会面临死锁等问题。
		第（3）种方式，在写应用程序代码时，逻辑比前面两种都复杂。
		综合考虑各方面因素，一般普遍认为第（3）种方式是大多数网络服务器采用的方式
		
方式二：就是事件驱动模型
	1.目前大部分的UI编程都是事件驱动模型，如很多UI平台都会提供onClick()事件，这个事件就代表鼠标按下事件。事件驱动模型大体思路如下：
		1）有一个事件（消息）队列
		2）鼠标按下时，往这个队列中增加一个点击事件（消息）；
		3）有个循环，不断从队列取出事件，根据不同的事件，调用不同的函数，如onClick()、onKeyDown()等；
		4）事件（消息）一般都各自保存各自的处理函数指针，这样，每个消息都有独立的处理函数；
	2.事件驱动编程是一种编程范式，这里程序的执行流由外部事件来决定。它的特点是包含一个事件循环，当外部事件发生时使用回调机制来触发相应的处理	
	3.在单线程同步模型中，任务按照顺序执行。如果某个任务因为I/O而阻塞，其他所有的任务都必须等待，直到它完成之后它们才能依次执行。这种明确的
	执行顺序和串行化处理的行为是很容易推断得出的。如果任务之间并没有互相依赖的关系，但仍然需要互相等待的话这就使得程序不必要的降低了运行速度
	4.在多线程版本中，这3个任务分别在独立的线程中执行。这些线程由操作系统来管理，在多处理器系统上可以并行处理，或者在单处理器系统上交错执行,
	这使得当某个线程阻塞在某个资源的同时其他线程得以继续执行。与完成类似功能的同步程序相比，这种方式更有效率，但程序员必须写代码来保护共享资
	源，防止其被多个线程同时访问。多线程程序更加难以推断，因为这类程序不得不通过线程同步机制如锁、可重入函数、线程局部存储或者其他机制来处理
	线程安全问题，如果实现不当就会导致出现微妙且令人痛不欲生的bug
	5.在事件驱动版本的程序中，3个任务交错执行，但仍然在一个单独的线程控制中。当处理I/O或者其他昂贵的操作时，注册一个回调到事件循环中，然后当
	I/O操作完成时继续执行。回调描述了该如何处理某个事件。事件循环轮询所有的事件，当事件到来时将它们分配给等待处理事件的回调函数。这种方式让程
	序尽可能的得以执行而不需要用到额外的线程。事件驱动型程序比多线程程序更容易推断出行为，因为程序员不需要关心线程安全问题。
	当我们面对如下的环境时，事件驱动模型通常是一个好的选择：
		1）程序中有许多任务，而且…
		2）任务之间高度独立（因此它们不需要互相通信，或者等待彼此）而且…
		3）在等待事件到来时，某些任务会阻塞。
	当应用程序需要在任务间共享可变的数据时，这也是一个不错的选择，因为这里不需要采用同步处理
	网络应用程序通常都有上述这些特点，这使得它们能够很好的契合事件驱动编程模型
	此处要提出一个问题，就是，上面的事件驱动模型中，只要一遇到IO就注册一个事件，然后主程序就可以继续干其它的事情了，只到io处理完毕后，继续恢复之前中断的任务，这本质上是怎么实现的呢？哈哈，下面我们就来一起揭开这神秘的面纱	

Select\Poll\Epoll异步IO	
	Python Select解析: http://www.cnblogs.com/alex3714/p/4372426.html			#还有隐藏任务呢，开不开心
	IO多路复用之select总结: http://www.cnblogs.com/Anker/p/3258674.html			#来看看这个
	IO多路复用(番外篇): http://www.cnblogs.com/alex3714/articles/5876749.html	#隐藏任务[2],超惊喜的是不是
	sever端：
		import select
		import socket
		import sys
		import queue
		server = socket.socket()
		server.setblocking(0)   #设置为非阻塞
		server.bind(('localhost',1222))
		server.listen(5)        #同时监听5个线程
		inputs = [server, ]
		outputs = []
		message_queues = {}
		while True:
			print("等...")
			readable, writeable, exeptional = select.select(inputs,outputs,inputs) #如果没有任何fd就绪,那程序就会一直阻塞在这里
			for s in readable: #每个s就是一个socket
				if s is server:     #server在有新连接进来的时候活动，也就是说有新连接进来条件成立
					conn, client_addr = s.accept()
					print("new connection from",client_addr)
					conn.setblocking(0)     #把链接设置成非阻塞
					inputs.append(conn)     #加到inputs列表里，等循环
					message_queues[conn] = queue.Queue() #接收到客户端的数据后,不立刻返回 ,暂存在队列里,以后发送
				else:                       #s不是server的话,那就只能是一个 与客户端建立的连接的fd（文件句柄）了
					data = s.recv(1024)      #客户端的数据过来了,在这接收
					if data:
						print("收到来自[%s]的数据:" % s.getpeername()[0], data)    #getpeername 是 socket方法
						message_queues[s].put(data) #收到的数据放到queue里,一会返回给客户端
						if s not  in outputs:
							outputs.append(s)    #为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端
					else:                       #如果收不到data代表什么呢? 代表客户端断开了呀
						print("客户端断开了",s)
						if s in outputs:
							outputs.remove(s)   #清理已断开的连接
						inputs.remove(s)        #清理已断开的连接
						del message_queues[s]   #清理已断开的连接
			for s in writeable:
				try :
					msg = message_queues[s].get_nowait()    #拿到客户端msg
				except queue.Empty:
					print("client [%s]" %s.getpeername()[0], "queue is empty..")
					outputs.remove(s)
				else:
					print("sending msg to [%s]"%s.getpeername()[0], msg)
					s.send(msg.upper())
			for s in exeptional:
				print("handling exception for ",s.getpeername())
				inputs.remove(s)
				if s in outputs:
					outputs.remove(s)
				s.close()
				del message_queues[s]
	client：
		import socket
		import sys
		messages = [ b'This is the message. ',
					b'It will be sent ',
					b'in parts.',
					]
		# Create a TCP/IP socket、
		# client = socket.socket()
		clients = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
				socket.socket(socket.AF_INET, socket.SOCK_STREAM),
				]
		# Connect the socket to the port where the server is listening
		for client in clients:             #建俩链接，为了不并发这样？？
			client.connect(('localhost', 1222))
		for message in messages:
			'''这段儿就是每个消息都用两个连接分别发一遍'''
			n = 0
			for client in clients:
				n+=1
				print('%s发送数据啦 : sending "%s %s"' % (client.getsockname(), message,n) )
				client.send(message)
			# Read responses on both sockets
			for client in clients:
				data = client.recv(1024)    #每个连接再获取下返回数据
				print( '%s接收数据啦: received "%s"' % (client.getsockname(), data) )
				if not data:
					print(sys.stderr, 'closing socket', client.getsockname() )

selectors模块
	selectors模块可以实现IO多路复用机制,它具有根据平台选出最佳的IO多路机制，比如在win的系统上他默认的是select模式而在linux上它默认的epoll。
	参考：http://www.cnblogs.com/guobaoyuan/p/6841904.html 		
