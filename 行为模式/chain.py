# !/usr/bin/env python 
# -*- coding: utf-8 -*-

# ------------------#
# 责任链模式（职责链模式、命令链）: 是一种行为设计模式， 允许你将请求沿着处理者链进行发送。 
# 收到请求后， 每个处理者均可对请求进行处理， 或将其传递给链上的下个处理者。
# ------------------#

"""
责任链模式 -- 用于让多个对象处理一个请求时，或者用于预先不知道由哪个对象来处理某种特定请求时，其原则如下:
    1、存在一个对象链（链表、树或者其他便捷的数据结构）。
    2、一开始将请求发送给第一个对象，让其处理。
    3、对象决定是否处理该请求。
    4、对象将请求转发给下一个对象。
    5、重复该过程，直到达到链尾。

责任链模式的最佳场景就是: 请假审批流程,
例如某学校的请求审批规则是: 
    1、请假1～3天（班主任）审批
    2、请假3~7天（班主任 + 年级主任）审批
    3、请假大于7天（班主任 + 年级主任 + 校长）审批
"""

from abc import abstractmethod


class BaseHandler:

    def __init__(self):
         self.next_handle = None

    def set_next_handle(self, handler: 'BaseHandler') -> None:
        self.next_handle = handler
    
    def get_next_handle(self) -> 'BaseHandler':
        return self.next_handle
    
    @abstractmethod
    def handle(self):
        raise NotImplementedError('`handle()` must be implemented.')


class HeadTeacher(BaseHandler):

    def handle(self, holiday: int):
        if holiday <= 3:
            print("当前审批人: 班主任, 审批意见: 通过，同意请假")
            return None
        next_handle = self.get_next_handle()
        assert next_handle, "出现异常，没有设置下一步处理人， 当前环节: 班主任审批"
        print("当前审批人: 班主任, 审批意见: 通过， 请上级领导进行审批")
        next_handle.handle(holiday)


class GradeDeanTeacher(BaseHandler):

    def handle(self, holiday: int):
        if holiday <= 7:
            print("当前审批人: 年级主任, 审批意见: 通过，同意请假")
            return None
        next_handle = self.get_next_handle()
        assert next_handle, "出现异常，没有设置下一步处理人， 当前环节: 年级主任审批"
        print("当前审批人: 年级主任, 审批意见: 通过， 请上级领导进行审批")
        next_handle.handle(holiday)


class HeadMasterTeacher(BaseHandler):

    def handle(self, holiday: int):
        print("当前审批人: 校长, 审批意见: 通过，同意请假")


class Application:

    def run(self):

        holiday = 6
        print(f"请假天数: {holiday}")
        first_handler = HeadTeacher()
        grade_dean = GradeDeanTeacher()
        head_master = HeadMasterTeacher()
        first_handler.set_next_handle(grade_dean)
        grade_dean.set_next_handle(head_master)
        first_handler.handle(holiday)


Application().run()

# output
"""
请假天数: 6
当前审批人: 班主任, 审批意见: 通过， 请上级领导进行审批
当前审批人: 年级主任, 审批意见: 通过，同意请假
"""