from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Userdb
from django.core import serializers
import json
def index(request):
    return render(request, 'user_login/index.html')
# Create your views here.
def all_json(request):
    users = Userdb.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')
def all_html(request):
    return render(request, 'user_login/all.html', { "users": Userdb.objects.all() })
def find(request):
    return render(request, 'user_login/all.html',
        { "users":    Userdb.objects.filter(first_name__startswith=request.POST['first_name_starts_with']) }
    )
def create(request):
    Userdb.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'])
    return render(request, 'user_login/all.html',{ "users": Userdb.objects.order_by("-id") })
