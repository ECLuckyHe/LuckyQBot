# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 16:44
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : GlobalValues.py
# @Software: PyCharm
from tkinter import BooleanVar


class GlobalValues:
    conn_host = None
    conn_port = None
    conn_authkey = None
    conn_qq = None
    conn_session_key = None

    is_connected = False
    command_head = None

    # 请注意：此处的debug_var为tkinter中BooleanVar对象，而非bool值
    debug_var = None

    # 请注意：此处的enable_varr为tkinter中BooleanVar对象，而非bool值
    enable_var = None
