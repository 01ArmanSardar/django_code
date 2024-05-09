from django.shortcuts import render ,redirect
from . import form
from . import models
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        add_form=form.add_psot(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('homepage')
    else:
         add_form=form.add_psot()
    return render(request,'add_post.html',{'form_data':add_form})

# edit post

def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    add_form=form.add_psot(instance=post)
    # print(post.title)
    if request.method == 'POST':
        add_form=form.add_psot(request.POST,instance=post)
        if add_form.is_valid():
            add_form.save()
            return redirect('homepage')
    return render(request,'add_post.html',{'form_data':add_form})

def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')