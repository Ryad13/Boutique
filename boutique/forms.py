from django import forms
 
from .models import Commande
 
class MoveForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['is_delivered']