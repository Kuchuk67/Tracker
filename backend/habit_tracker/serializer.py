from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        )
from habit_tracker.models import Habit


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = [
                'id',
                'user', 
                'place',
                'data',
                'action', 
                'nice',
                'related', 
                'period',
                'reward',
                'time',
                'pablic'
                ]