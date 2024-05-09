from django.shortcuts import render ,redirect
from . import form
# Create your views here.
def add_profile(request):
    if request.method == 'POST': # USER post request korche
        profileForm=form.ProfileForm(request.POST)  # user er post request data akhane capture korlam 
        if profileForm.is_valid(): # post request data gult valid kina check kortechi 
            profileForm.save() # jodhi data gulu valid hoi tahole database save hobhe 
            return redirect('homepage') #shob thik vabhe holeh homepage er url er thorw teh homepage patahy dibho
    else: #request.method jodhi get hoi tahole tahole normally website a gele blank form pabhe
       profileForm=form.ProfileForm() 
    return render(request,'add_profile.html',{'form_data':profileForm})