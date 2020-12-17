from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import userProfile


@receiver(post_save, sender=userProfile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance)


