from .models import Commande
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
# Create your views here.

def commandes_list(request):
        commandes = Commande.objects.filter(date_commande__lte=timezone.now()).order_by('date_commande')
        return render(request, 'boutique/commandes_list.html', {'commandes': commandes})
    
    
def commande_detail(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        form = MoveForm(request.POST, instance=commande)
        if form.is_valid():
            commande = form.save(commit=False)
            commande.date_commande = timezone.now()
            commande.save()
            form.save()
            return redirect('commande_detail', pk=pk)
    else:
        form = MoveForm(instance=commande)

    order_elements = commande.elementcommandes.all()
    total_price=0
    for element in commande.elementcommandes.all():
        total_price += element.produit.prix*element.quantite
    print(total_price)
    
    return render(request, 'boutique/commande_detail.html', 
                  {'commande': commande, 'form': form, 'order_elements': order_elements, 'total_price':total_price})