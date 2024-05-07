from django.db import models
class Musician(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    instrument_type=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"