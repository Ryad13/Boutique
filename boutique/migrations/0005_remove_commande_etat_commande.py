# Generated by Django 5.0.6 on 2024-05-31 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_commande_is_delivered_alter_elementcommande_commande_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='etat_commande',
        ),
    ]
