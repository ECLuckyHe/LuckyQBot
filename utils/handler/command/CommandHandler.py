# -*- coding: utf-8 -*-
# @Time    : 2021年3月12日 19:18
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : CommandHandler.py
# @Software: PyCharm
import requests

from utils.GlobalValues import GlobalValues
from utils.api.ResponseExceptions import WrongAuthkeyException, BotNotExistException
from utils.connect.Conn import Conn
from utils.constants import *
from utils.gui.operation.ConfigOperation import ConfigOperation
from utils.gui.operation.LoginListOperation import LoginListOperation
from utils.gui.operation.OpListOperation import OpListOperation


class CommandHandler:
    """
    指令handler，负责处理指令
    """

    @staticmethod
    def command_handler(command_list: list):
        """
        处理指令中心

        :param command_list: 指令分割后字符串列表
        :return: 执行状态，如果True则代表有该指令，否则没有
        """

        operation = command_list[0].lower()

        # 分路执行指令
        if operation == COMMANDS["help"]:
            CommandHandler.help()
        elif operation == COMMANDS["set"]:
            CommandHandler.set(command_list)
        elif operation == COMMANDS["show"]:
            CommandHandler.show(command_list)
        elif operation == COMMANDS["connect"]:
            CommandHandler.connect()
        elif operation == COMMANDS["disconnect"]:
            CommandHandler.disconnect()
        elif operation == COMMANDS["exit"]:
            CommandHandler.disconnect()
            return None
        else:
            return False

        return True

    @staticmethod
    def help():
        """
        关于help指令

        :return: 无
        """

        print(COMMANDS["helpContent"])

    @staticmethod
    def set(command_list: list):
        """
        关于set的指令

        :param command_list: 指令分割列表
        :return: 无
        """

        if len(command_list) != 3:
            print(COMMANDS["setHelp"])
            return

        # 获取操作
        operation = command_list[1].lower()
        arg = command_list[2]

        # 存储输入的内容
        if operation == "host":
            GlobalValues.conn_host = arg
        elif operation == "port":
            GlobalValues.conn_port = arg
        elif operation == "authkey":
            GlobalValues.conn_authkey = arg
        elif operation == "botqq":
            try:
                GlobalValues.conn_qq = int(arg)
            except ValueError:
                print(COMMANDS["setBotQQValueError"])
        else:
            print(COMMANDS["setHelp"])

    @staticmethod
    def show(command_list: list):
        """
        关于show的指令

        :param command_list: 指令分割列表
        :return:
        """

        if len(command_list) != 2:
            print(COMMANDS["showHelp"])
            return

        operation = command_list[1].lower()

        # 分支执行
        if operation == "loginlist":

            print(COMMANDS["loginListTableHead"])

            # 打印输出保存的登录列表
            login_list = LoginListOperation.get_list_from_file()
            for login in login_list:
                print(login["host"] + "\t" + login["port"] + "\t" + login["authkey"] + "\t" + login["qq"])

        elif operation == "oplist":
            print(COMMANDS["opListTableHead"])

            # 打印管理员QQ
            op_list = OpListOperation.get_list()
            for op in op_list:
                print(op)
        else:
            print(COMMANDS["showHelp"])

    @staticmethod
    def connect():
        """
        connect开始连接相关操作

        :return: 无
        """

        if GlobalValues.is_connected:
            print(COMMANDS["connectedError"])
            return

        # 无法正确连接到mirai的情况
        try:
            Conn.new_session_key()

        # 连接地址错误
        except (
            requests.exceptions.InvalidURL,
            requests.exceptions.ConnectionError
        ):
            print(COMMANDS["connectValueError"])
            return

        # 授权码错误
        except WrongAuthkeyException:
            print(COMMANDS["authkeyError"])
            return

        # Bot不存在错误
        except BotNotExistException:
            print(COMMANDS["botNotExistError"])
            return

        GlobalValues.is_connected = True

        # 修改上次连接键值对
        ConfigOperation.modify_dict("lastConnection", {
            "host": GlobalValues.conn_host,
            "port": GlobalValues.conn_port,
            "authkey": GlobalValues.conn_authkey,
            "qq": GlobalValues.conn_qq
        })

        print(COMMANDS["connectSuccess"])

    @staticmethod
    def disconnect():
        """
        断开连接

        :return: 无
        """
        if not GlobalValues.is_connected:
            print(COMMANDS["disconnectedError"])
            return

        # 释放Session
        Conn.release_session_key()

        # 修改连接状态
        GlobalValues.is_connected = False

        print(COMMANDS["disconnectSuccess"])
