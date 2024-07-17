from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import User


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, created, **kwargs):
    print(instance.username)
