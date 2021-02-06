# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:47
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Message.py
# @Software: PyCharm

from utils.constants import *
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

        # 下面构建sender，由于sender类型有很多，因此需要单独处理
        sender = msg_data["sender"]

        # 如果是群消息和临时消息，则sender为Member类型
        if self.type in [GROUP_MSG, TEMP_MSG]:
            self.sender = Member(
                sender["id"],
                sender["memberName"],
                sender["permission"],
                Group(
                    sender["group"]["id"],
                    sender["group"]["name"],
                    sender["group"]["permission"]
                )
            )

        # 如果是好友消息，则类型为Friend
        if self.type == FRIEND_MSG:
            self.sender = Friend(
                sender["id"],
                sender["nickname"],
                sender["remark"]
            )

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

