#!python
# -*- coding: utf8 -*-

from django.contrib import admin
from models import *


class ChatAdmin(admin.ModelAdmin):
    pass


admin.site.register(ChatMessage, ChatAdmin)
