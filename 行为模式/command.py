# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 命令模式: 是一种行为设计模式， 它可将请求转换为一个包含与请求相关的所有信息的独立对象，是一种数据驱动的设计模式
# 请求以命令的形式包裹在对象中，并传给调用对象。调用对象寻找可以处理该命令的合适的对象，并把该命令传给相应的对象，该对象执行命令。
# ------------------#

"""
在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系，但某些场合，比如需要对行为进行记录、撤销或重做、事务等处理时，
这种无法抵御变化的紧耦合的设计就不太合适
"""

class Command:
    """声明命令模式接口"""
    def __init__(self, obj):
        self.obj = obj

    def execute(self):
        pass


class ConcreteCommand(Command):
    """实现命令模式接口"""
    def execute(self):
        self.obj.run()


class Invoker:
    """接受命令并执行命令的接口"""
    def __init__(self):
        self._commands = []

    def add_command(self, cmd):
        self._commands.append(cmd)

    def remove_command(self, cmd):
        self._commands.remove(cmd)

    def run_command(self):
        for cmd in self._commands:
            cmd.execute()


class Receiver:
    """具体动作"""
    def __init__(self, word):
        self.word = word

    def run(self):
        print(self.word)


def client():
    """装配者"""
    test = Invoker()
    cmd1 = ConcreteCommand(Receiver('命令一'))
    test.add_command(cmd1)
    cmd2 = ConcreteCommand(Receiver('命令二'))
    test.add_command(cmd2)
    cmd3 = ConcreteCommand(Receiver('命令三'))
    test.add_command(cmd3)
    test.run_command()


if __name__ == '__main__':
    client()

