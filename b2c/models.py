#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Order(models.Model):
    NEW = 'new'
    ACTIVE = 'active'
    DECLINED = 'declined'
    DONE = 'done'
    STATUS_CHOICES = (
        (NEW, 'Новый'),
        (ACTIVE, 'В работе'),
        (DECLINED, 'Отказ'),
        (DONE, 'Выполнен'),
    )
    status = models.CharField(_(u'Статус'), choices=STATUS_CHOICES, max_length=10, default=NEW,
                              blank=False)
    email = models.EmailField(_(u'Email'))
    datetime = models.DateTimeField(_(u'Время создания'), default=timezone.now)
    sender = models.CharField(_(u'Отправитель'), max_length=50)
    phone = models.CharField(_(u'Телефон'), max_length=15, blank=True)
    destination = models.ForeignKey(
        'b2b.Printer',
        on_delete=models.CASCADE,
        default=None,
        null = True,
    )
    service = models.CharField(_(u'Услуга'), max_length=50)
    comment = models.TextField(_(u'Комментарий'))
    categories = models.ForeignKey(
        'b2b.Categories',
        on_delete=models.CASCADE,
        default='',
        null = True,
    )
    tags = models.ManyToManyField('b2b.Tags')
    market = models.BooleanField(_(u'Участвует в рынке заявок'), default=False)


    class Meta:
        verbose_name = _(u'Заявка')
        verbose_name_plural = _(u'Заявки')

    def __unicode__(self):
        return self.service