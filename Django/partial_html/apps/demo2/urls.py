from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book$', views.index),
    url(r'^book/add$', views.add),
    
]
