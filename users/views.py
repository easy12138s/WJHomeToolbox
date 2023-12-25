from django.shortcuts import render
from users.models import HomeUsers
from rest_framework import viewsets
from users.serializer import HomeUsersSerializers

# test
class HomeUsersViewSet(viewsets.ModelViewSet):
    queryset = HomeUsers.objects.all()
    serializer_class = HomeUsersSerializers
