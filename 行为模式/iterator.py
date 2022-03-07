# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 迭代器模式: 是一种行为设计模式， 让你能在不暴露集合底层表现形式 （列表、 栈和树等） 的情况下遍历集合中所有的元素。
# ------------------#

"""
实现迭代模式对于Python来说没有多余的代码，寥寥几行代码足可以实现迭代模式。
这个设计模式就不同多说了。python内置的迭代器、生成器
"""

def FibonacciSequence(n):
    x = 0
    y = 1
    i = 1
    while True:
        yield y
        if i == n:
            break
        x, y = y, x+y
        i += 1


if __name__ == '__main__':
    test = FibonacciSequence(7)
    next(test)
    1
    next(test)
    1
    next(test)
    2
    next(test)
    3
    next(test)
    5
    next(test)
    8
    next(test)
    13
    next(test)