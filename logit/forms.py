#!python
# -*- coding: utf8 -*-

from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
                       help_text=_(u"Обязательное поле."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = _(
            u'Обязательное поле. Не более 30 символов. Только английские буквы, цифры и символы @/./+/-/_.')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
