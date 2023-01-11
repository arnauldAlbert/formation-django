from django.db import models

# Create your models here.
class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    biographie = models.TextField(null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} "

    def __repr__(self):
        return self.nom

    def dict(self):
        return {"nom":self.nom,"prenom":self.prenom, "date_naissance":self.date_naissance,"biographie":self.biographie}

class Livre(models.Model):
    titre = models.CharField(max_length=120)
    nombre_pages = models.IntegerField()
    auteur = models.ForeignKey("Auteur", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"le livre {self.titre} de {self.nombre_pages} pages a été écrit par {self.auteur.nom}"
