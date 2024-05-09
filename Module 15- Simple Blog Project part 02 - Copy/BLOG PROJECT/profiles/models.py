from django.db import models
from Authors.models import Author
# Create your models here.
class Pofile(models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    author=models.OneToOneField(Author,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'profile_Name : {self.name}'