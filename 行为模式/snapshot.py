# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 备忘录模式: 是一种行为设计模式， 允许在不暴露对象实现细节的情况下保存和恢复对象之前的状态。
# ------------------#

"""
很多时候我们总是需要记录一个对象的内部状态，这样做的目的就是为了允许用户取消不确定或者错误的操作，
能够恢复到他原先的状态，使得他有"后悔药"可吃。这个模式主要是用来防丢失、撤销、恢复等。
备忘录模式最常见的场景如下所示:
    1.浏览器回退
    2.数据库备份与还原
    3.编辑器撤销与重做
    4.虚拟机生成快照与恢复
    5.Git版本管理
    6.棋牌游戏悔棋
"""


# 备忘录类
class StatusMemento:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 发起人类，象棋棋子
class ChessPoint:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    @property
    def position(self):
        return f"{self.name} --- <{self.x}, {self.y}> "
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def save(self) -> StatusMemento:
        return StatusMemento(self.x, self.y)
    
    def recover(self, status: StatusMemento) -> None:
        self.x = status.x
        self.y = status.y


class MementoCaretaker:

    def __init__(self, chese: ChessPoint) -> None:
        self._history = []
        self._chese = chese
    
    def backup(self) -> None:
        self._history.append(self._chese.save())
    
    def undo(self) -> None:
        if not len(self._history):
            return
        
        memento = self._history.pop()
        try:
            self._chese.recover(memento)
        except Exception:
            self.undo()
    
    

class Application:

    def run(self):
        chese = ChessPoint("車", 1, 1)
        memento_caretaker = MementoCaretaker(chese)
        print("初始位置: ", chese.position)

        memento_caretaker.backup()
        chese.move(5,6)
        print("移动到5,6: ",chese.position)

        memento_caretaker.backup()
        chese.move(10,10)
        print("移动到10,10: ",chese.position)
        
        memento_caretaker.undo()  # 悔棋
        print("悔棋到上一步: ", chese.position)


Application().run()

# output
"""
初始位置:  車 --- <1, 1> 
移动到5,6:  車 --- <5, 6> 
移动到10,10:  車 --- <10, 10> 
悔棋到上一步:  車 --- <5, 6> 
"""