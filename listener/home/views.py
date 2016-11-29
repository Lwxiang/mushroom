# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from wechat_sdk import WechatBasic

from listener.settings import appToken
from Magnet2Torrent.Magnet_To_Torrent2 import magnet2torrent


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

    # text from user
    body_text = request.body
    wechat = WechatBasic(token=appToken)
    wechat.parse_data(body_text)

    # get wechat message
    message = wechat.get_message()

    if message.type != 'text':
        return HttpResponse(wechat.response_text(u'说人话'))

    out = magnet2torrent(message.content)
    return HttpResponse(wechat.response_text(out))




