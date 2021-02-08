# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 21:11
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : ConfigOperation.py
# @Software: PyCharm

from utils.constants import *
import yaml


class ConfigOperation:
    """
    管理界面中的配置

    20210205 目前只有指令头、调试复选框和消息读取启用
    """

    @staticmethod
    def get_dir_from_file() -> dict:
        """
        从文件中读取内容

        :return: 无
        """

        # 该文件是否存在
        try:
            open(CONFIG_FILE_PATH, "r")
        except FileNotFoundError:
            ConfigOperation.__new_file()

        # 打开文件并读取
        with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
            config_dict = yaml.load(f, Loader=yaml.FullLoader)

        return config_dict

    @staticmethod
    def __new_file() -> None:
        """
        新建一个config.yml

        :return: 无
        """
        with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as f:
            yaml.dump({
                "commandHead": "#",
                "debug": False,
                "enable": False
            }, f)

    @staticmethod
    def __write_file(config_dict: dict) -> None:
        """
        写入新的内容到文件

        :param config_dict: 新的配置字典
        :return: 无
        """
        with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as f:
            yaml.dump(config_dict, f)

    @staticmethod
    def modify_dict(key: str, value) -> None:
        """
        修改字典键值对

        :param key: 键
        :param value: 值
        :return: 无
        """

        # 获取当前字典
        config_dict = ConfigOperation.get_dir_from_file()

        # 修改
        config_dict[key] = value

        # 写入到文件中
        ConfigOperation.__write_file(config_dict)
