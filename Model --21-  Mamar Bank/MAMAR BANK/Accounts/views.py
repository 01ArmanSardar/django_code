from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView,LoginView
# Create your views here.

class UserRegistrationView(FormView):
    template_name='UserRgistration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')
    
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form) # form_valid function call hobhe jodi sohb thik thake
    
class UserLogin(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')

class UserLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('homepage')