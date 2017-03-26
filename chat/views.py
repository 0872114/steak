#!python
# -*- coding: utf8 -*-

from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from models import *
from forms import ChatMessageForm
from django.http import JsonResponse
from django.db.models import Q
import json


def AjaxView(request):
    last_id = request.GET.get(u'lastmsg_id', None)
    currentOrderId = request.GET.get(u'order', None)
    msgs = ChatMessage.objects.filter(id__gt=int(last_id),order__id=int(currentOrderId))[:1]
    result = iterations_ajax(request,msgs)
    return JsonResponse(result)


def ChatView(request, id=None):
    if id is None:
        return redirect('./')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = ChatMessageForm()
        if request.user.id:
            args['order'] = id
            args['sender'] = request.user.id
            if 'message' in request.POST:
                form = ChatMessageForm(request.POST)
                if form.is_valid():
                    form.sender = request.user.id
                    form.save()
                    return redirect('./')
            else:
                msgs = ChatMessage.objects.filter(order__id=id)
                args['msgs'] = iterations(request,msgs)
                args['debug'] = request.user
                args['debug2'] = request.user.id
                return render_to_response('chat/chat.html', args)
        else:
            return render_to_response('please_login.html')



def iterations(request,x):
    kek = []
    for msg in x:
        usefull_shit = dict(
            sender=msg.sender,
            sender_id = msg.sender.id,
            order = msg.order.id,
            oder_destination = msg.order.destination.id,
            date=msg.date,
            message=msg.message,
            id=msg.id,
            style = ''
        )
        try:
            usefull_shit['order_sender'] = msg.order.user.id
        except AttributeError:
            usefull_shit['order_sender'] = 0
        if usefull_shit['sender_id'] == request.user.id:
            usefull_shit['style'] = 'fpv'  # first person view
        else:
            usefull_shit['style'] = 'tpv'  # third person view
        kek.append(usefull_shit)
    return tuple(kek)





def iterations_ajax(request, x):
    usefull_shit = dict()
    for msg in x:
        usefull_shit = dict(
            sender=str(msg.sender),
            sender_id = str(msg.sender.id),
            order = str(msg.order.id),
            oder_destination = msg.order.destination.id,
            date=msg.date,
            message=msg.message,
            id=msg.id,
            style = ''
        )
        try:
            usefull_shit['order_sender'] = msg.order.user.id
        except AttributeError:
            usefull_shit['order_sender'] = 0
        if usefull_shit['sender_id'] == str(request.user.id):
            usefull_shit['style'] = 'fpv'  # first person view
        else:
            usefull_shit['style'] = 'tpv'  # third person view
    return usefull_shit