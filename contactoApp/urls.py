from django.urls import path

from contactoApp import views

urlpatterns = [

    path('', views.contacto, name='contacto'),
]
