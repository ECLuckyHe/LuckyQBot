# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 18:33
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : ResponseExceptions.py
# @Software: PyCharm

class WrongAuthkeyException(Exception):
    """
    当返回信息状态码为1时的异常
    """
    def __str__(self):
        return "错误的Authkey"


class BotNotExistException(Exception):
    """
    当状态码为2时的异常
    """
    def __str__(self):
        return "指定的Bot不存在"


class SessionInvalidException(Exception):
    """
    当状态码为3时的异常
    """
    def __str__(self):
        return "Session失效或不存在"


class SessionNotCertifiedException(Exception):
    """
    当状态码为4时的异常
    """
    def __str__(self):
        return "Session未认证（未激活）"


class MessageReceiverNotExistException(Exception):
    """
    状态码为5时的异常
    """
    def __str__(self):
        return "发送消息目标不存在（指定对象不存在）"


class FileNotExistException(Exception):
    """
    状态码为6时的异常
    """
    def __str__(self):
        return "指定文件不存在"


class NoPermissionException(Exception):
    """
    状态码为10的异常
    """
    def __str__(self):
        return "Bot没有对应的操作权限"


class BotSpeakNotAllowedException(Exception):
    """
    状态码为20时的异常
    """
    def __str__(self):
        return "Bot当前无法向指定群发送信息"


class TooLongMessageException(Exception):
    """
    状态码为30时的异常
    """
    def __str__(self):
        return "消息过长"


class WrongAccessException(Exception):
    """
    状态码为400时的异常
    """
    def __str__(self):
        return "错误的访问"
