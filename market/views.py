#!python
# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from b2c.models import Order
from django.utils import timezone


def prepare_orders(orders):
    now = timezone.now()
    list = []

    for order in orders:
        order_data = dict(
            id = order.id,
            market = order.market,
            status = order.get_status_display(),
            email = order.email,
            datetime = order.datetime,
            sender = order.sender,
            user=order.user,
            service = order.service,
            comment = order.comment,
            destination = order.destination,
        )

        #Find out if order.destination.id exists (if an order is taken)
        try:
            order.destination.id
            order_data['taken'] = 1
        except AttributeError:
            order_data['taken'] = 0

        #Count full hours between now and when the order was created
        time_diff_hours = divmod((now - order.datetime).total_seconds(), 3600)[0]

        #Mark 3+ hours old unprocessed orders red, the new ones green,
        if (order.status == 'new'):
            if (time_diff_hours >= 3):
                order_data['tr_class'] = 'tr-market-red'
            else:
                order_data['tr_class'] = 'tr-market-green'
        list.append(order_data)
    tuple(list)#Tuples weigh less and process faster then lists
    return list

def bidmarket(request):
    orders = Order.objects.filter(market=True).exclude(user__isnull=True).order_by('datetime').reverse()
    list = prepare_orders(orders)
    return render_to_response('market/market.html', {'orders': list})

def received_orders(request):
    if request.user.id:
        orders = Order.objects.filter(destination__user_id=request.user.id).order_by('datetime').reverse()
        list = prepare_orders(orders)
        return render_to_response('market/received_orders.html', {'orders': list, 'id' : request.user.id})
    else:
        return render_to_response('please_login.html')