from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor


class VisualEditor(forms.ModelForm):
    is_hidden = False
    class Meta:
        model = FlatPage
        fields = '__all__'
        widgets = {
           'content': RedactorEditor(),
        }


class FlatPageCustom(FlatPageAdmin):
    form = VisualEditor


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)