from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(blank=True, verbose_name='Номер телефона')
    password = models.CharField(max_length=128, verbose_name = 'Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'