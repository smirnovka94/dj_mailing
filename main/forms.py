from django import forms
from main.models import Mailing


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StyleForDateTimeInput(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['begin_date'].widget = forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime', 'placeholder': '%m/%d/%y %H:%M:%S (DOB)'
            }
        )
        self.fields['close_date'].widget = forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime', 'placeholder': '%m/%d/%y %H:%M:%S'
            }
        )

class MailingForm(forms.ModelForm):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Mailing
        exclude = ('user',)

