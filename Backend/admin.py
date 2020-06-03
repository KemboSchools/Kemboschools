from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.MySchoolUser)
admin.site.register(models.MySchoolProfil)
admin.site.register(models.MySchoolApp)
admin.site.register(models.MySchoolMenu)
admin.site.register(models.MySchoolSousMenu)
admin.site.register(models.RelationUserProfil)
admin.site.register(models.MySchoolSchool)
admin.site.register(models.RelationSchoolUser)
admin.site.register(models.Adresse)

# Code Starly
admin.site.register(models.Details_school)
admin.site.register(models.Banque_liens_img_School)
admin.site.register(models.Activites_scolaire)
admin.site.register(models.Options_organisee)
