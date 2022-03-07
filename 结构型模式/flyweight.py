# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 享元模式（缓存、Cache）: 是一种结构型设计模式, 它摒弃了在每个对象中保存所有数据的方式
# 通过共享多个对象所共有的相同状态， 让你能在有限的内存容量中载入更多对象。
# ------------------#

"""
享元模式只有一个目的: 将内存消耗最小化。如果你的程序没有遇到内存容量不足的问题， 则可以暂时忽略该模式。
在面向对象程序设计过程中，有时会面临要创建大量相同或相似对象实例的问题。创建那么多的对象将会耗费很多的系统资源，它是系统性能提高的一个瓶颈。
例如，围棋和五子棋中的黑白棋子、大型3D游戏中的小兵、数据库中的连接池、12306余票查询系统。。。
下面我们使用享元模式模拟一个余票查询系统
"""

import random

class Ticket:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.over = random.randint(1,1000)
    
    @property
    def ticket_info(self):
        return f"{self.start} --> {self.end}, 余票: {self.over}"


class TicketFactory:

    def __init__(self) -> None:
        self.ticket_cache = {}
    
    def query(self, start: str, end: str) -> Ticket:
        key = f"{start}-{end}"
        # 假设我们要查询的起点、终点的车票信息已经被创建过了，那么就不再重复创建
        try:
            return self.ticket_cache[key]
        except KeyError:
            self.ticket_cache[key] = Ticket(start, end)
            return self.ticket_cache[key]


class Application:

    def run(self):
        ticket_factory = TicketFactory()

        ticket = ticket_factory.query("上海", "北京")
        print(ticket.ticket_info)

        ticket = ticket_factory.query("深圳", "北京")
        print(ticket.ticket_info)

        ticket = ticket_factory.query("上海", "北京")
        print(ticket.ticket_info)

        ticket = ticket_factory.query("深圳", "广州")
        print(ticket.ticket_info)

        ticket = ticket_factory.query("上海", "北京")
        print(ticket.ticket_info)

        ticket = ticket_factory.query("上海", "北京")
        print(ticket.ticket_info)


Application().run()

# output
"""
上海 --> 北京, 余票: 188
深圳 --> 北京, 余票: 676
上海 --> 北京, 余票: 188
深圳 --> 广州, 余票: 736
上海 --> 北京, 余票: 188
上海 --> 北京, 余票: 188
"""

# 在上面的代码中，看起来我们一共进行了6次查询，但是其实只创建了 3 个 Ticket对象
# 因为有四个查询都是查询北京到上海的余票