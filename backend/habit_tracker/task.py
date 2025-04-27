import json
from datetime import datetime
from typing import ClassVar

from celery.local import Proxy
from django.conf import settings
from django.utils import timezone
from django_celery_beat.models import (ClockedSchedule, CrontabSchedule,
                                       IntervalSchedule, PeriodicTask)

from config.celery import app
from habit_tracker.models import Habit
from telegram_bot.services import send_telegram_message


class TaskManager:
    """
    Вызывается c созданием объекта
    Вызывает задачу по времени clocked_time
    для переданного ID
    Получает данные:
    id объекта: int
    номер для идентификации задачи: int
    дата-тайм начала (может null),
    дата-тайм финиша (может null)
    """

    def __init__(
        self,
        habit_pk: int,
        period: str,
        time_start: datetime,
    ):
        self.habit_pk = habit_pk
        self.period = period
        # self.data_start = datetime.combine(data_start, time_start)
        self.time_start = time_start

        # делаем шедулеры
        self.schedule_start = self._clocked_schedule()

    def _clocked_schedule(self):
        """
        Назначаем шедулер или берем старый если есть
        """
        print("************", self.time_start.minute, self.time_start.hour, self.period)
        if self.time_start:
            schedule, _ = CrontabSchedule._default_manager.get_or_create(
                minute=self.time_start.minute,
                hour=self.time_start.hour,
                day_of_week=self.period,
                day_of_month="*",
                month_of_year="*",
            )
            return schedule
        return None

    @staticmethod
    def date_str(dt: datetime):
        """
        Переводим datetime в строковой вид
        """
        if dt:
            return dt.strftime("%Y-%m-%d %H:%M")
        else:
            return None

    def create(self):
        """
        Создать эвент. Создать задачи
        start_event на перевод по дате эвента в текущий и
        end_event  завершение
        """
        # если есть шедулера
        # ставим задачу на установку статуса на process
        # и задачу на установку статуса завершения
        task = "habit_tracker.task.task_habit"
        name_task = f"Task_{self.habit_pk}"
        instance = PeriodicTask._default_manager.filter(name=name_task).first()
        if not instance:
            instance = PeriodicTask._default_manager.create(
                crontab=self.schedule_start,
                one_off=False,
                name=name_task,
                task=task,
                start_time=datetime.now(),
                args=[self.habit_pk],
            )
        else:
            # Если таск есть
            instance.crontab = (self.schedule_start,)
            instance.save()

    def update(self, kwargs):
        self._task_update_status_event(kwargs)


@app.task()
def task_habit(id_habit):
    print("++++++++++++", id_habit)
    # send_telegram_message("cccccca", )
    id_habit = int(id_habit)
    habit = Habit.objects.get(pk=id_habit)
    message = (
        f"Напоминание: Выполните привычку '{habit.action}' в локации '{habit.place}' "
        f"время выполнения: {habit.time}. "
        f"Вознаграждение: {habit.reward if habit.reward else habit.related.action}."
    )
    send_telegram_message(message, habit.user.chat_id_telegram)
