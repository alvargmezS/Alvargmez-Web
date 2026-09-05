from django import forms
from django.core.exceptions import ValidationError

class FormContacto(forms.Form):

    nombre = forms.CharField(label='Nombre')
    empresa = forms.CharField(label='Empresa')
    email = forms.EmailField(label='Email')
    confirmar_email = forms.EmailField(label='Repite tu email')
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)

    def clean(self):
        datos = super().clean()
        email = datos.get('email')
        confirmar_email = datos.get('confirmar_email')

        if email and confirmar_email and email.lower() != confirmar_email.lower():
            raise ValidationError('Los correos no coinciden, revisa la dirección.')

        return datos