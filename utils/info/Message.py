# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:47
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Message.py
# @Software: PyCharm
from utils.GlobalValues import GlobalValues
from utils.api.MessageChain import MessageChain
from utils.connect.Conn import Conn
from utils.constants import *
from utils.gui.operation.OpListOperation import OpListOperation
from utils.info.Friend import Friend
from utils.info.Group import Group
from utils.info.Member import Member


class Message:
    """
    接收到的消息对象
    """

    def __init__(
            self,
            msg_data: dict
    ):
        """
        构造方法

        :param msg_data: 获取到的message data
        """
        self.type = msg_data["type"]
        self.message_chain = msg_data["messageChain"][1:]

        # 由于获取到的消息中message_chain中的第0项不是消息内容，所以要对该项处理
        source_info = msg_data["messageChain"][0]

        self.message_id = source_info["id"]

        # time为时间戳
        self.time = source_info["time"]

        # 下面构建sender，由于sender类型有多种，因此需要单独处理
        sender = msg_data["sender"]

        # 是否为指令
        if self.get_plain_text().startswith(GlobalValues.command_head):
            self.is_command = True
        else:
            self.is_command = False

        # 存储指令头
        self.command_head = GlobalValues.command_head

        # 如果是群消息和临时消息，则创建sender_member
        if self.type in [GROUP_MSG, TEMP_MSG]:
            self.sender_member = Member(
                sender["id"],
                sender["memberName"],
                sender["permission"],
                Group(
                    sender["group"]["id"],
                    sender["group"]["name"],
                    sender["group"]["permission"]
                )
            )

            # 是否为bot op
            if self.sender_member.qq in OpListOperation.get_list():
                self.is_op = True
            else:
                self.is_op = False

        # 如果是好友消息，则创建sender_friend
        if self.type == FRIEND_MSG:
            self.sender_friend = Friend(
                sender["id"],
                sender["nickname"],
                sender["remark"]
            )

            # 是否为bot op
            if self.sender_friend.qq in OpListOperation.get_list():
                self.is_op = True
            else:
                self.is_op = False

    def is_group_message(self) -> bool:
        """
        是否为群消息

        :return: 布尔值
        """
        return True if self.type == GROUP_MSG else False

    def is_temp_message(self) -> bool:
        """
        是否为临时消息

        :return: 布尔值
        """
        return True if self.type == TEMP_MSG else False

    def is_friend_message(self) -> bool:
        """
        是否为好友消息

        :return: 布尔值
        """
        return True if self.type == FRIEND_MSG else False

    def get_plain_text(self) -> str:
        """
        获取纯文本（即去除本文以外的内容并返回文本内容）

        :return: 文本内容
        """

        text = ""

        for one in self.message_chain:
            if one["type"] == "Plain":
                text += one["text"]

        return text

    def send_message_back(self, message_chain: MessageChain) -> None:
        """
        原路发送消息（接收到的消息从哪里来就往哪里发）

        :param message_chain: 消息内容chain
        :return: 无
        """
        if self.is_group_message():
            Conn.send_group_message(self.sender_member.group.id, message_chain)

        if self.is_temp_message():
            Conn.send_temp_message(
                self.sender_member.qq,
                self.sender_member.group.id,
                message_chain
            )

        if self.is_friend_message():
            Conn.send_friend_message(self.sender_friend.qq, message_chain)