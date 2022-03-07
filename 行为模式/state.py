# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 状态模式: 是一种行为设计模式， 让你能在一个对象的内部状态变化时改变其行为， 使其看上去就像改变了自身所属的类一样。
# ------------------#

"""
状态模式（State）经常用在带有状态的对象中。
什么是状态？我们以QQ聊天为例，一个用户的QQ有几种状态:
    1、离线状态（尚未登录）；
    2、正在登录状态；
    3、在线状态；
    4、忙碌状态。

状态设计模式的3个主要参与者
    1、State: 封装对象行为的接口，这个行为与对象的状态相关联
    2、ConcreteState: 实现State 接口的子类，ConcreteState 实现与对象的特定状态相关联的实际行为
    3、Context: 定义了客户感兴趣的接口，Context还维护了一个ConcreteState 子类的实例，
                该子类在内部定义了对象的特定状态的实现

我们下面设计了这样一个有限状态机，所有的状态: open、close、stop、run
并且状态的流转是有条件的: 
    1. open只能改成close、run
    2、close只能改成open
    ......
"""

from abc import ABC, abstractmethod
from multiprocessing import context

class Context:

    _state = None

    def __init__(self, state: 'State') -> None:
        self.transition_to(state)
    
    def transition_to(self, state: 'State'):
        print(f"状态更改为: {state.name}, 原状态为: {getattr(self._state, 'name', None)}")
        self._state = state
        self._state.context = self
    
    def change_to(self, handle_method):
        self._state.handle(handle_method)
    

class State(ABC):

    allowed = ["open", "close", "run", "stop"]

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    def handle(self, handle_method: str) -> None:
        handle_method = getattr(self, handle_method, None)
        if handle_method is not None:
            return handle_method()
        print(f"【ERROR】无法更改状态，当前状态为: {self.name}, 只允许更改的目标状态为: {','.join(self.allowed)}")

class OpenState(State):
    name = "open"
    allowed = ["close", "run"]

    def close(self):
        self.context.transition_to(CloseState())
    
    def run(self):
        self.context.transition_to(RunState())


class CloseState(State):
    name = "close"
    allowed = ["open"]

    def open(self):
        self.context.transition_to(OpenState())

class RunState(State):
    name = "run"
    allowed = ["stop"]

    def stop(self):
        self.context.transition_to(StopState())

class StopState(State):
    name = "stop"
    allowed = ["run", "close"]

    def run(self):
        self.context.transition_to(RunState())
    
    def close(self):
        self.context.transition_to(CloseState())


class Application:

    def run(self):
        context = Context(CloseState())
        context.change_to("open")
        context.change_to("run")
        context.change_to("close")

Application().run()

# output
"""
状态更改为: close, 原状态为: None
状态更改为: open, 原状态为: close
状态更改为: run, 原状态为: open
【ERROR】无法更改状态，当前状态为: run, 只允许更改的目标状态为: stop
"""