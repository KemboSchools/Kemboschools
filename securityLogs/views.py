from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse



def login_view(request):
    try:
        next = request.GET.get('next')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        print('user name %s' % (user.username))
        print('user pass %s' % (user.password))
        print('next %s' % (next))

        print('login touché if')
        dash_board = 'Enregistrement'

        context = {
            'title': dash_board,

        }
        # template = loader.get_template('aSideTop/Layout.html')
        return HttpResponseRedirect(reverse('MySchoolAccueil'))

    except Exception as e:
        print('problem %s' % (e))
        context = {
            'erreur': 'Veuillez compléter correctement les champs « nom d\'utilisateur » et « mot de passe » d\'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse. '}
        template = loader.get_template('securityLog/login.html')
        return HttpResponse(template.render(context, request))


def logout_view(request):
    print('login touché')
    logout(request)

    context = {'login': 'login'}
    template = loader.get_template('securityLog/login.html')
    return HttpResponse(template.render(context, request))


def iam_authenticated(request):
    try:
        print('authentification touché')
        if request.user.is_authenticated:
            print('authentification touché')
            return None
        else:
            context = {'login': 'login'}
            template = loader.get_template('securityLog/login.html')
            return HttpResponse(template.render(context, request))
    except Exception as e:
        print('iam_authenticated %s' % (e))


def creer_un_user(request):
    try:
        user = User()
        next = request.GET.get('next')
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        password = request.POST['password']

        user.set_password(password)
        print('mot de passe %s' % (password))
        user.save()

        user = authenticate(username=user.username, password=password)
        login(request, user)
        print('user name %s' % (user.username))
        print('user pass %s' % (user.password))
        print('next %s' % (next))

        print('login touché if')
        dash_board = 'Enregistrement'
        context = {
            'title': dash_board,
        }
        # template = loader.get_template('aSideTop/Layout.html')
        template = loader.get_template('main_layout/index/starter_template.html')
        return HttpResponse(template.render(context, request))

    except Exception as e:
        print('problem %s' % (e))
        context = {
            'erreur': 'Veuillez compléter correctement les champs « nom d\'utilisateur » et « mot de passe » d\'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse. '}
        template = loader.get_template('securityLog/register.html')
        return HttpResponse(template.render(context, request))


def get_registrer(request):
    context = {'title': 'Creation compte'}
    template = loader.get_template('securityLog/register.html')
    return HttpResponse(template.render(context, request))
