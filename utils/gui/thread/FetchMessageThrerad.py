# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 23:43
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : FetchMessageThrerad.py
# @Software: PyCharm
import time
from threading import Thread

from utils.GlobalValues import GlobalValues
from utils.connect.Conn import Conn


class FetchMessageThread(Thread):
    """
    获取消息并分析，交给插件处理

    默认为1s获取一次
    """
    def run(self):
        while True:
            time.sleep(1)

            # 如果未连接，则不接收消息
            if not GlobalValues.is_connected:
                continue

            # 如果未启用，则不接受消息
            if not GlobalValues.enable_var.get():
                continue

            Conn.fetch_message(1)