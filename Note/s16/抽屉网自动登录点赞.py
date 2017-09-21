# Author:Topaz
import requests

##1.首先登录任何页面，获取cookie
i1=requests.get(url="http://dig.chouti.com/help/service")

##2.用户登陆，携带cookie，后台对cookie中的gpsd进行授权
i2=requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone':"8618310703270",
        'password':"123456",
        'oneMonth':""
    },
    cookies=i1.co0okies.get_dict()
)

##3.点赞（只需要已经被授权的gpsd即可）
gpsd=i1.cookies.get_dict()['gpsd']
i3=requests.post(
    url="http://dig.chouti.com/link/vote?linksId=9536506",
    cookies={'gpsd':gpsd}
)
print(i3.text)