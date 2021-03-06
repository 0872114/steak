# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20170402_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                ('short_text', redactor.fields.RedactorField(default=b'', verbose_name='Text')),
                ('url', models.CharField(max_length=50, unique=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0430\u0442\u0438\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0441\u0442\u0430\u0442\u0438\u0447\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
