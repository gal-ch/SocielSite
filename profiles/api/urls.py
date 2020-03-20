from django.conf.urls import url
from django.urls import include, path
from profiles.api.views import BabysiiterProfileAPIView, BabysiiterProfileDetailAPIView

app_name = 'profiles-api'
urlpatterns = [

    path('sitter-list-api/', BabysiiterProfileAPIView.as_view()),
    path('sitter-detail-api/<pk>', BabysiiterProfileDetailAPIView.as_view()),
    path('sitter-detail-api/<pk>', BabysiiterProfileDetailAPIView.as_view()),

]