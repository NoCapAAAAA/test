from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', include('client.urls'), name='home'),
    path('accounts/', include('authentication.urls'), name='auth'),
    path('staff/', include('organization.urls'), name='organization'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)