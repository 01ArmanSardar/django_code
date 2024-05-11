from django.shortcuts import render ,redirect
from .forms import SignupForm,Login
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
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
            messages.success(request,'login Succesfully')
            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect('homepage')
    else:
        form=Login()
    return render(request,'Ahome.html',{'form':form})

def profile(request):
    return render(request,'profile.html')


def UserLogout(request):
    logout(request)
    return redirect('login')
    # return render(request,'profile.html')

