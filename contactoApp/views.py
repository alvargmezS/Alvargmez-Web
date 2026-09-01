from django.shortcuts import render

from contactoApp.forms import FormContacto


# Create your views here.

def contacto(request):

    form = FormContacto()

    return render(request, 'contacto/contacto.html', {'form': form})