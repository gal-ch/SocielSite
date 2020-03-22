from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from requests import request, HTTPError
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.http import request


class UserManager(DefaultUserManager):

    def get_or_create_facebook_user(self, user_pk, extra_data, profile_url):
        print(extra_data)
        user = User.objects.get(pk=user_pk)
        user.user_type = user.USER_TYPE_FACEBOOK
        user.profile_link = profile_url


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
    birthday = models.CharField(max_length=15,blank=True, null=True )
    profile_link = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=15,blank=True, null=True )
    user_token = models.ManyToManyField(Token)

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_user_token(self, user_pk):
        return Token.objects.get_or_create(user_id=user_pk)

