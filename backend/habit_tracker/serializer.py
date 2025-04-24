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
        
    def create(self, validated_data):
        print(validated_data)
        return Habit.objects.create(**validated_data)
    
    def list(self, data):
        print('********')
        print(self.data)
        return Habit(self.data)
    
    '''def to_representation(self, instance):
        """ Convert `username` to lowercase."""
        print('********',instance)
        ret = super().to_representation(instance)
        ret['action'] = ret['action'] + " Ура !!"
        print(ret)
        return ret'''
        
