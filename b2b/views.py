#!python
# -*- coding: utf8 -*-

from django.contrib import auth
from django.shortcuts import redirect, render
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
            printer_form.save_m2m()
            newuser = auth.authenticate(
                username=printer_form.cleaned_data['username'],
                password=printer_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect('user_profile')

        else:
            args['printers'] = printer_form
    return render(request, 'rstr/register.html', args)
