# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Backend.models import MySchoolUser
from Backend.models import MySchoolMenu
from Backend.models import MySchoolSousMenu
from Backend.models import RelationUserProfil
from Backend.models import MySchoolApp
from Backend.models import MySchoolSchool
from django.db.models import Q

class dao_menu(object):

    @staticmethod
    def getUtilisateur(id):
        try:
            utilisateur = MySchoolUser.objects.filter(utilisateur=id)
            for userId in utilisateur:
                idUser=userId.id
            return idUser
        except Exception as e:
            print("IL Y A PAS D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend(dao_menu(getUtilisateur)) err=",e)
            
    @staticmethod
    def getapps(user_id):
        try:
            list_ = []
            for p in RelationUserProfil.objects.filter(user=user_id):
                for ap in MySchoolApp.objects.filter(myschoolprofil=p.profil.id):
                    list_.append(ap)
            return list_
        except Exception as e:
            print("IL Y A PAS D'APPLICATIONS Backend(dao_menu(getapps)) err=", e)
          

    @staticmethod
    def getprofils(user_id):
        try:
            list_ = []
            for p in RelationUserProfil.objects.filter(user=user_id):
               list_.append(p)
            return list_
        except Exception as e:
            print("IL Y A PAS D'APPLICATIONS Backend(dao_menu(getprofils)) err=", e)
            
    
    @staticmethod
    def getschool(user_id):
        try:
            for p in RelationUserProfil.objects.filter(user=user_id):
                school=p.school
            return school
        except Exception as e:
            print("PAS D'ECOLE ,IL N'EST INSCRIT Backend(dao_menu(getschool)) err=", e)
           
    @staticmethod
    def listSchool():
        try:
            return  MySchoolSchool.objects.filter()
        except Exception as e:
            print("PAS D'ECOLE ,IL N'EST INSCRIT Backend(dao_menu(listSchool)) err=", e)
    
    @staticmethod
    def recherchelistSchool(recherche):
        try:
            return  MySchoolSchool.objects.filter(Q(name__contains=recherche) | Q(adress__pays__contains=recherche) | Q(adress__commune__contains=recherche) | Q(adress__quartier__contains=recherche))
        except Exception as e:
            print("PAS D'ECOLE ,IL N'EST INSCRIT Backend(dao_menu(listSchool)) err=", e)
    
    @staticmethod
    def getSchool(idSchool):
        try:
            return  MySchoolSchool.objects.get(pk=idSchool)
        except Exception as e:
            print("PAS D'ECOLE ,IL N'EST INSCRIT Backend(dao_menu(getSchool)) err=", e)