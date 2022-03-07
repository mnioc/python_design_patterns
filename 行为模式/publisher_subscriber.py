# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 观察者模式（发布、订阅模式）: 是一种行为设计模式， 允许你定义一种订阅机制， 可在对象事件发生时通知多个 “观察” 该对象的其他对象。
# ------------------#

"""
我们设计一种应用场景: 手机销售店做了一个发布订阅软件，手机购买者可以订阅消息、手机供应商也可以订阅消息
当手机不够卖的时候通知: 告诉消费者手机库存不多了尽量不要来、告诉手机供应商赶紧送货过来
当手机太多的时候通知: 告诉消费者手机库存很多快来买、告诉手机供应商先少送
"""

from abc import ABC, abstractmethod
import random
from typing import List

class PhoneStoryPublisher:
    def __init__(self):
        self._observers: List[Observer] = []
        self._inventory = 100
    
    @property
    def inventory(self):
        return self._inventory
    
    @inventory.setter
    def inventory(self, inventory: int):
        self._inventory = inventory
    
    def register(self, observer: 'Observer') -> None:
        self._observers.append(observer)

    def unregister(self, observer: 'Observer') -> None:
        self._observers.remove(observer)

    def notify_all(self):
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self) -> None:
        self._inventory = random.randint(1, 50)
        self.notify_all()

class Observer(ABC):

    @abstractmethod
    def update(self, publisher: PhoneStoryPublisher) -> None:
        raise NotImplementedError('`update()` must be implemented.')


class Consumer(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, publisher: PhoneStoryPublisher) -> None:
        if publisher.inventory >= 30:
            print(f"当前店内手机库存充足，顾客: {self.name} 欢迎您前来选购")

        

class Supplier(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, publisher: PhoneStoryPublisher) -> None:
        if 10 <= publisher.inventory <= 30:
            print(f"店内手机库存欠缺，供应商: {self.name} 可以逐渐补货")
        elif publisher.inventory < 10:
            print(f"店内手机库存严重不足，供应商: {self.name} 请马上补货")


class Application:

    def run(self):
        publisher = PhoneStoryPublisher()
        publisher.register(Consumer("Mr Wang"))
        publisher.register(Consumer("Mr Li"))
        publisher.register(Consumer("Miss Liu"))

        publisher.register(Supplier("供应商A"))
        publisher.register(Supplier("供应商B"))

        publisher.some_business_logic()
        print("----------------------------------------------------")
        publisher.some_business_logic()
        print("----------------------------------------------------")
        publisher.some_business_logic()
        print("----------------------------------------------------")
        publisher.some_business_logic()
        print("----------------------------------------------------")
        publisher.some_business_logic()

Application().run()

# output
"""
店内手机库存欠缺，供应商: 供应商A 可以逐渐补货
店内手机库存欠缺，供应商: 供应商B 可以逐渐补货
----------------------------------------------------
店内手机库存欠缺，供应商: 供应商A 可以逐渐补货
店内手机库存欠缺，供应商: 供应商B 可以逐渐补货
----------------------------------------------------
当前店内手机库存充足，顾客: Mr Wang 欢迎您前来选购
当前店内手机库存充足，顾客: Mr Li 欢迎您前来选购
当前店内手机库存充足，顾客: Miss Liu 欢迎您前来选购
----------------------------------------------------
当前店内手机库存充足，顾客: Mr Wang 欢迎您前来选购
当前店内手机库存充足，顾客: Mr Li 欢迎您前来选购
当前店内手机库存充足，顾客: Miss Liu 欢迎您前来选购
----------------------------------------------------
店内手机库存欠缺，供应商: 供应商A 可以逐渐补货
店内手机库存欠缺，供应商: 供应商B 可以逐渐补货
"""
        