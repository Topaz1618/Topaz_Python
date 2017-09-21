.. contents::
.. code:: python
  class MainHandler(tornado.web.RequestHandler):

    def get(self):
      http = httpclient.AsyncHTTPClient()
      http.fetch("http://127.0.0.1:8008/post/", self.callback)
      self.write('end')

    def callback(self, response):
      print(response.body)
