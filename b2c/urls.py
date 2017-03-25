from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', map, name="map"),
    url('^market/order/$', market, name="market"),
]