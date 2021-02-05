# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 17:59
# @Author  : Lucky_He
# @Email   : 673230244@qq.com
# @File    : RequestSender.py
# @Software: PyCharm
import json

import requests

from utils.GlobalValues import GlobalValues
from utils.api.ResponseExceptions import *


class RequestSender:
    """
    提供静态方法发送GET和POST请求
    """

    @staticmethod
    def send_get(request_keyword: str) -> dict:
        """
        发送GET请求并返回响应内容

        :param request_keyword: 根据mirai http中提供的请求地址关键字，不需要拥有"/"符号
        :return: 响应信息字典
        """
        url = "http://" + GlobalValues.conn_host + ":" + GlobalValues.conn_port + "/" + request_keyword

        # GET
        s = requests.session()
        headers = {"Connection": "close"}
        response = s.get(url=url, headers=headers)

        # 只有在调试模式下才输出
        if GlobalValues.debug_var.get():
            print("Response:", response.text)

        # 调用方法检查code，并抛出异常
        RequestSender.__check_status_code(json.loads(response.text))

        # 返回的是列表
        return json.loads(response.text)

    @staticmethod
    def send_post(request_keyword: str, data: dict) -> dict:
        """
        发送POST请求并返回相应内容

        :param request_keyword: 根据mirai http中提供的请求地址关键字，不需要拥有"/"符号
        :param data: request中的data，字典类型
        :return: 响应信息字典
        """
        # 只有在调试模式下才输出
        if GlobalValues.debug_var.get():
            print("Post Request:", request_keyword, data)

        url = "http://" + GlobalValues.conn_host + ":" + GlobalValues.conn_port + "/" + request_keyword
        data = json.dumps(data)

        # POST
        s = requests.session()
        headers = {"Connection": "close"}
        response = s.post(url=url, data=data, headers=headers)

        # 只有在调试模式下才输出
        if GlobalValues.debug_var.get():
            print("Response:", response.text)

        # 调用方法检查code，并抛出异常
        RequestSender.__check_status_code(json.loads(response.text))

        # 返回的是列表
        return json.loads(response.text)

    @staticmethod
    def __check_status_code(response_dict: dict) -> None:
        """
        检查返回结果状态码，抛出对应异常

        :param response_dict: 返回结果的列表
        :return: 无
        :exception WrongAuthkeyException
        :exception BotNotExistException
        :exception SessionInvalidException
        :exception SessionNotCertifiedException
        :exception MessageReceiverNotExistException
        :exception FileNotExistException
        :exception NoPermissionException
        :exception BotSpeakNotAllowedException
        :exception TooLongMessageException
        :exception WrongAccessException
        """

        # 出现的一些特殊情况可以直接忽略
        if not isinstance(response_dict, dict):
            return
        if "code" not in response_dict.keys():
            return

        code = response_dict["code"]
        if code == 1:
            raise WrongAuthkeyException()
        if code == 2:
            raise BotNotExistException()
        if code == 3:
            raise SessionInvalidException()
        if code == 4:
            raise SessionNotCertifiedException()
        if code == 5:
            raise MessageReceiverNotExistException()
        if code == 6:
            raise FileNotExistException()
        if code == 10:
            raise NoPermissionException()
        if code == 20:
            raise BotSpeakNotAllowedException()
        if code == 30:
            raise TooLongMessageException()
        if code == 400:
            raise WrongAccessException()
