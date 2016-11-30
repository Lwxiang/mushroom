# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('magnet', models.TextField(verbose_name='\u78c1\u529b\u94fe\u63a5')),
                ('torrent', models.TextField(default=b'', verbose_name='\u79cd\u5b50\u6587\u4ef6')),
                ('name', models.TextField(default=b'', verbose_name='\u6587\u4ef6\u540d')),
                ('uid', models.TextField(default=b'', verbose_name='ID')),
                ('state', models.TextField(default=b'Waiting', verbose_name='\u72b6\u6001')),
                ('down_speed', models.TextField(default=b'0.0 KiB/s', verbose_name='\u4e0b\u8f7d\u901f\u5ea6')),
                ('up_speed', models.TextField(default=b'0.0 KiB/s', verbose_name='\u4e0a\u4f20\u6570\u5ea6')),
                ('seeds', models.TextField(default=b'0', verbose_name='\u79cd\u5b50\u6570')),
                ('peers', models.TextField(default=b'0', verbose_name='\u8fde\u63a5\u6570')),
                ('availability', models.TextField(default=b'0.0', verbose_name='\u6709\u6548\u7387')),
                ('size', models.TextField(default=b'0.0 KiB/0.0 KiB', verbose_name='\u6587\u4ef6\u5927\u5c0f')),
                ('ratio', models.TextField(default=b'-1.000', verbose_name='\u6bd4\u7387')),
                ('seed_time', models.TextField(default=b'0 days 00:00:00', verbose_name='\u79cd\u5b50\u65f6\u95f4')),
                ('active', models.TextField(default=b'0 days 00:00:00', verbose_name='\u6d3b\u8dc3\u65f6\u95f4')),
                ('tracker_status', models.TextField(default=b'', verbose_name='\u6765\u6e90\u72b6\u6001')),
                ('progress', models.TextField(default=b'0.00%', verbose_name='\u8fdb\u5ea6')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('done_time', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('operate', models.CharField(max_length=100, verbose_name='\u64cd\u4f5c\u6307\u4ee4', choices=[(b'Pause', '\u6682\u505c'), (b'Download', '\u4e0b\u8f7d'), (b'MakeTorrent', '\u6b63\u5728\u8f6c\u6362torrent/magnet'), (b'FetchTorrent', '\u672c\u5730\u83b7\u53d6torrent/magnet')])),
                ('is_removed', models.BooleanField(default=False, verbose_name='\u662f\u5426\u79fb\u9664')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1',
                'verbose_name_plural': '\u4efb\u52a1',
            },
        ),
    ]
