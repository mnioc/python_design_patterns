# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 中介者模式: 是一种行为设计模式， 能让你减少对象之间混乱无序的依赖关系。 
# 该模式会限制对象之间的直接交互， 迫使它们通过一个中介者对象进行合作。
# ------------------#

"""
中介者模式就像代理模式的高级版，代理模式只代理一方，而中介者代理两方或者更多的角色
中介者模式往往在框架的设计层面上才用得到，比如著名的MVC（这里的C即Controller，就是一个中介者）。
平时业务代码很少出现这么高的耦合情况，如果滥用的话，反而会使项目变的更复杂。
"""

class Consumer:
    """消费者类"""

    def __init__(self, product, price):
        self.name = "消费者"
        self.product = product
        self.price = price

    def shopping(self, name):
        """买东西"""
        print("向{} 购买 {}价格内的 {}产品".format(name, self.price, self.product))


class Producer:
    """生产者类"""
    def __init__(self, product, price):
        self.name = "生产者"
        self.product = product
        self.price = price

    def sale(self, name):
        """卖东西"""
        print("向{} 销售 {}价格的 {}产品".format(name, self.price, self.product))


class Mediator:
    """中介者类"""

    def __init__(self):
        self.name = "中介者"
        self.consumer = None
        self.producer = None

    def sale(self):
        """进货"""
        self.consumer.shopping(self.producer.name)

    def shopping(self):
        """出货"""
        self.producer.sale(self.consumer.name)

    def profit(self):
        """利润"""
        print('中介净赚：{}'.format((self.consumer.price - self.producer.price )))

    def complete(self):
        self.sale()
        self.shopping()
        self.profit()


if __name__ == '__main__':
    consumer = Consumer('手机', 3000)
    producer = Producer("手机", 2500)
    mediator = Mediator()
    mediator.consumer = consumer
    mediator.producer = producer
    mediator.complete()