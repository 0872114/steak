# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b2c', '0005_auto_20170323_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='b2b.Printer'),
        ),
    ]
