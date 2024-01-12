from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.testapp import views

# 注册通用视图集
router = DefaultRouter()
router.register(prefix='viewsets', viewset=views.vscbv_test)

urlpatterns = [
    path('fbv/list/', views.fbv_test, name='fbv-test'),
    path('cbv/list/', views.cbv_test.as_view(), name='cbv-test'),
    path('gcbv/list/', views.gcbv_test.as_view(), name='gcbv-test'),
    # 路径自动分发
    path("", include(router.urls))

]
