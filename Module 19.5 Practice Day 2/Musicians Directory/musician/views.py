from django.shortcuts import render ,redirect
from . import form
from . import models
# Create your views here.
def home (request):
    if request.method == 'POST':
        musicianform=form.MusicianForm(request.POST)
        if musicianform.is_valid():
            musicianform.save()
            return redirect('homepage')
    else:
        musicianform=form.MusicianForm()
    return render(request,'Mhome.html',{'Musiciandata':musicianform})


def edit_musician (request,id):
    musician_edit=models.Musician.objects.get(pk=id)
    musicianform=form.MusicianForm(instance=musician_edit)
    if request.method == 'POST':
        musicianform=form.MusicianForm(request.POST,instance=musician_edit)
        if musicianform.is_valid():
            musicianform.save()
            return redirect('homepage')
    return render(request,'Mhome.html',{'Musiciandata':musicianform})