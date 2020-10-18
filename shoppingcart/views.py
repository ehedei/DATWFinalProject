from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from .forms import ContactForm, SignupForm
from .models import User, Appointment, Message


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = Message()
            message.name = form.cleaned_data['name']
            message.email = form.cleaned_data['email']
            message.subject = form.cleaned_data['subject']
            message.text = form.cleaned_data['text']
            message.save()
            return render(request, 'contact_ok.html')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)


@login_required
def booking(request):
    user = User.objects.get(pk=request.user.id)
    tomorrow = datetime.now() + timedelta(days=1)

    appointments = Appointment.objects.filter(user=None, startDateTime__gt = tomorrow.date()).order_by('startDateTime')

    user_appointments = user.appointments.all().order_by('-startDateTime')

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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = make_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.birthdate = form.cleaned_data['birthdate']
            user.emailContactAllowed = form.cleaned_data['emailContactAllowed']
            user.phonecallAllowed = form.cleaned_data['phonecallAllowed']

            user.save()

            return render(request, 'registration/signup_ok.html')

    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/signup.html', context)

