from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField
                                        )
from users.models import CustomUser



class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username",
                  "email",
                  ]