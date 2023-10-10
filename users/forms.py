from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from main.forms import StyleForMixin
from users.models import User


class UserForm (StyleForMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class VerificationForm(forms.Form):
    key = forms.CharField()


class ChangeForm_User(StyleForMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'name1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()