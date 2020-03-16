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


class RecommendationsOfSitter(models.Model):
    recommendation = models.TextField(blank=True, null=True)
    sitter = models.ForeignKey(BabysitterProfile, on_delete=models.CASCADE,related_name='recommendations')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recommendation} {self.sitter.user} {self.author}"


class ParentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='parent')
    # name = models.ForeignKey(User.default=None)
    city = models.CharField(max_length=200)
    kidsAge = models.IntegerField(default=0)
    about = models.TextField(default=None)

    def __str__(self):
        return f"{self.pk} {self.user} {self.city} {self.kidsAge} {self.about} "

    def __unicode__(self):
        return u"%s" % self.user

    def get_extra_data(self):
        return self.user.socialaccount_set.first().extra_data

