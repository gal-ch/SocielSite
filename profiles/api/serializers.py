from rest_framework import serializers
from profiles.models import BabysitterProfile


class BabysitterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabysitterProfile
        fields =[
            'user',
            'city',
            'age',
            'about',
            'experienceYears',
        ]
