# -*- coding:utf-8 -*-
from django.db import models


class Operator(object):
    PAUSE = "Pause"
    DOWNLOAD = "Download"
    MAKE = "MakeTorrent"
    FETCH = "FetchTorrent"


operator_choice = (
    (Operator.PAUSE, u'暂停'), (Operator.DOWNLOAD, u'下载'),
    (Operator.MAKE, u'正在转换torrent/magnet'), (Operator.FETCH, u'本地获取torrent/magnet'),
)


class Work(models.Model):
    """
    Download Work
    """
    # Basic
    magnet = models.TextField(u'磁力链接')
    torrent = models.TextField(u'种子文件', default='')
    name = models.TextField(u'文件名', default='')
    uid = models.TextField(u'ID', default='')
    state = models.TextField(u'状态', default='Waiting')
    down_speed = models.TextField(u'下载速度', default="0.0 KiB/s")
    up_speed = models.TextField(u'上传数度', default="0.0 KiB/s")
    seeds = models.TextField(u'种子数', default='0')
    peers = models.TextField(u'连接数', default='0')
    availability = models.TextField(u'有效率', default='0.0')
    size = models.TextField(u'文件大小', default="0.0 KiB/0.0 KiB")
    ratio = models.TextField(u'比率', default='-1.000')
    seed_time = models.TextField(u'种子时间', default="0 days 00:00:00")
    active = models.TextField(u'活跃时间', default="0 days 00:00:00")
    tracker_status = models.TextField(u'来源状态', default='')
    progress = models.TextField(u'进度', default='0.00%')

    # Time
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)
    done_time = models.DateTimeField(u'结束时间', blank=True, null=True)

    # Flag
    operate = models.CharField(u'操作指令', choices=operator_choice, max_length=100)
    is_removed = models.BooleanField(u'是否移除', default=False)

    class Meta:
        verbose_name = u'任务'
        verbose_name_plural = u'任务'

    def __unicode__(self):
        return str(self.id)

    def get_operate_name(self):
        for o in operator_choice:
            if self.operate == o[0]:
                return o[1]
        return ""

    def update_params(self, data):
        self.name = data.get('Name', '')
        self.uid = data.get('ID', '')
        self.state = data.get('State', '')
        self.down_speed = data.get('SpeedDown', '0.0 KiB/s')
        self.up_speed = data.get('SpeedUp', '0.0 KiB/s')
        self.seeds = data.get('Seeds', '0')
        self.peers = data.get('Peers', '0')
        self.availability = data.get('Availability', '0.00')
        self.size = data.get('Size', '0.0 KiB/0.0 KiB')
        self.ratio = data.get('Ratio', '-1.000')
        self.seed_time = data.get('SeedTime', '0 days 00:00:00')
        self.active = data.get('Active', '0 days 00:00:00')
        self.tracker_status = data.get('Tracker', '')
        self.progress = data.get('Progress', '0.00%')
        self.save()
