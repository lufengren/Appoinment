# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages 
import bcrypt 
# Create your views here.
#####################################################################################################
def loginpage(request):
	return render(request, 'beta/loginpage.html')

def registerpage(request):
	return render(request, 'beta/registerpage.html')







# def firstpage(request):

# 	return render(request, 'exam/loginpage.html')

# def register(request):
# 	errors = Users.objects.register_validator(request.POST)
# 	if len(errors):
# 		for tag, content in errors.iteritems():
# 			messages.error(request,content,extra_tags=tag)
# 		print"!"
# 		return redirect('/main')
# 	else:
# 		name = request.POST['name']
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		hashed_pw = bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())
# 		Users.objects.create(name=name, username =username, password=hashed_pw)
# 		messages.success(request, "you have successfully registered")
# 		return redirect('/main')

# def login(request):
# 	errors = Users.objects.login_validator(request.POST)
# 	if len(errors):
# 		for tag, content in errors.iteritems():
# 			messages.error(request, content, extra_tags=tag)
# 		return redirect('/main')
# 	else:
# 		user = Users.objects.get(username = request.POST['login_id'])
# 		request.session['id'] = user.id ########### SAVE SESSION['ID'] ON LOGIN 
# 		return redirect('/travels')

# def logout(request):
# 	request.session['id'] = None
# 	return redirect('/main')

#####################################################################################################