# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2b', '0018_auto_20170507_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='metro',
            field=models.CharField(blank=True, max_length=150, verbose_name='\u041c\u0435\u0442\u0440\u043e'),
        ),
        migrations.AddField(
            model_name='printer',
            name='schedule',
            field=models.CharField(blank=True, max_length=150, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
    ]
