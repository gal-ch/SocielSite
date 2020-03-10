from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework import serializers, generics, permissions
admin.autodiscover()


class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'address_line_1','address_line_2','city','pin_code','photo','password','access_token')


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('user', 'friend')


class MessagesSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer()
    recipient = ProfileSerializer()
    sent_timestamp = serializers.Field()
    class Meta:
            model = Message
            fields = ('body', 'recipient', 'sender', 'sent_timestamp')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


# class SocialSerializer(serializers.Serializer):
#     """
#     Serializer which accepts an OAuth2 access token and provider.
#     """
#     provider = serializers.CharField(max_length=255, required=True)
#     access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)
