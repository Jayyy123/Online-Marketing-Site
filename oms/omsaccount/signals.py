from turtle import pos
from django.dispatch import receiver
from django.db.models.signals import post_delete,post_save
from .models import User_Profile
from django.contrib.auth.models import User

@receiver(post_save, sender = User)
def create_profile(instance, created, sender, **kwargs):
    if created:
        user = instance
        profile = User_Profile.objects.create(
            user = user,
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
        )
@receiver(post_delete, sender = User_Profile)
def delete_profile(instance, sender, **kwargs):
    user = instance.user
    user.delete()
    