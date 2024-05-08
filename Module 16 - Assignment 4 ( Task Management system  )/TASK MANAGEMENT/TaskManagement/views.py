from django.shortcuts import render
from TaskCategory.models import taskCategory
def home (request):
    showtask=taskCategory.objects.all()
    return render(request,'home.html',{'showData':showtask})

