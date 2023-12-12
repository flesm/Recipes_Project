from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from .models import User


class UserProfileForm(UserChangeForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ['username', 'email']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    is_admin = forms.BooleanField(label='Администратор?', required=False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_admin')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Неправильный логин или пароль")

        return cleaned_data

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#
#
# class LoginForm(forms.ModelForm):
#     username = forms.CharField(label='Логін')
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Users
#         fields = ['username', 'password']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#
#         user = authenticate(username=username, password=password)
#         if not user:
#             raise forms.ValidationError("Неправильный логин или пароль")
#
#         return cleaned_data
