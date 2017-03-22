from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'main/', main_page, name="main_page"),
    url(r'about/', about, name="about"),
    url(r'printing1/', printing1, name="printing1"),
    url(r'printing2/', printing2, name="printing2"),
    url(r'printing3/', printing3, name="printing3"),
]