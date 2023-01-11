from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from . import models

class AuteurForm(ModelForm):
    class Meta:
        model = models.Auteur
        fields = ("nom", "prenom", "date_naissance", "biographie")
        labels = {
            "date_naissance" : _("Date de Naissance"),
            "prenom" : _("Prénom"),
        }

        localized_fields =('date_naissance',)

        widgets = {
            "date_naissance" : forms.TextInput(attrs={'type':'date',})
        }

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ("titre","nombre_pages","auteur")
        labels = {
            "nombre_pages" : _("Nombre de pages")
        }

class LivreForm2(ModelForm):
    class Meta:
        model = models.Livre
        fields = ("titre","nombre_pages")
        labels = {
            "nombre_pages" : _("Nombre de pages")
        }