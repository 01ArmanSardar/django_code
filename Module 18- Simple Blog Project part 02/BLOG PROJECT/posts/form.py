from django import forms
from .models import Post

class add_psot(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude=['author']
