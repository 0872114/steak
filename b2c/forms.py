#!python
# -*- coding: utf8 -*-

from django import forms
from django.forms import ModelForm
from models import Order
from b2b.models import Tags
from django.forms.widgets import CheckboxSelectMultiple


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['datetime']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
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
        self.fields["destination"].widget.attrs.update({"readonly": "readonly"})
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tags.objects.all()
