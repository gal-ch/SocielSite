from rest_framework import serializers
from profiles.models import BabysitterProfile
from users.models import CustomUser
import rest_auth.serializers
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'mobile', 'first_name', 'last_name', 'user_birthday', 'type')





