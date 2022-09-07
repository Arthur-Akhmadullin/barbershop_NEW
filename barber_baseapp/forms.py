from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'phone', 'date', 'time', ]

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Дата'}),
            'time': forms.Select(attrs={'placeholder': 'Время'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Телефон'}),
        }

        labels = {
            'date': (''),
            'time': (''),
            'name': (''),
            'phone': (''),
        }