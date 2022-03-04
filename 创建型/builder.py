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

    @property
    def food_name(self):
        return self.__name__

class Cola(Food):
    __name__ = "可乐"
    price = 6

class Milk(Food):
    __name__ = "牛奶"
    price = 12


class Chips(Food):
    __name__ = "薯条"
    price = 18


class Chicken(Food):
    __name__ = "鸡米花"
    price = 20


class Hamburg(Food):
    __name__ = "汉堡"
    price = 35


# class Application():
#     """点餐程序"""

#     order = []
#     order.append(Chips())
#     order.append(Hamburg())
#     [print(food.food_name, ": ", food.price) for food in order]
#     print("总价: ", sum([food.price for food in order]))


# ---------------------------------------------------------------------------------------------
# 点餐系统v2.0, 代码看着low，臃肿，决定采用建造器模式进行重构, 并且套餐由多种食物类型构成，
# 比如一个完整的套餐需要包含饮料、主食、小吃三个部分，我们的第一版代码是没有实现的

from abc import ABC, abstractmethod
from typing import Any

# 抽象套餐生成器
class PackageBuilder(ABC):

    @property
    @abstractmethod
    def package(self) -> None:
        pass

    @abstractmethod
    def add_staple(self) -> None:
        raise NotImplementedError('`add_staple()` must be implemented.')
    
    @abstractmethod
    def add_drink(self) -> None:
        raise NotImplementedError('`add_staple()` must be implemented.')
    
    @abstractmethod
    def add_snacks(self) -> None:
        raise NotImplementedError('`add_staple()` must be implemented.')


class ConcreteBuilderPackage(PackageBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._package = Package()
    
    @property
    def package(self) -> 'Package':
        package = self._package
        self.reset()
        return package
    
    def add_staple(self, food: Food) -> None:
        self._package.add("staple", food())
    
    def add_drink(self, food: Food) -> None:
        self._package.add("drink", food())
    
    def add_snacks(self, food: Food) -> None:
        self._package.add("snacks", food())


# 套餐
class Package:

    def __init__(self):
        self.staple = []
        self.drink = []
        self.snacks = []

    def add(self, food_type: str, food: Any) -> None:

        if food_type == "staple":
            self.staple.append(food)
        elif food_type == "drink":
            self.drink.append(food)
        elif food_type == "snacks":
            self.snacks.append(food)

    def show(self):
        print("您的套餐包含: ")
        staple = ",".join([food.food_name for food in self.staple])
        print(f"\t主食类: {staple}")
        drink = ",".join([food.food_name for food in self.drink])
        print(f"\t饮料类: {drink}")
        snacks = ",".join([food.food_name for food in self.snacks])
        print(f"\t小吃类: {snacks}")
        print(f"\t总价为: {sum([food.price for food in (self.snacks + self.drink + self.staple)])} 元")


class Application:

    def run(self):
        # 一个套餐对象由多个部分组成，包括主食、小吃、饮料。。。
        # 这样我们可以采用建造者模式，可以有效的避免类的实例化的时候需要进行大量的赋值
        builder = ConcreteBuilderPackage()
        builder.add_drink(Cola)
        builder.add_staple(Hamburg)
        builder.add_snacks(Chicken)
        builder.add_snacks(Chips)
        builder.package.show()


Application().run()

