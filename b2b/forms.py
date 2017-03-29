from models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

#!python
# -*- coding: utf8 -*-


class b2bCForm(UserCreationForm):
    class Meta:
        model = Printer
        fields = ('username', 'password1', 'address', 'password2', 'name', 'email', 'phone', 'website', 'services',
                   'lat', 'lon', 'logo', 'categories', 'tags')

    def __init__(self, *args, **kwargs):
        super(b2bCForm, self).__init__(*args, **kwargs)
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
        self.fields['address'].widget = forms.HiddenInput()
        self.fields['lat'].widget = forms.HiddenInput()
        self.fields['lon'].widget = forms.HiddenInput()