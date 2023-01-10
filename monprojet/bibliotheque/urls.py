from django.urls import path
from . import views

urlpatterns = [
    path("ajout/", views.ajout),
    path("traitement/", views.traitement),
    path("",views.all),
    path("affiche/<int:id>/", views.read),
    path("delete/<int:id>/", views.delete),
    path("update/<int:id>/", views.updateform),
    path("traitementupdate/<int:id>/",views.traitementupdate)
]