#!python
# -*- coding: utf8 -*-


from django.shortcuts import render_to_response, redirect
from forms import b2bCForm
from django.template.context_processors import csrf



def register(request):
    args = {}
    args.update(csrf(request))

    args['printers'] = b2bCForm
    if request.POST:
        printer_form = b2bCForm(request.POST, request.FILES)
        if printer_form.is_valid():
            printer_form.logo = request.FILES
            printer_form.save()
        else:
            args['printers'] = printer_form
    return render_to_response('rstr/register.html', args)



