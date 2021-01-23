# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 11:05
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : BotSelfEvent.py
# @Software: PyCharm
from utils.event.Event import Event
from utils.constants import *
from utils.info.Group import Group
from utils.info.Member import Member


class BotOnlineEvent(Event):
    """
    Bot登陆成功事件
    """

    def __init__(self, qq: int):
        """
        构造方法

        :param qq: 登陆成功的Bot的QQ号
        """
        Event.__init__(self)
        self.type = BOT_ONLINE_EVENT
        self.qq = qq


class BotOfflineActiveEvent(Event):
    """
    Bot主动离线事件
    """

    def __init__(self, qq: int):
        """
        构造方法

        :param qq: 主动离线的QQ号
        """
        Event.__init__(self)
        self.type = BOT_OFFLINE_ACTIVE_EVENT
        self.qq = qq


class BotOfflineForceEvent(Event):
    """
    Bot被挤下线
    """

    def __init__(self, qq: int):
        """
        构造方法

        :param qq: 被挤下线的QQ号
        """
        Event.__init__(self),
        self.type = BOT_OFFLINE_FORCE_EVENT
        self.qq = qq


class BotOfflineDroppedEvent(Event):
    """
    Bot被服务器断开或因网络问题而掉线
    """

    def __init__(self, qq: int):
        """
        构造方法

        :param qq: 被服务器断开或因网络问题而掉线的Bot的QQ号
        """
        Event.__init__(self)
        self.type = BOT_OFFLINE_DROPPED_EVENT
        self.qq = qq


class BotReloginEvent(Event):
    """
    Bot主动重新登录
    """

    def __init__(self, qq: int):
        """
        构造方法

        :param qq: 主动重新登录的Bot的QQ
        """
        Event.__init__(self)
        self.type = BOT_RELOGIN_EVENT
        self.qq = qq


class BotGroupPermissionChangeEvent(Event):
    """
    Bot在群里的权限被改变，操作人一定是群主
    """

    def __init__(
            self,
            origin: str,
            new: str,
            current: str,
            group: Group
    ):
        """
        构造方法

        :param origin: Bot的原权限
        :param new: Bot的新权限
        :param current: Bot的新权限
        :param group: 群信息对象
        """
        Event.__init__(self)
        self.type = BOT_GROUP_PERMISSION_CHANGE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group


class BotMuteEvent(Event):
    """
    Bot被禁言
    """

    def __init__(
            self,
            duration_seconds: int,
            operator: Member
    ):
        """
        构造方法

        :param duration_seconds: 禁言时间
        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = BOT_MUTE_EVENT
        self.duration_seconds = duration_seconds
        self.operator = operator


class BotUnmuteEvent(Event):
    """
    Bot被取消禁言
    """

    def __init__(
            self,
            operator: Member
    ):
        """
        构造方法

        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = BOT_UNMUTE_EVENT
        self.operator = operator


class BotJoinGroupEvent(Event):
    """
    Bot加入了一个新群
    """

    def __init__(
            self,
            group: Group
    ):
        """
        构造方法
        :param group: 群号
        :param group_name: 群名
        :param group_permission: Bot在群中的权限
        """
        Event.__init__(self)
        self.type = BOT_JOIN_GROUP_EVENT
        self.group = group


class BotLeaveActiveEvent(Event):
    """
    Bot主动退出一个群
    """

    def __init__(
            self,
            group: Group
    ):
        """
        构造方法

        :param group: 群信息
        """
        Event.__init__(self)
        self.type = BOT_LEAVE_ACTIVE_EVENT
        self.group = group


class BotLeaveKickEvent(Event):
    """
    Bot被踢出一个群
    """

    def __init__(
            self,
            group: Group
    ):
        """
        构造方法

        :param group: 群信息
        """
        Event.__init__(self)
        self.type = BOT_LEAVE_KICK_EVENT
        self.group = group