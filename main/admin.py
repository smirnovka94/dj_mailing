from django.contrib import admin

from main.models import FrequencyMailing, StatusMailing, Mailing, Message, Logs


@admin.register(FrequencyMailing)
class FrequencyMailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'frequency',)



@admin.register(StatusMailing)
class StatusMailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'frequency', 'satus')
    list_filter = ('frequency', 'satus')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')


@admin.register(Logs)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'data', 'satus', 'answer')
    list_filter = ('answer', 'satus')