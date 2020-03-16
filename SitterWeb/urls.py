from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    url('account/', include('allauth.urls')),
    path('', include('profiles.urls')),
    path('users/', include('users.api.urls')),

]





