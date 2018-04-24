from django.conf.urls import url
from . import views 

urlpatterns =[
	url(r'^$', views.index),
    #url(r'^login$', views.login),
    url(r'^register$', views.registerpage),
	url(r'^register/0$', views.register),
    url(r'^homepage$', views.homepage),
    url(r'^acceptpopup.html$', views.acceptpopup),
    url(r'^rejectpopup.html$', views.rejectpopup),
    url(r'^addschedule.html$', views.addschedule),
]
