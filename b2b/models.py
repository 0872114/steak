#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Printer(models.Model):
    name = models.CharField(_(u'Название'), max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField()
    services = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        verbose_name = _(u'Печатник')
        verbose_name_plural = _(u'Печатники')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.email)