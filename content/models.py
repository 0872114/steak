#!python
# -- coding: utf8 --

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')