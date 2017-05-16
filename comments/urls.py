from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^(?P<id>\d+)$', show_comments, name="comments"),
]
