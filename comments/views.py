#!python
# -*- coding: utf8 -*-

from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from b2b.models import Printer


def show_comments(request, id=None):
    if id is None:
        return redirect('./')
    else:
        printer = Printer.objects.get(id=id)
        data = dict(
            id=printer.id,
            name=printer.name,
            address=printer.address,
            phone=printer.phone,
            website=printer.website,
            services=printer.services,
        )
        try:
            data['logo'] = printer.logo.url
        except ValueError:
            data['logo'] = None
        try:
            data['metro'] = printer.metro
        except ValueError:
            data['metro'] = "N/A"
        try:
            data['schedule'] = printer.schedule
        except ValueError:
            data['schedule'] = "N/A"
        args = dict(printer = data, )
        return render(request, "comments/comments.html", args)

