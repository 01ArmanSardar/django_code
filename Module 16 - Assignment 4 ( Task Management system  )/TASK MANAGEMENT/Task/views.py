from django.shortcuts import render,redirect
from . import forms
from .models import TaskModel
# Create your views here.
def Thome(request):
    if request.method=='POST':
        task=forms.taskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('homepage')
    else:
        task=forms.taskForm()
    return render(request,'Thome.html',{'taskData':task})

def edit(request,id):
    edit_task=TaskModel.objects.get(pk=id)
    task=forms.taskForm(instance=edit_task)
    if request.method=='POST':
        task=forms.taskForm(request.POST,instance=edit_task)
        if task.is_valid():
            task.save()
            return redirect('homepage')
    return render(request,'Thome.html',{'taskData':task})

def delete(request,id):
    deleteTask=TaskModel.objects.get(pk=id)
    deleteTask.delete()
    return redirect('homepage')