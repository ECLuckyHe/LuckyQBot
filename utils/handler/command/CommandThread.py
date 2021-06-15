# -*- coding: utf-8 -*-
# @Time    : 2021年3月12日 19:17
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : CommandThread.py
# @Software: PyCharm
import os
import sys
from threading import Thread

from utils.GlobalValues import GlobalValues
from utils.gui.operation.ConfigOperation import ConfigOperation
from utils.gui.thread.FetchMessageThread import FetchMessageThread
from utils.handler.command.CommandHandler import CommandHandler
from utils.constants import *
import re


class CommandThread(Thread):
    """
    指令进程，负责操作控制台输入的内容
    """

    def run(self):

        # 开始信息
        print(COMMANDS["startMessage"])
        print(COMMANDS["helpGuide"])
        print(COMMANDS["exitGuide"])

        # 导入config
        config_dict = ConfigOperation.get_dir_from_file()
        GlobalValues.conn_host = config_dict["lastConnection"]["host"]
        GlobalValues.conn_port = config_dict["lastConnection"]["port"]
        GlobalValues.conn_authkey = config_dict["lastConnection"]["authkey"]
        GlobalValues.conn_qq = config_dict["lastConnection"]["qq"]
        GlobalValues.command_head = config_dict["commandHead"]

        # 运行消息进程
        fetch_message_thread = FetchMessageThread()
        fetch_message_thread.daemon = True
        fetch_message_thread.start()

        # 指令死循环
        while True:
            command = input("> ")

            # 分割指令
            command_list = re.sub(" +", " ", command).strip().split(" ")

            # 获取指令执行结果
            res = CommandHandler.command_handler(command_list)

            if res is None:

                # 为None时为退出程序
                print(COMMANDS["exiting"])
                break

            elif not res:

                # 为False时为错误指令
                print(COMMANDS["unknownCommandGuide"])