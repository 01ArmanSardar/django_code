from django.shortcuts import render,redirect,get_object_or_404
from .import forms
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from django.views.generic import TemplateView
from . models import Books,Category

def book(request,category_slug=None):
    data= Books.objects.all()
    if category_slug is not None:
        # category=Category.objects.get(slug=category_slug)
        category=get_object_or_404(Category,slug=category_slug)
        data=Books.objects.filter(category=category)
    categories=Category.objects.all()
    return render(request,'Bookpage.html',{'data':data,'category':categories})

def my_check(user):
    return user.is_superuser


@user_passes_test(my_check,login_url='homepage', redirect_field_name='next')
def add_category(request):
    if request.method=='POST':
        CategoryForm=forms.categoryForm(request.POST)
        if CategoryForm.is_valid():
            CategoryForm.save()
            return redirect('homepage')
    else:
        CategoryForm=forms.categoryForm()
    return render (request,'add_category.html',{'form_data':CategoryForm})
