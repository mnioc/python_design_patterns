# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# -----------#
# 抽象工厂模式 
# -----------#

"""
在下面的例子中，我们使用了抽象工厂模式实现了一个驱动加载的方法
同一种操作系统有不同的驱动方法，例如鼠标驱动、键盘驱动
不同的操作系统又有不同的驱动方法，例如 window鼠标驱动、linux鼠标驱动
在这个场景中，我们实现了一个抽象工厂类:
    
    AbstractDriveFactory: 驱动工厂，包含所有的驱动，例如鼠标驱动、键盘驱动

所有的驱动工厂子类都应该继承它，各自去重写自己的驱动适配方法，例如
    
    1、WindowDriveFactory: window 操作系统的鼠标键盘驱动适配
    2、LinuxDriveFactory: Linux 操作系统的鼠标键盘驱动适配

当有一天我们的程序需要去适配 maxos 的时候，我们直接去创建一个新类: MaxosDriveFactory 即可，无需更改其他现有代码
"""

from abc import ABC, abstractmethod


class AbstractDriveFactory(ABC):
    """
    Drive factory
    """
    @abstractmethod
    def create_mouse_drive(self):
        pass
    
    @abstractmethod
    def create_keyboard_drive(self):
        pass


class AbstractMouse:
    
    @abstractmethod
    def click(self) -> None:
        pass
    
    @abstractmethod
    def double_click(self) -> None:
        pass


class WindowMouseDrive(AbstractMouse):

    def click(self) -> None:
        print("window click")
    
    def double_click(self) -> None:
        print("window double_click")


class LinuxMouseDrive(AbstractMouse):

    def click(self) -> None:
        print("linux click")
    
    def double_click(self) -> None:
        print("linux double_click")


class AbstractKeyboard:

    @abstractmethod
    def press(self) -> None:
        pass


class WindowKeyboardDrive(AbstractKeyboard):

    def press(self):
        print("press window Keyboard")


class LinuxKeyboardDrive(AbstractKeyboard):

    def press(self):
        print("press linux Keyboard")


class WindowDriveFactory(AbstractDriveFactory):
    """
    Window OS Drive factory
    """
    def create_mouse_drive(self) -> WindowMouseDrive:
        return WindowMouseDrive()

    def create_keyboard_drive(self) -> WindowKeyboardDrive:
        return WindowKeyboardDrive()


class LinuxDriveFactory(AbstractDriveFactory):
    """
    Linux OS Drive factory
    """
    def create_mouse_drive(self) -> LinuxMouseDrive:
        return LinuxMouseDrive()

    def create_keyboard_drive(self) -> LinuxKeyboardDrive:
        return LinuxKeyboardDrive()


class DriveApplication():
    
    os_drive_mapping = {
        "linux": LinuxDriveFactory,
        "window": WindowDriveFactory
    }

    def __init__(self, os_type):
        self.os_type = os_type
        self._drive = None

    def load_drive(self):
        _drive_class = self.os_drive_mapping.get(self.os_type, None)
        assert _drive_class, "os drive not found"
        self._drive = _drive_class()

    @property
    def drive(self):
        if self._drive is None:
            self.load_drive()
        return self._drive
    
    @property
    def mouse_drive(self):
        return self.drive.create_mouse_drive()
    
    @property
    def keyboard_drive(self):
        return self.drive.create_keyboard_drive()


if __name__ == "__main__":
    os_type = "linux"
    app = DriveApplication(os_type)
    app.mouse_drive.click()
    app.mouse_drive.double_click()
    app.keyboard_drive.press()

