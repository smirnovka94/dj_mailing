# Generated by Django 4.2.6 on 2023-10-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_frequencymailing_options_alter_mailing_satus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='status',
            field=models.CharField(max_length=100, verbose_name='статус рассылки'),
        ),
    ]
