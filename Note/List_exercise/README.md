## 100个 List 操作练习： 
      这个链接里的练习很多，就是要一个个点进去，非常麻烦，写了个重用性不是很高的爬虫
      http://www.runoob.com/python/python-100-examples.html
      
## 启动
      scrapy crawl list_exercise  #启动爬虫
      Exercises.txt               #100个练习就写到这个文件里啦~ 
      
## 按照自己需求做更改
      - 每个练习写到单独的文件里（piplines.py下取消注释）
      def process_item(self, item, spider):
	   '''
	   每个练习写到单独的文件里，取消注释就OK
	   file_name = '%s.txt' %item['name']
	   with open(os.path.join('Exercises', file_name), mode='ab') as f:
	   	title = bytes('题目:%s\n'%item['title'] ,encoding='utf-8')
	   	content = bytes('Demo:\n%s\n输出:\n%s\n'%(item['demo'],item['output']),encoding='utf-8')
	   	f.write(title)
	   	f.write(content)
	   	f.flush()
	   '''
      - 只爬题目不爬答案，体验小学生做练习题的感觉（注释下面这行）~~ 
      content = bytes('Demo:\n%s\n输出:\n%s\n'%(item['demo'],item['output']),encoding='utf-8')




