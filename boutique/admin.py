from django.contrib import admin

# Register your models here.
from .models import *
 
admin.site.register(Commande)
admin.site.register(Produit)
admin.site.register(ElementCommande)
