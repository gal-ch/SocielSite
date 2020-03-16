from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    url('account/', include('allauth.urls')),
    path('', include('users.api.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^rest-auth/facebook/$', FacebookLoginView.as_view(), name='fb_login'),


]





