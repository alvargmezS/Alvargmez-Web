from django.shortcuts import render

from cvApp.models import cv


def home(request):

    contexto = {
        'cv': cv.objects.first(),
    }

    return render(request, 'alvargmez_web/home.html', contexto)