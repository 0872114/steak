# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20170322_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(choices=[('\u0413\u043b\u0430\u0432\u043d\u0430\u044f', b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f'), ('\u041e \u043d\u0430\u0441', b'\xd0\x9e \xd0\xbd\xd0\xb0\xd1\x81'), ('\u041e \u043f\u0435\u0447\u0430\u0442\u0438 1', b'\xd0\x9e \xd0\xbf\xd0\xb5\xd1\x87\xd0\xb0\xd1\x82\xd0\xb8 1'), ('\u041e \u043f\u0435\u0447\u0430\u0442\u0438 2', b'\xd0\x9e \xd0\xbf\xd0\xb5\xd1\x87\xd0\xb0\xd1\x82\xd0\xb8 2'), ('\u041e \u043f\u0435\u0447\u0430\u0442\u0438 3', b'\xd0\x9e \xd0\xbf\xd0\xb5\xd1\x87\xd0\xb0\xd1\x82\xd0\xb8 3')], max_length=50, unique=True),
        ),
    ]