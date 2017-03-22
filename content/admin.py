#! python
# -- coding: utf-8 ---

from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor
from models import Entry

class EntryAdminForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        widgets = {
           'short_text': RedactorEditor(),
        }

class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
