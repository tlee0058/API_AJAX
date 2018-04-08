from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^zappos/users/create$', views.create),
    url(r'^zappos/users/render$', views.users_render),
    url(r'^zappos/users/render/(?P<user_id>\d+)$', views.users_render)
]
