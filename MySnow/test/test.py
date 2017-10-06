#!/usr/bin/env python
# coding:utf-8
header_bytes = bytes()
rec =  b'GET /asyc/ HTTP/1.1\r\nHost: 127.0.0.1:8001\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.8\r\nCache-Control: max-age=0\r\nProxy-Connection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nX-Lantern-Version: 4.0.1\r\n\r\n'
cut = rec.split(b'\r\n\r\n')
a,b = cut
header_dic = {}

# deal = str(a)
deal = str(a,encoding="utf-8")
print(deal)
hold = deal.split('\r\n')
print(hold)
first_line  = hold[0].split(' ')
print(first_line)

first_line = hold[0].split(' ')
if len(first_line) == 3:
    method, url, protocol = first_line
    for line in hold:
        kv = line.split(':')
        print('kv:',kv)
        if len(kv) == 2:
            k, v = kv
            print('======',k,v)
            header_dic[k] = v
    print(header_dic)