from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages 
import bcrypt
from .models import User, Profile, Appointment, Schedule, Message
#####################################################################################################
def index(request):
	return render(request, 'beta/loginpage.html')

def registerpage(request):
	return render(request, 'beta/registerpage.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, message in errors.iteritems():
            messages.error(request, message, tag)
        return redirect('/register')
    else:
        user= User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
            admin = 0
        )

        messages.success(request, "You are successfully registered. Log in to verify.")
        return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, message in errors.iteritems():
            messages.error(request, message, tag)
        return redirect('/')
    else:
        this_user = User.objects.get(email = request.POST['login_id'])
        request.session['user_id'] = this_user.id  # Save session ID on successful login, so that we can retrieve when needed # -shawn
        return redirect('/main')  

def mainpage(request):
    return render(request, 'beta/mainpage.html')

def appointmentpage(request,id):
    appointment = Appointment.objects.get(id = id)
    user = appointment.user.all()
    context = {
        'appoint' : appointment,
        'user' : user,
    }
    return render(request,'beta/appointmentpage.html', context)