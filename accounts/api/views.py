import requests
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import generics, mixins, status
OAUTH2_REDIRECT_URI = 'http://localhost:8000/callback'
from SitterWeb import secrets
from .serializers import *
from allauth.account.adapter import get_adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from accounts import facebook
User = get_user_model()


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    serializer_class = SocialLoginSerializer


class UserListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class FacebookLogin(SocialLoginView):
#     """
#     Facebook login for system user accounts
#     """
#     adapter_class = FacebookOAuth2Adapter
#     client_class = OAuth2Client
#     callback_url = OAUTH2_REDIRECT_URI + "?chan=facebook"
#     serializer_class = SocialLoginSerializer
#
#     def process_login(self):
#         get_adapter(self.request).login(self.request, self.user)
#
#

#
#
def fb_exchange_token(request):
    """
    DEPRECATED Exchange a short lived facebook token for a long lived one
    """
    fb = facebook.Facebook()
    print(fb.client_secret)
    r = requests.get(fb.token_url + '?grant_type=fb_exchange_token' +
            '&client_id=' + secrets.SOCIAL_AUTH_FACEBOOK_KEY +
            '&client_secret=' + secrets.SOCIAL_AUTH_FACEBOOK_SECRET +
            '&fb_exchange_token=' + request.GET['access_token'])
    return HttpResponse(r.text)





