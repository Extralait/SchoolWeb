from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, OrganizationViewSet, CustomAuthToken, BestStudentViewSet, AchievementsViewSet, \
    PhotoViewSet, UserViewSet
from django.urls import include, path
from .views import UserProfileListCreateView, userProfileDetailView

router = routers.DefaultRouter()
router.register(r'events', EventViewSet,basename='event')
router.register(r'organisations', OrganizationViewSet,basename='organisation')
router.register(r'beststudents', BestStudentViewSet,basename='beststudent')
router.register(r'achievements', AchievementsViewSet,basename='achievements')
router.register(r'photo', PhotoViewSet,basename='photo')
router.register(r'user', UserViewSet,basename='user')


urlpatterns = [
    path("", include(router.urls)),
    path("token/", CustomAuthToken.as_view(), name='token'),
    # path("specialty/<int:pk>", OrganizationViewSet.as_view(), name='specialty'),
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
]