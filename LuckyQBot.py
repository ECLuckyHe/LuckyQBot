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


class ManagerWindowThread(Thread):
    def run(self):
        ManagerWindow()


ManagerWindowThread().start()


class MyThread(Thread):
    def run(self):
        printed = False
        while True:
            time.sleep(2)
            if not GlobalValues.is_connected:
                continue
            if not printed:
                Conn.set_member_info(
                    group=547664115,
                    member_id=1405038715,
                    name="狗来的"
                )
                printed = True


MyThread().start()