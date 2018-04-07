# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Title, Desc
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

def addnotes(request):
    if request.method == "POST":
        Title.objects.create(label=request.POST['title'])

    context = {
        'titles' : Title.objects.all(),
    }
    return render(request, 'notes/notes.html', context)

def adddesc(request, id):
    Desc.objects.create(text = request.POST['desc'], link=Title.objects.get(id=id))

    return redirect ('/addnotes')

def delete(request, id):
    Title.objects.get(id=id).delete()

    return render(request, 'notes/index.html')