from . import views
from django.urls import path 

urlpatterns = [
path('createUser/' , views.createUser),
path('ajouterDonneur/' , views.ajouterDonneur),
path('getUser/<str:email>' , views.getUser),
path('updaterUser/<str:utilisateur_id>' , views.update_utilisateur),
path('createAnounce/<str:pk>' , views.createAnounce),
path('getAllAnnounces/' , views.recuperToutLesAnnonces),
path('getAllAnnouncesUser/<str:pk>' , views.recupererAnnoncesUser),
path('SignalerProbleme/' , views.signalerProbelem),






    # <str:pk> means pk est un string
]  
    
