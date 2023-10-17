from django.contrib import admin


from main.models import FrequencyMailing, Mailing, Message


@admin.register(FrequencyMailing)
class FrequencyMailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'frequency',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'frequency', 'satus', 'user')
    list_filter = ('frequency', 'satus')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)

