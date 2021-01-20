# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 17:48
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Conn.py
# @Software: PyCharm
import json

from utils.GlobalValues import GlobalValues
from utils.RequestSender import RequestSender


class Conn:
    """
    用于连接mirai客户端所在服务器
    """

    @staticmethod
    def new_session_key():
        """
        连接并返回sessionKey

        :return: sessionKey
        """
        data = {
            "authKey": GlobalValues.conn_authkey
        }
        response_list = RequestSender.send_post("auth", data)

        # 获取返回内容中的sessionKey并作为返回值
        session_key = response_list["session"]
        Conn.__verify_session_key(session_key)
        return session_key

    @staticmethod
    def __verify_session_key(session_key):
        """
        校验SessionKey，此操作用于激活Session
        :return:
        """
        data = {
            "sessionKey": session_key,
            "qq": GlobalValues.conn_qq
        }
        RequestSender.send_post("verify", data)

    @staticmethod
    def release_session_key():
        """
        释放sessionKey

        :return: 无
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "qq": GlobalValues.conn_qq
        }
        RequestSender.send_post("release", data)