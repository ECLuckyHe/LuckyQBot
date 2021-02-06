# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:27
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Friend.py
# @Software: PyCharm

class Friend:
    """
    发送人信息
    """

    def __init__(
            self,
            qq: int,
            nickname: str,
            remark: str
    ):
        """
        构造方法

        :param qq: 发送者qq
        :param nickname: 发送者昵称
        :param remark: 发送者remark（暂不知有什么用）
        """
        self.qq = qq
        self.nickname = nickname
        self.remark = remark
