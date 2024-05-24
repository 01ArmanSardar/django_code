from django.shortcuts import render,redirect
from . import form
from brand.models import Carbrand
from car.models import car
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
# Create your views here.
def user(request):
    return render(request,'user.html')

def signup(request):
    signupFOrm=form.signupForm(request.POST)
    if request.method=='POST':
        if signupFOrm.is_valid():
            signupFOrm.save()
    else:
        signupFOrm=form.signupForm()
    return render(request,'user.html',{'form':signupFOrm,'type':'register'})

def userLogin(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'login succesfully')
                login(request,user)
                return redirect ('homepage')
            else:
                messages.warning(request,'login incorrect')
                return redirect('login')
                
    else :
        form=AuthenticationForm()
    return render(request,'user.html',{'form':form, 'type':'login'})


def userLogout(request):
    logout(request)
    return redirect('login')
# class userLogoutView(LogoutView):
#     template_name='logout.html'
#     # def get_success_url(self):
#     reverse_lazy('login')

# def Car(request):
#     carobject=car.objects.get(pk=id)
#     return render (request,'home.html',{'cardata':carobject})

# def Profile(request):
#     data=Post.objects.filter(author=request.user)

def editProfile(request):
    if request.method=='POST':
        profile_form=form.Changeuserform(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'profile updated Succesfully')
            return redirect('homepage')
    else:
        profile_form=form.Changeuserform(instance=request.user)
    return render (request,'editProfile.html',{'form':profile_form})