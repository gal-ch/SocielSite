from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserDetailAPIView, FacebookLoginView, fb_exchange_token
from django.conf.urls import url, include
from . import views


app_name = 'accounts-api'
urlpatterns = [
    path('accounts-rest/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),

    path('auth/facebook/', FacebookLoginView.as_view(), name="fb_login"),
    path('user_list/', views.UserListView.as_view(), name='user-list'),
    path('user_detail/<pk>', UserDetailAPIView.as_view(), name='detail'),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('auth/fb_exchange/', fb_exchange_token, name='fb_exchange_token'),

]