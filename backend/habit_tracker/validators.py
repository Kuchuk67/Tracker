from habit_tracker import exceptions
from urllib.parse import urlparse

class SimultaneousSelected:
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """
    requires_context = True
    def __call__(self, value, serializer_field):
        if value.get("related") and value.get("nice"):
            raise exceptions.UnprocessableEntityError(
                dict(
                    error="ValidationError",
                    serial="одновременный выбор 'related' и 'nice'.")
            )

class TimeValid:
    """
    Время выполнения должно быть не больше 120 секунд.
    """
    requires_context = True
    def __call__(self, value, serializer_field):
        #time_action = urlparse(self.time_action)
        print("*****",type(value.get("time")))
        print(value.get("time"))
        if  value.get("time") > 120 or value.get("time") <= 0:
            raise exceptions.UnprocessableEntityError(
                dict(error="ValidationError",
                     serial="должно быть в пределах 1-120 секунд.")
            )
