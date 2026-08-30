from django.shortcuts import render


def home(request):

    return render(request, 'alvargmez_web/home.html')