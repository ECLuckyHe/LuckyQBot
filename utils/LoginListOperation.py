# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 22:51
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : LoginListOperation.py
# @Software: PyCharm

from utils.constants import *
import yaml


class LoginListOperation:
    """
    用于操作存储的登录列表记录的类
    """

    @staticmethod
    def get_list_from_file() -> list:
        """
        从文件中获取内容的列表

        :return: 内容列表
        """

        # 测试有无该文件
        try:
            open(LOGIN_LIST_FILE_PATH, "r")
        except FileNotFoundError:
            LoginListOperation.__new_file()

        # 打开文件并读取
        with open(LOGIN_LIST_FILE_PATH, "r", encoding="utf-8") as f:
            login_list = yaml.load(f, Loader=yaml.FullLoader)

        return login_list

    @staticmethod
    def __new_file() -> None:
        """
        新建一个保存登录列表的文件

        :return: 无
        """
        with open(LOGIN_LIST_FILE_PATH, "w", encoding="utf-8") as f:
            yaml.dump([
                {
                    "host": "127.0.0.1",
                    "port": "8080",
                    "authkey": "ABCDEFG",
                    "qq": "123456789"
                }
            ], f)

    @staticmethod
    def __write_file(login_list: list) -> None:
        """
        写入新的内容到文件中

        :param login_list: 新的登录列表
        :return: 无
        """

        # 打开文件并写入
        with open(LOGIN_LIST_FILE_PATH, "w", encoding="utf-8") as f:
            yaml.dump(login_list, f)

    @staticmethod
    def add_to_list(host: str, port: str, authkey: str, qq: str) -> None:
        """
        添加新的登录项到列表中

        :param host: 地址
        :param port: 端口号
        :param authkey: 授权码
        :param qq: qq号码
        :return: 无
        """

        # 获取到当前列表
        login_list = LoginListOperation.get_list_from_file()

        # 创建新字典
        new_dir = {
            "host": host,
            "port": port,
            "authkey": authkey,
            "qq": qq
        }

        # 查重
        if new_dir in login_list:
            return

        # 向列表中添加新字典
        login_list.append(new_dir)

        # 重新写入到文件中
        LoginListOperation.__write_file(login_list)
