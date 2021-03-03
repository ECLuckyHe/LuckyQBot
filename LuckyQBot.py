# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 23:37
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : LuckyQBot.py
# @Software: PyCharm
import time

from utils.GlobalValues import GlobalValues
from utils.api.MessageChain import MessageChain

from utils.gui.ManagerWindow import ManagerWindow
from threading import Thread
from utils.connect.Conn import Conn

ManagerWindow()

class MyThread(Thread):
    def run(self):
        printed = False
        while True:
            time.sleep(2)
            if not GlobalValues.is_connected:
                continue
            if not printed:
                printed = True

# MyThread().start()
