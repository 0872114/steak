from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', map, name="b2c"),
    url('^market/', market, name="b2c"),
]