#!python
# -*- coding: utf8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Superuser (models.Model):
    reciever = models.EmailField(_(u'Paypal Аккаунт'))
    amout = models.IntegerField(_(u'Стоимость подписки'))

    class Meta:
        verbose_name = _(u'Paypal')
        verbose_name_plural = _(u'Paypal')


