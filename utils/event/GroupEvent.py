# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 18:17
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : GroupEvent.py
# @Software: PyCharm
from utils.event.Event import Event
from utils.info.Group import Group
from utils.info.Member import Member
from utils.constants import *


class GroupNameChangeEvent(Event):
    """
    某个群名改变
    """

    def __init__(
            self,
            origin: str,
            new: str,
            current: str,
            group: Group,
            operator: Member
    ):
        """
        构造方法

        :param origin: 原群名
        :param new: 新群名
        :param current: 新群名
        :param group: 改名的群信息
        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = GROUP_NAME_CHANGE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group
        self.operator = operator


class GroupEntranceAnnouncementChangeEvent(Event):
    """
    某群入群公告改变
    """

    def __init__(
            self,
            origin: str,
            new: str,
            current: str,
            group: Group,
            operator: Member
    ):
        """
        构造方法

        :param origin: 原公告
        :param new: 新公告
        :param current: 新公告
        :param group: 公告改变的群信息
        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = GROUP_ENTRANCE_ANNOUNCEMENT_CHANGE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group
        self.operator = operator


class GroupMuteAllEvent(Event):
    """
    全员禁言
    """

    def __init__(
            self,
            origin: bool,
            new: bool,
            current: bool,
            group: Group,
            operator: Member
    ):
        """
        构造方法

        :param origin: 原本是否处于全员禁言
        :param new: 现在是否处于全员禁言
        :param current: 现在是否处于全员禁言
        :param group: 群信息
        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = GROUP_MUTE_ALL_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group
        self.operator = operator


class GroupAllowAnonymousChatEvent(Event):
    """
    匿名聊天修改
    """

    def __init__(
            self,
            origin: bool,
            new: bool,
            current: bool,
            group: Group,
            operator: Member
    ):
        """
        构造方法

        :param origin: 原本匿名聊天是否开启
        :param new: 现在匿名聊天是否开启
        :param current: 现在匿名聊天是否开启
        :param group: 群信息
        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = GROUP_ALLOW_ANONYMOUS_CHAT_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group
        self.operator = operator


class GroupAllowConfessTalkEvent(Event):
    """
    坦白说修改
    """

    def __init__(
            self,
            origin: bool,
            new: bool,
            current: bool,
            group: Group,
            is_by_bot: bool
    ):
        """
        构造方法

        :param origin: 原本坦白说是否开启
        :param new: 现在坦白说是否开启
        :param current: 现在坦白说是否开启
        :param group: 群消息
        :param is_by_bot: 是否bot进行该操作
        """
        Event.__init__(self)
        self.type = GROUP_ALLOW_CONFESS_TALK_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group
        self.is_by_bot = is_by_bot


class GroupAllowMemberInviteEvent(Event):
    """
    允许群成员邀请好友加群
    """

    def __init__(
            self,
            origin: bool,
            new: bool,
            current: bool,
            group: Group,
            operator: Member
    ):
        """
        构造方法

        :param origin: 原本是否允许群员邀请好友加群
        :param new: 现在是否允许
        :param current: 现在是否允许
        :param group: 群信息
        :param operator: 操作者信息
        """
        Event.__init__(self)
        self.type = GROUP_ALLOW_MEMBER_INVITE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.group = group
        self.operator = operator


class MemberJoinEvent(Event):
    """
    新人入群
    """

    def __init__(
            self,
            member: Member
    ):
        """
        构造方法

        :param member: 新成员信息
        """
        Event.__init__(self)
        self.type = MEMBER_JOIN_EVENT
        self.member = member


class MemberLeaveKickEvent(Event):
    """
    成员被踢出群（不是bot）
    """

    def __init__(
            self,
            member: Member,
            operator: Member
    ):
        """
        构造方法

        :param member: 被踢成员
        :param operator: 操作成员
        """
        Event.__init__(self)
        self.type = MEMBER_LEAVE_KICK_EVENT
        self.member = member
        self.operator = operator


class MemberLeaveQuitEvent(Event):
    """
    成员主动离群（不是bot）
    """

    def __init__(
            self,
            member: Member
    ):
        """
        构造方法

        :param member: 成员
        """
        Event.__init__(self)
        self.type = MEMBER_LEAVE_QUIT_EVENT
        self.member = member


class MemberCardChangeEvent(Event):
    """
    群名片改动
    """

    def __init__(
            self,
            origin: str,
            new: str,
            current: str,
            member: Member,
            operator: Member
    ):
        """
        构造方法

        :param origin: 原来的群名片
        :param new: 新的群名片
        :param current: 新的群名片
        :param member: 被操作者信息
        :param operator: 操作者信息，可以是自己也可以是管理，为null时表示bot
        """
        Event.__init__(self)
        self.type = MEMBER_CARD_CHANGE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.member = member
        self.operator = operator


class MemberSpecialTitleChangeEvent(Event):
    """
    群头衔改动（只有群主可以操作）
    """

    def __init__(
            self,
            origin: str,
            new: str,
            current: str,
            member: Member
    ):
        """
        构造方法

        :param origin: 原头衔
        :param new: 现头衔
        :param current: 现头衔
        :param member: 被改动的成员信息
        """
        Event.__init__(self)
        self.type = MEMBER_SPECIAL_TITLE_CHANGE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.member = member


class MemberPermissionChangeEvent(Event):
    """
    成员权限改变的事件（该成员不是bot）
    """

    def __init__(
            self,
            origin: str,
            new: str,
            current: str,
            member: Member
    ):
        """
        构造方法

        :param origin: 原权限
        :param new: 新权限
        :param current: 新权限
        :param member: 被操作成员信息
        """
        Event.__init__(self)
        self.type = MEMBER_PERMISSION_CHANGE_EVENT
        self.origin = origin
        self.new = new
        self.current = current
        self.member = member


class MemberMuteEvent(Event):
    """
    群成员被禁言事件（该成员不是bot）
    """

    def __init__(
            self,
            duration_seconds: int,
            member: Member,
            operator: Member
    ):
        """
        构造方法

        :param duration_seconds: 禁言时间，单位为秒
        :param member: 被禁成员
        :param operator: 操作者，为null为bot操作
        """
        Event.__init__(self)
        self.type = MEMBER_MUTE_EVENT
        self.duration_seconds = duration_seconds
        self.member = member
        self.operator = operator


class MemberUnmuteEvent(Event):
    """
    群成员被取消禁言事件（不是bot）
    """

    def __init__(
            self,
            member: Member,
            operator: Member
    ):
        """
        构造方法

        :param member: 被操作者信息
        :param operator: 操作者信息，为null表示bot
        """
        Event.__init__(self)
        self.type = MEMBER_UNMUTE_EVENT
        self.member = member
        self.operator = operator
