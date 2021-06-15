# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 23:37
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : LuckyQBot.py
# @Software: PyCharm
import sys
import time

from utils.GlobalValues import GlobalValues
from utils.api.MessageChain import MessageChain

from threading import Thread
from utils.connect.Conn import Conn
from utils.handler.command.CommandThread import CommandThread
from utils.constants import *

args = sys.argv
l = len(args)

if l == 1:
    print(CMD_RUN_COMMAND_GUIDE)
    try:
        from utils.gui.ManagerWindow import ManagerWindow
        ManagerWindow()
    except ModuleNotFoundError:
        print(NO_GUI_MODEL_ERROR_MSG)
        print(CMD_RUN_COMMAND_GUIDE)
    exit()

if l == 2 and args[1] == COMMANDS["nogui"]:
    command_thread = CommandThread()
    command_thread.start()
else:
    print(WINDOW_RUN_COMMAND_GUIDE)
    print(CMD_RUN_COMMAND_GUIDE)