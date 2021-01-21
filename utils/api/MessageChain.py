# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 23:42
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : MessageChain.py
# @Software: PyCharm

class MessageChain:
    """
    用于处理消息列表messageChain
    """

    def __init__(self):
        # 创建一个列表，该列表用于作为messageChain
        self.__message_chain = []

    def __add(self, message_block: dict) -> None:
        """
        添加到message_chain中

        :param message_block: message_chain中的其中一个元素
        :return: 无
        """
        self.__message_chain.append(message_block)

    def get_message_chain(self) -> list:
        """
        获取message_chain列表

        :return: message_chain
        """
        return self.__message_chain

    def add_at(self, member_id: int) -> None:
        """
        艾特某人，仅在群中使用有效

        :param member_id: 群成员qq
        :return: 无
        """
        self.__add({
            "type": "At",
            "target": member_id
        })

    def add_at_all(self) -> None:
        """
        艾特全体成员，只有在群中有效

        :return: 无
        """
        self.__add({
            "type": "AtAll"
        })

    def add_face(self, face_id: int = None, name: str = None) -> None:
        """
        添加表情符号
        :param face_id: 表情编号，优先于name
        :param name: 表情名称（测试发现此处应该传入中文，如：斜眼笑）
        :return: 无
        """
        message_block = {
            "type": "Face"
        }
        if face_id is not None:
            message_block["faceId"] = face_id
        if name is not None:
            message_block["name"] = name
        self.__add(message_block)

    def add_plain_text(self, text: str) -> None:
        """
        添加纯文本

        :param text: 文本内容
        :return: 无
        """
        self.__add({
            "type": "Plain",
            "text": text
        })

    def add_image(
            self,
            group_image_id: str = None,
            friend_image_id: str = None,
            url: str = None,
            path: str = None
    ) -> None:
        """
        添加图片内容

        :param friend_image_id: 好友图片id，此处与好有图片冲突，没有弄清楚使用方法
        :param group_image_id: 群图片id，此处与好友图片冲突，没有弄清楚使用方法
        :param url: 图片url地址，优先于本地路径
        :param path: 本地路径
        :return: 无
        """
        message_block = {
            "type": "Image"
        }
        if group_image_id is not None and friend_image_id is not None:
            return
        if group_image_id is not None:
            message_block["imageId"] = group_image_id
        if friend_image_id is not None:
            message_block["imageId"] = friend_image_id
        if url is not None:
            message_block["url"] = url
        if path is not None:
            message_block["path"] = path
        self.__add(message_block)

    def add_flash_image(
            self,
            group_image_id: str = None,
            friend_image_id: str = None,
            url: str = None,
            path: str = None
    ) -> None:
        """
        发送闪照

        :param friend_image_id: 好友图片id，此处与好有图片冲突，没有弄清楚使用方法
        :param group_image_id: 群图片id，此处与好友图片冲突，没有弄清楚使用方法
        :param url: 图片url地址，优先于本地路径
        :param path: 本地路径
        :return: 无
        """
        message_block = {
            "type": "FlashImage"
        }
        if group_image_id is not None and friend_image_id is not None:
            return
        if group_image_id is not None:
            message_block["imageId"] = group_image_id
        if friend_image_id is not None:
            message_block["imageId"] = friend_image_id
        if url is not None:
            message_block["url"] = url
        if path is not None:
            message_block["path"] = path
        self.__add(message_block)

    def add_voice(
            self,
            voice_id: str = None,
            url: str = None,
            path: str = None
    ) -> None:
        """
        发送语音

        在该方法中，文件过大插件会抛出OverFileSizeMaxException异常，
        该异常无法在此处处理，且原作者似乎未提供文件的限制大小，
        请确保在此处正式使用该方法前测试是否抛出JSON方面的异常

        :param voice_id: 语音号，优先级最高，按照参数顺序逐渐降低
        :param url: url地址
        :param path: 本地路径
        :return: 无
        """
        message_block = {
            "type": "Voice"
        }
        if voice_id is not None:
            message_block["voiceId"] = voice_id
        if url is not None:
            message_block["url"] = url
        if path is not None:
            message_block["path"] = path
        self.__add(message_block)

    def add_xml(self, xml: str) -> None:
        """
        添加xml文本

        :param xml: xml文本内容
        :return: 无
        """
        self.__add({
            "type": "Xml",
            "xml": xml
        })

    def add_json(self, json: str) -> None:
        """
        添加json文本

        :param json: json文本内容
        :return: 无
        """
        self.__add({
            "type": "Json",
            "json": json
        })

    def add_app(self, app: str) -> None:
        """
        我也不懂这是什么，就先写在这里吧

        :param app: app内容
        :return: 无
        """
        self.__add({
            "type": "App",
            "content": app
        })

    def add_poke(self, poke: str) -> None:
        """
        戳一戳类型

        类型名有：

        "Poke": 戳一戳\n
        "ShowLove": 比心\n
        "Like": 点赞\n
        "Heartbroken": 心碎\n
        "SixSixSix": 666\n
        "FangDaZhao": 放大招

        :param poke: 类型名
        :return: 无
        """
        self.__add({
            "type": "Poke",
            "name": poke
        })