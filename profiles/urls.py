from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import BabysitterProfileListView, BabysitterProfileDetailView, BabysitterProfileUpdate, \
    ParentProfileListView, \
    ParentProfileDetailView, ParentUpdate, RecommendationsFormView, BabysitterProfileCreate

app_name = 'core'
urlpatterns = [
    path('', BabysitterProfileCreate.as_view(), name='user-add'),
    path('sitter_list/', BabysitterProfileListView.as_view(), name='sitter-list'),
    path('sitter/<int:pk>/', BabysitterProfileDetailView.as_view(), name='sitter-detail'),
    path('user/<int:pk>/', BabysitterProfileUpdate.as_view(), name='user-update'),
    path('parent/', ParentProfileListView.as_view(), name='parent-list'),
    path('parent/<int:pk>/', ParentProfileDetailView.as_view(), name='parent-detail'),
    path('profiles-api/', include('profiles.api.urls')),
]