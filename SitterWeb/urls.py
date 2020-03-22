from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('profiles.urls')),
    path('accounts-api/', include('accounts.api.urls')),
]





