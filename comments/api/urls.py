from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from comments.api.views import CommentListAPIView, CommentCreateAPIView

app_name = 'comments'
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),

]


