#!python
# -*- coding: utf8 -*-

from django import forms
from django.contrib.auth.models import User
from b2b.models import Printer
from b2b.forms import b2bCForm


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
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


class B2bUpdateProfile(b2bCForm):
    class Meta:
        model = Printer
        fields = ('username', 'address', 'name', 'first_name', 'last_name', 'email', 'phone', 'website', 'services',
                  'lat', 'lon', 'logo', 'categories', 'tags')

    def __init__(self, *args, **kwargs):
        super(B2bUpdateProfile, self).__init__(*args, **kwargs)
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
        self.fields.pop('password1')
        self.fields.pop('password2')
