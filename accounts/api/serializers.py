import rest_auth.serializers
from rest_framework import serializers
from rest_auth.registration.serializers import SocialLoginSerializer
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'user_type')

# class FacebookRegisterSerializer(serializers.ModelSerializer):
#     email = serializers.CharField()
#     photo = serializers.CharField(required=False, write_only=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'first_name', 'last_name', 'username', 'idsn']
#         extra_kwargs = {
#             'first_name': {'required': False, 'write_only': True},
#             'last_name': {'required': False, 'write_only': True},
#             'username': {'write_only': True},
#             'email': {'write_only': True},
#             'idsn': {'write_only': True, 'required':True},
#         }
#
#     def create(self, validated_data):
#         url = validated_data.get('photo')
#         del validated_data['photo']
#         user = CustomUser.objects.create_user(type="facebook", **validated_data)
#
#         return user
#
#
# class ListFacebookFriendSerializer(serializers.ModelSerializer):
#
#     id = serializers.StringRelatedField(source='friend.id')
#     username = serializers.StringRelatedField(source='friend.username')
#     first_name = serializers.StringRelatedField(source='friend.first_name')
#     last_name = serializers.StringRelatedField(source='friend.last_name')
#     # photo = serializers.StringRelatedField(source='friend.photo.url')
#     follow = serializers.SerializerMethodField()
#
#     def get_follow(self, obj):
#         return obj.user.follows.filter(follow=obj.friend).exists()
#         # return Follow.objects.filter(user=obj.user, follow=obj.follow).exists()
#
#     class Meta:
#         model = FacebookFriend
#         fields = ('username', 'first_name', 'last_name', 'photo', 'follow')
#
class GenerateFacebookList(serializers.Serializer):
    token = serializers.CharField(required=True)




