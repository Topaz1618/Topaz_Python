import tornado.web
from tornado import gen
import tornado_mysql
from tornado_mysql import pools

POOL = pools.Pool(
    dict(host='10.0.0.138',port=3306,user='dog',passwd='123456',db='topaz'),
    max_idle_connections=1,
    max_recycle_sec=3)
@gen.coroutine
def get_user_by_conn_pool(user):
    cur = yield POOL.execute("SELECT SLEEP(%s)", (user,))   #在pool中进行查询,返回Future产生closed光标,可以从游标中获取行，lastrowid等
    row = cur.fetchone()    #获取下一行
    raise gen.Return(row)  #手动引发一个异常
@gen.coroutine
def get_user(user):
    print('get_user',user)
    conn = yield tornado_mysql.connect(host='10.0.0.138',port=3306,passwd='123456',user='dog',db='topaz',charset='utf8')    #连接
    cur = conn.cursor()     #获取下一行
    print('cur',cur)
    # yield cur.execute("SELECT name,email FROM web_models_userprofile where name=%s", (user,))
    yield cur.execute("select sleep(10)")
    row = cur.fetchone()
    cur.close()
    conn.close()
    raise gen.Return(row)
class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('son.html')
    @gen.coroutine
    def post(self, *args, **kwargs ):
        user = self.get_argument('username')    #name为username的标签
        data = yield gen.Task(get_user, user)   #去找getuser，把user穿进去，适用于call的的异步功能
        if data:
            print('data',data)
            self.redirect('http://www.cnblogs.com')
        else:
            self.render('son.html')
settings = {
    'template_path': 'tpl',
    'static_path': 'static',  # 设置静态文件位置
    'static_url_prefix': '/static/',  # 设置前端前缀 <img src="/static/a.png?v=39b39f17e9f93251e9423fbe52651899">

}
application = tornado.web.Application([
    (r"/login", LoginHandler),
],**settings)
if __name__ == "__main__":
    application.listen(8886)
    tornado.ioloop.IOLoop.instance().start()      #一直监听
    tornado.web.type.get_content_version()