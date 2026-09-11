from django.urls import path

from blogApp import views

urlpatterns = [

    path('', views.blog, name='blog'),
]
