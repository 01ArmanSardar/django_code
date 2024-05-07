from django.shortcuts import render ,redirect
from . import form
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