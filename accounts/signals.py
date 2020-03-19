from django.conf import settings
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from accounts.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)