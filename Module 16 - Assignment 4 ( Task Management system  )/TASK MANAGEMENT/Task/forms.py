from django import forms
from . import models
class taskForm(forms.ModelForm):
    class Meta:
        model=models.TaskModel
        fields= '__all__'
