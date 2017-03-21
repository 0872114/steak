#!python
# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Printer(models.Model):
    name = models.CharField(_(u'Название'), max_length=30)
    address = models.CharField(_(u'Адрес'), max_length=50)
    email = models.EmailField(_(u'Email'))
    phone = models.CharField(_(u'Телефон'), max_length=15)
    website = models.URLField(_(u'Вебсайт'))
    services = models.CharField(_(u'Услуги'), max_length=50)
    lat = models.FloatField(_(u'Широта'))
    lon = models.FloatField(_(u'Долгота'))

    logo = models.ImageField(_(u'Логотип'), upload_to="printers", blank=True)

    categories = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
        default='',
    )
    tags = models.ForeignKey(
        'Tags',
        on_delete=models.CASCADE,
        default='',
    )


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
    cat = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
        default='',
        null = True,
        blank = True
    )


    class Meta:
        verbose_name = _(u'Тег')
        verbose_name_plural = _(u'Теги')

    def __unicode__(self):
        return u'%s [%s]%s' % (self.tag, self.cat.id, self.cat)