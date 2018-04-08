# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
# Create your views here.
def index(request):
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, 'zappos/users/index.html', context)

def create(request):
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    #print dir(request) is a good way to find out all methods
    print request.is_ajax()
    if request.is_ajax():
        return redirect("/zappos/users/render/" + str(user.id))
    return redirect ('/')

def users_render(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, "zappos/users/_render_user.html", context)
    #or return HttpResponse(context["user"].__dict__.__str__)