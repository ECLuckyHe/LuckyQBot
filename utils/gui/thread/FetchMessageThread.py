# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 23:43
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : FetchMessageThread.py
# @Software: PyCharm
import json
import time
from threading import Thread

from utils.GlobalValues import GlobalValues
from utils.connect.Conn import Conn

from utils.constants import *
from utils.info.Message import Message


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

            # 获取消息数据
            try:
                msg_data_list = Conn.fetch_message(1)["data"]
            except:
                # 捕捉到异常则继续
                continue

            # 获取到的列表为空
            if not msg_data_list:
                continue

            # 获取数据
            msg_data = msg_data_list[0]

            print(Message(msg_data).get_plain_text())