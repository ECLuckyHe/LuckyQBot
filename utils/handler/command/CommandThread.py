# -*- coding: utf-8 -*-
# @Time    : 2021年3月12日 19:17
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : CommandThread.py
# @Software: PyCharm
import os
import sys
from threading import Thread


class CommandThread(Thread):
    """
    指令进程，负责操作控制台输入的内容
    """
    def __init__(self, manager_window):
        Thread.__init__(self)
        self.manager_window = manager_window

    def run(self):
        pass
