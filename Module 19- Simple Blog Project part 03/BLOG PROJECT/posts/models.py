from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
# for user Uploaded file(2-6-24)
def user_directory_path(instance, mediaU): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, mediaU)

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)  # ekta post multiple categorir moddeh thakteh pare abar akta categorir moddeh multiple post takte pareh
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # image=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True) #global media file holeh upload_to='uploads/',
    upload = models.ImageField(upload_to = user_directory_path,blank=True,null=True) 

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