from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from habit_tracker.models import Habit
from habit_tracker.serializer import HabitSerializer
from rest_framework.response import Response


class HabitViewsSet(ModelViewSet):
    #pagination_class = EducationPagination
    serializer_class = HabitSerializer

    def get_queryset(self):
        """
        Returns the object the view is displaying
        only for current user.
        """
        return Habit.objects.filter(user = self.request.user.pk)

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.pk
        return super().create(request, *args, **kwargs)


class HabitListViews(ListAPIView):
    # pagination_class = EducationPagination
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(pablic=True)

