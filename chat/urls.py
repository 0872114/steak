#!python
# -*- coding: utf8 -*-


from django.conf.urls import url
from views import *

urlpatterns = [
    url('^chat_id_(?P<id>\d+)/$', chat_view, name="chat"),
    url('^ajax/test', ajax_view, name="chat_ajax")
]
