
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.api.serializers import UserSerializer, ListFacebookFriendSerializer, FacebookRegisterSerializer
from users.facebook import Facebook
from users.models import CustomUser, FacebookFriend
from rest_framework import generics, mixins, status
from django.shortcuts import get_object_or_404

class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    # authentication_classes = [JSONWebTokenAuthentication]


# class UserListView(generics.ListCreateAPIView):
#     queryset = models.CustomUser.objects.all()
#     serializer_class = serializers.UserSerializer
#


class UserListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #only Authentication user can creat profile

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FacebookFriendListApiView(generics.ListAPIView):
    serializer_class = ListFacebookFriendSerializer

    def get_queryset(self):
        return FacebookFriend.objects.filter(user = self.request.user)


class AuthFacebookView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if "token" in request.data:
            fb = Facebook(request.data['token'])
            user = get_object_or_404(CustomUser, idsn=fb.get_id())

            if user.type == "facebook":
                token = user.token()
                user = UserSerializer(instance=user).data
                return Response({"token": token, "user": user}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FacebookRegisterApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        if "token" in request.data and "username" in request.data:
            facebook = Facebook(request.data['token'])

            # User.objects.filter(idsn=facebook.get_id()).delete()

            serializer = FacebookRegisterSerializer(data=facebook.get_profile(request.data['username']))
            serializer.is_valid(raise_exception=True)
            serializer.save()

            user = UserSerializer(instance=serializer.instance)
            token = serializer.instance.token()

            friends_id = facebook.get_friends()

            if friends_id:
                friends = CustomUser.objects.filter(idsn__in=friends_id)
                FacebookFriend.objects.bulk_create(
                    [FacebookFriend(user_id=serializer.instance.id, friend=x) for x in friends.all()]
                    +
                    [FacebookFriend(user=x, friend_id=serializer.instance.id) for x in friends.all()]
                )

            return Response({"token": token, "user": user.data}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


