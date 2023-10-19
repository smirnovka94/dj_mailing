from django.db import models
from clients.models import Clients
from users.models import User

NULLABLE = {'blank': True, 'null': True}

class FrequencyMailing(models.Model):
    # Аргументы для периодичности рассылки
    TIMES = [
        ("10S", "раз в 10 секунд"),
        ("Daily", "раз в день,"),
        ("Weekly", "раз в неделю"),
        ("Monthly", "раз в месяц"),
    ]
    frequency = models.CharField(max_length=150,unique=True, choices=TIMES, verbose_name='периодичность рассылки')

    def __str__(self):
        return f'{self.frequency}'

    class Meta:
        verbose_name = 'Периодичность рассылки'
        verbose_name_plural = 'Периодичности рассылки'


class Message(models.Model):
    title = models.CharField(max_length=150,unique=True, verbose_name='Тема письма')
    content = models.TextField(verbose_name='Содержание письма')


class Mailing(models.Model):
    STATUSES = [
        ("Finish", "Завершена"),
        ("Create", "Создана"),
        ("Work", "Запущена"),
    ]

    name = models.CharField(max_length=150,unique=True, verbose_name='Название рассылки')
    frequency = models.ForeignKey(FrequencyMailing,on_delete=models.CASCADE, verbose_name='Периодичность рассылки')
    clients = models.ManyToManyField(Clients, verbose_name='Список получателей')
    message = models.ForeignKey(Message,on_delete=models.CASCADE, verbose_name='Сообщение')

    begin_date = models.DateTimeField(verbose_name='Дата начала рассылки', **NULLABLE)
    close_date = models.DateTimeField(verbose_name='Дата прекращения рассылки', **NULLABLE)

    satus = models.CharField(max_length=150, choices=STATUSES,
        default='Create', verbose_name='Cтатус рассылки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  verbose_name='пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Параметры рассылки'
        verbose_name_plural = 'Виды рассылок'


class Logs(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, verbose_name='статус рассылки')
    answer = models.CharField(max_length=150, verbose_name='ответ почтового сервера, если он был')

