from models import *
from django.contrib.auth.forms import UserCreationForm

#!python
# -*- coding: utf8 -*-


class b2bCForm(UserCreationForm):
    class Meta:
        model = Printer
        fields = ('username', 'password1', 'password2', 'name', 'email', 'address', 'phone', 'website', 'services',
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