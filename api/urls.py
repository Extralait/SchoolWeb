from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, OrganizationViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'specialty', OrganizationViewSet)


from django.urls import include, path

from .views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    path("", include(router.urls)),
    path("token/", CustomAuthToken.as_view(), name='token'),
    # path("specialty/<int:pk>", OrganizationViewSet.as_view(), name='specialty'),
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
]
