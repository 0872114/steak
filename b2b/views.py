from django.shortcuts import render_to_response, redirect
from forms import b2bCForm
from django.template.context_processors import csrf
from models import Printer
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User


def register(request):
    printers = Printer.objects.all()[:50]
    args = {}
    args.update(csrf(request))

    args['printers'] = b2bCForm
    if request.POST:
        printer_form = b2bCForm(request.POST, request.FILES)
        if printer_form.is_valid():
            printer_form.save()
        else:
            args['printers'] = printer_form
    return render_to_response('rstr/register.html', args)



