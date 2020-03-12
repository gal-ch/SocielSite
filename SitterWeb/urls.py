# from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/', include('profiles.urls')),
    path('api-auth/', include('rest_framework.urls')),

]




