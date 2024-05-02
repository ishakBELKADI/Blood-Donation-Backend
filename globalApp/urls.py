from . import views
from django.urls import path 

urlpatterns = [
path('createUser/' , views.createUser),
path('ajouterDonneur/' , views.ajouterDonneur),
path('getUser/<str:email>' , views.getUser),
path('updaterUser/<str:utilisateur_id>' , views.update_utilisateur),



    # <str:pk> means pk est un string
]  
    
