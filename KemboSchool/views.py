from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template import loader
from Backend.dao_menu.dao_menu import dao_menu
# Create your views here.


def applications(request):
    return None

# Liste des classes
def reachPortal (request):
    try:
    
        ecoles=dao_menu.listSchool()
       
        context = {
            'ecoles': ecoles,
            }
        template = loader.get_template('portal/index.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return render(request,'erreurs/erreur.html',{"fonc":"reachPortal","ms":e}) 


def lister_school_par_recherche_json(request):
   
    try:
     
       recherche = request.GET['rearch']
       print("votre recherche ",recherche)
       ecolesR=[]
       ecoles=dao_menu.recherchelistSchool(recherche)
       for ecole in ecoles:
           resultats={
               "title":"Portail",
               "nameScool":ecole.name,
               "pays":ecole.adress.pays,
               "commune":ecole.adress.commune,
               "quartier":ecole.adress.quartier,
               "avennue":ecole.adress.avennue,
               "numero":ecole.adress.numero
               }
           ecolesR.append(resultats)
           print(resultats)
       return JsonResponse(ecolesR, safe=False)
        
    except Exception as e:
        print(" exception ",e)
        return render(request,'erreurs/erreur.html',{"fonc":"lister_school_par_recherche_json","ms":e}) 

def getDetailSchool (request):
    try:
        ecoles=dao_menu.listSchool()
       
        context = {
            'ecoles': ecoles,
            }
        template = loader.get_template('portal/detailSchool.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return render(request,'erreurs/erreur.html',{"fonc":"getDetailSchool","ms":e}) 

#Pour Les erreur
def handler400(request,exception=None):
    return render(request,'erreurs/400.html',{},status=400)

def handler403(request,exception=None):
    return render(request,'erreurs/403.html',{},status=403)

def handler500(request,exception=None):
    return render(request,'erreurs/500.html',{},status=500)

def handler404(request,exception=None):
    return render(request,'erreurs/404.html',{},status=404)