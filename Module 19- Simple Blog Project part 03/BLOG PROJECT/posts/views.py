from django.shortcuts import render ,redirect
from . import form
from django.urls import reverse_lazy
from . import models
from  django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

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
    return render(request,'add_post.html',{'form':add_form})

# add_post using  class Based View
@method_decorator(login_required,name='dispatch')
class AddpostVIew(CreateView):
    model=models.Post
    form_class=form.add_psot
    template_name= 'add_post.html'
    success_url=reverse_lazy('homepage')
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


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

# edit_post view using Classed base view
@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model=models.Post
    form_class=form.add_psot
    template_name='add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')


@login_required
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

# delete_post view using classed base view
@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model =models.Post
    template_name='delete.html'
    success_url=reverse_lazy('homepage')
    pk_url_kwarg='id'


# using classed view for see our blog details in separate page

class BlogDetailsView(DetailView):
    model=models.Post
    template_name='details.html'
    pk_url_kwarg='id'

    def post(self,request,*args,**kargs):
        comment_form=form.ComentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object #post model er object ekhnae store korlam
        comments = post.comments.all()
        # if self.request.method == 'POST':
            # comment_form=form.ComentForm(data=self.request.POST)
            # if comment_form.is_valid():
            #     new_comment=comment_form.save(commit=False)
            #     new_comment.post=post
            #     new_comment.save()
        comment_form=form.ComentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context