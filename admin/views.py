from user.models import CustomUser
from user.serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
