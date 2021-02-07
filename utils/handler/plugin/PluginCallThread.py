# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 18:02
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : PluginCallThread.py
# @Software: PyCharm
from threading import Thread

from utils.event.Event import Event
from utils.info.Message import Message
from utils.connect.Conn import Conn


class OnFriendMessageThread(Thread):
    """
    收到的消息为好友消息时调用
    """
    def __init__(
            self,
            plugin_name: str,
            msg: Message
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param msg: 消息对象
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.msg = msg

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_friend_message(self.msg, Conn)")
        except AttributeError:
            pass


class OnGroupMessageThread(Thread):
    """
    收到的消息为群消息时调用
    """
    def __init__(
            self,
            plugin_name: str,
            msg: Message
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param msg: 消息对象
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.msg = msg

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_message(self.msg, Conn)")
        except AttributeError:
            pass


class OnTempMessageThread(Thread):
    """
    收到的消息为临时消息时调用
    """
    def __init__(
            self,
            plugin_name: str,
            msg: Message
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param msg: 消息对象
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.msg = msg

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_temp_message(self.msg, Conn)")
        except AttributeError:
            pass


class OnBotOnlineEventThread(Thread):
    """
    Bot登录成功调用
    """
    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_online_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotOfflineActiveEventThread(Thread):
    """
    Bot主动离线调用
    """
    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_offline_active_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotOfflineForceEventThread(Thread):
    """
    Bot被挤下线事件
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_offline_force_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotOfflineDroppedEventThread(Thread):
    """
    Bot被服务器断开或因网络问题而掉线调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_offline_dropped_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotReloginEventThread(Thread):
    """
    Bot主动重新登录调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_relogin_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotGroupPermissionChangeEventThread(Thread):
    """
    Bot在群里的权限被改变. 操作人一定是群主 调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_group_permission_change_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotMuteEventThread(Thread):
    """
    Bot被禁言调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_mute_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotUnmuteEventThread(Thread):
    """
    Bot被取消禁言调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_unmute_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotJoinGroupEventThread(Thread):
    """
    Bot加入了一个新群调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_join_group_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotLeaveActiveEventThread(Thread):
    """
    Bot主动退出一个群调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_leave_active_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotLeaveKickEventThread(Thread):
    """
    Bot被踢出一个群调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_leave_kick_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupRecallEventThread(Thread):
    """
    群消息撤回调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_recall_event(self.event, Conn)")
        except AttributeError:
            pass


class OnFriendRecallEventThread(Thread):
    """
    好友消息撤回调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_friend_recall_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupNameChangeEventThread(Thread):
    """
    某个群名改变调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_name_change_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupEntranceAnnouncementChangeEventThread(Thread):
    """
    某群入群公告改变调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_entrance_announcement_change_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupMuteAllEventThread(Thread):
    """
    全员禁言调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_mute_all_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupAllowAnonymousChatEventThread(Thread):
    """
    匿名聊天更改调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_allow_anonymous_chat_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupAllowConfessTalkEventThread(Thread):
    """
    坦白说更改调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_allow_confess_talk_event(self.event, Conn)")
        except AttributeError:
            pass


class OnGroupAllowMemberInviteEventThread(Thread):
    """
    允许群成员邀请好友加群调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_group_allow_member_invite_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberJoinEventThread(Thread):
    """
    新人入群的事件调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_join_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberLeaveKickEventThread(Thread):
    """
    成员被踢出群（不是bot）调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_leave_kick_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberLeaveQuitEventThread(Thread):
    """
    成员主动离群（不是bot）调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_leave_quit_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberCardChangeEventThread(Thread):
    """
    群名片改动调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_card_change_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberSpecialTitleChangeEventThread(Thread):
    """
    群头衔改动调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_special_title_change_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberPermissionChangeEventThread(Thread):
    """
    群头衔改动（不是bot）调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_permission_change_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberMuteEventThread(Thread):
    """
    群成员被禁言（不是bot）调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_mute_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberUnmuteEventThread(Thread):
    """
    群成员被取消禁言（不是bot）调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_unmute_event(self.event, Conn)")
        except AttributeError:
            pass


class OnNewFriendRequestEventThread(Thread):
    """
    添加好友申请调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_new_friend_request_event(self.event, Conn)")
        except AttributeError:
            pass


class OnMemberJoinRequestEventThread(Thread):
    """
    用户入群申请（Bot需要有管理员权限）调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_member_join_request_event(self.event, Conn)")
        except AttributeError:
            pass


class OnBotInvitedJoinGroupRequestEventThread(Thread):
    """
    Bot被邀请入群申请调用
    """

    def __init__(
            self,
            plugin_name: str,
            event: Event
    ):
        """
        构造方法

        :param plugin_name: 插件名
        :param event: 事件
        """
        Thread.__init__(self)
        self.plugin_name = plugin_name
        self.event = event

    def run(self):
        exec("from plugins import " + self.plugin_name)
        try:
            exec(self.plugin_name + ".on_bot_invited_join_group_request_event(self.event, Conn)")
        except AttributeError:
            pass


