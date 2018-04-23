from django.conf.urls import url
from . import views 

urlpatterns =[
	url(r'^$', views.index),
    # url(r'^login$', views.login),
    url(r'^register$', views.registerpage),
	url(r'^register/0$', views.register),
]
