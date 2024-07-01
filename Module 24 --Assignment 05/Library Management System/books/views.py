from django.shortcuts import render,redirect
from .import forms
# Create your views here.
from django.views.generic import TemplateView


class BookView(TemplateView):
    template_name = "bookpage.html"


def add_category(request):
    if request.method=='POST':
        CategoryForm=forms.categoryForm(request.POST)
        if CategoryForm.is_valid():
            CategoryForm.save()
            return redirect('homepage')
    else:
        CategoryForm=forms.categoryForm()
    return render (request,'add_category.html',{'form_data':CategoryForm})

