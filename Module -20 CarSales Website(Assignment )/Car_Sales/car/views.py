from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import DetailView
# Create your views here.
def car(request):
    return render(request,'car.html')

class CarDetails(DetailView):
    model=models.car
    template_name='carDetails.html'
    pk_url_kwarg='id'

    def car(self,request,*args,**kargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        car=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.cars=car
            new_comment.save()
        return self.get(request,*args,**kargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object #car model er object ekhnae store korlam
        comments = car.comments.all()
        comment_form=forms.CommentForm()
        

        context['comments']=comments
        context['comment_form']=comment_form
        return context