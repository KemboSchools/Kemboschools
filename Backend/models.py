# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from datetime import time, timedelta, datetime


##########################################################################################################
class ModelForTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Adresse (ModelForTime):
    pays = models.CharField(max_length=100, null=True, blank=True)
    commune = models.CharField(max_length=100, null=True, blank=True)
    quartier = models.CharField(max_length=100, null=True, blank=True)
    avennue = models.CharField(max_length=200, null=True, blank=True)
    numero= models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.commune
##########################################################################################################
class MySchoolSchool(models.Model):
    adress=models.ForeignKey('Adresse', blank=True, null=True,on_delete=models.CASCADE, related_name="SchoolAdress_set")
    name = models.CharField(max_length=100, null=True, blank=True)

#  # Debut de Code starly
#     """ Cette variable identifie de maniere unique le detail d une ecole"""
    details_school=models.OneToOneField('Details_school',on_delete=models.CASCADE,null=True,blank=True)
    banque_liens_img_school=models.OneToOneField('Banque_liens_img_School',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

# # Ici je creer un model qui contiendra tous les details de mon article --- Code starly
class Details_school(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    historique= models.TextField(null=True,blank=True)
    situation_geographique= models.TextField(null=True,blank=True)
    impact_sociaux_eco= models.TextField(null=True,blank=True)
    contacts=models.CharField(max_length=50, null=True, blank=True)
    devise=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Banque_liens_img_School(models.Model):
    """docstring for Banque_liens_img_schools
        cette classe nous permet de recuperer le path des images de base pour notre layout"""
    lien= models.CharField(max_length=100, null=True, blank=True)
    carousel= models.CharField(max_length=100, null=True, blank=True)
    portfolio=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """ Tres utile lorsqu on veut faire un alt sur l image"""
        # return "Image de : %s %s" % (MySchoolSchool.name, self.lien)
        return self.lien

class Activites_scolaire(models.Model):
    """docstring for Activites_scolaires"""
    titre_activite=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    lien_img=models.CharField(max_length=100, null=True, blank=True)
    my_school_school=models.ForeignKey('MySchoolSchool', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return "Activite : [ %s ] DE %s" % (self.titre_activite,self.my_school_school.name)

class Options_organisee(models.Model):
    """docstring for Options_organisees"""
    titre_option=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(max_length=100,null=True, blank=True)
    lien_img=models.CharField(max_length=100, null=True, blank=True)
    my_school_school=models.ForeignKey('MySchoolSchool', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return "Option : [ %s ] - [ %s ] DE %s" % (self.id,self.titre_option,self.my_school_school.name,)

# Fin STARLY

#ici le user doit d'abord faire partie de l'ecole après il peut etre assigner à un profil "RelationUserProfil"
#parceque avant d'assigner 'un profil à un user, on doit d'abor selectionner tous les user lier à l'ecole
class RelationSchoolUser(ModelForTime):
    school = models.ForeignKey('MySchoolSchool', blank=True, null=True,on_delete=models.CASCADE, related_name="MySchoolSchool_set")
    schooluser = models.ForeignKey('MySchoolUser', blank=True, null=True,on_delete=models.CASCADE, related_name="myschoolschoolSet_r")
    # inscrit, Renvoyer,quiter.
    etat = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.school)+" "+str(self.schooluser)+" "+str(self.etat)


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
        return str(self.school) +" "+str(self.profil)+" "+str(self.user)

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

