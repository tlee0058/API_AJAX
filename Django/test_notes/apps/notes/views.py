# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Title, Desc
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
# Create your views here.
def index(request):
    context = {
        'titles' : Title.objects.all(),
    }
    return render(request, 'notes/index.html', context)

def addnotes(request):
    
    new_title = Title.objects.create(label=request.POST['title'])
    context = {'title' : Title.objects.get(id=new_title.id)}

    return render(request, 'notes/_notes.html', context)

def adddesc(request, id):
    new_desc = Desc.objects.create(text = request.POST['desc'], link=Title.objects.get(id=id))
    context = {
        'desc' : Desc.objects.get(id=new_desc.id)
    }

    return render(request, 'notes/_notes.html', context)
    

def delete(request, id):
    Title.objects.get(id=id).delete()
    return redirect ('/')
