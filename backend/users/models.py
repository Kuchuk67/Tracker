from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    api_telegram = models.CharField(max_length=50,
                              default='expected',
                              verbose_name='статус ивента',
                              help_text='Текущий статус данного ивента',
                              )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
