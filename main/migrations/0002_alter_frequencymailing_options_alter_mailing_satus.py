# Generated by Django 4.2.6 on 2023-10-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frequencymailing',
            options={'verbose_name': 'Периодичность рассылки', 'verbose_name_plural': 'Периодичности рассылки'},
        ),
        migrations.AlterField(
            model_name='mailing',
            name='satus',
            field=models.CharField(choices=[('Finish', 'Завершена'), ('Create', 'Создана'), ('Work', 'Запущена')], default='Create', max_length=150, verbose_name='Cтатус рассылки'),
        ),
    ]