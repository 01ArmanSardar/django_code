from django.shortcuts import render ,redirect
from . import form
from . import models
# Create your views here.
def home(request):
    if request.method =='POST':
        albumform= form.AlbumForm(request.POST)
        if albumform.is_valid():
            albumform.save()
            return redirect ('homepage')
    else:
        albumform=form.AlbumForm()        
    return render(request,'Ahome.html',{'albumdata':albumform})

# edit table

def editTable(request,id):
    edit=models.Album.objects.get(pk=id)
    albumform= form.AlbumForm(instance=edit)
    if request.method =='POST':
        albumform= form.AlbumForm(request.POST,instance=edit)
        if albumform.is_valid():
            albumform.save()
            return redirect ('homepage')      
    return render(request,'Ahome.html',{'albumdata':albumform})

# delete table

def delete_table(request,id):
    deleteTable=models.Album.objects.get(pk=id)
    deleteTable.delete()
    return redirect('homepage')