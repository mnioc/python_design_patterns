# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 原型模式: 使你能够复制对象， 甚至是复杂对象， 而又无需使代码依赖它们所属的类
# ------------------#

"""
原型模式关注的是大量相同对象或相似对象的创建问题，意图在于通过复制一个已经存在的实例来获得一个新的实例，以避免重复创建此类实例带来的开销。
被复制的实例就是这个“原型”，这个原型是可定制的。
原型模式最为核心的两点是: 拷贝、属性更新
   1、拷贝指深拷贝copy.deepcopy，
   2、属性更新是类的自有属性__dict__的更新。
"""

# ---------------------------------------------------------------------------------------------
# 使用原型模式，创建版本管理系统v1.0, 我们完全利用python的特性即可
import copy


class Product:

    def __init__(self, name, developer, content, version):
        self.name = name
        self.developer = developer,
        self.content = content
        self.version = version or '0.1.0'
    
    def __str__(self) -> str:
        return f"name: {self.name}, developer: {self.developer}, version: {self.version}"
    
    def deepcopy(self) -> 'Product':
        return copy.deepcopy(self)
    
    def copy(self) -> 'Product':
        return copy.copy(self)


if  __name__=="__main__":

    product_v1 = Product("商场管理系统", "mnio", "init commit", '0.1.0')
    print(product_v1)

    product_v2 = product_v1.deepcopy()
    product_v2.content = "This is version 1.0"
    product_v2.version = '1.0.0'
    print(product_v2)

    