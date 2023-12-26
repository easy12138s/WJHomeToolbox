from users.models import HomeUsers
from rest_framework import viewsets
from utils.serializer import HomeUsersSerializers

# test
class HomeUsersViewSet(viewsets.ModelViewSet):
    queryset = HomeUsers.objects.all()
    serializer_class = HomeUsersSerializers
