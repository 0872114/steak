#!python
# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from forms import OrderForm
from django.template.context_processors import csrf
from b2b.models import Printer
from django.db.models import Q


def map(request):
    args = {}
    args.update(csrf(request))
    args['form'] = OrderForm
    args['printers'] = []

    if 'filter' in request.POST and request.POST['filter']:
        filter = request.POST['filter']
        args['get'] = filter
        printers = Printer.objects.filter(Q(name__icontains=filter) | \
                                          Q(categories__category__icontains=filter) | \
                                          Q(tags__tag__icontains=filter)).distinct()
    else:
        printers = Printer.objects.all()[:50]
        if request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('./')

    #Fill marker template args
    for printer in printers:
        marker = dict(
            coords_name="lalo_" + str(printer.id),
            lat=str(printer.lat).replace(',', '.'),
            lon=str(printer.lon).replace(',', '.'),
            marker_name="marker_" + str(printer.id),
            address=printer.address,
            name=printer.name
        )
        args['printers'].append(marker)
    tuple(args['printers'])

    return render_to_response('b2c/map.html', args)
