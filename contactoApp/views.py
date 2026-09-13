from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from contactoApp.forms import FormContacto


# Create your views here.

def contacto(request):

    form = FormContacto()

    if request.method == 'POST':
        form = FormContacto(request.POST)

        if form.is_valid():
            nombre = request.POST.get('nombre')
            empresa = request.POST.get('empresa')
            email = request.POST.get('email')
            email_respuesta = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage("Mensaje desde Formulario de contacto Alvargmez-web",
                                 f'Nombre: {nombre} \n\n Empresa: {empresa} \n\n {contenido} \n\n {email}',
                                 "web@alvargmez.es", ["web@alvargmez.es"], reply_to=[email])

            emailrespuesta = EmailMessage("Mensaje de web.alvargmez.es",
                                 f'Has enviado un mensaje a traves de web.alvargmez.es Con el siguiente contenido: \n\n {contenido} \n\n Contactaremos lo antes posible\n\n Saludos',
                                 "web@alvargmez.es", [f'{email_respuesta}'], reply_to=['web@alvargmez.es'])


            try:
                email.send()
                emailrespuesta.send()
                messages.success(request, 'Mensaje enviado correctamente.')
                return redirect('contacto')

            except Exception:
                messages.error(request, 'No se pudo enviar el mensaje, inténtalo de nuevo más tarde.')
                return redirect('contacto')

    return render(request, 'contacto/contacto.html', {'form': form})