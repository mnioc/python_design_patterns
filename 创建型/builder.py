# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 生成器（建造者）模式: 将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以常见不同的表示
# 目标对象由组件构成的场景中，很适合建造者模式
# ------------------#

# ---------------------------------------------------------------------------------------------
# 点餐系统v1.0，不包含任何设计模式


class Food:
    """食品类"""

    def __init__(self) -> None:
        self.price = 0

    @property
    def food_name(self):
        return self.__name__

class Cola(Food):

    __name__ = "可乐"

    def __init__(self) -> None:
        self.price = 6

class Chips(Food):

    __name__ = "薯条"

    def __init__(self) -> None:
        self.price = 18

class Hamburg(Food):

    __name__ = "汉堡"

    def __init__(self) -> None:
        self.price = 35

class Application():
    """点餐程序"""

    order = []
    order.append(Chips())
    order.append(Hamburg())
    [print(food.food_name, ": ", food.price) for food in order]
    print("总价: ", sum([food.price for food in order]))


# ---------------------------------------------------------------------------------------------
# 点餐系统v2.0, 代码看着low，臃肿，决定采用建造器模式进行重构, 并且订单需要根据食物类型进行分类统计，
# 比如一个完整的订单需要包含饮料、主食、小吃三个部分，我们的第一版代码是没有实现的

from abc import ABC, abstractmethod

class OrderBuilder(ABC):

    @abstractmethod
    def add_staple(self):
        raise NotImplementedError('`add_staple()` must be implemented.')
    
    @abstractmethod
    def add_drink(self):
        raise NotImplementedError('`add_staple()` must be implemented.')
    
    @abstractmethod
    def add_snacks(self):
        raise NotImplementedError('`add_staple()` must be implemented.')
    

# class 
