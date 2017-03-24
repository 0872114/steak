#!python
# -*- coding: utf8 -*-

from django.forms import ModelForm
from models import ChatMessage


class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        exclude = ['date']