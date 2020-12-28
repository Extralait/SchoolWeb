
from rest_framework import routers
from .views import EventViewSet, CustomAuthToken
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'events', EventViewSet,basename='event')



urlpatterns = [
    path("", include(router.urls)),
    path("token/", CustomAuthToken.as_view(), name='token'),
]
