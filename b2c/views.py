#!python
# -*- coding: utf8 -*-

from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.context_processors import csrf
from b2b.models import Printer, Tags
from forms import OrderForm
from datetime import datetime


def map(request, template='b2c/map.html'):
    args = {}
    args.update(csrf(request))
    args['form'] = OrderForm
    args['printers'] = []
    if request.user.id:
        user = request.user
        args['user_id'] = request.user.id
        args['user_first_name'] = user.first_name
        args['user_last_name'] = user.last_name
        args['user_email'] = user.email

    tags = Tags.objects.distinct()
    mystring = ''
    for tag in tags:
        mydict = u'%d:%d' % (tag.id, tag.cat.id)
        mystring = u'%s, %s' % (mystring, mydict)

    args['tags'] = '{%s}' % (mystring[2:])

    if 'filter' in request.POST and request.POST['filter']:
        filter = request.POST['filter']
        args['get'] = filter
        printers = Printer.objects.filter(Q(name__icontains=filter) | \
                                          Q(categories__category__icontains=filter) | \
                                          Q(tags__tag__icontains=filter) | \
                                          Q(sub_expires__gt=datetime.now()) ).distinct().order_by('name')
    else:
        printers = Printer.objects.filter(sub_expires__gt=datetime.now()).order_by('name')
        if request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('./')

    # Fill marker template args
    for printer in printers:
        marker = dict(
            coords_name="lalo_" + str(printer.id),
            lat=str(printer.lat).replace(',', '.'),
            lon=str(printer.lon).replace(',', '.'),
            marker_name="marker_" + str(printer.id),
            address=printer.address,
            name=printer.name,
            id=printer.id,
            phone=printer.phone,
            website=printer.website,
            services=printer.services,
            schedule=printer.schedule,
        )
        try:
            marker['logo'] = printer.logo.url
        except ValueError:
            marker['logo'] = None
        try:
            marker['metro'] = printer.metro
        except ValueError:
            marker['metro'] = "N/A"
        try:
            marker['schedule'] = printer.schedule
        except ValueError:
            marker['schedule'] = "N/A"
        args['printers'].append(marker)
    tuple(args['printers'])

    args['cycle'] = range(5)
    return render(request, template, args)


def market(request):
    if request.user.id:
        if request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('market_success')

        return map(request, template='b2c/market.html')
    else:
        return render(request, 'please_login.html')


def market_success(request):
        return render(request, 'b2c/market_success.html')


def sort_by_name_bubble(list):
    return True