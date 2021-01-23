# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 17:53
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : RecallEvent.py
# @Software: PyCharm
from utils.event.Event import Event
from utils.info.Group import Group
from utils.info.Member import Member
from utils.constants import *


class GroupRecallEvent(Event):
    """
    群消息撤回
    """

    def __init__(
            self,
            author_id: int,
            message_id: int,
            time: int,
            group: Group,
            operator: Member
    ):
        """
        构造方法

        :param author_id: 原消息发送者的QQ号
        :param message_id: 原消息id
        :param time: 原消息发送时间
        :param group: 消息撤回所在的群
        :param operator: 撤回消息的操作人，为null的时候表示bot本身
        """
        Event.__init__(self)
        self.type = GROUP_RECALL_EVENT
        self.author_id = author_id
        self.message_id = message_id
        self.time = time
        self.group = group
        self.operator = operator


class FriendRecallEvent(Event):
    """
    好友消息撤回
    """

    def __init__(
            self,
            author_id: int,
            message_id: int,
            time: int,
            operator_qq: int
    ):
        """
        构造方法

        :param author_id: 原消息发送者qq
        :param message_id: 原消息id
        :param time: 原消息发送时间
        :param operator_qq: 好友qq或者botqq（？？？原文档是这么写的啊）
        """
        Event.__init__(self)
        self.type = FRIEND_RECALL_EVENT
        self.author_id = author_id
        self.message_id = message_id
        self.time = time
        self.operator_qq = operator_qq