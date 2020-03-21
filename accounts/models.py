from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from requests import request, HTTPError
from django.db import models


class UserManager(DefaultUserManager):

    def get_or_create_facebook_user(self, user_pk, extra_data, profile_url):
        print(extra_data)
        user = User.objects.get(pk=user_pk)
        user.user_type = user.USER_TYPE_FACEBOOK
        user.profile_image = profile_url
        user.user_birthday = models.DateField(blank=True, null=True)

        try:
            response = request('GET', profile_url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass

        user.save()

        return user


class CustomUser(AbstractUser):
    USER_TYPE_DJANGO = 'D'
    USER_TYPE_FACEBOOK = 'F'
    USER_TYPE_CHOICES = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='F')
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return self.username




