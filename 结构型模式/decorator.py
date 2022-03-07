# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 装饰模式: 是一种结构型设计模式, 允许你通过将对象放入包含行为的特殊封装对象中来为原对象绑定新的行为。。
# 动态地给一个对象添加一些额外得职责，就增加功能来说，装饰模式比生成子类更为灵活。
# ------------------#

"""
当我们想要给一个已经存在的类增加一些功能的时候，毫无疑问，我们第一反应都将会是继承这个类，然后在子类中去实现增加的新功能
但是， 你不能忽视继承可能引发的几个严重问题。
    1、继承是静态的。 你无法在运行时更改已有对象的行为， 只能使用由不同子类创建的对象来替代当前的整个对象。
    2、子类只能有一个父类
装饰器模式有点类似于继承，关于使用装饰器还是继承的选择，原则是当需要更多的行为时候，装饰器通常会更简练，
而在需要根据情况动态修改对象的行为时，就必须使用装饰器。装饰器具有相同的接口名，因此可以为目标对象创建多个装饰器
"""

import MySQLdb

class DatabaseWrapper:

    def __init__(self):
        self._conn = None
    
    def create_connect(self):
        self._conn = MySQLdb.connect(host='localhost',port = 3306,user='root',passwd='123456',db ='db_name')
    
    @property
    def connect(self):
        if self._conn is None:
            self.create_connect()
        return self._conn
    
    def save(self):
        print("执行save()")
    
    def insert(self):
        print("执行insert()")


# 此时，假设我们需要对上面的类进行拓展，又不想通过继承的方式，那么我们可以这样做

class DatabaseDecorator:
    
    def __init__(self, database_wrapper):
        self.database_wrapper = database_wrapper
    
    def redo(self):
        print("执行redo()")

    # 通过这个魔术方式，我们就能返回 DatabaseWrapper 的所有属性
    def __getattr__(self, attr):
        return getattr(self.database_wrapper, attr)


class Application:

    def run(self):
        database = DatabaseDecorator(DatabaseWrapper())
        database.insert()
        database.save()
        database.redo()

Application().run()

# output
"""
执行insert()
执行save()
执行redo()
"""