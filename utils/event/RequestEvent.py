# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 20:04
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : RequestEvent.py
# @Software: PyCharm
from utils.event.Event import Event
from utils.constants import *


class NewFriendRequestEvent(Event):
    """
    添加好友申请
    """

    def __init__(
            self,
            event_id: int,
            from_qq: int,
            group_id: int,
            nick: str,
            message: str
    ):
        """
        构造方法

        :param event_id: 事件id，响应时用其标识
        :param from_qq: 申请人qq
        :param group_id: 申请人如果通过某个群加好友，则该项为群号，否则为0
        :param nick: 申请人的昵称或群名片
        :param message: 申请消息
        """
        Event.__init__(self)
        self.type = NEW_FRIEND_REQUEST_EVENT
        self.event_id = event_id
        self.from_qq = from_qq
        self.group_id = group_id
        self.nick = nick
        self.message =message


class MemberJoinRequestEvent(Event):
    """
    用户入群申请（Bot需要有管理员权限）
    """

    def __init__(
            self,
            event_id: int,
            from_qq: int,
            group_id: int,
            group_name: str,
            nick: str,
            message: str
    ):
        """
        构造方法

        :param event_id: 事件号
        :param from_qq: 申请人qq
        :param group_id: 申请进入的群号
        :param group_name: 群名称
        :param nick: 申请人昵称或群名片
        :param message: 申请消息
        :return:
        """
        Event.__init__(self)
        self.type = MEMBER_JOIN_REQUEST_EVENT
        self.event_id = event_id
        self.from_qq = from_qq
        self.group_id = group_id
        self.group_name = group_name
        self.nick = nick
        self.message = message


class BotInvitedJoinGroupRequestEvent(Event):
    """
    Bot被邀请入群申请
    """

    def __init__(
            self,
            event_id: int,
            from_qq: int,
            group_id: int,
            group_name: str,
            nick: str,
            message: str
    ):
        """
        构造方法

        :param event_id: 事件号
        :param from_qq: 邀请人qq
        :param group_id: 被邀请进入的群号
        :param group_name: 被邀请进入的群名
        :param nick: 邀请人昵称
        :param message: 邀请消息
        """
        Event.__init__(self)
        self.type = BOT_INVITED_JOIN_GROUP_REQUEST_EVENT
        self.event_id = event_id
        self.from_qq = from_qq
        self.group_id = group_id
        self.group_name = group_name
        self.nick = nick
        self.message = message
