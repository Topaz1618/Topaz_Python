<p>这是一个普通段落：</p>

<pre><code>
class MainHandler(tornado.web.RequestHandler):
        @asynchronous
        @gen.coroutine
        def get(self):
            print('start get ')
            http = httpclient.AsyncHTTPClient()
            http.fetch("http://127.0.0.1:8008/post/", self.callback)
            self.write('end')

        def callback(self, response):
            print(response.body)
</code></pre>
