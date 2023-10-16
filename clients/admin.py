from django.contrib import admin

from clients.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email','name1','name2','name3','description','user')

    list_filter = ('name1', 'name2', 'name3')
    search_fields = ('email', 'content',)