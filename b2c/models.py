#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
    NEW = 'new'
    ACTIVE = 'active'
    DECLINED = 'declined'
    FINISHED = 'finished'
    STATUS_CHOICES = (
        (NEW, 'Новый'),
        (ACTIVE, 'В работе'),
        (DECLINED, 'Отказ'),
        (FINISHED, 'Выполнен'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default=NEW, max_length=50, blank=False)
    email = models.EmailField(_(u'Email'))
    datetime = models.DateTimeField(_(u'Время создания'), default=timezone.now)
    sender = models.CharField(_(u'Отправитель'), max_length=50)
    user = models.ForeignKey(
        User,
        related_name='order_user',
        on_delete=models.CASCADE,
        default='',
        null = True,
    )
    phone = models.CharField(_(u'Телефон'), max_length=15, blank=True)
    destination = models.ForeignKey(
        'b2b.Printer',
        on_delete=models.CASCADE,
        blank=True,
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
    market = models.BooleanField(_(u'На рынке заявок'), default=False)

    class Meta:
        verbose_name = _(u'Заявка')
        verbose_name_plural = _(u'Заявки')

    def __unicode__(self):
        return self.service