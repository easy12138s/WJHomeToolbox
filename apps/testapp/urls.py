from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.testapp import views


urlpatterns = [
    path('fbv/list/', views.fbv_test, name = 'fbv-test'),
    path('cbv/list/', views.cbv_test.as_view(), name = 'cbv-test'),
    path('gcbv/list/', views.gcbv_test.as_view(), name = 'gcbv-test'),
]
