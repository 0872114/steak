#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Printer(User):
    user = models.OneToOneField(User, null=False)
    name = models.CharField(_(u'Название компании'), max_length=30)
    middle_name = models.CharField(_(u'Отчество'), default='', blank=True, max_length=30)
    address = models.CharField(_(u'Адрес'), max_length=500)
    phone = models.CharField(_(u'Контактный номер телефона'), max_length=15)
    website = models.URLField(_(u'Вебсайт'))
    services = models.CharField(_(u'Услуги'), max_length=50)
    lat = models.FloatField(_(u'Широта'))
    lon = models.FloatField(_(u'Долгота'))
    logo = models.ImageField(_(u'Логотип'), upload_to="printers", blank=True)
    categories = models.ManyToManyField('b2b.Categories', verbose_name=u'Категории')
    tags = models.ManyToManyField('b2b.Tags', verbose_name=u'Теги')
    subscribed = models.BooleanField(_(u'Подписка активна'), default=False)
    sub_expires = models.DateTimeField(_(u'Подписка истекает'), null=True)
    metro = models.CharField(_(u'Метро'), max_length=150, blank=True)
    schedule = models.CharField(_(u'Время работы'), max_length=150, blank=True)

    class Meta:
        verbose_name = _(u'Печатник')
        verbose_name_plural = _(u'Печатники')

    def __unicode__(self):
        return u'%s' % (self.name)


class Categories(models.Model):
    category = models.CharField(_(u'Категория'), max_length=50)

    class Meta:
        verbose_name = _(u'Категория')
        verbose_name_plural = _(u'Категории')

    def __unicode__(self):
        return u'%s' % (self.category)


class Tags(models.Model):
    tag = models.CharField(_(u'Тег'), max_length=50)
    cat = models.ManyToManyField(
        'b2b.Categories', verbose_name=u'Категории'
    )

    class Meta:
        verbose_name = _(u'Тег')
        verbose_name_plural = _(u'Теги')

    def __unicode__(self):
        return u'%s' % (self.tag)
