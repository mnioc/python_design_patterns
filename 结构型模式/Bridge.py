# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 桥接模式: 是一种结构型设计模式， 可将一个大类或一系列紧密相关的类拆分为抽象和实现两个独立的层次结构， 从而能在开发时分别使用。
# 也就是将抽象化(Abstraction)与实现化(Implementation)解耦，使得二者可以独立地变化
# ------------------#

"""
桥接模式的关注点在于多个相关的类如何组合，例如下面我们要做的一个社交平台
我们可以调用qq发消息、也可以调用微信发消息，客户端有两种
我们可以发送图片信息、也可以发送文字信息，也可以发送转账信息，信息类型有三种
那么假设我们使用单一的类去实现的话：需要 2*3中组合类，这样类就太多了
"""


from abc import ABC, abstractmethod

class MsgClient:

    @abstractmethod
    def send_msg_to(self, msg, to_user):
        raise NotImplementedError('`send_msg_to()` must be implemented.')


class QQClient(MsgClient):

    def send_msg_to(self, msg, to_user):
        print(f"【QQ消息】hello，{to_user}， {msg}")


class WechatClient(MsgClient):

    def send_msg_to(self, msg, to_user):
        print(f"【微信消息】hello，{to_user}， {msg}")


class MsgClientHandle:

    def __init__(self, msg_client: MsgClient) -> None:
        self.msg_client = msg_client
    
    def send(self, msg, to_user):
        self.msg_client.send_msg_to(msg, to_user)


class TransferMsg(MsgClientHandle):

    def send(self, msg, to_user):
        msg = msg + "【转账信息，只能使用微信客户端发送】"
        super().send(msg, to_user)


class RedPacketMsg(MsgClientHandle):

    def send(self, msg, to_user):
        msg = msg + "【QQ红包，只能使用QQ客户端发送】"
        super().send(msg, to_user)


class Application:

    def run(self):
        qq = QQClient()
        msg_client = RedPacketMsg(qq)
        msg_client.send("给你发了一个QQ红包，快去QQ领取", "user1")

Application().run()
