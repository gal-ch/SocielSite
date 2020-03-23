from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('profiles.urls')),
    path('accounts-api/', include('accounts.api.urls')),


    url(r'^1234/$', TemplateView.as_view(template_name="home.html")),
    url(r'^api/comments/', include('comments.api.urls')),
]



from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

