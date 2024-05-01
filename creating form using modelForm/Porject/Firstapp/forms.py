from django import forms
from Firstapp.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields= '__all__'
        # exclude=['adress']
        labels={
            'name':'student Name',
            'roll':'student Roll',
            'father_name':'student Father Name'
        }
        widgets = {
        #    'name' : forms.TextInput(attrs={'class' : 'btn-primary'})
       }
        help_texts={
            'name': "type your name please"
        }
        error_messages={
            'name':{'required':'your name is requierd'},
            
        }
