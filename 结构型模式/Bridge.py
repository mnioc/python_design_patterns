# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 桥接模式: 是一种结构型设计模式， 可将一个大类或一系列紧密相关的类拆分为抽象和实现两个独立的层次结构， 从而能在开发时分别使用。
# 也就是将抽象化(Abstraction)与实现化(Implementation)解耦，使得二者可以独立地变化
# ------------------#

"""
桥接模式的关注点在于多个相关的类如何组合，生活中最常见的软件案例就是支付了，例如我们使用某团、超市收银等等
他们都做了聚合支付，就是我们可以选择的支付方式有：微信支付、支付宝支付、银联支付
然后我们的验证方式又可以支持密码验证、指纹验证、人脸识别认证
那么，假如我们采用传统的组合类的方式，一共需要写 3 * 3 = 9 个组合类
    1. 微信指纹支付
    2. 微信密码支付
    3. 支付宝人脸识别支付
    ......
当我们又出现新的支付方式或者验证方式的时候，我么还需要不断的增加新类，这样就会非常的冗余，使用桥接模式就能解决这个问题
"""


# ---------------------------------------------------------------------------------------------
# 原始代码可能是这样的, 非常的不优雅

def pay(pay, pay_type):
    if pay == "alipay":
        if pay_type == "face":
            ...
        elif pay_type == "password":
            ...
        elif pay_type == "touch":
            ...
    elif pay == "wechat_pay":       
        if pay_type == "face":
            ...
        elif pay_type == "password":
            ...
        elif pay_type == "touch":
            ...



# ---------------------------------------------------------------------------------------------
# 采用桥接模式

from abc import ABC, abstractmethod


class IPayType:

    @abstractmethod
    def pay(self):
        raise NotImplementedError('`pay()` must be implemented.')


    @abstractmethod
    def pay_check(self):
        raise NotImplementedError('`pay_check()` must be implemented.')


class FacePay(IPayType):

    def pay_check(self):
        print("人脸识别校验通过")
    
    def pay_to(self, user, money):
        print(f"向{user}支付{money}元")


class TouchPay(IPayType):

    def pay_check(self):
        print("指纹识别校验通过")
    
    def pay_to(self, user, money):
        print(f"向{user}支付{money}元")


class IPayClient(IPayType):

    def __init__(self, pay_type: IPayType) -> None:
        self.pay_type = pay_type

    def pay(self, user: str, money: float):
        self.pay_type.pay_check()
        self.pay_type.pay_to(user, money)


class AliPay(IPayClient):

    def pay(self, user: str, money: float):
        print("正在使用支付宝支付...")
        return super().pay(user, money)


class WechatPay(IPayClient):

    def pay(self, user: str, money: float):
        print("正在使用微信支付...")
        return super().pay(user, money)


class Application:

    def run(self):
        AliPay(FacePay()).pay("王记小笼包", 20)


Application().run()

# output
"""
正在使用支付宝支付...
人脸识别校验通过
向王记小笼包支付20元
"""
