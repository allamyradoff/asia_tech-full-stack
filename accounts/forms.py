from dataclasses import field
from django import forms

from .models import Account


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Напишите пароль',
        'class':'form-control'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подвердите пароль', 
        'class':'form-control'

    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите имя',
        'class':'form-control'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите фамилаю',
        'class':'form-control'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите телефон',
        'class':'form-control'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите Email',
        'class':'form-control'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']



    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Введите оба паролья правильно")

