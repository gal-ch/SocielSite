from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser


class MyUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'user_type', 'birthday', 'profile_link','user_token' )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, MyUserAdmin)

