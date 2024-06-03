from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE

class UserRegistrationForm(UserCreationForm):
    birthDate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.CharField(max_length=10,choices=GENDER_TYPE)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)\
    
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','account_type','gender','postal_code','country']
