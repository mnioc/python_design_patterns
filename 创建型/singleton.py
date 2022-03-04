# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 单例模式: 让你能够保证一个类只有一个实例， 并提供一个访问该实例的全局节点。
# ------------------#

"""
为何要确保一个类只能有一个实例呢？有一些场景可以说明: 例如我们的写入日志文件、读取文件、数据库连接、打印机处理程序等，
这些场景希望程序在运行过程中只生成一个实例，避免对同一资源产生相互冲突的请求
"""


class Singleton(object):

    def __new__(cls, *args, **kw):

        # 如果当前类没有实例，那么将会创建一个实例
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        # 否则返回该实例
        return cls._instance

if __name__=="__main__" :
    s1 = Singleton()
    s2 = Singleton()
    # s1,s2将会指向同一个对象
    print(s1, s2)