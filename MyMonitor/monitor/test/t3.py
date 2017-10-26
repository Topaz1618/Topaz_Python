#_*_coding:utf-8_*_
# Author:Topaz
import sys
class H(object):
    def __init__(self,a):
        self.a = a
        print(self.a)
        self.check()
    def check(self):
        if len(self.a) < 2:
            print("滚蛋")
        else:
            if hasattr(H,self.a[1]):
                print("有")
                func = getattr(H,self.a[1])
                func()
            else:
                print("没有滚蛋")
    @staticmethod
    def start():
        print("是他就是他小哪吒")

if __name__ == "__main__":
    a = H(sys.argv)