from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        )
from habit_tracker.models import Habit


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = ["place",
                  "day_action",
                  "time_action",
                  "action",
                  "nice",
                  "related",
                  "period",
                  "reward",
                  "time",
                  "pablic",
                  "user", ]
        
