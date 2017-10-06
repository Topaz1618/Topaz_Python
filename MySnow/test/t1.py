#_*_coding:utf-8_*_
# Author:Topaz
class HttpResponse(object):
    def __init__(self,message):
        self.message = message
        print('message类型',type(self.message))
    def response(self):
        return bytes(self.message,encoding="utf-8")

class HttpNotFound(HttpResponse):
    def __init__(self,message):
        super(HttpNotFound,self).__init__(message)
a = HttpNotFound('404')
print(a.response())

class daddy(object):
    '''先来个父类'''
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def why(self):
        print("关于 %s %s 的故事有很多,不知道你想听哪一个" % (self.name, self.job))
    def __del__(self):
        print("now who you daddy right %s" % self.name)

class master(daddy):
    def __init__(self, name, job):
        super(master, self).__init__(name, job)
        self.why()
    def person(self):
        print("【%s】 意识nb 草丛queen 国服第一%s" % (self.name, self.job))

class adc(daddy):
    def __init__(self, name, job, hurt):
        super(adc, self).__init__(name, job)
        self.hurt = hurt
    def person(self):
        print("【%s】 %s走位风骚，伤害高" % (self.name, self.job))

a = adc('Topaz', '后羿', '10000+')
# a1 = adc('阿猫', '孙尚香', '20000+')
b = master('Topaz喵', '妲己')
# b1 = master('Topaz喵', '貂蝉')
a.person()
# a1.person()
b.person()
# b1.person()