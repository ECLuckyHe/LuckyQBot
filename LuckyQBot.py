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

from utils.gui.ManagerWindow import ManagerWindow
from threading import Thread
from utils.connect.Conn import Conn
from utils.handler.command.CommandThread import CommandThread

window = ManagerWindow()



window.root.mainloop()
