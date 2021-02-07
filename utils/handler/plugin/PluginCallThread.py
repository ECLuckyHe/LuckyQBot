# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 18:02
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : PluginCallThread.py
# @Software: PyCharm
from threading import Thread

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