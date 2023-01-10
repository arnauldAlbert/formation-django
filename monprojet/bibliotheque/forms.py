from django.forms import ModelForm
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