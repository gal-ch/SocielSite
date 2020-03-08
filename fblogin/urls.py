from django.conf.urls import url
from django.urls import path, include

from fblogin.views import FacebookLogin, FacebookConnect

urlpatterns = [
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect')
]