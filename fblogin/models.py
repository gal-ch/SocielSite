from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class UserFacebook(models.Model):
    user = models.ForeignKey(User, primary_key=True)
    facebook_id = models.BigIntegerField(default=0, unique=True)
    access_token = models.CharField(max_length=400, default="")
    is_show = models.BooleanField(default=True)

    class Meta:
        app_label = 'fblogin'


