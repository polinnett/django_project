from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import Profile


class UserForm(UserCreationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите логин:'}))
    password1 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль:'}))
    password2 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль:'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class ProfileForm(forms.ModelForm):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя:'}))
    age = forms.IntegerField(label='', required=True, widget=forms.NumberInput(attrs={'placeholder': 'Ваш возраст:'}))
    height = forms.IntegerField(label='', required=True, widget=forms.NumberInput(attrs={'placeholder': 'Ваш рост:'}))
    weight = forms.IntegerField(label='', required=True, widget=forms.NumberInput(attrs={'placeholder': 'Ваш вес:'}))
    photo = forms.ImageField(label='Выберите фото', required=True, widget=forms.FileInput(
        attrs={'placeholder': 'Введите логин:', 'id': 'upload', 'accept': 'image/*'}))

    class Meta:
        model = Profile
        fields = [
            'name',
            'age',
            'height',
            'weight',
            'photo'
        ]

    # методы валидациии
    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 100 or age < 10:
            raise ValidationError('Неверный возраст')
        return age

    def clean_height(self):
        height = self.cleaned_data['height']
        if height > 220 or height < 150:
            raise ValidationError('Неверный рост')
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight > 200 or weight < 30:
            raise ValidationError('Неверный вес')
        return weight


class LoginForm(forms.Form):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите логин:'}))
    password = forms.CharField(label='', required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль:'}))