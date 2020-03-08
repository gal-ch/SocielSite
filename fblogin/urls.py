from django.urls import path

from fblogin import views
from fblogin.views import UserList, UserDetails, GroupList
from django.contrib.auth import views as auth_views

app_name = 'fblogin'
urlpatterns = [
    #   path('accounts/login/', auth_views.LoginView.as_view()),
    path('secret', views.secret_page, name='secret'),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]
