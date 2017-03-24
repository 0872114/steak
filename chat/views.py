#!python
# -*- coding: utf8 -*-

from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from models import *
from forms import ChatMessageForm


def ChatView(request):
    args = {}
    args.update(csrf(request))
    args['form'] = ChatMessageForm()
    if request.user:
        useless = request.user
        use_this = User.objects.get(username=useless).id
        args['order'] = 1
        args['sender'] = use_this
        receiverid = request.POST.get('user')
        if 'last_message' in request.POST:
            msgs = ChatMessage.objects.filter(id > request.POST.get('id'), sender=request.POST.get('sender'))
            args['msgs'] = iterations(msgs)
            return render_to_response('chat/chat.html', args)

        if 'message' in request.POST:
            form = ChatMessageForm(request.POST)
            if form.is_valid():
                form.sender = use_this
                form.save()
                return redirect('./')
        else:
            msgs = ChatMessage.objects.filter(sender=use_this)
            args['msgs'] = iterations(msgs)
            return render_to_response('chat/chat.html', args)


    else:
        return render_to_response("<html><body> Hello World </body></html>")



def iterations(x):
    kek = []
    for msg in x:
        usefull_shit = dict(
            sender=msg.sender,
            date=msg.date,
            message=msg.message,
            id=msg.id
        )
        kek.append(usefull_shit)
    return tuple(kek)

