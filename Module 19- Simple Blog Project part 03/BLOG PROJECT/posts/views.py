from django.shortcuts import render ,redirect
from . import form
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        add_form=form.add_psot(request.POST)
        if add_form.is_valid():
            # add_form.cleaned_data['author'] =request.user
            add_form.instance.author=request.user
            add_form.save()
            return redirect('homepage')
    else:
         add_form=form.add_psot()
    return render(request,'add_post.html',{'form_data':add_form})

# edit post
@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    add_form=form.add_psot(instance=post)
    # print(post.title)
    if request.method == 'POST':
        add_form=form.add_psot(request.POST,instance=post)
        if add_form.is_valid():
            add_form.instance.author=request.user
            add_form.save()
            return redirect('homepage')
    return render(request,'add_post.html',{'form_data':add_form})


@login_required
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')