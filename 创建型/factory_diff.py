# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ----------------
# 几种工厂模式的比较
# ----------------
from abc import ABC, abstractmethod


# 业务场景：A公司是一家做给不同的电脑厂商外设做驱动检测的公司，那么就需要一个执行驱动检测的程序，早期的时候，公司业务不大，规模很小，所以就只做鼠标驱动
# [1]-------------------------------------------无工厂---------------------------------------------------
# 早期的代码非常简单，也非常的清晰

class MouseDriver:
    """鼠标驱动"""

    def click(self):
        print("鼠标执行了单击操作")


class HPMouseDriver:
    """HP牌鼠标驱动"""

    def click(self):
        print("HP品牌鼠标执行了单击操作")
    

class DellMouseDriver:
    """Dell牌鼠标驱动"""

    def click(self):
        print("Dell品牌鼠标执行了单击操作")


class Application():

    def run_check(self):
        hp_mouse_drive = HPMouseDriver()
        hp_mouse_drive.click()

        dell_mouse_drive = DellMouseDriver()
        dell_mouse_drive.click()




# [2]-------------------------------------------简单工厂---------------------------------------------------
# 后面类开始变多了，代码开始变得臃肿，并且希望能通过一个统一的入口去管理
# 于是，程序员们决定对这部分代码进行重构，经过商讨决定采用 静态工厂方法(Static Factory Method)模式 去进行重构

class SimpleDriverFactory:
    """
    工厂方法包含了一个可以实例化所有驱动的方法，业务代码不需要再去实例化不同的驱动类了，实现了责任分离
    当客户类需要的时候，委托工厂类创建驱动类的对象
    NOTE
    但是!!! 它违背了开闭原则!!!
    当我们新加入其他厂商驱动的时候，我们不得不去更改该工厂类的方法以适配新的需求。
    """

    @staticmethod
    def get_drive(option):
        drive = None
        if option == "hp":
            drive = HPMouseDriver()
        elif option == "dell":
            drive = DellMouseDriver()
        return drive


class Application:

    def run_check(self):
        SimpleDriverFactory.get_drive("dell").click()
        SimpleDriverFactory.get_drive("hp").click()





# [3]-------------------------------------------工厂方法模式---------------------------------------------------
# 还是刚才做驱动检测的那家公司，由于业务线的发展，他们有了更多的客户，但同时也不得不进行新一轮的重构，这一次的重构是因为什么呢？
# 是因为他们每次新加入厂商检测方法的时候，都需要去改动简单工厂里面的 if else 语句，并且if 语句越来越多，拓展性实在是太差了。


class MouseDriverFactory(ABC):

    @abstractmethod
    def get_dirve_instance(self) -> MouseDriver:
        raise NotImplementedError('`get_dirve_instance()` must be implemented.')
    
    def execute_check(self):
        mouse_dirve = self.get_dirve_instance()
        mouse_dirve.click()


class HPMouseDriverFactory(MouseDriverFactory):

     def get_dirve_instance(self) -> HPMouseDriver:
         return HPMouseDriver()


class DellMouseDriverFactory(MouseDriverFactory):

     def get_dirve_instance(self) -> DellMouseDriver:
         return DellMouseDriver()


class Application():

    def run_check(self):
        DellMouseDriverFactory().execute_check
        HPMouseDriverFactory().execute_check




# [4]-------------------------------------------抽象工厂模式---------------------------------------------------
# 还是刚才做驱动检测的那家公司，随着业务的发展，跨平台的需求应运而生，于是他们需要去对mac、linux、window不同的操作系统进行兼容

# 抽象工厂，声明了一组能返回不同抽象产品的方法，例如：window鼠标驱动和linux鼠标驱动同属于鼠标驱动这一系列
class MouseDriverFactory(ABC):

    @abstractmethod
    def get_window_dirve_instance(self) -> MouseDriver:
        raise NotImplementedError('`get_window_dirve_instance()` must be implemented.')
    
    @abstractmethod
    def get_linux_dirve_instance(self) -> MouseDriver:
        raise NotImplementedError('`get_linux_dirve_instance()` must be implemented.')
    
    @abstractmethod
    def execute_check(self) -> None:
        pass


# 具体工厂： 这里是 HP 品牌工厂，HP的鼠标需要进行window、linux的适配
class HPDriverFactory(MouseDriverFactory):

    def get_window_dirve_instance(self) -> 'HPWindowMouseDriver':
        return HPWindowMouseDriver()
    
    def get_linux_dirve_instance(self) -> 'HPLinuxMouseDriver':
        return HPLinuxMouseDriver()
    
    def execute_check(self):
        self.get_window_dirve_instance().click()
        self.get_linux_dirve_instance().click()

# # 具体工厂： 这里是 Dell 品牌工厂，Dell的鼠标需要进行window、linux的适配
class DellDriverFactory(MouseDriverFactory):

    def get_window_dirve_instance(self) -> 'DellWindowMouseDriver':
        return DellWindowMouseDriver()
    
    def get_linux_dirve_instance(self) -> 'DellLinuxMouseDriver':
        return DellLinuxMouseDriver()

    def execute_check(self):
        self.get_window_dirve_instance().click()
        self.get_linux_dirve_instance().click()


class WindowMouseDriver:

    def click(self):
        print("Window环境下鼠标执行了单击操作")


class HPWindowMouseDriver(WindowMouseDriver):

    def click(self):
        print("Window环境下HP品牌鼠标执行了单击操作")


class DellWindowMouseDriver(WindowMouseDriver):

    def click(self):
        print("Window环境下Dell品牌鼠标执行了单击操作")


class LinuxMouseDriver:

    def click(self):
        print("Linux环境下鼠标执行了单击操作")


class HPLinuxMouseDriver(LinuxMouseDriver):

    def click(self):
        print("Linux环境下HP品牌鼠标执行了单击操作")


class DellLinuxMouseDriver(LinuxMouseDriver):

    def click(self):
        print("Linux环境下Dell品牌鼠标执行了单击操作")


class Application:

    def __init__(self):
        self._driver_factory = None
    
    def load_driver_factory(self, driver_factory_class):
        return driver_factory_class()
    
    def run_check(self):
        self.load_driver_factory(HPDriverFactory).execute_check()
        self.load_driver_factory(DellDriverFactory).execute_check()

