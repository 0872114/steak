from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', bidmarket, name="market_orders"),
    url(r'^my_orders/$', received_orders, name="my_orders"),
    url(r'^order_(?P<id>\d+)$', show_order, name="market_order"),
]