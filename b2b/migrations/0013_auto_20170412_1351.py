# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2b', '0012_printer_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
    ]