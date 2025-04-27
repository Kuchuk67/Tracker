from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    # pay = SerializerMethodField()
    """def get_pay(self, user):
    return [{"дата":pay_item.data_at,
             "сумма":pay_item.summa_pay
             } for pay_item in Pay.objects.filter(user=user).order_by('id')]"""

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "password",
            "email",
            "api_telegram",
        ]


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(UserCreateSerializer, self).create(validated_data)
