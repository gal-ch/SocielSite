from django.contrib import admin
from .models import BabysitterProfile, ParentProfile, RecommendationsOfSitter

admin.site.register(BabysitterProfile)
admin.site.register(ParentProfile)


class RecommendationsOfSitterModelAdmin(admin.ModelAdmin):
    def get_age(self, obj, *args, **kwargs):
        return str(obj.age)

admin.site.register(RecommendationsOfSitter, RecommendationsOfSitterModelAdmin)