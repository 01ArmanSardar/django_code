from django.shortcuts import render ,redirect
from . import forms
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        categoryForm=forms.categoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('homepage')
    else:
        categoryForm=forms.categoryForm()
    return render(request,'add_category.html',{'form_data':categoryForm})
