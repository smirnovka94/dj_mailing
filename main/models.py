from datetime import datetime

from django.conf import settings
from django.db import models

from clients.models import Clients

NULLABLE = {'blank': True, 'null': True}

class FrequencyMailing(models.Model):
    # Аргументы для периодичности расстылки

    frequency = models.CharField(max_length=150,unique=True, verbose_name='периодичность рассылки')

    def __str__(self):
        return f'{self.frequency}'

    class Meta:
        verbose_name = 'Периодичность рассылки'
        verbose_name_plural = 'Периодичности рассылки'


class StatusMailing(models.Model):
    # Аргументы для Статуса рассылок
    # ВВЕСТИ ДАННЫЕ ПО УМОЛЧАНИЮ (завершена. создана, запущена)
    name = models.CharField(max_length=150,unique=True, verbose_name='cтатус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус рассылки'
        verbose_name_plural = 'Статусы рассылки'

class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема письма')
    content = models.TextField(verbose_name='Содержание письма')

class Mailing(models.Model):
    name = models.CharField(max_length=150,unique=True, verbose_name='Название рассылки')

    frequency = models.ForeignKey(FrequencyMailing,on_delete=models.CASCADE, verbose_name='Периодичность рассылки')
    clients = models.ManyToManyField(Clients, verbose_name='Список получателей')
    massage = models.ForeignKey(Message,on_delete=models.CASCADE, verbose_name='Сообщение')

    begin_data = models.DateTimeField(verbose_name='Дата начала рассылки', **NULLABLE)
    close_data = models.DateTimeField(verbose_name='Дата прекращения рассылки', **NULLABLE)

    # data = models.ForeignKey(Logs, verbose_name='дата отправки')
    satus = models.ForeignKey(StatusMailing,on_delete=models.CASCADE, default='0000000', verbose_name='Cтатус рассылки')
    # owner = models.ForeignKey(User
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Параметры рассылки'
        verbose_name_plural = 'Виды рассылок'




class Logs(models.Model):
    data = models.DateTimeField(verbose_name='Дата и время последней попытки')
    satus = models.ForeignKey(StatusMailing, on_delete=models.CASCADE, verbose_name='статус рассылки')
    answer = models.CharField(max_length=150, verbose_name='ответ почтового сервера, если он был')

