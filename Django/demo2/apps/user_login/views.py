# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .forms import RegisterForm
from django.core import serializers
import json

# Create your views here.
def index(request):
    form = RegisterForm()
    context = { "regForm": form }
    return render(request, "user_login/forms.html", context)

def get_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type="application/json")

def get_html(request):
    users = User.objects.all()
    return render(request, 'user_login/all.html', {'users': users})

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST['findname'])
    return render(request, 'user_login/all.html', {'users': users})

def create(request):
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email_address = request.POST['email']) 
    users = User.objects.all()
    return render(request, "user_login/all.html", {'users': users})