# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 11:45
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Member.py
# @Software: PyCharm
from utils.info.Group import Group


class Member:
    """
    成员信息
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

        :param qq: 成员qq
        :param name: 成员群名片
        :param permission: 成员权限
        :param group: 所在群或操作群
        """
        self.qq = qq
        self.name = name
        self.permission = permission
        self.group = group
