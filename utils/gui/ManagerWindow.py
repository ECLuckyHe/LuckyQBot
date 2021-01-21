# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 23:40
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : ManagerWindow.py
# @Software: PyCharm

from tkinter import Tk, Frame, Label, Scrollbar
from tkinter.constants import *
from tkinter.ttk import Notebook, Entry, Button, Treeview
import requests
from utils.connect.Conn import Conn
from utils.GlobalValues import GlobalValues
from utils.gui.LoginListOperation import LoginListOperation
from utils.constants import *
from utils.connect.ResponseExceptions import *


class ManagerWindow:
    """
    主管理界面入口类，直接无参数创建对象即可。
    """

    # 窗口宽高
    WIN_WIDTH = 800
    WIN_HEIGHT = 600

    def __init__(self):
        # 界面根节点
        self.root = Tk()

        # 主窗口标题
        self.root.title(MANAGER_TITLE)

        # 主窗口分辨率
        self.root.geometry("%sx%s+%s+%s" % (
            self.WIN_WIDTH,
            self.WIN_HEIGHT,
            int((self.root.winfo_screenwidth() - self.WIN_WIDTH) / 2),
            int((self.root.winfo_screenheight() - self.WIN_HEIGHT) / 2)
        ))
        self.root.minsize(self.WIN_WIDTH, self.WIN_HEIGHT)

        # 选项卡
        self.tab_main = Notebook(self.root)
        self.tab_main.pack()
        self.frame_login = Frame(self.tab_main, bg=BG_COLOR)
        self.frame_login.pack(side=TOP)
        self.tab_main.add(self.frame_login, text=TAB_NAME_LIST["login"]["text"])
        self.frame_manage = Frame(self.tab_main, bg=BG_COLOR)
        self.tab_main.add(self.frame_manage, text=TAB_NAME_LIST["manage"]["text"])
        self.tab_main.pack(expand=True, fill=BOTH)

        # 初始化登录选项卡
        self.__init_login_tab()

        # 关闭窗口自动释放Session
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.__on_close_root())

        # 刷新显示
        self.__refresh()

        # 显示界面
        self.root.mainloop()

    def __init_login_tab(self):
        """
        初始化登录选项卡界面

        :return: 无
        """
        # 左边列表的frame
        frame_login_list = Frame(self.frame_login, bg=BG_COLOR)
        frame_login_list.pack(
            side=LEFT,
            expand=True,
            fill=BOTH,
            padx=5,
            pady=5
        )

        # 列表，用于保存连接记录
        self.treeview_login_list = Treeview(
            frame_login_list,
            columns=[
                LOGIN_GUIDE["host"],
                LOGIN_GUIDE["port"],
                LOGIN_GUIDE["authkey"],
                LOGIN_GUIDE["qq"]
            ],
            show="headings",
            selectmode=BROWSE
        )
        self.treeview_login_list.pack(
            expand=True,
            fill=BOTH,
            side=LEFT
        )
        self.treeview_login_list.column(
            LOGIN_GUIDE["host"],
            width=0
        )
        self.treeview_login_list.heading(
            LOGIN_GUIDE["host"],
            text=LOGIN_GUIDE["host"]
        )
        self.treeview_login_list.column(
            LOGIN_GUIDE["port"],
            width=0
        )
        self.treeview_login_list.heading(
            LOGIN_GUIDE["port"],
            text=LOGIN_GUIDE["port"]
        )
        self.treeview_login_list.column(
            LOGIN_GUIDE["authkey"],
            width=40
        )
        self.treeview_login_list.heading(
            LOGIN_GUIDE["authkey"],
            text=LOGIN_GUIDE["authkey"]
        )
        self.treeview_login_list.column(
            LOGIN_GUIDE["qq"],
            width=0
        )
        self.treeview_login_list.heading(
            LOGIN_GUIDE["qq"],
            text=LOGIN_GUIDE["qq"]
        )

        # 设定双击事件
        self.treeview_login_list.bind(
            "<Double-Button-1>",
            lambda event: self.__on_double_click_login_list_content()
        )

        # 设定登录列表的滚动条
        scrollbar_login_list = Scrollbar(frame_login_list)
        scrollbar_login_list.pack(fill="y", expand=True)
        self.treeview_login_list.config(yscrollcommand=scrollbar_login_list.set)
        scrollbar_login_list.config(command=self.treeview_login_list.yview)

        # 登录界面显示的那一坨
        frame_login_menu = Frame(self.frame_login, bg=BG_COLOR)
        frame_login_menu.pack(side=LEFT)

        # mirai端地址
        Label(frame_login_menu, text=LOGIN_GUIDE["host"], bg=BG_COLOR).grid(row=0, sticky=E, padx=5, pady=5)
        self.entry_host = Entry(frame_login_menu)
        self.entry_host.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        # mirai端端口号
        Label(frame_login_menu, text=LOGIN_GUIDE["port"], bg=BG_COLOR).grid(row=1, sticky=E, padx=5, pady=5)
        self.entry_port = Entry(frame_login_menu)
        self.entry_port.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        # mirai端http授权码
        Label(frame_login_menu, text=LOGIN_GUIDE["authkey"], bg=BG_COLOR).grid(
            row=2,
            sticky=E,
            padx=5,
            pady=5
        )
        self.entry_authkey = Entry(frame_login_menu, show=PWD_CHAR_CIRCLE)
        self.entry_authkey.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # 用于激活sessioKey的qq号码
        Label(frame_login_menu, text=LOGIN_GUIDE["qq"], bg=BG_COLOR).grid(
            row=3,
            sticky=E,
            padx=5,
            pady=5
        )
        self.entry_qq = Entry(frame_login_menu)
        self.entry_qq.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # 连接按钮
        self.btn_connect = Button(
            frame_login_menu,
            text=BTN_TEXT_CONN["connect"],
            width=15,
            command=lambda: self.__on_click_connect_event(),
        )
        self.btn_connect.grid(row=4, columnspan=2, padx=5, pady=5)

        # 添加到登录列表按钮
        self.btn_save_login = Button(
            frame_login_menu,
            width=15,
            text=BTN_TEXT_ADD_LOGIN,
            command=lambda: self.__on_click_add_to_login_list()
        )
        self.btn_save_login.grid(row=5, columnspan=2, padx=5, pady=5)

        # 状态栏
        self.label_login_status_bar = Label(
            self.root,
            text=LOGIN_STATUS_BAR_TEXT["notConnect"],
            fg=STATUS_BAR_COLOR["normal"]
        )
        self.label_login_status_bar.pack(side=LEFT)

    def __on_click_connect_event(self):
        """
        点击连接按钮事件

        :return: 无
        """

        if not GlobalValues.is_connected:
            # 如果是要连接

            # 存到全局使用变量
            GlobalValues.conn_host = self.entry_host.get()
            GlobalValues.conn_port = self.entry_port.get()
            GlobalValues.conn_authkey = self.entry_authkey.get()
            try:
                # 转换为整型后保存
                GlobalValues.conn_qq = int(self.entry_qq.get())
            except ValueError:
                self.label_login_status_bar.config(text=LOGIN_STATUS_BAR_TEXT["wrongQQ"], fg=STATUS_BAR_COLOR["failed"])
                return

            # 修改文本框为不可修改
            self.__set_login_entries_active(False)

            # 修改按钮内容
            self.btn_connect.config(text=BTN_TEXT_CONN["disconnect"])

            # 修改状态栏内容
            self.label_login_status_bar.config(text=LOGIN_STATUS_BAR_TEXT["connecting"], fg=STATUS_BAR_COLOR["normal"])

            # 调用连接
            try:
                Conn.new_session_key()
            except (
                requests.exceptions.InvalidURL,
                requests.exceptions.ConnectionError,
            ):
                # 连接错误

                # 错误信息显示到状态栏
                self.label_login_status_bar.config(
                    text=LOGIN_STATUS_BAR_TEXT["connectFailed"],
                    fg=STATUS_BAR_COLOR["failed"]
                )

                # 修改文本框为可修改
                self.__set_login_entries_active(True)
                self.btn_connect.config(text=BTN_TEXT_CONN["connect"])
                return
            except WrongAuthkeyException:
                # 授权码错误

                # 显示到状态栏
                self.label_login_status_bar.config(
                    text=LOGIN_STATUS_BAR_TEXT["wrongAuthkey"],
                    fg=STATUS_BAR_COLOR["failed"]
                )

                # 修改文本框为可修改
                self.__set_login_entries_active(True)
                self.btn_connect.config(text=BTN_TEXT_CONN["connect"])
                return

            except BotNotExistException:
                # bot不存在错误
                self.label_login_status_bar.config(
                    text=LOGIN_STATUS_BAR_TEXT["qqNotExist"],
                    fg=STATUS_BAR_COLOR["failed"]
                )

                # 修改文本框为可修改
                self.__set_login_entries_active(True)
                self.btn_connect.config(text=BTN_TEXT_CONN["connect"])
                return

            self.label_login_status_bar.config(
                text=LOGIN_STATUS_BAR_TEXT["connected"],
                fg=STATUS_BAR_COLOR["passed"]
            )

            # 修改连接状态值
            GlobalValues.is_connected = True

        else:
            # 如果要断开连接

            # 修改文本框为可修改
            self.__set_login_entries_active(True)

            # 修改按钮名称
            self.btn_connect.config(text=BTN_TEXT_CONN["connect"])

            # 修改属性值
            self.label_login_status_bar.config(
                text=LOGIN_STATUS_BAR_TEXT["disconnectSuccess"],
                fg=STATUS_BAR_COLOR["normal"]
            )

            # 释放session
            Conn.release_session_key()

            # 修改连接状态值
            GlobalValues.is_connected = False

    def __set_login_entries_active(self, active: bool):
        """
        设置登录界面文本框的可用性

        :param active: bool，如果为False则禁用掉文本框，否则启用
        :return: 无
        """
        if active:
            self.entry_host.config(state=ACTIVE)
            self.entry_port.config(state=ACTIVE)
            self.entry_authkey.config(state=ACTIVE)
            self.entry_qq.config(state=ACTIVE)
        else:
            self.entry_host.config(state=DISABLED)
            self.entry_port.config(state=DISABLED)
            self.entry_authkey.config(state=DISABLED)
            self.entry_qq.config(state=DISABLED)

    def __on_close_root(self):
        """
        关闭窗口的事件
        :return: 无
        """

        # 如果正在连接则释放连接
        if GlobalValues.is_connected:
            Conn.release_session_key()

        # 杀掉root
        self.root.destroy()

    def __refresh(self):
        """
        用于刷新界面，在必要时调用

        :return: 无
        """

        def refresh_login_list():
            """
            刷新登录列表

            :return: 无
            """

            # 删除目前表中的所有内容
            self.treeview_login_list.delete(*self.treeview_login_list.get_children())

            # 把登录列表内容添加到显示中
            for one_record in LoginListOperation.get_list_from_file():
                self.treeview_login_list.insert("", index=END, values=(
                    one_record["host"],
                    one_record["port"],
                    one_record["authkey"],
                    one_record["qq"]
                ))

        # 调用刷新登录列表
        refresh_login_list()

    def __on_click_add_to_login_list(self):
        """
        将填写内容添加到列表中
        :return: 无
        """

        # 非空检测
        if [
            self.entry_host.get(),
            self.entry_port.get(),
            self.entry_authkey.get(),
            self.entry_qq.get()
        ] == [""] * 4:
            return

        # 调用添加登录项方法
        LoginListOperation.add_to_list(
            self.entry_host.get(),
            self.entry_port.get(),
            self.entry_authkey.get(),
            self.entry_qq.get()
        )

        # 刷新显示
        self.__refresh()

    def __on_double_click_login_list_content(self):
        """
        双击登录列表项目时，自动填充到右侧

        :return: 无
        """

        # 获取选中的项目，我也不懂，反正就是这样写
        index = 0
        for item in self.treeview_login_list.selection():

            # 获取item的值
            item_list = self.treeview_login_list.item(item, "values")

            # 获取需要的项目并设置
            self.entry_host.delete(0, END)
            self.entry_host.insert(END, item_list[0])
            self.entry_port.delete(0, END)
            self.entry_port.insert(END, item_list[1])
            self.entry_authkey.delete(0, END)
            self.entry_authkey.insert(END, item_list[2])
            self.entry_qq.delete(0, END)
            self.entry_qq.insert(END, item_list[3])
