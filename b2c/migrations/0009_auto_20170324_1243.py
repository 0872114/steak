# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b2c', '0008_auto_20170324_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='b2b.Printer'),
        ),
    ]
