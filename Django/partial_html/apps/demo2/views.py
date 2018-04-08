# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
from .models import Book

# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request, 'demo2/index.html', context)

def add(request):
    new = Book.objects.create(title = request.POST['title'], desc=request.POST['desc'])
    context = {
        'book' : Book.objects.get(id=new.id)
    }
    return render(request, 'demo2/_render.html', context)