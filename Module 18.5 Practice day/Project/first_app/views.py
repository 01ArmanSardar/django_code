from django.shortcuts import render ,redirect
from .forms import SignupForm,Login
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def home(request):
    return render(request,'Ahome.html')


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=SignupForm()
    return render(request,'Ahome.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        form=Login(request.POST)
        if form.is_valid():

            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            print(user)
            if user is not None:
                
                messages.success(request,'login Succesfully')
                login(request,user)
                
                return redirect('homepage')
    else:
        form=Login()
    return render(request,'Ahome.html',{'form':form})

def profile(request):
    return render(request,'profile.html')


def UserLogout(request):
    messages.success(request,'logout Succesfully')
    logout(request)
    return redirect('login')
    # return render(request,'profile.html')

# 12345678pa

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