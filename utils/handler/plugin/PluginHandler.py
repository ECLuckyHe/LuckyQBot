# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 17:32
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : PluginHandler.py
# @Software: PyCharm

import os

from utils.info.Message import Message
from utils.handler.plugin.PluginCallThread import *


class PluginHandler:
    """
    处理插件文件夹的操作相关类
    """

    @staticmethod
    def get_plugin_name_list() -> list:
        """
        获取插件列表文件

        :return: 无
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