# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2c', '0002_auto_20170321_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.CharField(default=b'bidmarket', max_length=50, verbose_name='\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
