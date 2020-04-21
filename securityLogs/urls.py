from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^registrer/save$', views.creer_un_user, name='registrer_view'),
    url(r'^registrer/form$', views.get_registrer, name='get_registrer_view'),
    url(r'^verificationUsernameEmail/form$', views.get_Username, name='verificationUsernameEmail'),
]
