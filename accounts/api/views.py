import requests
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework import generics, mixins, status, viewsets
from SitterWeb import secrets
from accounts import facebook
User = get_user_model()
from django.http import HttpResponse, JsonResponse, FileResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import generics, permissions, status, views
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    serializer_class = SocialLoginSerializer


class UserListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

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


