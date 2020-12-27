from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # path to our account's app endpoints
    path("api/", include("api.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
