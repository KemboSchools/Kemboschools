"""MySchoolKembo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler400,handler403,handler404,handler500
from . import views


handler404='KemboSchool.views.handler400'
handler404='KemboSchool.views.handler403'
handler404='KemboSchool.views.handler404'
handler404='KemboSchool.views.handler500'



urlpatterns = [
    path('MySchool/', include('MySchool.urls')),
    path('SecurityLogs/', include('securityLogs.urls')),
    path('Applications/', views.applications, name="applications"),
    # Portaill 
    path('kemboSchools/', views.reachPortal, name="portal"),
    path('kemboSchoolsRecherche/', views.lister_school_par_recherche_json, name="rechercheSchool"),
    #detailSchool 
    path('kemboSchoolsDetails/', views.getDetailSchool, name="detailSchool"),

    #-------------------------------------------------------
    path('admin/', admin.site.urls),
    
]
