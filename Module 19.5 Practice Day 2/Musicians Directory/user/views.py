from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
# Create your views here.

def signupForm(request):
    if request.method=='POST':
        SignUp_form=forms.RegistationFoem(request.POST)
        if SignUp_form.is_valid():
            SignUp_form.save()
            return redirect('homepage')
    else:
          SignUp_form=forms.RegistationFoem()  
    return render(request,'signup.html',{'form':SignUp_form})

class userLogin(LoginView):
     template_name='login.html'
     def get_success_url(self):
        return reverse_lazy('homepage')
     
def userLogout(request):
    logout(request)
    return redirect('login')
