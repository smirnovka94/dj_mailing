from django import forms
from clients.models import Clients


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ('user',)

