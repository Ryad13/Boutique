from django.urls import path
from . import views

urlpatterns = [
    path('', views.commandes_list, name='commandes_list'),
    path('commande/<int:pk>/', views.commande_detail, name='commande_detail'),
    path('commande/<str:id_commande>/?<str:message>', views.commande_detail, name='commande_detail_mes'),
]