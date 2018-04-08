# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Text
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

def addnotes(request):
    Text.objects.create(title=request.POST['title'])
    context = {
        'notes' : Text.objects.all(),
    }
    return render(request, 'notes/notes.html', context)

