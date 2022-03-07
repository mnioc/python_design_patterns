# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 外观模式（过程模式）: 是一种结构型设计模式, 能为程序库、 框架或其他复杂类提供一个简单的接口。
# 有助于隐藏系统的内部复杂性，并且通过一个简化的接口向客户端暴露必要的部分。本质上，外观是在已有复杂系统之上实现的一个抽象层
# ------------------#

"""
主要用于以下场景:
    1、为复杂的模块或子系统提供外界访问的模块。
    2、子系统相对独立。
    3、预防低水平人员带来的风险

例如: 我们要实现一个运维故障报警系统, 该系统有几个子系统组成
    1、监控产生告警
    2、发送告警通知邮件
    3、根据故障类型自动执行脚本
"""

class Alarm:

    def create_alarm(self):
        alarm_text = "xxx系统出现异常，请尽快处理"
        print(alarm_text)
        return alarm_text


class EmailSender:

    def send_email(self, msg, to_user):
        print(f"发送邮件: {msg} 给 {to_user}")


class AutomaticScript:

    def process(self):
        print("开始自动处理故障..")


class Facade:

    def operation(self):
        alarm_text = Alarm().create_alarm()
        EmailSender().send_email(alarm_text, "系统运维工程师")
        AutomaticScript().process()


class Application:

    def run(self):
        Facade().operation()


Application().run()

# output
"""
xxx系统出现异常，请尽快处理
发送邮件: xxx系统出现异常，请尽快处理 给 系统运维工程师
开始自动处理故障..
"""