from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        )
from habit_tracker.models import Habit
from habit_tracker.validators import SimultaneousSelected, TimeValid

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
                      )
        
    '''def to_representation(self, instance):
        """ Convert `username` to lowercase."""
        print('********',instance)
        ret = super().to_representation(instance)
        ret['action'] = ret['action'] + " Ура !!"
        print(ret)
        return ret

    def to_internal_value(self, data):
        print('********', data)
        valid = super().to_internal_value(data)
        return valid'''