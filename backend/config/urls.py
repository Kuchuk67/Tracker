from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
from rest_framework.permissions import AllowAny
from rest_framework import routers
from config.settings import API_VERSION
from rest_framework.permissions import AllowAny
from users.views import UserViewSet, UserCreateAPIView


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API документация к проекту",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(API_VERSION+"schema/", SpectacularAPIView.as_view(), name="schema"),
    path(API_VERSION+"swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui" ),
    # habit_tracker
    path(API_VERSION, include("habit_tracker.urls", namespace="habit")),
    # users
    path(API_VERSION, include("users.urls", namespace="users")),

]

