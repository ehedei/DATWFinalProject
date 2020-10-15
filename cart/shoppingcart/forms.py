from django import forms
from django.core.exceptions import ValidationError

from .models import User


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, label='Nombre:')
    email = forms.EmailField(required=True, max_length=50, label='Email:')
    subject = forms.CharField(required=True, max_length=100, label='Asunto:')
    text = forms.CharField(required=True, max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Límite de 500 caracteres'}), label='Mensaje:')


class SignupForm(forms.Form):
    username = forms.CharField(required=True, max_length=50, label='Nombre de usuario:')
    password = forms.CharField(required=True, max_length=50, label='Contraseña:', widget=forms.PasswordInput)
    repeated_password = forms.CharField(required=True, max_length=50, label='Repita su Contraseña:', widget=forms.PasswordInput)
    email = forms.EmailField(required=True, max_length=50, label='Dirección de correo electrónico:')
    first_name = forms.CharField(required=True, max_length=50, label='Nombre:')
    last_name = forms.CharField(required=True, max_length=50, label='Apellidos:')
    birthdate = forms.DateField(required=True, label='Fecha de nacimiento:', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    phonecallAllowed = forms.BooleanField(label='¿Permite que se le llame por teléfono?', required=False)
    emailContactAllowed = forms.BooleanField(label='¿Permite que nos comuniquemos con usted por email?', required=False)


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este usuario ya existe en la aplicación', code='invalid')
        else:
            return username


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este email ya existe en la aplicación', code='invalid')
        else:
            return email


    def clean(self):
        cleaned_data = super().clean()

        email = self.cleaned_data.get('email')
        repeatedEmail = self.cleaned_data.get('repeated_password')

        if repeatedEmail != email:
            raise ValidationError('La contraseña no coincide', code='invalid')
        else:
            return cleaned_data

