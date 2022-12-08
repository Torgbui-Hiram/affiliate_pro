from . models import User
from django import forms
from django.forms import ModelForm

# create a user login form


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'password1')
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter first_name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter last_name'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}), }
        labels = {'first_name': '',
                  'last_name': '',
                  'password': '',
                  'password1': '', }
