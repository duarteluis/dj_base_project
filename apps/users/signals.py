from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProfilUser

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.type == sender.TYPEPROFILE.USER:
        profile_ = ProfilUser(user=instance)
        profile_.save()
