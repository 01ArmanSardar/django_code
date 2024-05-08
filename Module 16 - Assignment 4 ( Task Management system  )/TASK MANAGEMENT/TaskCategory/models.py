from django.db import models
from Task.models import TaskModel

# Create your models here.
class taskCategory(models.Model):
    Categoryname=models.CharField(max_length=20)
    Tasks=models.ManyToManyField(TaskModel)

    def __str__(self):
        return f'{self.Categoryname}'