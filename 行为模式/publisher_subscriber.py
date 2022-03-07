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

class PhoneStoryPublisher:
  def __init__(self):
    pass
  def register(self):
    pass
  def unregister(self):
    pass
  def notifyAll(self):
    pass
