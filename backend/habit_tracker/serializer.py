from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        )
from habit_tracker.models import Habit


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        
    def to_representation(self, value):
        #return "rgb(%d, %d, %d)" % (value.red, value.green, value.blue)
        return  222 # int(value.day_action) + 1

    def to_internal_value(self, data):
        data = data.get('day_action')
        #red, green, blue = [int(col) for col in data.split(',')]
        return 555 #int(data) - 1
        #pass