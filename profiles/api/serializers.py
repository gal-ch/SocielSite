# from rest_framework import serializers
# from profiles.models import BabysitterProfile
#
#
# class BabysitterProfileSerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField('get_username_from_author')
#     image = serializers.SerializerMethodField('validate_image_url')
#
#     class Meta:
#         model = BabysitterProfile
#         fields = ['pk', 'city', 'age', 'about', 'experienceYears']
#
#
