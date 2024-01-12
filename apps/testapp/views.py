from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .models import HomeUsers
from .serializer import HomeUsersSerializers
from rest_framework import viewsets

# 信号机制生成token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# django信号机制
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def generate_token(sender, instance=None, created=False, **kwargs):
    """
    创建用户时自动生成token
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance)


"""     函数视图 FBV    """
@api_view(['GET', 'POST'])
def fbv_test(request):
    if request.method == "GET":
        userAll = HomeUsers.objects.all()
        s = HomeUsersSerializers(userAll, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        s = HomeUsersSerializers(data=request._post)
        if s.is_valid():
            s.save()
            return Response(data='ok', status=status.HTTP_200_OK)
        return Response(data=s.errors, status=status.HTTP_411_LENGTH_REQUIRED)


"""类视图 CBV"""

class cbv_test(APIView):
    @staticmethod
    def get(request):
        """

        :param request:
        :return:
        """
        userAll = HomeUsers.objects.all()
        s = HomeUsersSerializers(instance=userAll, many=True)  # 获取数据库数据 instance=
        return Response(data=s.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        """

        :param request:
        :return:
        """
        s = HomeUsersSerializers(data=request.data)  # 获取前端数据 data=
        if s.is_valid():
            s.save()
            return Response(data='ok', status=status.HTTP_200_OK)
        return Response(data=s.errors, status=status.HTTP_411_LENGTH_REQUIRED)


"""通用类视图 GCBV"""
class gcbv_test(generics.ListCreateAPIView):
    queryset = HomeUsers.objects.all()
    serializer_class = HomeUsersSerializers


"""视图集 VIEWSETS"""
class vscbv_test(viewsets.ModelViewSet):
    queryset = HomeUsers.objects.all()
    serializer_class = HomeUsersSerializers


""""认证与权限"""
