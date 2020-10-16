from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    birthdate = models.DateField('Fecha de nacimiento', null=False)
    phonecallAllowed = models.BooleanField('¿Permite que se le llame por teléfono?', default=True)
    emailContactAllowed = models.BooleanField('¿Permite que nos comuniquemos con usted por email?', default=True)


class Appointment(models.Model):
    startDateTime = models.DateTimeField('Inicio programado de la cita', null=False)
    endDateTime = models.DateTimeField('Final programado de la cita', null=False)
    creationDateTime = models.DateTimeField('Fecha de creación de la cita', null=False, blank=True, default=now)
    bookingDateTime = models.DateTimeField('Fecha de la reserva', null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.RESTRICT, related_name='appointments', related_query_name="appointment")

    class Meta:
        verbose_name: 'Cita'
        verbose_name_plural: 'Citas'
        ordering: ['startDateTime']


class Message(models.Model):
    text = models.CharField('Mensaje', null=False, blank=False, max_length=500)
    subject = models.CharField('Asunto', null=False, blank=False, max_length=100)
    email = models.CharField('Email', null=False, blank=False, max_length=50)
    name = models.CharField('Nombre', null=False, blank=False, max_length=50)
    sendDateTime = models.DateTimeField('Fecha de envío del comentario', null=False, default=now)

    class Meta:
        verbose_name: 'Mensaje'
        verbose_name_plural: 'Mensajes'
        ordering: ['-sendDateTime']
