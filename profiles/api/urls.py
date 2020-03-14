from django.conf.urls import url
from django.urls import include, path
# from .views import FacebookLogin
from profiles.api.views import BabysiiterProfileAPIView, BabysiiterProfileDetailAPIView

app_name = 'profiles-api'
urlpatterns = [
    path('users/', include('users.api.urls')),
    path('sitter-list-api/', BabysiiterProfileAPIView.as_view()),
    path('sitter-detail-api/<pk>', BabysiiterProfileDetailAPIView.as_view()),


    path('rest-auth/', include('rest_auth.urls')),
    path('account/', include('allauth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),

]