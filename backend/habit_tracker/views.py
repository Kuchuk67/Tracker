from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from habit_tracker.models import Habit
from habit_tracker.serializer import HabitSerializer

class HabitViewsSet(ModelViewSet):
    #pagination_class = EducationPagination
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
