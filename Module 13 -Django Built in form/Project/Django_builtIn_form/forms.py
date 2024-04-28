from django import forms
from django.core import validators
# widgets er muloto kaj hocceh django field keh html input a convert korah
class contactForm(forms.Form):
    name=forms.CharField(label='Full name',initial='Arman',help_text='Enter your Full Name',required= False,disabled=True,widget=forms.Textarea)
    # file=forms.FileField()
    email=forms.EmailField(label='input your eamil')
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    cehck=forms.BooleanField()
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    Appoinment=forms.CharField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    # singel value er ketreh amrah charfeild use korleio hobhe ,kintu jkhn e choice feild bah multiple choice er khota asbhee tkhn kintu charfeild dile hobhe nah tkhn choiceFeild er jonno choiceFeild ar multipleChoiceFeild er jonno multipleChoiceFeild e use korteh , CharFeild amrah muloto use koreth jkhn kono feild a amarah singel value input nibho
    CHOICES=[('S', 'small'),('M','mediuam'),('B','big')]
    size =forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL=[('P','peeproni',),('M','mashroom'),('C','cheez')]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)

# class studentform (forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.EmailField()
    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 charcter")
    #     return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('must  include .com with your email ')
    #     return valemail

    # aktah function er moddei amrah caile validation er kaj gulu koreh niteh parih, this process is below
    # def clean (self):
    #     cleaned_data = super().clean()
    #     valname =self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']   
    #     if len(valname) <10:
    #         raise forms.ValidationError('must include 10 character in your name')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('your email must contain .com') 
       
     
# belows line we provide some built in validators
# nicher function tah aktah custom validators create korlam ar kih ,bakih nicher shob gulai kintu built-in
def Cusotom_Len_check_Validators(value):
    if len(value)<10:
        raise forms.ValidationError('enter a value at least 10 chars')
class studentform(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message='Enter a name where maximum 10 chracter')])
    text=forms.CharField(widget=forms.TextInput,validators=[Cusotom_Len_check_Validators])
    email=forms.EmailField(validators=[validators.EmailValidator(message='enter a valid email please')])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(30,message='age must be meximum 30 years'),validators.MinValueValidator(10,message='age must minimum 10 years')])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='file extention must be pdf format')])

# password matching project
class passwordForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        valpass=self.cleaned_data['password']
        revalpass=self.cleaned_data['repassword']
        valname=self.cleaned_data['name']
        if valpass != revalpass:
            raise forms.ValidationError('password not match ,please try again')
        if len(valname)<5:
            raise forms.ValidationError('name at least 6 chas long')
