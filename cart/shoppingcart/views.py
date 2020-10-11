from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import User, Appointment


def index(request):
    print (request.user)
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


@login_required
def booking(request):

    user = User.objects.get(pk=request.user.id)
    tomorrow = datetime.now() + timedelta(days=1)

    appointments = Appointment.objects.filter(user=None, startDateTime__gte = tomorrow.date())

    user_appointments = Appointment.objects.filter(user=user)

    context = {
        'appointments': appointments,
        'user_appointments': user_appointments,
    }
    return render(request, 'booking.html', context)


@login_required
def book(request, pk):
    appointment = Appointment.objects.get(pk=pk)

    if appointment.user == None:
        appointment.user = User.objects.get(pk=request.user.id)
        appointment.save()
        return redirect('booking')

    else:
        return render(request, 'booking_error.html')


