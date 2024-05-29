from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    AlbumName=models.CharField(max_length=30)
    albumRelaseData=models.DateTimeField(auto_now_add=True)
    Musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    CHOICES=[('1', '1'),('2','2'),('3','3'),('4','4')]
    RatingNow= models.CharField(max_length=20, choices=CHOICES)
    def __str__(self):
        return f'{self.AlbumName}'
    