# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 策略模式: 是一种行为设计模式， 它在超类中定义了一个算法的框架， 允许子类在不修改结构的情况下重写算法的特定步骤。
# ------------------#

"""
模板方法（Template Method）是一个比较简单的模式。它的主要思想是，定义一个操作的一系列步骤，
对于某些暂时确定不下来的步骤，就留给子类去实现好了，这样不同的子类就可以定义出不同的步骤。
模版方法模式在 Python 框架中很常见。 开发者通常使用它来向框架用户提供通过继承实现的、 对标准功能进行扩展的简单方式。
"""


from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()  # 交给子类去实现
        self.base_operation2()
        self.hook1() # 交给子类去实现
        self.required_operations2() # 交给子类去实现
        self.base_operation3()
        self.hook2() # 交给子类去实现

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")

class Application:

    def client_code(self, abstract_class: AbstractClass) -> None:
        abstract_class.template_method()

    def run(self):
        self.client_code(ConcreteClass1())

Application().run()

# output
"""
AbstractClass says: I am doing the bulk of the work
ConcreteClass1 says: Implemented Operation1
AbstractClass says: But I let subclasses override some operations
ConcreteClass1 says: Implemented Operation2
AbstractClass says: But I am doing the bulk of the work anyway
"""