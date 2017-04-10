#!python
# -*- coding: utf8 -*-


from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'register/$', register, name="b2b_register"),
]
