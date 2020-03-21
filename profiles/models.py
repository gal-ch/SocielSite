from datetime import timezone, datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.timesince import timesince
User = get_user_model()
from accounts.models import CustomUser

ageChoices = [(x, int(x)) for x in range(18, 70)]
expChoices = [(x, int(x)) for x in range(0, 30)]


class BabysitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='babysitter')
    city = models.CharField(max_length=200, default=None)
    age = models.IntegerField(choices=ageChoices, default=18)
    about = models.TextField(default=None)
    experienceYears = models.IntegerField(choices=expChoices, default=0, blank=True)

    def __str__(self):
        return f"{self.pk} {self.user} {self.city} {self.age} {self.about} {self.experienceYears}"

    def get_email_user(self, user):
        return self.user.email

    def get_extra_data(self):
        return self.user.socialaccount_set.first().extra_data

    def get_absolute_url(self):
        return reverse("core:sitter-detail", kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse("core:sitter-detail", kwargs={'pk': self.pk})


class RecommendationsOfSitter(models.Model):
    recommendation = models.TextField(blank=True, null=True)
    sitter = models.ForeignKey(BabysitterProfile, on_delete=models.CASCADE,related_name='recommendations')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publish_data = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return f"{self.recommendation} {self.sitter.user} {self.author}"

    @property
    def age(self):
        now = datetime.now()
        publish_time = datetime.combine(self.publish_data, datetime.now().min.time())
        try:
            difference = now - publish_time
        except:
            return "unknown"
        if difference <= timedelta(minutes=1):
            return "just now"
        return '{time} ago'. format(time=timesince(publish_time).split(',')[0])


class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent')
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

    def get_absolute_url(self):
        return reverse("core:parent-detail", kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse("core:parent-detail", kwargs={'pk': self.pk})


class RecommendationsOfParent(models.Model):
    recommendation = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(ParentProfile, on_delete=models.CASCADE, related_name='recommendations')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recommendation} {self.parent.user} {self.author}"

