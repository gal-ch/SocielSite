from django.conf.urls import url
from django.urls import include, path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *


app_name = 'accounts-api'
urlpatterns = [
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user_list/', views.UserListView.as_view(), name='user-list'),
    path('user_detail/<pk>', UserDetailAPIView.as_view(), name='detail'),
    path('auth/facebook/', FacebookLoginView.as_view(), name="fb_login"),


    # path('relation/facebook-list/', FacebookFriendListApiView.as_view(), name='relation-facebook'),
    # # path('auth/facebook/', AuthFacebookView.as_view()),
    # path('auth/register/facebook/', FacebookRegisterApiView.as_view(), name='register-facebook'),

    # System users login

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('auth/fb_exchange/', fb_exchange_token, name='fb_exchange_token'),







]