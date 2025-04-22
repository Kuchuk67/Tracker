from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from config.settings import API_VERSION
from habit_tracker.views import HabitViewsSet, HabitListViews


router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r'habit',
                viewset=HabitViewsSet,
                basename = 'habit'
                )

app_name = "habit"

urlpatterns = [
    # habit_tracker
    path('', include(router.urls)),
    path("habit_list/", HabitListViews.as_view(), name="habit_list"),


]