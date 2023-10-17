from django.contrib import admin

from clients.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email','first_name','last_name','patronymic','description','user')

    list_filter = ('first_name', 'last_name', 'patronymic')
    search_fields = ('email', 'content',)