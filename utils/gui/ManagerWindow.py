# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 23:40
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : ManagerWindow.py
# @Software: PyCharm
from tkinter import Tk, Frame, Label, Scrollbar, Menu, Text, messagebox, Checkbutton, BooleanVar
from tkinter.constants import *
from tkinter.ttk import Notebook, Entry, Button, Treeview
import requests

from utils.api.MessageChain import MessageChain
from utils.connect.Conn import Conn
from utils.GlobalValues import GlobalValues
from utils.gui.operation.ConfigOperation import ConfigOperation
from utils.gui.operation.LoginListOperation import LoginListOperation
from utils.constants import *
from utils.api.ResponseExceptions import *
from utils.gui.operation.OpListOperation import OpListOperation
from utils.gui.thread.FetchMessageThread import FetchMessageThread


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
        self.tab_main.pack(expand=True, fill=BOTH)

        # 登录选项卡
        self.frame_login = Frame(self.tab_main, bg=BG_COLOR)
        self.frame_login.pack(side=TOP)
        self.tab_main.add(self.frame_login, text=TAB_NAME_LIST["login"]["text"])

        # 管理选项卡
        self.frame_manage = Frame(self.tab_main, bg=BG_COLOR)
        self.tab_main.add(self.frame_manage, text=TAB_NAME_LIST["manage"]["text"])

        # 好友选项卡
        self.frame_friend = Frame(self.tab_main, bg=BG_COLOR)
        self.frame_friend.pack(side=TOP)
        self.tab_main.add(self.frame_friend, text=TAB_NAME_LIST["friends"]["text"])

        # 群选项卡
        self.frame_group = Frame(self.tab_main, bg=BG_COLOR)
        self.frame_group.pack(side=TOP)
        self.tab_main.add(self.frame_group, text=TAB_NAME_LIST["groups"]["text"])

        # 初始化登录选项卡
        self.__init_login_tab()

        # 初始化好友选项卡
        self.__init_friend_tab()

        # 初始化群选项卡
        self.__init_group_tab()

        # 初始化管理选项卡
        self.__init_manage_tab()

        # 关闭窗口自动释放Session
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.__on_close_root())

        # 刷新显示
        self.__refresh()

        # 运行相关线程
        fetch_message_thread = FetchMessageThread()
        fetch_message_thread.daemon = True
        fetch_message_thread.start()

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

        # 设置列表右键菜单
        self.treeview_login_list.bind("<Button-3>", self.__show_login_list_pop_up_menu)

        # 登录界面显示的那一坨
        frame_login_menu = Frame(self.frame_login, bg=BG_COLOR)
        frame_login_menu.pack(side=LEFT, padx=5, pady=5)

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

    def __init_friend_tab(self):
        """
        初始化好友选项卡内容

        :return: 无
        """

        # 创建好友列表框架
        frame_friend_list = Frame(self.frame_friend, bg=BG_COLOR)
        frame_friend_list.pack(
            side=LEFT,
            expand=True,
            fill=BOTH,
            padx=5,
            pady=5
        )

        # 创建消息测试发送框架
        frame_friend_send = Frame(self.frame_friend, bg=BG_COLOR)
        frame_friend_send.pack(
            side=LEFT,
            padx=5,
            pady=5
        )

        # 设置列表
        self.treeview_friend_list = Treeview(
            frame_friend_list,
            columns=[
                FRIEND_GUIDE["qq"],
                FRIEND_GUIDE["nickname"],
                FRIEND_GUIDE["remark"]
            ],
            show="headings",
            selectmode=BROWSE
        )
        self.treeview_friend_list.pack(
            expand=True,
            fill=BOTH,
            side=LEFT
        )
        self.treeview_friend_list.column(
            FRIEND_GUIDE["qq"],
            width=0
        )
        self.treeview_friend_list.heading(
            FRIEND_GUIDE["qq"],
            text=FRIEND_GUIDE["qq"]
        )
        self.treeview_friend_list.column(
            FRIEND_GUIDE["nickname"],
            width=0
        )
        self.treeview_friend_list.heading(
            FRIEND_GUIDE["nickname"],
            text=FRIEND_GUIDE["nickname"]
        )
        self.treeview_friend_list.column(
            FRIEND_GUIDE["remark"],
            width=0
        )
        self.treeview_friend_list.heading(
            FRIEND_GUIDE["remark"],
            text=FRIEND_GUIDE["remark"]
        )

        # 刷新列表按钮
        Button(
            frame_friend_send,
            text=BTN_FRIEND_REFRESH,
            command=lambda: self.__on_click_refresh_friend_list_event()
        ).grid(row=0, padx=5, pady=5)

        # 发送纯文本窗口标题
        Label(frame_friend_send, text=SEND_TITLE, bg=BG_COLOR).grid(row=1, padx=5, pady=5)

        # 发送纯文本窗口
        self.text_friend_send = Text(frame_friend_send, width=30, height=5)
        self.text_friend_send.grid(row=2, padx=5, pady=5)

        # 发送按钮
        Button(
            frame_friend_send,
            text=BTN_SEND,
            command=lambda: self.__on_click_send_friend_message()
        ).grid(row=3, padx=5, pady=5)

    def __init_group_tab(self):
        """
        初始化群选项卡内容

        :return: 无
        """

        # 创建好友列表框架
        frame_group_list = Frame(self.frame_group, bg=BG_COLOR)
        frame_group_list.pack(
            side=LEFT,
            expand=True,
            fill=BOTH,
            padx=5,
            pady=5
        )

        # 创建消息测试发送框架
        frame_group_send = Frame(self.frame_group, bg=BG_COLOR)
        frame_group_send.pack(
            side=LEFT,
            padx=5,
            pady=5
        )

        # 设置列表
        self.treeview_group_list = Treeview(
            frame_group_list,
            columns=[
                GROUP_GUIDE["group"],
                GROUP_GUIDE["name"],
                GROUP_GUIDE["permission"]
            ],
            show="headings",
            selectmode=BROWSE
        )
        self.treeview_group_list.pack(
            expand=True,
            fill=BOTH,
            side=LEFT
        )
        self.treeview_group_list.column(
            GROUP_GUIDE["group"],
            width=0
        )
        self.treeview_group_list.heading(
            GROUP_GUIDE["group"],
            text=GROUP_GUIDE["group"]
        )
        self.treeview_group_list.column(
            GROUP_GUIDE["name"],
            width=0
        )
        self.treeview_group_list.heading(
            GROUP_GUIDE["name"],
            text=GROUP_GUIDE["name"]
        )
        self.treeview_group_list.column(
            GROUP_GUIDE["permission"],
            width=0
        )
        self.treeview_group_list.heading(
            GROUP_GUIDE["permission"],
            text=GROUP_GUIDE["permission"]
        )

        # 刷新列表按钮
        Button(
            frame_group_send,
            text=BTN_FRIEND_REFRESH,
            command=lambda: self.__on_click_refresh_group_list_event()
        ).grid(row=0, padx=5, pady=5)

        # 发送纯文本窗口标题
        Label(frame_group_send, text=SEND_TITLE, bg=BG_COLOR).grid(row=1, padx=5, pady=5)

        # 发送纯文本窗口
        self.text_group_send = Text(frame_group_send, width=30, height=5)
        self.text_group_send.grid(row=2, padx=5, pady=5)

        # 发送按钮
        Button(
            frame_group_send,
            text=BTN_SEND,
            command=lambda: self.__on_click_send_group_message()
        ).grid(row=3, padx=5, pady=5)

    def __init_manage_tab(self):
        """
        初始化管理选项卡

        :return: 无
        """

        f_manage = Frame(self.frame_manage, bg=BG_COLOR)
        f_manage.pack(padx=5, pady=5, expand=True)

        # 指定头指示
        Label(f_manage, text=MANAGE_GUIDE["commandHead"], bg=BG_COLOR).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=E
        )

        # 指令头文本框
        self.entry_command_head = Entry(f_manage)
        self.entry_command_head.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        # 调试复选框
        self.debug_var = BooleanVar()
        checkbutton_debug = Checkbutton(
            f_manage,
            text=MANAGE_GUIDE["debug"],
            onvalue=True,
            offvalue=False,
            variable=self.debug_var,
            bg=BG_COLOR
        )
        checkbutton_debug.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # 启用机器人
        self.enable_var = BooleanVar()
        checkbutton_enable = Checkbutton(
            f_manage,
            text=MANAGE_GUIDE["enable"],
            onvalue=True,
            offvalue=False,
            variable=self.enable_var,
            bg=BG_COLOR
        )
        checkbutton_enable.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # 配置保存
        Button(
            f_manage,
            text=MANAGE_GUIDE["saveConfig"],
            command=self.__on_click_save_config
        ).grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=EW
        )

        # bot管理qq列表
        self.treeview_op_list = Treeview(
            f_manage,
            columns=[
                MANAGE_GUIDE["botOpQQ"]
            ],
            show="headings",
            selectmode=BROWSE
        )
        self.treeview_op_list.column(MANAGE_GUIDE["botOpQQ"], width=200)
        self.treeview_op_list.heading(MANAGE_GUIDE["botOpQQ"], text=MANAGE_GUIDE["botOpQQ"])
        self.treeview_op_list.grid(
            row=4,
            column=0,
            columnspan=3,
            rowspan=10,
            sticky=EW
        )

        # 列表右键
        self.treeview_op_list.bind("<Button-3>", self.__show_op_list_pop_up_menu)

        # 添加管理标签
        Label(f_manage, text=MANAGE_GUIDE["addOpQQ"], bg=BG_COLOR).grid(row=14, column=0, padx=5, pady=5)

        # 添加管理文本框
        self.entry_add_op = Entry(f_manage)
        self.entry_add_op.grid(row=14, column=1, padx=5, pady=5)

        # 添加添加按钮
        Button(
            f_manage,
            text=MANAGE_GUIDE["btnAddOpQQ"],
            command=lambda: self.__on_click_add_op()
        ).grid(row=14, column=2, padx=5, pady=5, sticky=EW)

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

        def refresh_op_list():
            """
            刷新bot管理员qq列表

            :return: 无
            """

            # 删除目前表中的所有内容
            self.treeview_op_list.delete(*self.treeview_op_list.get_children())

            # 把内容添加到显示中
            for one_record in OpListOperation.get_list_from_file():
                self.treeview_op_list.insert("", index=END, values=(
                    one_record
                ))

        def refresh_config():
            """
            刷新配置

            :return: 无
            """

            # 读取config
            config_dict = ConfigOperation.get_dir_from_file()

            # 将文件中的内容显示到界面中
            self.entry_command_head.delete(0, END)
            self.entry_command_head.insert(END, config_dict["commandHead"])

            # 设置复选框默认勾选
            self.debug_var.set(config_dict["debug"])
            self.enable_var.set(config_dict["enable"])

            # 将内容设置到全局变量
            GlobalValues.command_head = config_dict["commandHead"]
            GlobalValues.debug_var = self.debug_var
            GlobalValues.enable_var = self.enable_var

        # 调用刷新登录列表
        refresh_login_list()

        # 调用刷新op列表
        refresh_op_list()

        # 刷新config显示
        refresh_config()

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

        # 获取item的值
        item_list = self.treeview_login_list.item(self.treeview_login_list.focus(), "values")

        # 获取需要的项目并设置
        self.entry_host.delete(0, END)
        self.entry_host.insert(END, item_list[0])
        self.entry_port.delete(0, END)
        self.entry_port.insert(END, item_list[1])
        self.entry_authkey.delete(0, END)
        self.entry_authkey.insert(END, item_list[2])
        self.entry_qq.delete(0, END)
        self.entry_qq.insert(END, item_list[3])

    def __show_login_list_pop_up_menu(self, event):
        """
        显示右键菜单

        :param event: 事件
        :return: 无
        """
        def on_delete_event(iid):
            """
            删除选项的事件

            :return: 无
            """

            # 删除该项
            LoginListOperation.remove_from_list(*self.treeview_login_list.item(iid, "values"))
            self.treeview_login_list.delete(iid)
            self.__refresh()

        # 获取选择对象
        iid = self.treeview_login_list.identify_row(event.y)

        # 如果有选择，则弹出右键菜单
        if iid:
            self.treeview_login_list.selection_set(iid)
            menu_pop_up = Menu(self.treeview_login_list, tearoff=False)
            menu_pop_up.add_command(
                label=POP_UP_MENU_DELETE_STR,
                command=lambda: on_delete_event(iid)
            )
            menu_pop_up.post(event.x_root, event.y_root)

    def __on_click_refresh_friend_list_event(self):
        """
        点击刷新好友列表事件

        :return: 无
        """
        try:
            # 如果未连接，则可能会抛出异常，此处直接弹出错误消息框
            friend_list = Conn.get_friend_list()
        except:
            messagebox.showerror(message=REFRESH_ERROR_MSG)
            return

        # 删除列表内容
        self.treeview_friend_list.delete(*self.treeview_friend_list.get_children())

        # 解析friend_list
        for friend_block in friend_list:
            self.treeview_friend_list.insert("", index=END, values=(
                friend_block["id"],
                friend_block["nickname"],
                friend_block["remark"]
            ))

    def __on_click_refresh_group_list_event(self):
        """
        点击刷新群列表事件

        :return: 无
        """
        try:
            # 如果未连接，则可能会抛出异常，此处直接弹出错误消息框
            group_list = Conn.get_group_list()
        except:
            messagebox.showerror(message=REFRESH_ERROR_MSG)
            return

        # 删除列表内容
        self.treeview_group_list.delete(*self.treeview_group_list.get_children())

        # 解析group_list
        for group_block in group_list:
            self.treeview_group_list.insert("", index=END, values=(
                group_block["id"],
                group_block["name"],
                group_block["permission"]
            ))

    def __on_click_send_friend_message(self):
        """
        点击发送消息给好友按钮

        :return: 无
        """

        # 获取到选中好友的值列表
        value_list = self.treeview_friend_list.item(self.treeview_friend_list.focus(), "values")

        try:
            # 获取qq并发送消息
            qq = value_list[0]
            message_chain = MessageChain()
            text = self.text_friend_send.get(1.0, END)
            if text == "\n":
                return
            message_chain.add_plain_text(text)
            Conn.send_friend_message(qq, message_chain.get_message_chain())
            self.text_friend_send.delete(1.0, END)
        except:
            messagebox.showerror(message=SEND_ERROR_MSG)
            return

    def __on_click_send_group_message(self):
        """
        点击发送消息给群按钮

        :return: 无
        """

        # 获取到选中群的值列表
        value_list = self.treeview_group_list.item(self.treeview_group_list.focus(), "values")

        try:
            # 获取qq并发送消息
            qq = value_list[0]
            message_chain = MessageChain()
            text = self.text_group_send.get(1.0, END)
            if text == "\n":
                return
            message_chain.add_plain_text(text)
            Conn.send_group_message(qq, message_chain.get_message_chain())
            self.text_group_send.delete(1.0, END)
        except:
            messagebox.showerror(message=SEND_ERROR_MSG)
            return

    def __on_click_add_op(self):
        """
        点击添加op按钮事件

        :return: 无
        """

        content = self.entry_add_op.get()

        # 如果添加op的文本框中没有东西，则不添加
        if content == "":
            return

        # 如果转换数字出错则不添加
        try:
            op_qq = int(content)
        except ValueError:
            return

        # 添加到op列表中
        OpListOperation.add_to_list(op_qq)

        # 刷新显示
        self.__refresh()

    def __show_op_list_pop_up_menu(self, event):
        """
        op列表右键菜单

        :return: 无
        """

        def on_delete_event(op_qq):
            """
            删除选项的事件

            :return: 无
            """

            # 删除该项
            # 注意此处的强转，由于能够保证显示出来的内容一定只含有数字，故可以直接转换
            OpListOperation.remove_from_list(int(self.treeview_op_list.item(op_qq, "values")[0]))
            self.treeview_op_list.delete(op_qq)
            self.__refresh()

        # 获取选择对象
        op_qq = self.treeview_op_list.identify_row(event.y)

        # 如果有选择，则弹出右键菜单
        if op_qq:
            menu_pop_up = Menu(self.treeview_op_list, tearoff=False)
            self.treeview_op_list.selection_set(op_qq)
            menu_pop_up.add_command(
                label=POP_UP_MENU_DELETE_STR,
                command=lambda: on_delete_event(op_qq)
            )
            menu_pop_up.post(event.x_root, event.y_root)

    def __on_click_save_config(self):
        """
        点击保存配置事件

        :return: 无
        """

        content = self.entry_command_head.get()

        # 如果为空，则不存入，但是刷新
        # 这样是为了保证点击后会显示原来的设置
        if content == "":
            self.__refresh()
            return

        ConfigOperation.modify_dict("commandHead", content)
        ConfigOperation.modify_dict("debug", self.debug_var.get())
        ConfigOperation.modify_dict("enable", self.enable_var.get())

        # 刷新
        self.__refresh()

        # 弹出对话框
        messagebox.showinfo(message=MANAGE_GUIDE["successSaveCommandHeadMsg"])
