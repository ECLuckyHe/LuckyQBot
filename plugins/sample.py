# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 17:44
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : sample.py.py
# @Software: PyCharm

from utils.api.MessageChain import MessageChain


def on_friend_message(msg, Conn):
    if msg.get_plain_text() == "lucky好帅":
        mc = MessageChain()
        mc.add_plain_text("你也好帅！")
        msg.send_message_back(mc)


def on_group_message(msg, Conn):
    if msg.get_plain_text() == "lucky好帅":
        mc = MessageChain()
        mc.add_plain_text("你们也好帅！")
        msg.send_message_back(mc)


def on_temp_message(msg, Conn):
    if msg.get_plain_text() == "lucky好帅":
        mc = MessageChain()
        mc.add_plain_text("你也很帅！")
        msg.send_message_back(mc)


def on_bot_leave_kick_event(event, Conn):
    print()