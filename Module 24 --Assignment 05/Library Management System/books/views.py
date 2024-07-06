from django.shortcuts import render,redirect,get_object_or_404
from .import forms
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from . import models
from django.views.generic.detail import DetailView
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


class BlogDetailsView(DetailView):
    model=models.book
    template_name='details.html'
    pk_url_kwarg='id'

    def post(self,request,*args,**kargs):
        comment_form=form.ComentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object #book model er object ekhnae store korlam
        comments = book.comments.all()
        comment_form=form.ComentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context