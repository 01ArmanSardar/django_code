from django.shortcuts import render ,redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,update_session_auth_hash ,logout
from django.contrib import messages
from posts.models import Post
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form=forms.registrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'account created successfully')
            return redirect('login')
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
                return redirect('profile')
            else :
                messages.warning(request,'Information is incorrect')
                return redirect('register')
    else :
        form=AuthenticationForm()
    return render(request,'register.html',{'form_data':form, 'type':'Login'})


@login_required
def profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})


@login_required
def editProfile(request):
    if request.method == 'POST':
        profile_form=forms.changeuserform(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'profile updated successfully')
            return redirect('profile')
    else:
        profile_form=forms.changeuserform(instance=request.user)
    return render(request,'editProfile.html',{'form_data':profile_form})


def passChange(request):
    if request.method == 'POST':
        passchange_form=PasswordChangeForm(request.user,data=request.POST)
        if passchange_form.is_valid():
            passchange_form.save()
            messages.success(request,'password updated successfully')
            update_session_auth_hash(request,passchange_form.user)
            return redirect('profile')
    else:
        passchange_form=PasswordChangeForm(user=request.user)
    return render(request,'passChange.html',{'form_data':passchange_form})


def user_logout(request):
    logout(request)
    return redirect('login')
