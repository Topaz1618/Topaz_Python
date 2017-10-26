#_*_coding:utf-8_*_
# Author:Topaz
import json
import time

a = [None,time.time()]
print(type(a))
b = json.dumps(a)
print(type(b))
c = json.loads(b)
print(type(c))

