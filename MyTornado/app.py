#_*_coding:utf-8_*_
# Author:Topaz
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.concurrent import Future
from MyTornado import uimethods as mt
from MyTornado import uimodules as md

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("login_user")
class LoginHandler(tornado.web.RequestHandler):
    '''访问  http://127.0.0.1:8888/login  ==> 输出 name = username 的input标签里输入的内容，并弹窗666'''
    @gen.coroutine
    def get(self):
        self.render('son.html')
        future = Future()
        future.add_done_callback(self.post)
        yield future
    def post(self, *args, **kwargs):
        print('nihao')
        file_metas = file_metas = self.request.files["fff"]  # 添加这句就是获取文件，fff 就是上传<input>的name
        print(file_metas)
        for meta in file_metas:
            file_name = meta['filename']  # meta里的filename就是文件名
            with open(file_name, 'wb') as f:
                f.write(meta['body'])  # body写到本地
        self.redirect('/')
        user = self.get_argument('username')
        if user == "topaz":
            self.set_secure_cookie('login_user', 'Topaz')
            self.redirect('/')
        else:
            self.render('son.html', **{'status': '用户名或密码错误'})
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        login_user = self.get_secure_cookie('login_user',None)
        if login_user:
            self.write(login_user)
        else:
            self.redirect('/login')
settings = {
    'template_path': 'tpl',     #配置模板,也就是html文件的地儿
    'ui_methods': mt,            #注册ui方法
    'ui_modules': md,            #注册ui模块
    'static_path': 'static',    #设置静态文件位置
    'static_url_prefix': '/static/', #设置前端前缀 <img src="/static/a.png?v=39b39f17e9f93251e9423fbe52651899">
    'cookie_secret':'t114uXSkw1SZ6xlWOCASQWYKkIuW7Wl2bTnbsLzsJyoOI7EqnnaT8HDzFNbB9Ryw',
    "xsrf_cookies": True,
}

# Tronado的路由系统，看了感觉真可怜
application = tornado.web.Application([
    (r"/login", LoginHandler),      # http://127.0.0.1:8887/login 去找 LoginHandler 处理
    (r"/", MainHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8887)        #监听8887
    tornado.ioloop.IOLoop.instance().start()      #一直监听
    tornado.web.type.get_content_version()



