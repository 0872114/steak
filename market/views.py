#!python
# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from b2c.models import Order


def bidmarket(request):
    args = {}
    list = []
    orders = Order.objects.filter(market=True).order_by('datetime').reverse()
    for order in orders:
        order_data = dict(
            id = u'%s' % (order.id),
            market = order.market,
            status = order.get_status_display(),
            email = order.email,
            datetime = order.datetime,
            sender = order.sender,
            service = order.service,
            comment = order.comment,
        )
        list.append(order_data)
    tuple(list)
    return render_to_response('market/market.html', { 'orders' : list})