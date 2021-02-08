# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 17:32
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : PluginHandler.py
# @Software: PyCharm

import os

from utils.event.Event import Event
from utils.handler.plugin.PluginCallThread import *
from utils.constants import *


class PluginHandler:
    """
    处理插件文件夹的操作相关类
    """

    plugin_list = None

    @staticmethod
    def get_plugin_name_list() -> list:
        """
        获取插件列表文件

        :return: 插件列表名称
        """
        if PluginHandler.plugin_list is None:
            PluginHandler.plugin_list = PluginHandler.__get_plugin_name_from_file()
        return  PluginHandler.plugin_list

    @staticmethod
    def __get_plugin_name_from_file() -> list:
        """
        从文件中获取插件列表名称

        :return: 插件列表名称
        """
        # 载入插件文件夹
        try:
            import plugins
        except ModuleNotFoundError:
            # 文件夹不存在则创建文件夹
            PluginHandler.__new_folder()

        # 获取plugins目录中插件名称列表
        plugin_name_list = []

        for file_name in os.listdir("plugins"):
            if file_name.endswith(".py") and file_name != "__init__.py":
                # 去除.py后保存到新列表中
                plugin_name_list.append(file_name[:-3])

        return plugin_name_list

    @staticmethod
    def __new_folder() -> None:
        """
        创建新的插件文件夹

        :return: 无
        """

        os.mkdir("plugins")

        with open("plugins/__init__.py", "w", encoding="utf-8") as f:
            f.write("")

    @staticmethod
    def call_init() -> None:
        """
        运行插件init方法，该方法在加载时使用

        :return: 无
        """
        for plugin_name in PluginHandler.get_plugin_name_list():
            init_thread = None

            # 对每个plugin_name创建一个线程
            init_thread = InitThread(plugin_name)
            init_thread.daemon = True
            init_thread.start()

    @staticmethod
    def call_on_message(msg: Message) -> None:
        """
        执行插件内关于消息的函数

        :return: 无
        """
        for plugin_name in PluginHandler.get_plugin_name_list():

            message_thread = None
            # 每个plugin_name都创建一个线程
            if msg.is_friend_message():
                # 如果是好友消息
                message_thread = OnFriendMessageThread(plugin_name, msg)

            elif msg.is_group_message():
                # 如果是群消息
                message_thread = OnGroupMessageThread(plugin_name, msg)

            elif msg.is_temp_message():
                # 如果是临时消息
                message_thread = OnTempMessageThread(plugin_name, msg)

            message_thread.daemon = True
            message_thread.start()

    @staticmethod
    def call_on_event(event: Event):
        """
        执行插件内关于事件的函数

        :param event: 事件
        :return: 无
        """
        for plugin_name in PluginHandler.get_plugin_name_list():

            event_thread = None
            # 每个event都创建一个线程
            if event.type == BOT_ONLINE_EVENT:
                event_thread = OnBotOnlineEventThread(plugin_name, event)

            elif event.type == BOT_OFFLINE_ACTIVE_EVENT:
                event_thread = OnBotOfflineActiveEventThread(plugin_name, event)

            elif event.type == BOT_OFFLINE_FORCE_EVENT:
                event_thread = OnBotOfflineForceEventThread(plugin_name, event)

            elif event.type == BOT_OFFLINE_DROPPED_EVENT:
                event_thread = OnBotOfflineDroppedEventThread(plugin_name, event)

            elif event.type == BOT_RELOGIN_EVENT:
                event_thread = OnBotReloginEventThread(plugin_name, event)

            elif event.type == BOT_GROUP_PERMISSION_CHANGE_EVENT:
                event_thread = OnBotGroupPermissionChangeEventThread(plugin_name, event)

            elif event.type == BOT_MUTE_EVENT:
                event_thread = OnBotMuteEventThread(plugin_name, event)

            elif event.type == BOT_UNMUTE_EVENT:
                event_thread = OnBotUnmuteEventThread(plugin_name, event)

            elif event.type == BOT_JOIN_GROUP_EVENT:
                event_thread = OnBotJoinGroupEventThread(plugin_name, event)

            elif event.type == BOT_LEAVE_ACTIVE_EVENT:
                event_thread = OnBotLeaveActiveEventThread(plugin_name, event)

            elif event.type == BOT_LEAVE_KICK_EVENT:
                event_thread = OnBotLeaveKickEventThread(plugin_name, event)

            elif event.type == GROUP_RECALL_EVENT:
                event_thread = OnGroupRecallEventThread(plugin_name, event)

            elif event.type == FRIEND_RECALL_EVENT:
                event_thread = OnFriendRecallEventThread(plugin_name, event)

            elif event.type == GROUP_NAME_CHANGE_EVENT:
                event_thread = OnGroupNameChangeEventThread(plugin_name, event)

            elif event.type == GROUP_ENTRANCE_ANNOUNCEMENT_CHANGE_EVENT:
                event_thread = OnGroupEntranceAnnouncementChangeEventThread(plugin_name, event)

            elif event.type == GROUP_MUTE_ALL_EVENT:
                event_thread = OnGroupMuteAllEventThread(plugin_name, event)

            elif event.type == GROUP_ALLOW_ANONYMOUS_CHAT_EVENT:
                event_thread = OnGroupAllowAnonymousChatEventThread(plugin_name, event)

            elif event.type == GROUP_ALLOW_CONFESS_TALK_EVENT:
                event_thread = OnGroupAllowConfessTalkEventThread(plugin_name, event)

            elif event.type == GROUP_ALLOW_MEMBER_INVITE_EVENT:
                event_thread = OnGroupAllowMemberInviteEventThread(plugin_name, event)

            elif event.type == MEMBER_JOIN_EVENT:
                event_thread = OnMemberJoinEventThread(plugin_name, event)

            elif event.type == MEMBER_LEAVE_KICK_EVENT:
                event_thread = OnMemberLeaveKickEventThread(plugin_name, event)

            elif event.type == MEMBER_LEAVE_QUIT_EVENT:
                event_thread = OnMemberLeaveQuitEventThread(plugin_name, event)

            elif event.type == MEMBER_CARD_CHANGE_EVENT:
                event_thread = OnMemberCardChangeEventThread(plugin_name, event)

            elif event.type == MEMBER_SPECIAL_TITLE_CHANGE_EVENT:
                event_thread = OnMemberSpecialTitleChangeEventThread(plugin_name, event)

            elif event.type == MEMBER_PERMISSION_CHANGE_EVENT:
                event_thread = OnMemberPermissionChangeEventThread(plugin_name, event)

            elif event.type == MEMBER_MUTE_EVENT:
                event_thread = OnMemberMuteEventThread(plugin_name, event)

            elif event.type == MEMBER_UNMUTE_EVENT:
                event_thread = OnMemberUnmuteEventThread(plugin_name, event)

            elif event.type == NEW_FRIEND_REQUEST_EVENT:
                event_thread = OnNewFriendRequestEventThread(plugin_name, event)

            elif event.type == MEMBER_JOIN_REQUEST_EVENT:
                event_thread = OnMemberJoinRequestEventThread(plugin_name, event)

            elif event.type == BOT_INVITED_JOIN_GROUP_REQUEST_EVENT:
                event_thread = OnBotInvitedJoinGroupRequestEventThread(plugin_name, event)

            event_thread.daemon = True
            event_thread.start()
