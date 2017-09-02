进程:
	把程序加载到内存，系统为程序分配资源才能运行，运行中的程序叫做进程
	缺点：进程只能在一个时间干一件事情，会阻塞
线程：
	线程是操作系统能够运算调度的最小单位，被包含在进程中，一个进程多个线程，每个线程可以并行执行不同任务，是进程中的实际运作单位
这篇文章透彻的剖析了GIL对python多线程的影响，强烈推荐看一下：http://www.dabeaz.com/python/UnderstandingGIL.pdf

python threadding模块：
	第一种调用方式：直接调用
		import threading
		import time
		def nihao(n):
			print(n)
			time.sleep(2)
		if __name__ == "__main__":
			t1 = threading.Thread(target=nihao,args=(1,))
			t2 = threading.Thread(target=nihao,args=(2,))
			t1.start()
			t2.start()
			print(t1.getName())
			print(t2.getName())	
	第二种调用方式：继承式调用
		import threading
		import time
		class MyT(threading.Thread):
			def __init__(self,num):
				threading.Thread.__init__(self)
				self.num = num
			def run(self):
				print(self.num)
				time.sleep(2)
		if __name__ == '__main__':
			t1 = MyT(1)
			t2 = MyT(2)
			t1.start()
			t2.start()	

Join&Daemon			
	import time
	import threading
	def run(n):
		print('running:',n)
		time.sleep(2)
	def main():
		for i in range(5):
			t = threading.Thread(target=run, args=[i, ])
			t.start()
			t.join(timeout=1)
			print('starting thread', t.getName())
	m = threading.Thread(target=main, args=[])
	m.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
	m.start()
	m.join(timeout=2)
	print("---main thread done----")
	#join参考：http://blog.csdn.net/zhangzheng0413/article/details/41728869
	
线程锁：3.0上完全看不出效果
	import time
	import threading
	def addNum():
		global num  # 在每个线程中都获取这个全局变量
		print('--get num:', num)
		time.sleep(1)
		lock.acquire()  # 修改数据前加锁
		num -= 1  # 对此公共变量进行-1操作
		lock.release()  # 修改后释放
	num = 100  # 设定一个共享变量
	thread_list = []
	lock = threading.Lock()  # 生成全局锁
	for i in range(100):
		t = threading.Thread(target=addNum)
		t.start()
		thread_list.append(t)
	for t in thread_list:  # 等待所有线程执行完毕
		t.join()
	print('final num:', num)

RLock（递归锁）
	import threading, time
	def run1():
		print("grab the first part data")
		lock.acquire()
		global num
		num += 1
		lock.release()
		return num
	def run3():
		lock.acquire()
		res = run1()
		lock.release()
		print(res)
	if __name__ == '__main__':
		num = 0
		lock = threading.RLock()
		for i in range(5):
			t = threading.Thread(target=run3)
			t.start()
	while threading.active_count() != 1:
		print('test',threading.active_count())
	else:
		print('----all threads done---')
		print(num)
		
Semaphore(信号量)
	互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据
	import threading, time
	def run(n):
		pp.acquire()
		n+=1
		print("正在运行",n)
		time.sleep(1)
		pp.release()
	if __name__ == "__main__":
		num = 0
		pp = threading.BoundedSemaphore(3)
		for  i in range(6):
			t = threading.Thread(target=run,args=(i,))
			t.start()
	while threading.active_count() != 1:
		pass
	else:
		print('都停了',num)	
		
Timer
	def hello():
		print("hello, world")
	t = Timer(30.0, hello)
	t.start()  # after 30 seconds, "hello, world" will be printed
	
Events
	起到flag的作用，event.isSet()实际上就是拿到True和False
	实例1：
		import threading,time
		import random
		def light():
		'''这段代码自转，活在自己的世界里，9次以内是绿灯，10-12是黄灯，13-19是红灯，不停打印自己现在是什么灯'''
			if not event.isSet():
				event.set() #wait就不阻塞 #绿灯状态
			count = 0
			while True:
				if count < 10:
					print('\033[42;1m--green light on---\033[0m')
				elif count <13:
					print('\033[43;1m--yellow light on---\033[0m')
				elif count <20:
					if event.isSet():
						event.clear()
					print('\033[41;1m--red light on---\033[0m')
				else:
					count = 0
					event.set() #打开绿灯
				time.sleep(1)
				count +=1
		def car(n):
		'''一共三个线程，都无限循环这段代码，休眠后检查light线程啥情况，根据情况打印语句'''
			while True:
				time.sleep(random.randrange(10))	#在10里面选个随机数
				if  event.isSet(): #绿灯
					print("car [%s] is running.." % n)
				else:
					print("car [%s] is waiting for the red light.." %n)
		if __name__ == '__main__':
			event = threading.Event()
			Light = threading.Thread(target=light)
			Light.start()
			for i in range(3):	#调用三次car
				t = threading.Thread(target=car,args=(i,))	#起三个car线程
				t.start()
	实例2：
		import threading, time
		import random
		def door():
			door_open_time_counter = 0
			while True:
				if door_swiping_event.is_set():     #True
					print("\033[32;1mdoor opening....\033[0m")
					door_open_time_counter +=1
				else:
					print("\033[31;1mdoor closed...., swipe to open.\033[0m")
					door_open_time_counter = 0 #清空计时器
					door_swiping_event.wait()
				if door_open_time_counter > 3:#门开了已经3次了,再来用
					door_swiping_event.clear()  #==> door_swiping_event.is_set() = False
				time.sleep(0.5)
		def staff(n):
			print("staff [%s] is comming..." % n )
			while True:
				if door_swiping_event.is_set(): #True
					print("\033[34;1mdoor is opened, passing.....\033[0m")
					break
				else:
					print("staff [%s]  刷卡开门....." % n)
					door_swiping_event.set()
				time.sleep(0.5)
		door_swiping_event  = threading.Event() #设置事件
		door_thread = threading.Thread(target=door)
		door_thread.start()
		for i in range(3):
			p = threading.Thread(target=staff,args=(i,))
			time.sleep(random.randrange(3))
			p.start()
			
queue队列：			
	class queue.Queue(maxsize=0) #先入先出
	class queue.LifoQueue(maxsize=0) #last in fisrt out 
	class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列		
		Queue.qsize()
		Queue.empty() #return True if empty  
		Queue.full() # return True if full 
		Queue.put(item, block=True, timeout=None)
		Queue.put_nowait(item)
		Queue.get(block=True, timeout=None)
		Queue.get_nowait()
		Queue.task_done()
		Queue.join() block直到queue被消费完毕		
			
生产消费者模型：
	在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度
	为什么要使用生产者和消费者模式：
		在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式
	什么是生产者消费者模式
		生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力
	代码：
		import threading
		import queue
		def Poll():
			for i in range(5):
				q.put(i)
			print("骨头都放到缓存里了，等狗来")
			q.join()
			print("没了，明天再来哈")
		def Dog(n):
			while q.qsize() > 0:
				print('%s 拿走 骨头'%n,q.get())
				q.task_done()
		q = queue.Queue()
		poll = threading.Thread(target=Poll)
		poll.start()
		dog = Dog('金毛')

多进程：
	from multiprocessing import Process
	import os
	def info():
		print('module name:', __name__)
		print('parent process:', os.getppid())
		print('process id:', os.getpid())
	def f(name):
		info()
		print('hello', name)
	if __name__ == '__main__':
		p = Process(target=f, args=('bob',))
		p.start()
		p.join()        #注释下join试试，print顺序变了
		print('b')
					
进程间通讯			
	不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法		
	Queues
		from multiprocessing import Process, Queue
		def f(q):
			q.put([42, None, 'hello'])
		if __name__ == '__main__':
			q = Queue()
			p = Process(target=f, args=(q,))
			p.start()
			print(q.get())  # prints "[42, None, 'hello']"
	Pipes(根据上面的意会)
		from multiprocessing import Process, Pipe
		def f(conn):
			conn.send([42, None, 'hello'])
			conn.close()
		if __name__ == '__main__':
			parent_conn, child_conn = Pipe()
			p = Process(target=f, args=(child_conn,))
			p.start()
			print(parent_conn.recv())  # prints "[42, None, 'hello']"
			p.join()
	Managers
		from multiprocessing import Process, Manager
		def f(d, l):
			d[1] = '1'  #key数字，v字符串
			d['2'] = 2  #key字符串,v数字
			d[0.25] = None
			l.append(1)
			# print(l)
		if __name__ == '__main__':
			with Manager() as manager:
				d = manager.dict()  #打开一个字典
				l = manager.list(range(5))  #创建一个字典
				p_list = []
				for i in range(3):
					p = Process(target=f, args=(d, l))  #打开3个进程
					p.start()
					p.join()    #加了join就能拿到想要的数据了
					# print(l)  #没join，这样拿到的l没有f处理过的痕迹。。
					# print(p)    #<Process(Process-2, started)>
				'''这里不造为啥要加到列表里，再取出来，效果都一样，'''
					# p_list.append(p)  #[<Process(Process-2, stopped)>, <Process(Process-3, stopped)>, <Process(Process-4, stopped)>]
				# for res in p_list:
				#     print(p_list)
				#     res.join()
				print(d)
				print(l)

进程同步
	from multiprocessing import Process, Lock
	def f(lock, num):
		lock.acquire()  #用传进来的lock加个锁，眼熟不？？线程那块儿你们曾有一面之缘
		try:
			print('hello world', num)   #到此一游
		finally:
			lock.release()  #解锁
	if __name__ == '__main__':
		lock = Lock()       #实例化lock方法
		for num in range(3):    #起三个进程
			Process(target=f, args=(lock, num)).start() #都小学六年级了你写字儿还一笔一划吗??		

进程池
	进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止
	import time
	def Dog(i):
		print("wang")
		time.sleep(1)
		return i + 1
	def Bar(arg):
		print('Bar:', arg)
	if __name__ == "__main__":
		pool = Pool(5)
		for i in range(3):
			pool.apply_async(Dog, (i,),callback=Bar)    #非阻塞，去掉callback看区别
			# pool.apply(Dog,(i,))           #阻塞
		print('end')
		pool.close()
		pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
	
	#进程池更多： http://www.cnblogs.com/kaituorensheng/p/4465768.html
			
