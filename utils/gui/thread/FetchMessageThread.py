# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 23:43
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : FetchMessageThread.py
# @Software: PyCharm
import time
from threading import Thread

from utils.GlobalValues import GlobalValues
from utils.connect.Conn import Conn
from utils.event.BotSelfEvent import *
from utils.event.RecallEvent import *
from utils.event.GroupEvent import *
from utils.event.RequestEvent import *
from utils.event.Event import Event
from utils.handler.plugin.PluginHandler import PluginHandler
from utils.constants import *
from utils.info.Group import Group
from utils.info.Member import Member

from utils.info.Message import Message


class FetchMessageThread(Thread):
    """
    获取消息并分析，交给插件处理

    默认为1s获取一次
    """

    data = None

    def run(self):
        while True:
            time.sleep(1)

            # 如果未连接，则不接收消息
            if not GlobalValues.is_connected:
                continue

            # 如果未启用，则不接受消息
            if not GlobalValues.enable_var.get():
                continue

            # 获取消息数据
            # 同时处理可能出现的异常，直接忽略
            try:
                data_list = Conn.fetch_message(1)["data"]
            except Exception as e:
                # 捕捉到异常后打印并重新循环
                print(e)
                continue

            # 获取到的列表为空
            if not data_list:
                continue

            # 获取数据
            self.data = data_list[0]
            data_type = self.data["type"]

            if data_type.endswith("Message"):
                # 判断为消息再读取
                msg = Message(self.data)

                # 调用执行插件内容
                PluginHandler.call_on_message(msg)

            elif data_type.find("Event") != -1:
                try:
                    event = self.get_event()
                except TypeError as e:
                    # 20210209更新
                    # 此处有时会抛出TypeError，怀疑是mirai http本身问题
                    print(str(e))
                    continue

                # 调用执行插件内容
                PluginHandler.call_on_event(event)

    def get_event(self) -> Event:
        """
        获取事件内容并创建对应对象

        :return: 事件对象
        """

        data = self.data
        event_type = data["type"]

        # 对每种事件创建对象

        # bot自身事件
        if event_type == BOT_ONLINE_EVENT:
            return BotOnlineEvent(data["qq"])

        if event_type == BOT_OFFLINE_ACTIVE_EVENT:
            return BotOfflineActiveEvent(data["qq"])

        if event_type == BOT_OFFLINE_FORCE_EVENT:
            return BotOfflineForceEvent(data["qq"])

        if event_type == BOT_OFFLINE_DROPPED_EVENT:
            return BotOfflineDroppedEvent(data["qq"])

        if event_type == BOT_RELOGIN_EVENT:
            return BotReloginEvent(data["qq"])

        if event_type == BOT_GROUP_PERMISSION_CHANGE_EVENT:
            group = data["group"]
            return BotGroupPermissionChangeEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                )
            )

        if event_type == BOT_MUTE_EVENT:
            operator = data["operator"]
            group = operator["group"]
            return BotMuteEvent(
                data["durationSeconds"],
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        group["id"],
                        group["name"],
                        group["permission"]
                    )
                )
            )

        if event_type == BOT_UNMUTE_EVENT:
            operator = data["operator"]
            group = operator["group"]
            return BotUnmuteEvent(
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        group["id"],
                        group["name"],
                        group["permission"]
                    )
                )
            )

        if event_type == BOT_JOIN_GROUP_EVENT:
            group = data["group"]
            return BotJoinGroupEvent(
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                )
            )

        if event_type == BOT_LEAVE_ACTIVE_EVENT:
            group = data["group"]
            return BotLeaveActiveEvent(
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                )
            )

        if event_type == BOT_LEAVE_KICK_EVENT:
            group = data["group"]
            return BotLeaveKickEvent(
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                )
            )

        # 消息撤回事件
        if event_type == GROUP_RECALL_EVENT:
            group = data["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return GroupRecallEvent(
                data["authorId"],
                data["messageId"],
                data["time"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == FRIEND_RECALL_EVENT:
            return FriendRecallEvent(
                data["authorId"],
                data["messageId"],
                data["time"],
                data["operator"]
            )

        # 群事件
        if event_type == GROUP_NAME_CHANGE_EVENT:
            group = data["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return GroupNameChangeEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == GROUP_ENTRANCE_ANNOUNCEMENT_CHANGE_EVENT:
            group = data["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return GroupEntranceAnnouncementChangeEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == GROUP_MUTE_ALL_EVENT:
            group = data["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return GroupMuteAllEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == GROUP_ALLOW_ANONYMOUS_CHAT_EVENT:
            group = data["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return GroupAllowAnonymousChatEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == GROUP_ALLOW_CONFESS_TALK_EVENT:
            group = data["group"]
            return GroupAllowConfessTalkEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                data["isByBot"]
            )

        if event_type == GROUP_ALLOW_MEMBER_INVITE_EVENT:
            group = data["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return GroupAllowMemberInviteEvent(
                data["origin"],
                data["new"],
                data["current"],
                Group(
                    group["id"],
                    group["name"],
                    group["permission"]
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_JOIN_EVENT:
            member = data["member"]
            member_group = member["group"]
            return MemberJoinEvent(
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_LEAVE_KICK_EVENT:
            member = data["member"]
            member_group = member["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return MemberLeaveKickEvent(
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_LEAVE_QUIT_EVENT:
            member = data["member"]
            member_group = member["group"]
            return MemberLeaveQuitEvent(
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_CARD_CHANGE_EVENT:
            member = data["member"]
            member_group = member["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return MemberCardChangeEvent(
                data["origin"],
                data["new"],
                data["current"],
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_SPECIAL_TITLE_CHANGE_EVENT:
            member = data["member"]
            member_group = member["group"]
            return MemberSpecialTitleChangeEvent(
                data["origin"],
                data["new"],
                data["current"],
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_PERMISSION_CHANGE_EVENT:
            member = data["member"]
            member_group = member["group"]
            return MemberPermissionChangeEvent(
                data["origin"],
                data["new"],
                data["current"],
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_MUTE_EVENT:
            member = data["member"]
            member_group = member["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return MemberMuteEvent(
                data["durationSeconds"],
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        if event_type == MEMBER_UNMUTE_EVENT:
            member = data["member"]
            member_group = member["group"]
            operator = data["operator"]
            operator_group = operator["group"]
            return MemberUnmuteEvent(
                Member(
                    member["id"],
                    member["memberName"],
                    member["permission"],
                    Group(
                        member_group["id"],
                        member_group["name"],
                        member_group["permission"]
                    )
                ),
                Member(
                    operator["id"],
                    operator["memberName"],
                    operator["permission"],
                    Group(
                        operator_group["id"],
                        operator_group["name"],
                        operator_group["permission"]
                    )
                )
            )

        # 申请事件
        if event_type == NEW_FRIEND_REQUEST_EVENT:
            return NewFriendRequestEvent(
                data["eventId"],
                data["fromId"],
                data["groupId"],
                data["nick"],
                data["message"]
            )

        if event_type == MEMBER_JOIN_REQUEST_EVENT:
            return MemberJoinRequestEvent(
                data["eventId"],
                data["fromId"],
                data["groupId"],
                data["groupName"],
                data["nick"],
                data["message"]
            )

        if event_type == BOT_INVITED_JOIN_GROUP_REQUEST_EVENT:
            return BotInvitedJoinGroupRequestEvent(
                data["eventId"],
                data["fromId"],
                data["groupId"],
                data["groupName"],
                data["nick"],
                data["message"]
            )
