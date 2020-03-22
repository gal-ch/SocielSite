from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
User = get_user_model()
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse


class UserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
                  'email',
                  'username',
                  'first_name',
                  'last_name',
                  'user_type',
                  'profile_link',
                  'birthday',
                  'gender',
                  'uri',
                  )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('accounts-api:detail', kwargs= {'pk':obj.pk}, request=request)
        # return "users/user_detail/{pk}".format(pk=obj.pk)


class GenerateFacebookList(serializers.Serializer):
    token = serializers.CharField(required=True)


class SignUpSerializer(RegisterSerializer):
    name = serializers.CharField(required=True, write_only=True)

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user

