from django.shortcuts import render,redirect
from . import forms
# Create your views here.
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def register(request):
    if request.method=='POST':
        register_form=forms.regirtrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'account created succesfully')
        else:
            register_form=forms.regirtrationForm()
        return render(request,'register.html',{'Rform':register_form})
        