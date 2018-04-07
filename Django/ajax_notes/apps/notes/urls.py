from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addnotes$', views.addnotes),
    url(r'^adddesc/(?P<id>\d+)$', views.adddesc),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    
]