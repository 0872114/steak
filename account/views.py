#!python
# -*- coding: utf8 -*-

from forms import *
from django.shortcuts import render
from b2b.models import Printer
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def account(request):
    is_printer = check_printer(request)
    return render(request, 'account/personal_account.html', {'is_printer': is_printer})


def slave_account(request):
    args = {'is_printer': check_printer(request)}
    instance = User.objects.get(id=request.user.id)
    if request.POST:
        form = UpdateProfile(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('./')
    args['form'] = UpdateProfile(request.POST or None, instance=instance)
    args['page'] = 'user_data'
    return render(request, 'account/slave.html', args)


def master_account(request):
    args = {'is_printer': check_printer(request)}
    instance = Printer.objects.get(id=request.user.id)
    if request.POST:
        form = B2bUpdateProfile(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('./')
    args['form'] = B2bUpdateProfile(request.POST or None, instance=instance)
    args['page'] = 'printer_data'
    return render(request, 'account/master.html', args)


def change_password(request):
    args = {'is_printer': check_printer(request)}
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, u'Вы успешно сменили пароль!')
            return redirect('./')
        else:
            messages.error(request, u'Пожалуйста, исправьте ошибку в пароле.')
    else:
        args['form'] = PasswordChangeForm(request.user)
    args['page'] = 'password_change'
    return render(request, 'account/password_change.html', args)


def check_printer(request):
    try:
        Printer.objects.get(user__id=request.user.id)
    except AttributeError:
        return render(request, 'please_login.html')

    except Printer.DoesNotExist:
        return False

    return True
