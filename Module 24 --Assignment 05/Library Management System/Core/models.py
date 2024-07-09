from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='account')
    balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Account"