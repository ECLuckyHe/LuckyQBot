# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 11:42
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Group.py
# @Software: PyCharm

class Group:
    """
    群信息对象
    """

    def __init__(
            self,
            id: int,
            name: str,
            permission: str
    ):
        """
        构造方法

        :param id: 群号
        :param name: 群名
        :param permission: 群权限
        """
        self.id = id
        self.name = name
        self.permission = permission