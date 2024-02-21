from django import forms
from .models import New

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostNewsForm(forms.Form):
    title = forms.CharField(max_length=120)
    description = forms.CharField()
    tags = forms.CharField(max_length=120)