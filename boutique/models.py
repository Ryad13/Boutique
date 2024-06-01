# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    est_disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product/images', null=True, blank=True)

    def __str__(self):
        return self.nom
        
class Commande(models.Model):
    nom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    date_commande = models.DateTimeField(auto_now_add=True)
    # etat_commande = models.CharField(max_length=100)
    is_delivered = models.BooleanField(default=False)
    def __str__(self):
            return self.nom_client
        
class ElementCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='elementcommandes')
    quantite = models.IntegerField()
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='elementcommandes')
    
    def __str__(self):
        return self.produit.nom