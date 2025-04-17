from rest_framework.generics import ListAPIView,RetrieveAPIView, CreateAPIView
from users.models import CustomUser
from users.serializer import UserCreateSerializer, UserSerializer
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()




