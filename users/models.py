from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    TYPE = (
        ('SITTER', ('sitter')),
        ('PERANT', ('parent'))
    )
    user_birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(default='', max_length=50, unique=True)
    # photo = ImageField(_('photo'), blank=True, default=DEFAULT_PHOTO)
    fcm = models.CharField(max_length=250, null=True, blank=True) #FCM token for push notification
    idsn = models.CharField(max_length=128, null=True, db_index=True, blank=True) #ID facebook
    title = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(
        max_length=32,
        choices=TYPE,
        default='SITTER',
    )

    class Meta:
        app_label = 'users'

    def token(self):
        return self.token()


class FacebookFriend(models.Model):
    user = models.ForeignKey(CustomUser, related_name="facebook_friends", on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # follow = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.user, self.friend)


