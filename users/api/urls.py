from django.conf.urls import url
from django.urls import include, path
from . import views
from .views import FacebookLoginView

app_name = 'users-api'
urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),

    url(r'^rest-auth/facebook/$', FacebookLoginView.as_view(), name='fb_login'),



]