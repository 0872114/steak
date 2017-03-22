#!python
# -- coding: utf8 --

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField



class Entry(models.Model):
    POSSBILE_TITLES = (
        (_(u'Главная'), 'Главная'),
        (_(u'О нас'), 'О нас'),
        (_(u'О печати 1'), 'О печати 1'),
        (_(u'О печати 2'), 'О печати 2'),
        (_(u'О печати 3'), 'О печати 3'),
    )
    title = models.CharField(choices=POSSBILE_TITLES, unique=True, max_length=50, blank=False)
    short_text = RedactorField(verbose_name=u'Text', default="")


    class Meta:
        verbose_name = _(u'Редактор')
        verbose_name_plural = _(u'Редактор')

    def __unicode__(self):
        return self.title