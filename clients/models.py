from django.db import models
from datetime import datetime

from django.conf import settings

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):
    # mailings = models.ForeignKey(Mailing)#Список рассылок
    email = models.EmailField(unique=True, verbose_name='email')
    name1 = models.CharField(max_length=30, verbose_name='Имя')
    name2 = models.CharField(max_length=30, verbose_name='Фамилия')
    name3 = models.CharField(max_length=30, verbose_name='Отчество', **NULLABLE)

    description = models.TextField(verbose_name='Комментарий', **NULLABLE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='пользователь')
    def __str__(self):
        return f'{self.email} ({self.name1} {self.name2})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'