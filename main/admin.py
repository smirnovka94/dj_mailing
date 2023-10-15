from django.contrib import admin

from main.management.commands.runapscheduler import Command
from main.models import FrequencyMailing, Mailing, Message, Logs


@admin.register(FrequencyMailing)
class FrequencyMailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'frequency',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'frequency', 'satus')
    list_filter = ('frequency', 'satus')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)

