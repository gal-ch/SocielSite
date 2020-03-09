# from django.urls import path
#
# from fblogin import views
# from .views import UserList, UserDetails, GroupList, SocialLoginView
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'fblogin'
urlpatterns = [
    #path('accounts/login/', auth_views.LoginView.as_view()),

]
