import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from globalApp.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        
     user= json.loads(request.body)
     print(user)
     try:
         usercreated= Utilisateur.objects.create(
         nom = user["nom"],
         prenom = user["prenom"],
         numtel = user["numtel"],
         groupSanguin= user["groupSanguin"],
         willaya = user["willaya"],
         daira = user["daira"],
         email = user["email"].lower(), 
       )
     except Exception as e :
         print(str(e))
         return JsonResponse({"message" : "erreur : " + str(e)})

     return JsonResponse({"message" : "utilisateur crée" })
    return JsonResponse(  {"messsage " : "Objet non  créé reqete get"} )


def getUser(request , email):
    if email == "":
        return JsonResponse({'error': 'Paramètre email manquant'}, status=400)
    else:
        utilisateur = Utilisateur.objects.get(email = email)
        print(utilisateur)
        user_data = {
                'id': utilisateur.id,
                'nom': utilisateur.nom,
                'prenom': utilisateur.prenom,
                'email': utilisateur.email,
                'numtel': utilisateur.numtel,
                'groupSanguin': utilisateur.groupSanguin,
                'willaya': utilisateur.willaya,
                'daira': utilisateur.daira,
            }
        return JsonResponse(user_data)
    
@csrf_exempt
def ajouterDonneur(request):
    if request.method == 'POST':
     user= json.loads(request.body)
     print(user["utilisateur"])
     usercreated = None
     try:
         usercreated= Utilisateur.objects.create(
         nom = user["utilisateur"]["nom"],
         prenom = user["utilisateur"]["prenom"],
         numtel = user["utilisateur"]["numtel"],
         groupSanguin= user["utilisateur"]["groupSanguin"],
         willaya = user["utilisateur"]["willaya"],
         daira = user["utilisateur"]["daira"],
         email = user["utilisateur"]["email"], 
       )
        #  usercreated.save()
         donneur = Donneur.objects.create(
             utilisateur = usercreated,
             statu = "Apte"
         )
         print(donneur)
     except Exception as e :
         print(str(e))
         return JsonResponse({"message" : "erreur : " + str(e)})

     return JsonResponse({"message" : "Donneur crée" })
    return JsonResponse(  {"messsage " : "Objet non  créé reqete get"} )

@csrf_exempt
def update_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, pk=utilisateur_id)

    if request.method == 'PUT':
        utilisateurUpdated = json.loads(request.body)
        nom = utilisateurUpdated['nom']
        prenom = utilisateurUpdated['prenom']
        email = utilisateurUpdated['email'].lower()
        numtel = utilisateurUpdated['numtel']
        groupSanguin = utilisateurUpdated['groupSanguin']
        willaya = utilisateurUpdated['willaya']
        daira = utilisateurUpdated['daira']

        # Mettre à jour les champs de l'utilisateur
        utilisateur.nom = nom
        utilisateur.prenom = prenom
        # utilisateur.email = email
        utilisateur.numtel = numtel
        utilisateur.groupSanguin = groupSanguin
        utilisateur.willaya = willaya
        utilisateur.daira = daira

        # Enregistrer les modifications dans la base de données
        utilisateur.save()

        return JsonResponse({'success': 'Utilisateur mis à jour avec succès'})
    
    # Renvoyer les détails de l'utilisateur
    user_data = {
        'nom': utilisateur.nom,
        'prenom': utilisateur.prenom,
        'email': utilisateur.email,
        'numtel': utilisateur.numtel,
        'groupSanguin': utilisateur.groupSanguin,
        'willaya': utilisateur.willaya,
        'daira': utilisateur.daira,
    }
    return JsonResponse(user_data)