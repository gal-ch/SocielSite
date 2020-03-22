from typing import Any
from django.http import HttpRequest, HttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse


# class SocialAccountAdapter(DefaultSocialAccountAdapter):
#
#     def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
#         return True
#

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        print("DefaultSocialAccountAdapter.save_user")
        user = super(MySocialAccountAdapter, self).save_user(request, sociallogin, form)
        user.email = sociallogin.user.email
        user.birthday = sociallogin.account.extra_data['birthday']
        user.profile_link = sociallogin.account.extra_data['link']

        user.save()

        return user