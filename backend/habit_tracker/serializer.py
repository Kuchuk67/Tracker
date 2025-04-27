from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        )
from habit_tracker.models import Habit
from habit_tracker.validators import (SimultaneousSelected,
                                        TimeValid,
                                        SignNice,
                                        HabitNiceValid,
                                        PeriodValid,
                                      )
from habit_tracker.task import TaskManager

class HabitSerializer(ModelSerializer):



    class Meta:
        model = Habit
        fields = ["place",
                  "time_action",
                  "action",
                  "nice",
                  "related",
                  "period",
                  "reward",
                  "time",
                  "public",
                  "user", ]
        validators = (SimultaneousSelected(),
                      TimeValid(),
                      SignNice(),
                      HabitNiceValid(),
                      PeriodValid(),
                      )
        
    def create(self, validated_data):
        instance = super().create(validated_data)
        TaskManager(instance.pk, instance.period, instance.time_action).create()
        return instance
    