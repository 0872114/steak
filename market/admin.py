#!python
# -*- coding: utf8 -*-

from django.contrib import admin
from models import *


class MarketCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(MarketComment, MarketCommentAdmin)
