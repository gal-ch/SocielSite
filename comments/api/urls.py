from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from comments.api.views import CommentListAPIView

app_name = 'comments'
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),


]


