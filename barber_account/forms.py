from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'class': 'icon-user',
                                                             'placeholder': 'Логин'}
                                                      )
                               )
    password = forms.CharField(required=False,
                               widget=forms.PasswordInput(attrs={'class': 'icon-password',
                                                                 'placeholder': 'Пароль'}
                                                          )
                               )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Еще раз пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

        labels = {
            'username': ('Имя пользователя (логин)'),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'user-edit-form'}),
            'last_name': forms.TextInput(attrs={'class': 'user-edit-form'}),
            'email': forms.TextInput(attrs={'class': 'user-edit-form'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth']

        widgets = {
            'date_of_birth': forms.TextInput(attrs={'class': 'profile-edit-form'}),
        }

        labels = {
            'date_of_birth': ('Дата рождения'),
        }