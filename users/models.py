from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=10, blank=True, null=True)

    # class Meta:
    #     app_label = 'users'

    def __str__(self):
        return self.email