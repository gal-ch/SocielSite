# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
from rest_framework import generics, mixins
from profiles.api.serializers import BabysitterProfileSerializer
from profiles.models import BabysitterProfile


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter



