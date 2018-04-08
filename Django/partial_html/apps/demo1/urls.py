from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^demo$', views.index),
    url(r'^demo1/create$', views.create),
]
