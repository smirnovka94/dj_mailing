from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    name1 = models.CharField(max_length=30, verbose_name='Имя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}({self.name1})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'