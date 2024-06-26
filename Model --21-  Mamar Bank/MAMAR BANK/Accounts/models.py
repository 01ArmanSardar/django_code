# from django.db import models
# from django.contrib.auth.models import User
# from .constants import ACCOUNT_TYPE,GENDER_TYPE
# # Create your models here.

# class UserBankAccount(models.Model):
#     user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
#     accountType=models.CharField(max_length=10,choices=ACCOUNT_TYPE)
#     accountNo=models.IntegerField(unique=True,null=True)
#     birthDate=models.DateField(null=True,blank=True)
#     gender=models.CharField(max_length=10,choices=GENDER_TYPE)
#     Initial_deposite_date=models.DateField(auto_now_add=True)
#     balance=models.DecimalField(default=0,max_digits=10,decimal_places=2)
#     isBankRupt=models.BooleanField(default=False)
    
#     def __str__(self):
#         return f'acNo: {self.accountNo}'

# class UserAddress(models.Model):
#     user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
#     street_address=models.CharField(max_length=100)
#     city=models.CharField(max_length=100)
#     postal_code=models.IntegerField()
#     country=models.CharField(max_length=100)

#     def __str__(self):
#         return f'name :{self.user.first_name}'


#/////////////////////////////////////////////////////////////

from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
# Create your models here.

class UserBankAccount(models.Model):
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    accountType=models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    accountNo=models.IntegerField(unique=True,null=True)
    birthDate=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_TYPE)
    Initial_deposite_date=models.DateField(auto_now_add=True)
    balance=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    isBankRupt=models.BooleanField(default=False)
    
    def __str__(self):
        return f'acNo: {self.accountNo}'

class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)

    def __str__(self):
        return f'name :{self.user.first_name}'