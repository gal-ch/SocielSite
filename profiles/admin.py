from django.contrib import admin
from .models import BabysitterProfile, ParentProfile, RecommendationsOfSitter

admin.site.register(BabysitterProfile)
admin.site.register(ParentProfile)
admin.site.register(RecommendationsOfSitter)