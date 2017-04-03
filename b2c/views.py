#!python
# -*- coding: utf8 -*-

from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.context_processors import csrf

from b2b.models import Printer, Tags
from forms import OrderForm


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
                                          Q(tags__tag__icontains=filter)).distinct()
    else:
        printers = Printer.objects.all()
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
            id=printer.id
        )
        args['printers'].append(marker)
    tuple(args['printers'])

    return render(request, template, args)


def market(request):
    if request.user.id:
        return map(request, template='b2c/market.html')
    else:
        return render(request, 'please_login.html')
