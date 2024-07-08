from django.db import models
from Core.models import Account
# Create your models here.
class Transaction(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,default=True,related_name='account')
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    balance=models.DecimalField(decimal_places=2,max_digits=12)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['timestamp']