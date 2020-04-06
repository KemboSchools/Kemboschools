from django.shortcuts import render
from securityLogs.views import iam_authenticated
from Backend.dao_menu.dao_menu import dao_menu
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
# Create your views here.


def MySchoolAccueil(request):
    try:
        if request.user.is_authenticated:
            dash_board = 'tableau de bord stock'
            getuser_id=request.user.id
            userId= dao_menu.getUtilisateur(getuser_id)
            lesApp = dao_menu.getapps(userId)
            lesProfils = dao_menu.getprofils(userId)
            ecole=dao_menu.getschool(getuser_id)
            #template = loader.get_template('aSideTop/Layout.html')
            context = {
                'index': ecole,
                'getapps': lesApp,
                'profils': lesProfils
            }
            template = loader.get_template('MySchool/index.html')
            return HttpResponse(template.render(context, request))
        else:
            context = {'login': 'login'}
            template = loader.get_template('securityLog/login.html')
            return HttpResponse(template.render(context, request))
    except Exception as e:
        print("ERREUR MySchoolAccueil", e)
        context = {'login': 'login'}
        template = loader.get_template('securityLog/login.html')
        return HttpResponse(template.render(context, request))

@login_required(redirect_field_name='securityLog/login.html')
def nothing(request):
    return HttpResponse("Url reussi avec succes")


