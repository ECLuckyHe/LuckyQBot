# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 23:43
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : FetchMessageThread.py
# @Software: PyCharm
import time
from threading import Thread

from utils.GlobalValues import GlobalValues
from utils.connect.Conn import Conn
from utils.handler.plugin.PluginHandler import PluginHandler

from utils.info.Message import Message


class FetchMessageThread(Thread):
    """
    获取消息并分析，交给插件处理

    默认为1s获取一次
    """

    def __init__(self):
        """
        构造方法
        """

        Thread.__init__(self)
        self.msg: Message

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
            # 同时处理可能出现的异常，直接忽略
            try:
                data_list = Conn.fetch_message(1)["data"]
            except Exception as e:
                # 捕捉到异常则重新循环
                print(e)
                continue

            # 获取到的列表为空
            if not data_list:
                continue

            # 获取数据
            data = data_list[0]

            if data["type"].endswith("Message"):
                self.msg = Message(data)

                # 调用执行插件内容
                PluginHandler.call_on_message(self.msg)