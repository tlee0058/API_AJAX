# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Userdb
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json


# Create your views here.
def index(request):
    context = {
        'users' : Userdb.objects.all()
    }
    return render(request, 'demo1/index.html', context)

def create(request):
    new = Userdb.objects.create(username=request.POST['username'], email=request.POST['email'])
    context = {
        'user' : Userdb.objects.get(id=new.id)
    }
    return render(request, 'demo1/_render.html', context)