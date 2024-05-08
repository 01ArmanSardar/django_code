from django import forms
from .models import taskCategory

class categoryform(forms.ModelForm):
    class Meta:
        model=taskCategory
        fields='__all__'