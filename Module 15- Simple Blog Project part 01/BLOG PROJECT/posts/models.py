from django.db import models
from categories.models import Category
from Authors.models import Author
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)  # ekta post multiple categorir moddeh thakteh pare abar akta categorir moddeh multiple post takte pareh
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'