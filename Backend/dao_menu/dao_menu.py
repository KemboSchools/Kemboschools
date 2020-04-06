# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Backend.models import MySchoolUser
from Backend.models import MySchoolMenu
from Backend.models import MySchoolSousMenu
from Backend.models import RelationUserProfil
from Backend.models import MySchoolApp



class dao_menu(object):

    @staticmethod
    def getUtilisateur(id):
        try:
            utilisateur = MySchoolUser.objects.filter(utilisateur=id)
            print("Utilisateur __id",utilisateur)
            for userId in utilisateur:
                idUser=userId.id
            return idUser
        except Exception as e:
            print("IL Y A PAS D'UTILISATEUR AVEC CETTE IDENTIFIANT",e)
            return None
    @staticmethod
    def getapps(user_id):
        try:
            list_ = []
            for p in RelationUserProfil.objects.filter(user=user_id):
                for ap in MySchoolApp.objects.filter(myschoolprofil=p.profil.id):
                    list_.append(ap)
            return list_
        except Exception as e:
            print("IL Y A PAS D'APPLICATIONS", e)
            return None

    @staticmethod
    def getprofils(user_id):
        try:
            list_ = []
            for p in RelationUserProfil.objects.filter(user=user_id):
               list_.append(p)
            return list_
        except Exception as e:
            print("IL Y A PAS D'APPLICATIONS", e)
            return None
    
    @staticmethod
    def getschool(user_id):
        try:
            for p in RelationUserProfil.objects.filter(user=user_id):
                school=p.school
            return school
        except Exception as e:
            print("PAS D'ECOLE ,IL N'EST INSCRIT", e)
            return None
