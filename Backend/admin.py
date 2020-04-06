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
