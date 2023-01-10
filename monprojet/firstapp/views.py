from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def formulaire(request):
    return render(request, "formulaire.html")

def traitement(request):
    nom = ""
    nom = request.GET["nom"]
    return render(request,"traitement.html",{"nom": nom})