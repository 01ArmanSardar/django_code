from django.shortcuts import render
from car.models import car
from brand.models import Carbrand
def home(request,carbrand_slug=None):
    Carobject=car.objects.all()
    if carbrand_slug is not None:
        brandName=Carbrand.objects.get(slug=carbrand_slug)
        Carobject=car.objects.filter(brandName=brandName)

    return render (request,'home.html',{'Cardata':Carobject})

# def Cars(request):
#     Carobject=car.objects.all()
#     return render (request,'home.html',{'Cardata':Carobject})