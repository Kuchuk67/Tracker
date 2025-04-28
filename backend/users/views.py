from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from users.serializer import UserCreateSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
