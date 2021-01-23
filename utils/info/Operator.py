# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 11:45
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Operator.py
# @Software: PyCharm
from utils.info.Group import Group


class Operator:
    """
    操作者信息
    """

    def __init__(
            self,
            qq: int,
            name: str,
            permission: str,
            group: Group
    ):
        """
        构造方法

        :param qq: 操作者qq
        :param name: 操作者群名片
        :param permission: 操作者权限
        :param group: 操作的群
        """
        self.qq = qq
        self.name = name
        self.permission = permission
        self.group = group
