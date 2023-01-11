from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms, models

# Create your views here.
def ajout(request):
    form = forms.AuteurForm()
    return render(request, "bibliotheque/ajout.html", {"form": form})

def traitement(request):
    lform = forms.AuteurForm(request.POST)
    if lform.is_valid():
        auteur = lform.save()
        return render(request, "bibliotheque/affiche.html", {"auteur": auteur})
    else:
        return render(request, "bibliotheque/ajout.html", {"form": lform})

def all(request):
    liste = models.Auteur.objects.all()
    return render(request,"bibliotheque/index.html",{"liste":liste})

def read(request, id):
    auteur = models.Auteur.objects.get(pk = id)
    return render(request,"bibliotheque/affiche.html",{"auteur": auteur})

def delete(request, id):
    auteur = models.Auteur.objects.get(pk = id)
    auteur.delete()
    return HttpResponseRedirect("/bibliotheque/")

def updateform(request,id):
    auteur = models.Auteur.objects.get(pk=id)
    form = forms.AuteurForm(auteur.__dict__)
    return render(request, "bibliotheque/update.html", {"form": form, "id":id})

def traitementupdate(request,id):
    lform = forms.AuteurForm(request.POST)
    if lform.is_valid():
        auteur = lform.save(commit=False)
        auteur.id = id
        auteur.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform})

def ajoutLivre(request):
    form = forms.LivreForm()
    return render(request, "bibliotheque/ajoutLivre.html", {"form": form})

def traitementlivre(request):
    lform = forms.LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request, "bibliotheque/affichelivre.html", {"livre": livre})
    else:
        return render(request, "bibliotheque/ajoutlivre.html", {"form": lform})

def ajoutLivre2(request,idauteur):
    form = forms.LivreForm2()
    return render(request, "bibliotheque/ajoutLivre2.html", {"form": form, "idauteur":idauteur})

def traitementlivre2(request,idauteur):
    lform = forms.LivreForm2(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.auteur_id = idauteur
        livre.auteur = models.Auteur.objects.get(pk=id)
        livre.save()
        return render(request, "bibliotheque/affichelivre.html", {"livre": livre})
    else:
        return render(request, "bibliotheque/ajoutlivre2.html", {"form": lform, "id":idauteur})