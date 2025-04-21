from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    api_telegram = models.CharField(max_length=50,
                              default=None,
                              null=True,
                              blank=True,
                              verbose_name='Telegram_ID пользователя',
                              help_text='Telegram_ID для бота рассылки',
                              )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def __repr__(self):
        return f"{self.pk} {self.email}"
