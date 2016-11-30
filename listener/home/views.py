# -*- coding:utf-8 -*-
import json

from django.http import HttpResponse
from wechat_sdk import WechatBasic

from listener.settings import appToken, keyword_check, keyword_download, keyword_pause, keyword_remove
from models import Operator, Work


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

    # check message type
    if message.type != 'text':
        return HttpResponse(wechat.response_text(u'说人话'))

    # check if magnet
    if message.content.startswidth("magnet:?xt=urn:btih:"):
        work = Work(magnet=message.content, operate=Operator.DOWNLOAD)
        work.save()
        return HttpResponse(wechat.response_text(u'链接已添加！回复【%s】显示详情。' % keyword_check))

    # user check
    if message.content == keyword_check:
        works = Work.objects.filter(is_removed=False).order_by('-create_time')
        work_list = u'任务详情：\n'
        for index, work in enumerate(works):
            name = work.name if work.name else u'名字解析中'
            speed = work.down_speed
            progress = work.progress
            operate = work.get_operate_name()
            work_list += "%d. %s [%s] [%s] [%s]\n" % (index, name, speed, progress, operate)
        work_list += u'回复【%s】=下载，【%s】=暂停，【%s】=删除，后跟相应数字' % (
            keyword_download, keyword_pause, keyword_remove)
        return HttpResponse(wechat.response_text(work_list))

    return HttpResponse(wechat.response_text(u'待开发'))


def monitor(request):
    """
    daemon agent backend monitor
    :param request:
    :return:
    """
    if request.method != "POST":
        return HttpResponse(json.dumps({'result': False, 'message': 'post required', 'data': {}}))

    try:
        post_data = json.loads(request.POST.get('data', '[]'))
    except (Exception,):
        return HttpResponse(json.dumps({'result': False, 'message': 'params invalid', 'data': {}}))

    # post data
    for single_data in post_data:
        magnet = single_data.get('Magnet', '')
        try:
            work = Work.objects.get(magnet=magnet)
            work.update_params(single_data)
        except (Exception,):
            continue

    # get operate
    works = Work.objects.all()
    data = []
    for single_work in works:
        data.append({
            'magnet': single_work.magnet,
            'operate': single_work.operate
        })
    return HttpResponse(json.dumps({'result': True, 'message': 'Success', 'data': json.dumps(data)}))
