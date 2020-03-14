from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.api.serializers import UserSerializer
from users.models import CustomUser
from rest_framework import generics, mixins


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    authentication_classes = [JSONWebTokenAuthentication]


class UserListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #only Authentication user can creat profile

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)