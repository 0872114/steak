#!python
# -*- coding: utf8 -*-

from models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms

class b2bCForm(UserCreationForm):
    class Meta:
        model = Printer
        fields = ('username', 'password1', 'address', 'password2', 'name', 'schedule', 'metro', 'first_name', 'middle_name', 'last_name', 'phone', 'email', 'website', 'services',
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
        self.fields['username'].help_text = _(u'<ul><li>Обязательное поле. Не более 30 символов. Только английские буквы, цифры и символы @/./+/-/_.</li></ul>')
        self.fields['phone'].help_text = _(u'<ul><li>Указанный телефон будет виден всем пользователям.</li></ul>')
        self.fields['tags'].help_text = _(u'<ul><li>Для выбора нескольких тегов зажмите Ctrl.</li></ul>')
        self.fields['categories'].help_text = _(u'<ul><li>Для выбора нескольких категорий зажмите Ctrl.</li></ul>')
        self.fields['password2'].help_text = _(u'<ul><li>Для подтверждения введите, пожалуйста, пароль ещё раз.</li></ul>')
        self.fields['address'].widget = forms.HiddenInput()
        self.fields['lat'].widget = forms.HiddenInput()
        self.fields['lon'].widget = forms.HiddenInput()