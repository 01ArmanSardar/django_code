from django.shortcuts import render ,redirect
from . import forms
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form=forms.registrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('register')
    else:
        register_form=forms.registrationForm()
    return render(request,'register.html',{'form_data':register_form})









# def add_author(request):
#     if request.method == 'POST':
#         authorform=forms.AuthorForm(request.POST)
#         if authorform.is_valid():
#             authorform.save()
#             return redirect('homepage')
#     else:
#         authorform=forms.AuthorForm()
#     return render(request,'add_author.html',{'form_data':authorform})