# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2c', '0007_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='market',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430 \u0440\u044b\u043d\u043a\u0435 \u0437\u0430\u044f\u0432\u043e\u043a'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(b'new', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9'), (b'active', b'\xd0\x92 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb5'), (b'declined', b'\xd0\x9e\xd1\x82\xd0\xba\xd0\xb0\xd0\xb7'), (b'finished', b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd')], default=b'new', max_length=50),
        ),
    ]
