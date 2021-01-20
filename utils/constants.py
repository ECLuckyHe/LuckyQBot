# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 16:51
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : constants.py
# @Software: PyCharm

MANAGER_TITLE = "LuckyQBot主管理器"

BG_COLOR = "white"

TAB_NAME_LIST = {
    "login": {
        "text": "登录",
        "num": 0
    },
    "manage": {
        "text": "机器人管理",
        "num": 1
    }
}

LOGIN_GUIDE = {
    "host": "连接地址",
    "port": "端口号",
    "authkey": "授权码(authKey)",
    "qq": "QQ号"
}

PWD_CHAR_CIRCLE = "●"
PWD_CHAR_STAR = "*"

BTN_TEXT_CONN = {
    "connect": "连接",
    "disconnect": "断开连接"
}

BTN_TEXT_ADD_LOGIN = "添加到列表"

LOGIN_STATUS_BAR_TEXT = {
    "notConnect": "未连接",
    "connecting": "正在连接",
    "connectFailed": "连接失败，请检查地址和端口号是否正确",
    "wrongQQ": "错误的QQ号格式，请输入纯数字QQ号",
    "wrongAuthkey": "错误的授权码",
    "qqNotExist": "指定QQBot不存在，请输入正确QQ",
    "connectSuccess": "连接成功",
    "disconnectSuccess": "断开连接"
}

STATUS_BAR_COLOR = {
    "failed": "red",
    "passed": "green",
    "normal": "black"
}

LOGIN_LIST_FILE_PATH = "login_list.yml"
