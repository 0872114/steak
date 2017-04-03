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
        exclude = ['datetime', 'status']

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
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tags.objects.all()
        self.fields["destination"].required = False


class StatusForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status', ]

    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({
            "onchange": "this.form.submit()"
        })


class SetDestinationForm(ModelForm):
    class Meta:
        model = Order
        fields = ['destination']

    def __init__(self, *args, **kwargs):
        super(SetDestinationForm, self).__init__(*args, **kwargs)
        self.fields['destination'].widget.attrs.update({
            "onchange": "this.form.submit()"
        })
