from django.shortcuts import render ,redirect
from . forms import categoryform
# Create your views here.
def TChome(request):
    if request.method=='POST':
        categoryview=categoryform(request.POST)
        if categoryview.is_valid():
            categoryview.save()
            return redirect('homepage')
    else:
        categoryview=categoryform()
    return render(request,'TChome.html',{'categorydata':categoryview})
    