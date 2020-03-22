import json

from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from profiles.models import BabysitterProfile, ParentProfile, RecommendationsOfSitter
from accounts.models import CustomUser


class RecommendationsOfSitterSerializer(serializers.ModelSerializer):
    author_user = serializers.SerializerMethodField(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = RecommendationsOfSitter
        fields = [
            'recommendation',
            'author_user',
            'publish_data',
            'uri',
        ]

    def get_author_user(self, obj):
        user = self.context.get("user")
        return obj.get_author_user(user)

    def get_uri(self, obj):
        return "users/user_detail/{pk}".format(pk=obj.author.pk)


class BabysitterProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    recommendations = RecommendationsOfSitterSerializer(read_only=True, many=True)

    class Meta:
        model = BabysitterProfile
        fields =[
            'email',
            'city',
            'age',
            'experienceYears',
            'about',
            'user',
            'recommendations',

        ]

    def get_uri(self, obj):
        return "users/user_detail/{pk}".format(pk=obj.author.pk)


class ParentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParentProfile
        fields =[
            'user',
            'city',
            'kidsAge',
            'about',
        ]



