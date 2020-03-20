from asyncio import exceptions
from rest_framework import serializers
from profiles.models import BabysitterProfile, ParentProfile
from accounts.models import CustomUser


class BabysitterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabysitterProfile
        fields =[
            'user',
            'city',
            'age',
            'experienceYears',
            'about',
        ]


class ParentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentProfile
        fields =[
            'user',
            'city',
            'kidsAge',
            'about',
        ]


# class UserSitterSerializer(serializers.ModelSerializer):
#     userprofile = BabysitterProfileSerializer()
#
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'first_name', 'last_name', 'email', 'userprofile',)
#         read_only_fields = ('id', 'username', 'email',)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         user_profile_detail = validated_data.get('userprofile')
#
#         userprofile = ''
#         try:
#             userprofile = BabysitterProfile.objects.get(user=instance.id)
#         except BabysitterProfile.DoesNotExist:
#             exceptions.NotFound(_('Error, please try later...'))
#         else:
#             userprofile.profile_pic = user_profile_detail.get('profile_pic', userprofile.profile_pic)
#
#             userprofile.facebook = user_profile_detail.get('facebook', userprofile.facebook)
#
#         userprofile.save()
#         instance.save()
#
#         return instance


