# -*- coding:utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^$', 'home.views.handler'),
                       url(r'monitor/$', 'home.views.monitor'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
