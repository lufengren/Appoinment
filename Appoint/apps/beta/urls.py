from django.conf.urls import url
from . import views 

urlpatterns =[
	url(r'^$', views.index), # login page
    url(r'^login/0$', views.login), # POST _ Login
    url(r'^register$', views.registerpage), # register page
	url(r'^register/0$', views.register), # POST _ Register
	url(r'^main$', views.mainpage) # MAIN PAGE 
]