from django.shortcuts import render
from . forms import contactForm, studentform,passwordForm
# Create your views here.
def home(request):
    return render(request,'Apphome.html')

def DjangoForm(request):
    if request.method=='POST':
        form =contactForm(request.POST, request.FILES)
        if form.is_valid():
            # django form field a file nie jodhi kono kaj korah hoi tkhn normally nicher 4 tah line add korteh hoi,nicher line gulur korar karon hocceh dhori amrha kono aktah file upload korlam jar size hoito 1gb toh seh ketreh kintu amaderh system tah slow hoie jabhe ,tai file tah keh choto korar choto korar jonno nicher code tah
            # file= form.cleaned_data['file']
            # with open('./Django_builtIn_form/Uploaded_image_from_forms/' +file.name, 'wb+') as destination:
            #     for chunck in file.chunks():
            #         destination.write(chunck)
            print(form.cleaned_data)
    else:
        form=contactForm()
    return render(request,'django_form.html',{'form':form})

def StudentForm(request):
    if request.method=='POST':
        form=studentform(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=studentform()
    return render(request,'django_form.html',{'form':form})


def passwordCHeckForm(request):
    if request.method=='POST':
        form=passwordForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=passwordForm()
    return render(request,'django_form.html',{'form':form})