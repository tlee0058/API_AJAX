# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Userdb(models.Model):
    username = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)