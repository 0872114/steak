#!python
# -*- coding: utf8 -*-

""" Адреса уровня приложения

    Внутренние урлы работают, если их заинклудить в базовых урлах

    # grill/urls.py:
    ...
    url(r'^sample/', include('sample.urls')),
    ...

    Добавляются к урлу, указанному в инклуде, то есть sample/ как префикс,

    в данном случае - sample/subaddr:
    ...
    url(r'subaddr', home),
    ...

    ниже в коде работает адрес просто sample/
"""


from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'', home),
]