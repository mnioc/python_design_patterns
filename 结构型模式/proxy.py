# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 代理模式: 是一种结构型设计模式, 让你能够提供对象的替代品或其占位符。 代理控制着对于原对象的访问， 并允许在将请求提交给对象前后进行一些处理。
# ------------------#

"""
代理模式跟我们之前说的装饰模式有点类似，例如，下面我们可以使用代理模式对本地的http请求进行拦截
"""

from email import header
import requests

class HttpRequestBase:
    session = requests.session()

    def fetch(self, method: str, url: str, **kwargs):
        method = method.lower()
        handle = getattr(self.session, method)
        if handle is None or not hasattr(handle, '__call__'):
            raise AttributeError("Request method not allowed")
        response = handle(url, **kwargs)
        return response


class HttpProxy(HttpRequestBase):

    def fetch_proxy(self, method, url, **kwargs):
        print("准备发起一个http请求...")
        header = {"Content-Type": "application/json"}
        res = self.fetch(method=method, url=url, headers=header ,**kwargs)
        print("请求结束...")
        return res


class Application:

    def run(self):
        HttpProxy().fetch_proxy("get", "http://www.baidu.com")


Application().run()

# output:
"""
准备发起一个http请求...
请求结束...
"""
# 在上面的例子中，我们给请求加了一层代理，使得我们能够在请求发起前后记录debug信息，并且自动加上请求头