from django.conf.urls import url
from django.urls import include, path


from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import FacebookLoginView

app_name = 'users-api'
urlpatterns = [
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLoginView.as_view(), name='fb_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('user_list/', views.UserListView.as_view(), name='user-list'),
    path('profile/', include('profiles.api.urls')),






]