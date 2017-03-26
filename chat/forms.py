#!python
# -*- coding: utf8 -*-

from django.forms import ModelForm
from models import ChatMessage


class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        exclude = ['date']

    def __init__(self, *args, **kwargs):
        super(ChatMessageForm, self).__init__(*args, **kwargs)
        # add common css class to all widgets
        for field in iter(self.fields):
            # get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes += " form-control"
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                "class": classes
            })