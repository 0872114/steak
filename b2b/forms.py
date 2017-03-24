
from django import forms
from models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms.widgets import CheckboxSelectMultiple


class b2bCForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ('name', 'email', 'address', 'phone', 'website', 'services', 'lat', 'lon', 'logo', 'categories', 'tags')

