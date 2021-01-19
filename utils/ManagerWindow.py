# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 23:40
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : ManagerWindow.py
# @Software: PyCharm
from tkinter import Tk, Frame, Label, Button
from tkinter.constants import *
from tkinter.ttk import Notebook, Entry


class ManagerWindow:
    """
    主管理界面入口类，直接无参数创建对象即可。
    """

    # 窗口宽高
    WIN_WIDTH = 600
    WIN_HEIGHT = 400

    def __init__(self):
        # 界面根节点
        self.root = Tk()

        # 主窗口标题
        self.root.title("LuckyQBot主管理器")

        # 主窗口分辨率
        self.root.geometry("%sx%s+%s+%s" % (
            self.WIN_WIDTH,
            self.WIN_HEIGHT,
            int((self.root.winfo_screenwidth() - self.WIN_WIDTH) / 2),
            int((self.root.winfo_screenheight() - self.WIN_HEIGHT) / 2)
        ))

        # 选项卡
        self.tab_main = Notebook(self.root)
        self.tab_main.pack(padx=5, pady=5)
        self.frame_login = Frame(self.tab_main, bg="white")
        self.frame_login.pack(side=TOP)
        self.tab_login = self.tab_main.add(self.frame_login, text="登录")
        self.frame_manage = Frame(self.tab_main, bg="white")
        self.tab_manage = self.tab_main.add(self.frame_manage, text="机器人设置")
        self.tab_main.pack(expand=True, fill=BOTH)

        # 登录界面显示的那一坨
        frame_login_menu = Frame(self.frame_login, bg="white")
        frame_login_menu.pack()

        # mirai端地址
        Label(frame_login_menu, text="连接地址", bg="white").grid(row=0, sticky=E, padx=5, pady=5)
        self.entry_host = Entry(frame_login_menu)
        self.entry_host.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        # mirai端端口号
        Label(frame_login_menu, text="端口号", bg="white").grid(row=1, sticky=E, padx=5, pady=5)
        self.entry_port = Entry(frame_login_menu)
        self.entry_port.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        # mirai http授权码
        Label(frame_login_menu, text="授权码(authKey)", bg="white").grid(
            row=2,
            sticky=E,
            padx=5,
            pady=5
        )
        self.entry_authkey = Entry(frame_login_menu)
        self.entry_authkey.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # 连接按钮
        Button(frame_login_menu, text="连接", width=15).grid(row=3, columnspan=2)

        self.root.mainloop()