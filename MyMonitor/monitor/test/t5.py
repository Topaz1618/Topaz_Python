#_*_coding:utf-8_*_
# Author:Topaz
#时间戳转换
import time
t = 1508065726.8387375
st = time.localtime(t)
a = time.strftime('%Y-%m-%d %H:%M:%S', st)

print(a)