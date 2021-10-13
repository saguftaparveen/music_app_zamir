from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Music(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        upload_to='thumbnails/', null=True, blank=True)
    file = models.FileField(upload_to='music/')
    artists = models.ManyToManyField('Artist')

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    pic=models.ImageField(upload_to='pic/',null=True,blank=True)
    
    def __str__(self):
        return self.name

class Playlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    songs=models.ManyToManyField('Music')

    def __str__(self):
        return f"{self.user} favourites"