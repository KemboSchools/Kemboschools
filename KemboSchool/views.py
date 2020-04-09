from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from Backend.dao_menu.dao_menu import dao_menu
# Create your views here.


def applications(request):
    pass

def reachPortal (request):
    try:
        ecoles=dao_menu.listSchool()
        print("ecole ",ecoles)
        context = {
            'ecoles': ecoles,
            }
        template = loader.get_template('portal/index.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return render(request,'erreurs/erreur.html',{"fonc":"reachPortal","ms":e}) 

#Pour Les erreur
def handler400(request,exception=None):
    return render(request,'erreurs/400.html',{},status=400)

def handler403(request,exception=None):
    return render(request,'erreurs/403.html',{},status=403)

def handler500(request,exception=None):
    return render(request,'erreurs/500.html',{},status=500)

def handler404(request,exception=None):
    return render(request,'erreurs/404.html',{},status=404)