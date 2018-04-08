# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Note
from django.core import serializers
import json
# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def postIt(request):
    
    note = Note.objects.create(context=request.POST['desc'])
    
    return render(request, 'posts/posts.html', {'note': note})