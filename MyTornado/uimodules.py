#_*_coding:utf-8_*_
# Author:Topaz
from tornado.web import UIModule
from tornado import escape
class custom(UIModule):
    def render(self, *args, **kwargs):
        return escape.xhtml_escape('<h1>Topaz</h1>')

    # def javascript_files(self):
    #     '''在页面生成<script src="c1.js"></script>
    #     <script src="c2.js"></script>'''
    #     return ['c1.js','c2.js']
    # def embedded_javascript(self):
    #     '''在页面生成<script>alert(123)</script>'''
    #     return "alert(123)"
    # def css_files(self):
    #     '''生成<link href="c1.css" rel="stylesheet">'''
    #     return ['c1.css','c2.css']
    # def embedded_css(self):
    #     '''在页面生成<style> c1.{color:red;}（return的内容） </style>'''
    #     return "c1.{color:red;}"
