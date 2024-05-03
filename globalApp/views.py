import datetime
import json
from time import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from globalApp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


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

@csrf_exempt
def createAnounce(request , pk):
    if request.method == 'POST':
        try:
            
          info= json.loads(request.body)
          utilisateur = Utilisateur.objects.get(id = pk)
          date_objet = timezone.datetime.strptime(info["date_de_Don_max"], '%Y-%m-%dT%H:%M:%S.%f')
          date_aware = timezone.make_aware(date_objet)
          annonce = Annonce.objects.create(
            utilisateur = utilisateur,
            description = info["description"],
            groupSanguin=info["groupSanguin"],
            place=info["place"],
            date_de_Don_max= date_aware,
            numerotelephone= info["numerotelephone"]
              )
          return JsonResponse({"message" : "annonce creé"})
        except Exception as e :
         print(str(e))
         return JsonResponse({"message :" : "erreur : " + str(e)}) 
    return JsonResponse({"message :" , "methode doit etre POST"})   
    

def recuperToutLesAnnonces(request):
    annonces = Annonce.objects.all()

    # Sérialiser les annonces en format JSON
    data = []
    for annonce in annonces:
        utilisateur = Utilisateur.objects.get(id = annonce.utilisateur.id)
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
        data.append({
            'id':annonce.id,
            'utilisateur': user_data,
            'description': annonce.description,
            'groupSanguin': annonce.groupSanguin,
            'place': annonce.place,
            'date_de_publication': annonce.date_de_publication.isoformat(),
            'date_de_Don_max': annonce.date_de_Don_max.isoformat() if annonce.date_de_Don_max else None,
            'numerotelephone': annonce.numerotelephone,
            'date_de_modification': annonce.date_de_modification.isoformat() if annonce.date_de_modification else None,
        })
    return JsonResponse(data, safe=False)


def recupererAnnoncesUser(request , pk):
    annonces = Annonce.objects.filter(utilisateur = Utilisateur.objects.get(id = pk))
    if annonces.exists():
            data = []
            for annonce in annonces:
                utilisateur = Utilisateur.objects.get(id = annonce.utilisateur.id)
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
                data.append({
                            'id': annonce.id,
                             'utilisateur': user_data,
                              'description': annonce.description,
                              'groupSanguin': annonce.groupSanguin,
                               'place': annonce.place,
                                'date_de_publication': annonce.date_de_publication.isoformat(),
                                'date_de_Don_max': annonce.date_de_Don_max.isoformat() if annonce.date_de_Don_max else None,
                                'numerotelephone': annonce.numerotelephone,
                                'date_de_modification': annonce.date_de_modification.isoformat() if annonce.date_de_modification else None,
                                      })
            return JsonResponse(data , safe=False)
    else:
        return JsonResponse({"message":"Vous avez publier aucune annonce"})

        
@csrf_exempt
def supprimerAnnounce(request , pk):
    if request.method == 'DELETE':
        try :
            annonce = Annonce.objects.get(id = pk)
            annonce.delete()
            return JsonResponse({"message" : "annonce supprimé"})
        except Exception as e:
            print(str(e))
            return JsonResponse({"message" : "erreur : " + str(e)}) 
    return JsonResponse({"message" : "requete non DELETE"})

@csrf_exempt
def modifierAnnounce(request , pk):
    if request.method == 'PUT':
        annonce = Annonce.objects.get(id = pk)
        annonce_updated = json.loads(request.body)
        description = annonce_updated['description']
        group_sanguin = annonce_updated['groupSanguin']
        place = annonce_updated['place']
        date_de_don_max = annonce_updated['date_de_Don_max']
        numerotelephone = annonce_updated['numerotelephone']
    # date_de_modification = annonce_updated['date_de_modification']  # Si nécessaire

    # Mettre à jour les champs de l'annonce
        annonce.description = description
        annonce.groupSanguin = group_sanguin
        annonce.place = place
        annonce.date_de_Don_max = date_de_don_max
        annonce.numerotelephone = numerotelephone
        annonce.save()
        return JsonResponse({"message":"annonce mets a jour"})

@csrf_exempt
def signalerProbelem(request):
  if request.method == 'POST':
      data = json.loads(request.body)
      utilisateur = Utilisateur.objects.get(id = data["id"])
      probleme = Problems.objects.create(
        problem = data["problem"],
        utilisateur_src = utilisateur
       )
      return JsonResponse({"message" : "probleme signalé"})
  return JsonResponse({"message" : "requete doit etre post"})
   
def createDemande(request):
    return request

def modifierEtatDemande(request):
    return request

def recupererDonneurs(request):
    return request

