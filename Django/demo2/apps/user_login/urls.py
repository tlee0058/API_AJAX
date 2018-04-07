from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^get_json$', views.get_json),
    url(r'^get_html$', views.get_html),
    url(r'^find$', views.find),
    url(r'^create$', views.create),
    
    
]