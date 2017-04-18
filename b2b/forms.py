#!python
# -*- coding: utf8 -*-

from models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms

class b2bCForm(UserCreationForm):
    class Meta:
        model = Printer
        fields = ('username', 'password1', 'address', 'password2', 'name', 'first_name', 'middle_name', 'last_name', 'phone', 'email', 'website', 'services',
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
        self.fields['username'].help_text = _(u'Обязательное поле. Не более 30 символов. Только английские буквы, цифры и символы @/./+/-/_.')
        self.fields['phone'].help_text = _(u'Указанный телефон будет виден всем пользователям.')
        self.fields['tags'].help_text = _(u'Для выбора нескольких тегов зажмите Ctrl.')
        self.fields['categories'].help_text = _(u'Для выбора нескольких категорий зажмите Ctrl.')
        self.fields['address'].widget = forms.HiddenInput()
        self.fields['lat'].widget = forms.HiddenInput()
        self.fields['lon'].widget = forms.HiddenInput()