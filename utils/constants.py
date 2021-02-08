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
    },
    "friends": {
        "text": "好友（测试使用）",
        "num": 2
    },
    "groups": {
        "text": "群（测试使用）",
        "num": 3
    },
    "plugins": {
        "text": "插件列表",
        "num": 4
    }
}

LOGIN_GUIDE = {
    "host": "连接地址",
    "port": "端口号",
    "authkey": "授权码(authKey)",
    "qq": "QQ号"
}

FRIEND_GUIDE = {
    "qq": "QQ",
    "nickname": "昵称",
    "remark": "remark（保留，不知道是啥）"
}

GROUP_GUIDE = {
    "group": "群号",
    "name": "群名",
    "permission": "权限"
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
    "connected": "已连接",
    "disconnectSuccess": "连接已断开"
}

STATUS_BAR_COLOR = {
    "failed": "red",
    "passed": "green",
    "normal": "black"
}

LOGIN_LIST_FILE_PATH = "login_list.yml"

POP_UP_MENU_DELETE_STR = "删除"

SEND_TITLE = "测试发送内容"

BTN_SEND = "发送消息"

BTN_FRIEND_REFRESH = "刷新好友列表"

REFRESH_ERROR_MSG = "发生错误，请确保已连接"

SEND_ERROR_MSG = "未选择对象或对象不存在"

# PERMISSION
PERMISSION_OWNER = "OWNER"
PERMISSION_ADMINISTRATOR = "ADMINISTRATOR"
PERMISSION_MEMBER = "MEMBER"

# EVENT
BOT_ONLINE_EVENT = "BotOnlineEvent"
BOT_OFFLINE_ACTIVE_EVENT = "BotOfflineEventActive"
BOT_OFFLINE_FORCE_EVENT = "BotOfflineEventForce"
BOT_OFFLINE_DROPPED_EVENT = "BotOfflineEventDropped"
BOT_RELOGIN_EVENT = "BotReloginEvent"
BOT_GROUP_PERMISSION_CHANGE_EVENT = "BotGroupPermissionChangeEvent"
BOT_MUTE_EVENT = "BotMuteEvent"
BOT_UNMUTE_EVENT = "BotUnmuteEvent"
BOT_JOIN_GROUP_EVENT = "BotJoinGroupEvent"
BOT_LEAVE_ACTIVE_EVENT = "BotLeaveEventActive"
BOT_LEAVE_KICK_EVENT = "BotLeaveEventKick"
GROUP_RECALL_EVENT = "GroupRecallEvent"
FRIEND_RECALL_EVENT = "FriendRecallEvent"
GROUP_NAME_CHANGE_EVENT = "GroupNameChangeEvent"
GROUP_ENTRANCE_ANNOUNCEMENT_CHANGE_EVENT = "GroupEntranceAnnouncementChangeEvent"
GROUP_MUTE_ALL_EVENT = "GroupMuteAllEvent"
GROUP_ALLOW_ANONYMOUS_CHAT_EVENT = "GroupAllowAnonymousChatEvent"
GROUP_ALLOW_CONFESS_TALK_EVENT = "GroupAllowConfessTalkEvent"
GROUP_ALLOW_MEMBER_INVITE_EVENT = "GroupAllowMemberInviteEvent"
MEMBER_JOIN_EVENT = "MemberJoinEvent"
MEMBER_LEAVE_KICK_EVENT = "MemberLeaveEventKick"
MEMBER_LEAVE_QUIT_EVENT = "MemberLeaveEventQuit"
MEMBER_CARD_CHANGE_EVENT = "MemberCardChangeEvent"
MEMBER_SPECIAL_TITLE_CHANGE_EVENT = "MemberSpecialTitleChangeEvent"
MEMBER_PERMISSION_CHANGE_EVENT = "MemberPermissionChangeEvent"
MEMBER_MUTE_EVENT = "MemberMuteEvent"
MEMBER_UNMUTE_EVENT = "MemberUnmuteEvent"
NEW_FRIEND_REQUEST_EVENT = "NewFriendRequestEvent"
MEMBER_JOIN_REQUEST_EVENT = "MemberJoinRequestEvent"
BOT_INVITED_JOIN_GROUP_REQUEST_EVENT = "BotInvitedJoinGroupRequestEvent"

MANAGE_GUIDE = {
    "commandHead": "指令头",
    "debug": "调试模式（在消息最后追加[调试]字样）",
    "botOpQQ": "Bot管理员QQ",
    "addOpQQ": "添加Bot管理QQ",
    "btnAddOpQQ": "添加管理QQ",
    "removeOpQQ": "删除管理QQ",
    "saveConfig": "保存配置",
    "successSaveCommandHeadMsg": "保存成功！",
    "enable": "启用机器人（取一条消息、执行事件、从消息记录中删除）"
}

OP_LIST_FILE_PATH = "op_list.yml"

CONFIG_FILE_PATH = "config.yml"

# 消息来源
GROUP_MSG = "GroupMessage"
FRIEND_MSG = "FriendMessage"
TEMP_MSG = "TempMessage"

PLUGIN_LABEL_TEXT = "插件列表仅显示被识别到的.py文件，如需增加、重载或删除插件，请手动重启程序"

PLUGIN_GUIDE = {
    "pluginName": "插件名"
}