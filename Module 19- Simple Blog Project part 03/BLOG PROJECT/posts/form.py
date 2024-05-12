from django import forms
from .models import Post,Comment

class add_psot(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude=['author']

class ComentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['post','date']
