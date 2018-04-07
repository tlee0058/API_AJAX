# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Title(models.Model):
    label = models.CharField(max_length = 255)
    

class Desc(models.Model):
    text = models.TextField(null=True, blank=True)
    link = models.OneToOneField(Title, related_name="description")