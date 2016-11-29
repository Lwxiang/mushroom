# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from wechat_sdk import WechatBasic

from listener.settings import appToken


def handler(request):
    """
    wechat backend handler
    :param request:
    :return:
    """
    if request.method == "GET":
        # wechat server signature
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', '')
        wechat = WechatBasic(token=appToken)
        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse('INVALID')
    else:
        # text from user
        body_text = request.body
        wechat = WechatBasic(token=appToken)
        wechat.parse_data(body_text)

        # get wechat message
        message = wechat.get_message()


