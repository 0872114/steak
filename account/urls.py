#!python
# -*- coding: utf8 -*-

from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'profile/$', account, name="user_profile"),
    url(r'profile/data/$', slave_account, name='user_data'),
    url(r'profile/printer_data/$', master_account, name='printer_data'),
    url(r'profile/password/$', change_password, name='password_change')
]
