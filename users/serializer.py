# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: serializer.py
    @time: 2023/12/25 10:28
"""
from rest_framework import serializers
from users.models import HomeUsers


class HomeUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeUsers
        fields = '__all__'
