from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)  # ekta post multiple categorir moddeh thakteh pare abar akta categorir moddeh multiple post takte pareh
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True) #global media file holeh upload_to='uploads/',

    def __str__(self):
        return f'{self.title}'
    

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'