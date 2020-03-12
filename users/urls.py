from django.urls import include, path

from .views import UserListView
app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view()),
]