from django.shortcuts import render

# Create your views here.

def proyectos(request):

    return render(request, 'proyectos/proyectos.html')