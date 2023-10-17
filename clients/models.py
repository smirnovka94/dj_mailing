from django.db import models
from datetime import datetime

from django.conf import settings

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):

    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', **NULLABLE)

    description = models.TextField(verbose_name='Комментарий', **NULLABLE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='пользователь')
    def __str__(self):
        return f'{self.email} ({self.first_name} {self.last_name})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'