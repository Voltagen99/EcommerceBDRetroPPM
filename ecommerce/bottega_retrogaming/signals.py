from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    # Questo segnale crea un profilo Customer automaticamente ogni volta
    # che un nuovo oggetto User viene creato.

    if created:
        CustomUser.objects.create(user=instance, name=instance.username, email=instance.email)