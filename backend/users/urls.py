from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
from users.views import UserCreateAPIView

from rest_framework.permissions import AllowAny
# from users.apps import UsersConfig
# from users.views import (UserViewSet,)

app_name = "users"

urlpatterns = [
    #path('user/', UserViewSet.as_view({'get':'list'}), name='user'),
    path('register/', UserCreateAPIView.as_view(),name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
          name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)),
          name='token_refresh'),
    

]


