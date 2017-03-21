#!python
# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from forms import OrderForm
from django.template.context_processors import csrf
from b2b.models import Printer


def map(request):
    printers = Printer.objects.all()[:50]
    args = {}
    args.update(csrf(request))
    args['form'] = OrderForm
    args['printers'] = []

    for printer in printers:
        marker = dict(
            coords_name = "lalo_" + str(printer.id),
            lat = str(printer.lat).replace(',', '.'),
            lon = str(printer.lon).replace(',', '.'),
            marker_name = "marker_" + str(printer.id),
            address = printer.address,
            name = printer.name
        )
        args['printers'].append(marker)
    tuple(args['printers'])

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')

    return render_to_response('b2c/map.html', args)
