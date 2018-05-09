# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.
class GoodsInfoInline(admin.StackedInline):
    model = GoodsInfo
    extra = 5

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle', 'isDelete']
    inlines = [GoodsInfoInline]

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'isDelete']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)