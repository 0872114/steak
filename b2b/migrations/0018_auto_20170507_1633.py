# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2b', '0017_auto_20170418_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='address',
            field=models.CharField(max_length=500, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
    ]
