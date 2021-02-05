# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 16:05
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : OpListOperation.py
# @Software: PyCharm
import yaml

from utils.constants import *


class OpListOperation:
    """
    操作bot的op列表的类
    """

    @staticmethod
    def get_list_from_file() -> list:
        """
        从文件中获取内容的列表

        :return: 内容列表
        """

        # 该文件是否存在
        try:
            open(OP_LIST_FILE_PATH, "r")
        except FileNotFoundError:
            OpListOperation.__new_file()

        # 打开文件并读取
        with open(OP_LIST_FILE_PATH, "r", encoding="utf-8") as f:
            op_list = yaml.load(f, Loader=yaml.FullLoader)

        return op_list

    @staticmethod
    def __new_file() -> None:
        """
        新建一个保存bot op列表的文件

        :return: 无
        """
        with open(OP_LIST_FILE_PATH, "w", encoding="utf-8") as f:
            yaml.dump([], f)

    @staticmethod
    def __write_file(op_list: list) -> None:
        """
        写入新的内容到文件中

        :param op_list: 新的op列表
        :return: 无
        """
        with open(OP_LIST_FILE_PATH, "w", encoding="utf-8") as f:
            yaml.dump(op_list, f)

    @staticmethod
    def add_to_list(op_qq: int) -> None:
        """
        添加新的op到列表中

        :param op_qq: 新的op qq号
        :return: 无
        """

        # 获取当前列表
        op_list = OpListOperation.get_list_from_file()

        # 查重
        if op_qq in op_list:
            return

        # 添加到列表中
        op_list.append(op_qq)

        # 写入到文件中
        OpListOperation.__write_file(op_list)

    @staticmethod
    def remove_from_list(op_qq: int) -> None:
        """
        从列表中删除一个op的qq号

        :param op_qq: 要删除的qq
        :return: 无
        """

        # 获取当前列表
        op_list = OpListOperation.get_list_from_file()

        # 获取并删除这个qq
        op_list.remove(op_qq)

        # 写入到文件
        OpListOperation.__write_file(op_list)
