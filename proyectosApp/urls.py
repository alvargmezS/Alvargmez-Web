from django.contrib import admin
from django.urls import path

from proyectosApp import views

urlpatterns = [

    path('', views.proyectos, name='proyectos'),
]
