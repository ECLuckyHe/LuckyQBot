# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 17:48
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : Conn.py
# @Software: PyCharm

from utils.GlobalValues import GlobalValues
from utils.api.MessageChain import MessageChain
from utils.connect.RequestSender import RequestSender


class Conn:
    """
    用于连接mirai客户端所在服务器
    """

    @staticmethod
    def new_session_key() -> dict:
        """
        连接并返回sessionKey

        :return: 请求返回的内容
        """
        data = {
            "authKey": GlobalValues.conn_authkey
        }
        response_dict = RequestSender.send_post("auth", data)

        # 获取返回内容中的sessionKey并作为返回值
        session_key = response_dict["session"]

        # 激活session并保存sessionKey
        Conn.__verify_session_key(session_key)
        GlobalValues.conn_session_key = session_key

        return response_dict

    @staticmethod
    def __verify_session_key(session_key: str) -> dict:
        """
        校验SessionKey，此操作用于激活Session

        :return: 响应内容
        """
        data = {
            "sessionKey": session_key,
            "qq": GlobalValues.conn_qq
        }
        return RequestSender.send_post("verify", data)

    @staticmethod
    def release_session_key() -> dict:
        """
        释放sessionKey

        :return: 响应内容
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "qq": GlobalValues.conn_qq
        }
        return RequestSender.send_post("release", data)

    @staticmethod
    def send_friend_message(qq: int, message_chain: MessageChain, quote: int = None) -> dict:
        """
        发送消息给好友

        :param qq: 接收方qq
        :param quote: 引用消息号
        :param message_chain: 消息列表

        :return: 请求响应的内容
        """

        # 添加调试信息
        if GlobalValues.debug_var.get():
            message_chain.add_plain_text("[调试]")

        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "qq": qq,
            "messageChain": message_chain.get_message_chain()
        }
        if quote is not None:
            data["quote"] = quote
        return RequestSender.send_post("sendFriendMessage", data)

    @staticmethod
    def send_temp_message(qq: int, group: int, message_chain: MessageChain, quote: int = None) -> dict:
        """
        发送临时消息

        :param message_chain:
        :param qq: 接收方qq
        :param group: 接收方所在群
        :param message_chain: 消息列表
        :param quote: 引用消息号

        :return: 返回结果
        """

        # 添加调试信息
        if GlobalValues.debug_var.get():
            message_chain.add_plain_text("[调试]")

        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "qq": qq,
            "group": group,
            "messageChain": message_chain.get_message_chain()
        }
        if quote is not None:
            data["quote"] = quote
        return RequestSender.send_post("sendTempMessage", data)

    @staticmethod
    def send_group_message(group: int, message_chain: MessageChain, quote: int = None) -> dict:
        """
        发送群消息

        :param group: 群号
        :param message_chain: 消息列表
        :param quote: 引用消息号
        :return: 响应信息
        """

        # 添加调试信息
        if GlobalValues.debug_var.get():
            message_chain.add_plain_text("[调试]")

        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "group": group,
            "messageChain": message_chain.get_message_chain()
        }
        if quote is not None:
            data["quote"] = quote
        return RequestSender.send_post("sendGroupMessage", data)

    @staticmethod
    def recall_message(message_id: int) -> dict:
        """
        撤回消息

        撤回群内消息的，需要有对应权限

        发送消息两分钟内可以撤销

        :param message_id: 撤回消息号
        :return: 响应结果
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": message_id
        }
        return RequestSender.send_post("recall", data)

    @staticmethod
    @DeprecationWarning
    def send_image_message_by_url(
            urls: list,
            qq: int = None,
            group: int = None
    ) -> dict:
        """
        通过url发送图片，由于出现不知如何解决的问题，请不要使用这个方法，而是使用messageChain代替

        如果传入了参数qq，则向该qq好友发送图片

        如果传入了群号，则向对应群发送图片

        如果传入了参数qq了群号，则发送临时消息图片

        :param urls: 图片url列表
        :param qq: qq号
        :param group: 群号
        :return: 响应信息
        """
        import warnings
        warnings.warn("请不要使用该方法，会抛出异常，按照报错推断应该是mirai http本身的问题", DeprecationWarning)
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "urls": urls
        }
        if qq is not None:
            data["qq"] = qq
        if group is not None:
            data["group"] = group
        return RequestSender.send_post("sendImageMessage", data)

    @staticmethod
    def fetch_message(count: int) -> dict:
        """
        获取bot接收到的最老消息和最老各类事件（会从消息记录中删除）

        :param count: 获取消息数
        :return: 响应结果
        """
        request_keyword = "fetchMessage?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&count=" + str(count)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def fetch_latest_message(count: int) -> dict:
        """
        获取bot接收到的最新消息和最新各类事件（会从消息记录中删除）

        :param count: 获取消息数
        :return: 响应结果
        """
        request_keyword = "fetchLatestMessage?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&count=" + str(count)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def peek_message(count: int) -> dict:
        """
        获取bot接收到的最老消息和最老各类事件（不会从消息记录中删除）

        注意：获取到的永远是最老的那条

        :param count: 获取消息数
        :return: 响应结果
        """
        request_keyword = "peekMessage?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&count=" + str(count)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def peek_latest_message(count: int) -> dict:
        """
        获取bot接收到的最新消息和最新各类事件（不会从消息记录中删除）

        注意：获取到的永远是最新的那条

        :param count: 获取消息数
        :return: 响应结果
        """
        request_keyword = "peekLatestMessage?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&count=" + str(count)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def get_message_from_id(id: int) -> dict:
        """
        通过消息号获取某条消息

        :param id: 消息号
        :return: 响应结果
        """
        request_keyword = "messageFromId?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&id=" + str(id)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def get_message_count() -> dict:
        """
        获取缓存消息总数（不包含被删除的）

        :return: 响应结果
        """
        request_keyword = "countMessage?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def get_friend_list() -> dict:
        """
        获取好友列表

        :return: 响应结果
        """
        request_keyword = "friendList?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def get_group_list() -> dict:
        """
        获取群列表

        :return: 响应结果
        """
        request_keyword = "groupList?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def set_mute(group: int, member_qq: int, time: int = None) -> dict:
        """
        设置禁言

        :param group: 指定群号
        :param member_qq: 指定成员qq号
        :param time: 禁言时间，默认为0
        :return: 响应结果
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": int(group),
            "memberId": member_qq,
        }
        if time is not None:
            data["time"] = time
        return RequestSender.send_post("mute", data)

    @staticmethod
    def set_unmute(group: int, member_qq: int) -> dict:
        """
        解除禁言

        :param group: 群号
        :param member_qq: 成员qq号
        :return: 响应信息
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group,
            "memberId": member_qq
        }
        return RequestSender.send_post("unmute", data)

    @staticmethod
    def kick_member(group: int, member_qq: int, msg: str = None) -> dict:
        """
        移除指定成员（需要有相关权限）

        :param group: 群号
        :param member_qq: 成员qq
        :param msg: 移除消息（？）
        :return: 响应信息
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group,
            "memberId": member_qq
        }
        if msg is not None:
            data["msg"] = msg
        return RequestSender.send_post("kick", data)

    @staticmethod
    def quit_group(group: int) -> dict:
        """
        退出群聊

        :param group: 群号
        :return: 响应结果
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group
        }
        return RequestSender.send_post("quit", data)

    @staticmethod
    def mute_all(group: int) -> dict:
        """
        禁言全体

        :param group: 指定群号
        :return: 响应结果
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group
        }
        return RequestSender.send_post("muteAll", data)

    @staticmethod
    def unmute_all(group: int) -> dict:
        """
        解除全体禁言

        :param group:群号
        :return: 响应结果
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group
        }
        return RequestSender.send_post("unmuteAll", data)

    @staticmethod
    def get_group_config(group: int) -> dict:
        """
        获取群设置

        :param group: 群号
        :return: 响应信息
        """
        request_keyword = "groupConfig?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&target=" + str(group)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def set_group_config(
            group: int,
            group_name: str = None,
            group_announcement: str = None,
            confess_talk: bool = None,
            allow_member_invite: bool = None,
            auto_approve: bool = None,
            anonymous_chat: bool = None
    ) -> dict:
        """
        修改群设置

        :param group: 群号
        :param group_name: 群名称
        :param group_announcement: 群公告
        :param confess_talk: 是否开启坦白说
        :param allow_member_invite: 是否允许群员邀请
        :param auto_approve: 是否开启自动审批入群
        :param anonymous_chat: 是否允许匿名聊天
        :return: 返回结果
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group,
            "config": {}
        }
        if group_name is not None:
            data["config"]["name"] = group_name
        if group_announcement is not None:
            data["config"]["announcement"] = group_announcement
        if confess_talk is not None:
            data["config"]["confessTalk"] = confess_talk
        if allow_member_invite is not None:
            data["config"]["allowMemberInvite"] = allow_member_invite
        if auto_approve is not None:
            data["config"]["autoApprove"] = auto_approve
        if anonymous_chat is not None:
            data["config"]["anonymousChat"] = anonymous_chat
        return RequestSender.send_post("groupConfig", data)

    @staticmethod
    def get_member_info(group: int, member_qq: int) -> dict:
        """
        获取群成员资料

        :param group: 群号
        :param member_qq: 成员qq号
        :return: 响应信息
        """
        request_keyword = "memberInfo?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        request_keyword += "&target=" + str(group)
        request_keyword += "&memberId=" + str(member_qq)
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def set_member_info(
            group: int,
            member_id: int,
            name: str = None,
            special_title: str = None
    ) -> dict:
        """
        设置群成员信息

        :param group: 群号
        :param member_id: 成员qq号
        :param name: 新的群名片
        :param special_title: 新的群头衔
        :return:
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "target": group,
            "memberId": member_id,
            "info": {}
        }
        if name is not None:
            data["info"]["name"] = name
        if special_title is not None:
            data["info"]["specialTitle"] = special_title
        return RequestSender.send_post("memberInfo", data)

    @staticmethod
    def get_session_config() -> dict:
        """
        获取session配置

        :return: 响应结果
        """
        request_keyword = "config?sessionKey="
        request_keyword += GlobalValues.conn_session_key
        return RequestSender.send_get(request_keyword)

    @staticmethod
    def set_session_config(
            cache_size: int = None,
            enable_websocket: bool = None
    ) -> dict:
        """
        设置session配置

        :param cache_size: 缓存大小
        :param enable_websocket: 是否开启Websocket
        :return: 响应信息
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key
        }
        if cache_size is not None:
            data["cacheSize"] = cache_size
        if enable_websocket is not None:
            data["enableWebsocket"] = enable_websocket
        return RequestSender.send_post("config", data)

    # 此处没有注册Mirai指令相关的包装

    @staticmethod
    def resp_new_friend_request(
            event_id: int,
            from_qq: int,
            group_id: int,
            operate: int,
            message: str
    ):
        """
        处理添加新好友事件

        :param event_id: 事件号
        :param from_qq: 申请人qq
        :param group_id: 申请人所在群，为0表示不是从群内 添加
        :param operate: 响应操作类型，0表示同意，1表示拒绝，2表示拒绝并拉黑
        :param message: 回复的信息
        :return: 无
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "eventId": event_id,
            "fromId": from_qq,
            "groupId": group_id,
            "operate": operate,
            "message": message
        }
        return RequestSender.send_post("resp/newFriendRequestEvent", data)

    @staticmethod
    def resp_member_join_request(
            event_id: int,
            from_qq :int,
            group_id: int,
            operate: int,
            message: str
    ):
        """
        处理入群申请

        :param event_id: 事件号
        :param from_qq: 申请人qq
        :param group_id: 加的群号
        :param operate: 响应操作类型，0同意，1拒绝，2忽略，3拒绝并拉黑不再接受请求，4忽略并拉黑不再接受请求
        :param message: 回复信息
        :return:
        """
        data = {
            "sessionKey": GlobalValues.conn_session_key,
            "eventId": event_id,
            "fromId": from_qq,
            "groupId": group_id,
            "operate": operate,
            "message": message
        }
        return RequestSender.send_post("resp/memberJoinRequestEvent", data)

    @staticmethod
    def resp_bot_invited_join_group_request_event(
            event_id: int,
            from_qq: int,
            group_id: int,
            operate: int,
            message: str
    ):
        """
        处理被邀请入群申请

        :param event_id: 事件号
        :param from_qq: 邀请人qq
        :param group_id: 被邀请入群群号
        :param operate: 被邀请入群群名
        :param message: 回复的信息
        :return: 无
        """
        data = {
            "sessionKey": GlobalValues,
            "eventId": event_id,
            "fromId": from_qq,
            "groupId": group_id,
            "operate": operate,
            "message": message
        }
        return RequestSender.send_post("resp/botInvitedJoinGroupRequestEvent", data)