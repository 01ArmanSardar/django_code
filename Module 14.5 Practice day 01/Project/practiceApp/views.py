from django.shortcuts import render
from . forms import practiceDjangoForm
from . import models
# Create your views here.
def home(request):
    return render(request,'home.html')

def djangoform(request):
    form=practiceDjangoForm(request.POST)
    if form.is_valid():
        print (form.cleaned_data)
    return render(request,'djangoForm.html',{'formData':form})

def modelFields(request):
    examlemodel=models.ExampleModel.objects.all()
    return render(request,'model_feildForm.html',{'data':examlemodel})
