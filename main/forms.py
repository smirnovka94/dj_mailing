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

class MailingForm(StyleForDateTimeInput, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'
