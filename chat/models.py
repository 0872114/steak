#!python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from b2c.models import Order
from django.utils import timezone


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, null=True)
    order = models.ForeignKey(Order, null=True)
    date = models.DateTimeField(default=timezone.now)
    message = models.TextField()
