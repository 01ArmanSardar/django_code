from django.shortcuts import render
from car.models import car
from brand.models import Carbrand

def home(request,carbrand_slug=None):
    Carobject=car.objects.all()
    # brandName=Carbrand.objects.all()
    if carbrand_slug is not None:
        # brandName=Carbrand.objects.filter(slug=carbrand_slug)
        brnadName=Carbrand.objects.get(slug=carbrand_slug)
        Carobject=car.objects.filter(brnadName=brnadName)
    BrandName=Carbrand.objects.all()
    
    return render (request,'home.html',{'Cardata':Carobject, 'brand':BrandName})


def Brand(request,carbrand_slug=None):
    brandname=Carbrand.objects.all()
    # if carbrand_slug is not None:
# def Cars(request):
#     Carobject=car.objects.all()
#     return render (request,'home.html',{'Cardata':Carobject})