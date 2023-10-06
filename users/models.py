from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    name1 = models.CharField(max_length=30, verbose_name='Имя')
    name2 = models.ImageField(max_length=20, verbose_name='Фамилия', **NULLABLE)
    name3 = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)

    description = models.TextField(verbose_name='Комментарий')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}({self.name1}, {self.name2}, {self.description})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'