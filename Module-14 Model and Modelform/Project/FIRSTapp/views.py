from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    student=models.student.objects.all()
    print(student)
    return render(request,'home.html',{'data':student})

def deletestudent(request, roll):
    std=models.student.objects.get(pk=roll).delete()
    return redirect('homepage')