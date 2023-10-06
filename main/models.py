from datetime import datetime

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class FrequencyMailing(models.Model):
    # Аргументы для периодичности расстылки
    # ВВЕСТИ ДАННЫЕ ПО УМОЛЧАНИЮ (Раз в день, неделю, месяц)
    frequency = models.DateTimeField()

    def __str__(self):
        return f'{self.frequency}'

    class Meta:
        verbose_name = 'Периодичность рассылки'
        verbose_name_plural = 'Периодичности рассылки'


class StatusMailing(models.Model):
    # Аргументы для Статуса рассылок
    # ВВЕСТИ ДАННЫЕ ПО УМОЛЧАНИЮ (завершена. создана, запущена)
    name = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус рассылки'
        verbose_name_plural = 'Статусы рассылки'


class Mailing(models.Model):
    name = models.CharField(max_length=150,unique=True, verbose_name='Название рассылки')
    # email = models.EmailField(unique=True, verbose_name='email')
    frequency = models.ForeignKey(FrequencyMailing, verbose_name='Периодичность_рассылки')

    satus = models.ForeignKey(StatusMailing, verbose_name='статус рассылки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Периодичность_рассылки'
        verbose_name_plural = 'Периодичности_рассылки'

class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема письма')
    slug = models.TextField(verbose_name='Тема письма')


class Logs(models.Model):
    data = models.DateField(default=datetime.now(), verbose_name='Дата и время последней попытки')
    satus = models.ForeignKey(StatusMailing, verbose_name='статус рассылки')
    answer = models.CharField(max_length=150, verbose_name='ответ почтового сервера, если он был')
