from django.db.models.signals import pre_delete, post_save
from rest_framework.authtoken.models import Token
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from io import BytesIO
from urllib.request import urlopen
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# @receiver(user_signed_up)
# def user_signed_up(request, user, **kwargs):
#     if len(user.socialaccount_set.all()) > 0:
#         social_account = user.socialaccount_set.all()[0]
#         uid = social_account.uid
#         gender = social_account.extra_data.get('gender', None)
#         user.gender = gender
#         birthday = social_account.extra_data.get('birthday', None)
#         user.birthday = birthday
#         link = social_account.get_avatar_url()
#     #    avatar_image = urlopen(avatar)
#     #    io = BytesIO(avatar_image.read())
#       #  user.profile_image.save('{}.jpg'.format(uid), File(io))
#         user.name = user.get_full_name()
#     user.save()



