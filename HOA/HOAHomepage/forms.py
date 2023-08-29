from django.forms import ModelForm
from django import forms
from HOAApi.models import *


class RegistrerForm(ModelForm):
    class Meta:
        model = Beboer
        fields = ('navn', 'adresse', 'tlf', 'brugernavn', 'password', 'mail')
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(ModelForm):
    class Meta:
        model = Beboer
        fields = ('brugernavn', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }