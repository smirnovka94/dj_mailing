# Generated by Django 4.2.6 on 2023-10-16 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_mailing_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('can_change_mailing', 'Can_change_product_active')], 'verbose_name': 'Параметры рассылки', 'verbose_name_plural': 'Виды рассылок'},
        ),
    ]