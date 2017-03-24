#!python
# -*- coding: utf8 -*-


from django.conf.urls import url
from views import *

urlpatterns = [
    url('^test/', ChatView, name="chat"),
]