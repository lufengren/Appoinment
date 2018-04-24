# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages 
import bcrypt
from .models import User
# Create your views here.
#####################################################################################################
def index(request):
	return render(request, 'beta/loginpage.html')

def registerpage(request):
	return render(request, 'beta/registerpage.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, message in errors.iteritems():
            messages.error(request, message,tag)
        return redirect('/registerpage')
    
    else:
        user= User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['id']=user.id
        request.session['username']=user.username
        return redirect("/homepage")

def homepage(request):
    #user=User.objects.get(id=request.session['id'])
    # schedules=user.schedules.all()
    # context={
    #     'schedules':schedules,
    # }
    return render(request,"beta/homepage.html")

def acceptpopup(request):
    return render(request,"beta/acceptpopup.html")

def rejectpopup(request):
    return render(request,"beta/rejectpopup.html")

def addschedule(request):
    return render(request,"beta/addschedule.html")
    




       

