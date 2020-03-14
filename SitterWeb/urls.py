from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('account/', include('allauth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),


]





