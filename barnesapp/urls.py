from django.conf.urls import *
from django.contrib import admin
from barnesapp import views


urlpatterns =[
        url(r'^$', views.index, name='index'),
]