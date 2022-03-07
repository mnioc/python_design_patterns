# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 策略模式: 是一种行为设计模式，它能让你定义一系列算法， 并将每种算法分别放入独立的类中，以使算法的对象能够相互替换。。
# ------------------#

"""
以购物车结算为例，假设网站针对普通会员、Prime会员有不同的折扣。
同时活动期间还有一个满100减20的活动，这些就可以作为策略实现。
"""

from abc import abstractmethod


class DiscountStrategy:

    @abstractmethod
    def get_discount(self, total: float) -> float:
        raise NotImplementedError('`get_discount()` must be implemented.')


class UserDiscountStrategy(DiscountStrategy):
    """普通会员打九折"""
    def get_discount(self, total: float) -> float:
        return total * 0.9

class PrimeUserDiscountStrategy(DiscountStrategy):
    """Prime会员打75折"""
    def get_discount(self, total: float) -> float:
        return total * 0.75

class OverDiscountStrategy(DiscountStrategy):
    """满100减20优惠"""
    def get_discount(self, total: float) -> float:
        return total - 20 if total >= 100 else total


class DiscountContext:

    def __init__(self, strategy: DiscountStrategy) -> None:
        self.strategy = strategy
    
    @property
    def strategy(self) -> DiscountStrategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def calculate_price(self, total: float) -> float:
        return self.strategy.get_discount(total)


class Application:

    def run(self):
        discount_context = DiscountContext(UserDiscountStrategy())
        print("使用普通会员折扣，一共花费: ", discount_context.calculate_price(105))

        discount_context.strategy = OverDiscountStrategy()
        print("使用满减折扣，一共花费: ", discount_context.calculate_price(105))

        discount_context.strategy = OverDiscountStrategy()
        print("使用Prime会员折扣，一共花费: ", discount_context.calculate_price(105))

Application().run()

# output
"""
使用普通会员折扣，一共花费:  94.5
使用满减折扣，一共花费:  85
使用Prime会员折扣，一共花费:  85
"""