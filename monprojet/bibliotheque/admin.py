from django.contrib import admin

# Register your models here.
from .models import Auteur, Livre

admin.site.register(Auteur)
admin.site.register(Livre)