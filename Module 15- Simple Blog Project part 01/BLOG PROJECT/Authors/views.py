from django.shortcuts import render ,redirect
from . import forms
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        authorform=forms.AuthorForm(request.POST)
        if authorform.is_valid():
            authorform.save()
            return redirect('homepage')
    else:
        authorform=forms.AuthorForm()
    return render(request,'add_author.html',{'form_data':authorform})