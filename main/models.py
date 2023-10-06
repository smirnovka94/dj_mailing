from datetime import datetime

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class FrequencyMailing(models.Model):
    # Аргументы для периодичности расстылки
    # ВВЕСТИ ДАННЫЕ ПО УМОЛЧАНИЮ (Раз в день, неделю, месяц)
    # PERIOD_CHOICES = [
    #     ('MN', 'Ежеминутная'),
    #     ('HR', 'Часовая'),
    #     ('DL', 'Еженедельная'),
    #     ('WK', 'Еженедельная')
    # ]
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
    # STATUS_CHOICES = [
    #     ('CR', 'Создана'),
    #     ('SL', 'Запущена'),
    #     ('FL', 'Завершена')
    # ]
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус рассылки'
        verbose_name_plural = 'Статусы рассылки'


class Mailing(models.Model):
    name = models.CharField(max_length=150,unique=True, verbose_name='Название рассылки')
    # email = models.EmailField(unique=True, verbose_name='email')
    frequency = models.ForeignKey(FrequencyMailing,on_delete=models.CASCADE, verbose_name='Периодичность рассылки')

    satus = models.ForeignKey(StatusMailing,on_delete=models.CASCADE, verbose_name='Cтатус рассылки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Периодичность рассылки'
        verbose_name_plural = 'Периодичности рассылки'

class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема письма')
    content = models.TextField(verbose_name='Тема письма')


class Logs(models.Model):
    data = models.DateField(verbose_name='Дата и время последней попытки')
    satus = models.ForeignKey(StatusMailing, on_delete=models.CASCADE, verbose_name='статус рассылки')
    answer = models.CharField(max_length=150, verbose_name='ответ почтового сервера, если он был')
