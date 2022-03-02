# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# -----------#
# 几种工厂模式的比较
# -----------#
from abc import ABC, abstractmethod


# 业务场景：A公司是一家做驱动检测的公司，那么就需要一个执行驱动检测的程序，早期的时候，公司业务不大，规模很小，所以就只做了鼠标与键盘驱动
# [1]-------------------------------------------无工厂---------------------------------------------------
# 早期的代码非常简单，也非常的清晰

class MouseDriver:
    """鼠标驱动"""

    def click(self):
        print("执行了单击操作")
    
    def double_click(self):
        print("执行了双击操作")


class KeyboardDrive:
    """键盘驱动"""

    def press_enter(self):
        print("按下了enter键")


# if __name__ == "__main__":
#     mouse_drive = MouseDriver()
#     mouse_drive.click()
#     mouse_drive.double_click()

#     keyboard_drive = KeyboardDrive()
#     keyboard_drive.press_enter()



# [2]-------------------------------------------简单工厂---------------------------------------------------
# 后面类开始变多了，代码开始变得臃肿，并且希望能通过一个统一的入口去管理
# 于是，程序员们决定对这部分代码进行重构，经过商讨决定采用 静态工厂方法(Static Factory Method)模式 去进行重构

class DriverFactory:
    """
    工厂方法包含了一个可以实例化所有驱动的方法，业务代码不需要再去实例化不同的驱动类了，实现了责任分离
    当客户类需要的时候，委托工厂类创建驱动类的对象
    NOTE
    但是!!! 它违背了开闭原则!!!
    当我们新加入其他驱动的时候，我们不得不去更改该工厂类的方法以适配新的需求。
    """

    @staticmethod
    def get_drive(option):
        drive = None
        if option == "mouse":
            drive = MouseDriver()
        elif option == "keyboard":
            drive = KeyboardDrive()
        return drive


# if __name__ == "__main__":
#     mouse_drive = DriverFactory.get_drive("mouse")
#     mouse_drive.click()
#     mouse_drive.double_click()

#     keyboard_drive = DriverFactory.get_drive("keyboard")
#     keyboard_drive.press_enter()


# [3]-------------------------------------------工厂方法模式---------------------------------------------------
# 还是刚才做驱动检测的那家公司，由于业务线的发展，他们有了更多的客户，但同时也不得不进行新一轮的重构，这一次的重构是因为什么呢？
# 是因为他们需要对不同操作系统环境下的驱动进行检测，这个时候该如何对代码进行重构呢？

class DriverFactory(ABC):

    @abstractmethod
    def create_mouse_drive(self) -> MouseDriver:
        raise NotImplementedError('`create_mouse_drive()` must be implemented.')
    
    @abstractmethod
    def create_keyboard_drive(self) -> MouseDriver:
        raise NotImplementedError('`create_keyboard_drive()` must be implemented.')

    def execute_check(self):
        mouse_dirve = self.create_mouse_drive()
        mouse_dirve.click()
        mouse_dirve.double_click()

        keyboard_drive = self.create_keyboard_drive()
        keyboard_drive.press_enter()
        

class WindowDriverFactory(DriverFactory):

    def create_mouse_drive(self) -> 'WindowMouseDriver':
        return WindowMouseDriver()
    
    def create_keyboard_drive(self) -> 'WindowKeyboardDriver':
        return WindowKeyboardDriver()


class WindowMouseDriver(MouseDriver):

    def click(self):
        print("window 鼠标执行了单击操作")
    
    def double_click(self):
        print("window 鼠标执行了双击操作")


class WindowKeyboardDriver(KeyboardDrive):

    def press_enter(self):
        print("window 键盘按下了enter键")


class LinuxDriverFactory(DriverFactory):

    def create_mouse_drive(self) -> 'LinuxMouseDriver':
        return LinuxMouseDriver()
    
    def create_keyboard_drive(self) -> 'LinuxKeyboardDriver':
        return LinuxKeyboardDriver()


class LinuxMouseDriver(MouseDriver):

    def click(self):
        print("Linux 鼠标执行了单击操作")
    
    def double_click(self):
        print("Linux 鼠标执行了双击操作")


class LinuxKeyboardDriver(KeyboardDrive):

    def press_enter(self):
        print("Linux 键盘按下了enter键")


class DriverApp:
    
    def __init__(self, os_type):
        
        self.driver = None
        if os_type == "window":
            self.driver = WindowDriverFactory()
        elif os_type == "linux":
            self.driver = LinuxDriverFactory()
        
        assert self.driver, "driver must not None"

    def execute_check(self):
        return self.driver.execute_check()


if __name__ == "__main__":
    DriverApp("linux").execute_check()


# -------------------------------------------抽象工厂模式---------------------------------------------------
# 还是刚才做驱动检测的那家公司，由于业务线的发展，他们有了更多的客户，但同时也不得不进行新一轮的重构，这一次的重构是因为什么呢？
# 原来是市面上有很多的制作鼠标、键盘的厂商，他们希望能够使用他们的驱动检测程序给自己家制作的鼠标，键盘做检测

