from django import forms

class FormContacto(forms.Form):

    nombre = forms.CharField(label='Nombre')
    empresa = forms.CharField(label='Empresa')
    email = forms.EmailField(label='Email')
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)