from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=20)
    Description=models.CharField(max_length=50)
    is_completed =models.BooleanField(default=False)
    AssignDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'