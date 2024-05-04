from django import forms
from django.forms.widgets import NumberInput
import datetime
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class practiceDjangoForm(forms.Form):
    name=forms.CharField(max_length=20)
    comment=forms.CharField(widget=forms.Textarea ,label='please type your comment is below box')
    comment=forms.CharField(widget=forms.Textarea(attrs={'row':5}))
    email=forms.EmailField(initial='example@gmail.com')
    agree=forms.BooleanField()
    date=forms.DateField(initial=datetime.date.today)
    birth_date=forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_yeaar_choices=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    decivalue=forms.DecimalField()
    my_favorite_color=[('green','Green'),('red','Red'),('blue','Blue')]
    favroite_color=forms.ChoiceField(choices=my_favorite_color)
    Rfavroitecolor=forms.ChoiceField(widget=forms.RadioSelect,choices=my_favorite_color)
    favroitecolors=forms.MultipleChoiceField(choices=my_favorite_color)
    Checkfavroitecolors=forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple,choices=my_favorite_color)


