from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    TYPE = (
        ('SITTER', ('sitter')),
        ('PERANT', ('parent'))
    )
    mobile = models.CharField(max_length=10, blank=True, null=True)
    user_birthday = models.DateField(blank=True, null=True)
    type = models.CharField(
        max_length=32,
        choices=TYPE,
        default='SITTER',
    )

    class Meta:
        app_label = 'users'


# class Address(models.Model):
#     profile = models.ForeignKey('Profile', related_name='addresses', on_delete=models.CASCADE, null=True)
#     address = models.TextField()
#     lat = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
#     lng = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
#     user_type = models.PositiveSmallIntegerField(default=1)
#     avatar = models.ImageField(blank=True, upload_to='avatar/')
#     gender = models.CharField(max_length=64, blank=True)
#     description = models.TextField(blank=True)
#     specialization = models.TextField(blank=True)
#
#     dob = models.DateField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#
#     phone = models.CharField(max_length=64, unique=True)
#     national_id = models.CharField(max_length=100, blank=True)
#     driving_license = models.CharField(max_length=100, blank=True)
#     license_plate = models.CharField(max_length=255, blank=True)
#     delivery_method = models.PositiveSmallIntegerField(default=0)