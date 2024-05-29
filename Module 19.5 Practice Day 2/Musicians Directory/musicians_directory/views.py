from django.shortcuts import render
from album.models import Album
def home(request):
    directoryData=Album.objects.all()
    return render(request,'home.html',{'musicData':directoryData})