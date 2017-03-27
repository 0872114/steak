#!python
# -*- coding: utf8 -*-


from django.conf.urls import url
from views import *


urlpatterns = [
    url('^chat_id_(?P<id>\d+)/$', ChatView, name="chat"),
    url('^ajax/test', AjaxView, name="chat_ajax")
]