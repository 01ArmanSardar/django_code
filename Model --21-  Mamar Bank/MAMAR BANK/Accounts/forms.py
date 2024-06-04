from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from .models import UserBankAccount,UserAddress

class UserRegistrationForm(UserCreationForm):
    birthDate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)
    
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email','account_type','birthDate','city','street_address','gender','postal_code','country']

    def save (self,commit=True):
        our_user =super().save(commit=False) #ami dataBase data Save korbho nah akhn
        if commit==True:
            our_user.save()
            Account_type=self.cleaned_data.get('account_type')
            Gender=self.cleaned_data.get('gender')
            PostalCode=self.cleaned_data.get('postal_code')
            Country=self.cleaned_data.get('country')
            BirthDate=self.changed_data.get('birthDate')
            City=self.changed_data.get('city')
            Street_Address=self.changed_data.get('street_address')

            UserAddress.objects.create(
              user=our_user,
              postal_code=PostalCode,
              country=Country,
              city=City,
              street_address=Street_Address
            )
            UserBankAccount.objects.create(
                user=our_user,
                birthDate=BirthDate,
                gender=Gender,
                account_type=Account_type,
                accountNo=100000+our_user.id
            )
        return our_user
    
    def __init__ (self,*args,**kwargs): #
        super().__init__(*args,**kwargs) #parent tah keh inherit koechi 
        for field in self.fields: #ai liner er manhe hocceh ai form a joutGulah field ache shob Gula keh amra ak ak kore nibho
            # nicer line gulu teh amrah mulutoh form er jeh field gulu aceh seh gular style add korchi ,aghe toh frontend a tekeh add krtm but akhne backend teke korlam ar kih
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })




