# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440',
                'verbose_name_plural': '\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b',
            },
        ),
    ]
