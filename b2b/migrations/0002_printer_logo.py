# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2b', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='logo',
            field=models.ImageField(blank=True, upload_to=b'printers', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f'),
        ),
    ]
