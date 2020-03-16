from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import CustomUser

ageChoices = [(x, int(x)) for x in range(18, 70)]
expChoices = [(x, int(x)) for x in range(0, 30)]


class BabysitterProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='babysitter')
    city = models.CharField(max_length=200, default=None)
    age = models.IntegerField(choices=ageChoices, default=18)
    about = models.TextField(default=None)
    experienceYears = models.IntegerField(choices=expChoices, default=0, blank=True)


    def __str__(self):
        return f"{self.pk} {self.user} {self.city} {self.age} {self.about} {self.experienceYears}"

    def __unicode__(self):
        return u"%s" % self.user

