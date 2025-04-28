from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from habit_tracker.models import Habit
from users.models import CustomUser

CustomUser = get_user_model()


class HabitTestCase(TestCase):
    """
    Тесты endpoint, permissions, validators
    """
    def setUp(self):
        self.client = APIClient()

        # Создание пользователя
        self.admin_user = CustomUser.objects.create(
            email="user@user.com", is_staff=True, is_superuser=True
        )
        self.admin_user.set_password("123456789")
        self.admin_user.save()
        self.client.force_authenticate(user=self.admin_user)

        """self.user_1 = CustomUser.objects.create(
            email="user@example.com",
            tg_username="test_user",
            tg_chat_id="12345",
        )
        self.user_1.set_password("user1")
        self.user_1.save()"""

        """self.user_2 = CustomUser.objects.create(
            email="other@example.com",
            tg_username="other_user",
            tg_chat_id="54321",
        )
        self.user_2.set_password("user2")
        self.user_2.save()
"""
        # Привычки для тестов


        self.habit2 = Habit.objects.create(
            user=self.user_1,
            place="Дома",
            action="Посмотреть стендап",
            time_to_complete=10,
            is_published=False,
            nice=True
        )

        self.habit1 = Habit.objects.create(
            user=self.user_1,
            place="Дома",
            action="Достать тренажер",
            time_to_complete=30,
            is_published=True,
            related=1,
        )

        self.habit3 = Habit.objects.create(
            user=self.user_2,
            place="Спортзал",
            action="Выйти на тренировку",
            time_to_complete=120,
            is_published=True,
        )
        self.habit3 = Habit.objects.create(
            user=self.user_1,
            place="по дороге в офис",
            reward="купить кофе",
            action="Пройти мимо останоки",
            time_to_complete=10,
            is_published=False,
        )
