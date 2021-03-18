# -*- coding: utf-8 -*-
# @Time    : 2021年3月12日 19:17
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : CommandThread.py
# @Software: PyCharm
import os
import sys
from threading import Thread

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