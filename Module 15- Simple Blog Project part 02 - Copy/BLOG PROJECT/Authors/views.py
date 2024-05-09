from django.shortcuts import render ,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form=forms.registrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'account created successfully')
            return redirect('register')
    else:
        register_form=forms.registrationForm()
    return render(request,'register.html',{'form_data':register_form, 'type':'Register'})


def user_login(request):
    if request.method =='POST':
        form =AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'logIn  successfully')
                login(request,user)
                return redirect('login')
            else :
                messages.warning(request,'Information is incorrect')
                return redirect('register')
    else :
        form=AuthenticationForm()
    return render(request,'register.html',{'form_data':form, 'type':'Login'})








# def add_author(request):
#     if request.method == 'POST':
#         authorform=forms.AuthorForm(request.POST)
#         if authorform.is_valid():
#             authorform.save()
#             return redirect('homepage')
#     else:
#         authorform=forms.AuthorForm()
#     return render(request,'add_author.html',{'form_data':authorform})