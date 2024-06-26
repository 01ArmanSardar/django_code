from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Login(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','first_name','last_name','email']