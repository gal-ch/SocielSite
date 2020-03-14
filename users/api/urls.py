from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'users-api'
urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),

]