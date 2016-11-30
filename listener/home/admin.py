# -*- coding:utf-8 -*-
from django.contrib import admin

from models import Work


class WorkAdmin(admin.ModelAdmin):
    list_display = ('magnet', 'name')


admin.site.register(Work, WorkAdmin)
