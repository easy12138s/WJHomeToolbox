from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users import views

router = DefaultRouter()
router.register('', views.HomeUsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
