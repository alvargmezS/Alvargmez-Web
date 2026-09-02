from django.shortcuts import render

from proyectosApp.models import proyecto


# Create your views here.

def proyectos(request):

    proyectos = proyecto.objects.prefetch_related('tecnologias')

    return render(request, 'proyectos/proyectos.html', {'proyectos': proyectos})