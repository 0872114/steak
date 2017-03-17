#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    email = models.EmailField(_(u'Email'))
    datetime = models.DateTimeField(_(u'Время создания'), auto_now_add=False)
    sender = models.CharField(_(u'Отправитель'), max_length=50)
    destination = models.CharField(_(u'Получатель'), max_length=50)
    service = models.CharField(_(u'Услуга'), max_length=50)
    comment = models.TextField(_(u'Комментарий'), max_length=250)


    class Meta:
        verbose_name = _(u'Заявка')
        verbose_name_plural = _(u'Заявки')

    def __unicode__(self):
        return self.name