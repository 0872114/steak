#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


class MarketComment(models.Model):
    datetime = models.DateTimeField(_(u'Время создания'), default=timezone.now)
    comment = models.TextField(_(u'Комментарий'))
    sender = models.ForeignKey(
        'b2b.Printer',
        on_delete=models.CASCADE,
        null=True,
    )
    order = models.ForeignKey(
        'b2c.Order',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = _(u'Комментарий')
        verbose_name_plural = _(u'Комментарии')

    def __unicode__(self):
        return str(self.id)
