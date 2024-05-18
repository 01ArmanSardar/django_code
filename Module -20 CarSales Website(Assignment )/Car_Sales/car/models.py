from django.db import models
from brand.models import Carbrand
# Create your models here.
class car(models.Model):
    image=models.FileField(upload_to='uploads/')
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    brnadName=models.ForeignKey(Carbrand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name