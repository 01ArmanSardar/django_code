from django import forms
from .models import Pofile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Pofile
        fields= '__all__'