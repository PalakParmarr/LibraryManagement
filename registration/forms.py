from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phonenumber = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phonenumber']
