# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from datetime import time, timedelta, datetime


class ModelForTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class MySchoolSchool(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

#ici le user doit d'abord faire partie de l'ecole après il peut etre assigner à un profil "RelationUserProfil"
#parceque avant d'assigner 'un profil à un user, on doit d'abor selectionner tous les user lier à l'ecole 
class RelationSchoolUser(ModelForTime):
    school = models.ForeignKey('MySchoolSchool', blank=True, null=True,on_delete=models.CASCADE, related_name="MySchoolSchool_set")
    schooluser = models.ForeignKey('MySchoolUser', blank=True, null=True,on_delete=models.CASCADE, related_name="myschoolschoolSet_r")
    # inscrit, Renvoyer,quiter.
    etat = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.schooluser)


class MySchoolUser(ModelForTime):
    utilisateur = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="for_user_id")
    titre = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titre

class RelationUserProfil(models.Model):
    profil = models.ForeignKey('MySchoolProfil', blank=True, null=True,on_delete=models.CASCADE, related_name="MySchoolUser_set")
    user = models.ForeignKey('MySchoolUser', blank=True, null=True,on_delete=models.CASCADE, related_name="myschooluserSet")
    school = models.ForeignKey('MySchoolSchool', blank=True, null=True,on_delete=models.CASCADE, related_name="myschoolschoolSet")
    def __str__(self):
        return str(self.profil)

class MySchoolProfil (ModelForTime):
    titre = models.CharField(max_length=100, null=True, blank=True)
    niveau = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titre

class MySchoolApp(ModelForTime):
    myschoolprofil = models.ForeignKey('MySchoolProfil', blank=True, null=True, on_delete=models.CASCADE, related_name="MySchoolProfil_set")
    titre = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    background_color = models.CharField(max_length=100, null=True, blank=True)
    background_image = models.CharField(max_length=100, null=True, blank=True)
    installer = models.BooleanField()
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.titre

# Create your models here.

class MySchoolMenu (ModelForTime):
    myschoolapp = models.ForeignKey('MySchoolApp', on_delete=models.CASCADE,related_name="MySchoolApp_set", blank=True, null=True)
    titre = models.CharField(max_length=100, null=True, blank=True)
    nomModule = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.titre

class MySchoolSousMenu (ModelForTime):
    myschoolmenu = models.ForeignKey('MySchoolMenu', on_delete=models.CASCADE,related_name="MySchoolSousMenu_set", blank=True, null=True)
    titre = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titre
